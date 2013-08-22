#!/usr/bin/perl

require 5.6.0;    # needs perl > 5.6.0

# p5httpd: Tiny HTTP server, roughly HTTP 1.0 compliant according to
# RFC 1945
# - POD documentation at end of file
# - User-serviceable configuration section below.
# - Should work without configuration and without any additional files


package p5httpd;    # keep namespace separate from CGI scripts
use strict;
our $version = 0.07;

################# Configuration section #######################

# All filenames below have to be absolute (except $icondir).

# A value of "" means that there is a reasonable default, which may
# depend on the installation directory.

# If $configdir/config_$osname exists, it is read after this
# configuration section

# ----------------- Basic configuration -----------------------

# The server root directory is the place where requests for
# http://this_host/ will look:
# Default: ./html under the directory where p5httpd lives

our $server_root = "";

# Config files are better kept in a separate directory, to avoid
# clutter and to avoid worsening p5httpd's already dismal security :-)
# Default: $server_root/../config

our $config_dir = "";

# The port on which p5httpd will listen. NB: ports below 1024 require
# root privileges on unix machines! Default: 80

our $port = 4711;

# List of mime types (absolute pathname).  You may use apaches
# mime.types, or /etc/mime.types on unix machines. Default:
# $configdir/mime.types, or else a minimal builtin list.

our $mime_types = "";


# Handlers associate a specal cgi script in cgi-bin directory with
# specific mime-types
our %handlers ; # = ("text/xml" => "xml.cgi");

# Which filenames to treat as index files
# Default: none

our @index_filenames = qw(index.htm index.html);

# ------------------ Forking and executing ------------------------

# Forking policy. $never_fork and $fork_always do just what they say,;
# $fork_after_first_invocation will cause the server to fork akways *except*
# the first time a particular cgi script is run. This will ensure that
# all needed modules are already loaded whenever the script is run
# again, just as with mod_perl.

my ( $never_fork, $fork_after_first_invocation, $fork_always ) = ( 1, 2, 3 );
our $when_to_fork = $never_fork;

# if a relative path matches this regexp (case-insensitively), it is
# treated as a cgi script, and we'll try to eval or execute it.
# Default: "\.cgi$" (matching any file with extension .cgi)
# other possibilities: "\.pl$" or "\.(cgi|pl)$" or "\/cgi-bin\/"

our $cgi_scriptname_regexp = "";

# Whether to run cgi scripts by evaling or executing. $cgis_are_evaled
# and $cgis_are_executed do just what they say, $only_perl_is_evaled
# will run perl scripts by evaling and any other programs by executing
# them.  This is a tad expensive, as all cgi's have to
# be sniffed and tasted before they are run.

my ( $cgis_are_evaled, $only_perl_is_evaled, $cgis_are_executed ) = ( 1, 2, 3 );
our $eval_or_execute = $cgis_are_evaled;

# -------------------- Icons -------------------------------------

# Whether to show icons in a directory listing
our $show_icons = 1;

# icon directory, relative to $server_root. Default: "icons"
our $icondir = "";    # relative name here!

# -------------------- Authentication ---------------------------

# Whether to use basic authentication as per HTTP/1.0
# Only enable this when really needed, as it makes all requests slower
our $use_authentication = 0;

# Default: $config_dir/htpasswd
our $password_file = "";

# For every request, p5httpd will climb up the directory tree until it
# finds either an explicitely public or a private directory. This will
# determine whether a password is required. Default: Everything is private,
# i.e. @public_directories = (), @private_directories = qw(/).
# Directories are specified relative to server root, but you still
# have to use leading and trailing slashes here:

our @public_directories  = qw(/);
our @private_directories = qw(/wiki/secret/);

############## End of configuration section ########################

use Socket;
use English;
use Cwd qw(cwd abs_path);
use autouse 'IPC::Open2' => qw( open2 );
;    # only import when needed, as EPOC (and maybe Windows?) doesn't have it.

our (
  $localname,  $OSNAME,   $HOSTNAME,            $I_am_child,
  %mime_types, %cgi_urls, %encrypted_passwords, %private,
  %public,     $invocation
);

initialise();
main_loop();
exit;

################################## Subroutines ###################

sub logerr($$);
sub logmsg($);
sub log_and_die($);
sub cat($$;$);    # forward declarations

sub initialise {
  $HOSTNAME = $ENV{HOSTNAME} || "localhost";
  $I_am_child = 0
    ; # Will be 1 in child after a fork(). Children wil just exit after finishing work.


  $PROGRAM_NAME =~ s#\\#/#g;
  my ($p5httpd_homedir) = ( $PROGRAM_NAME =~ m#^(.*)/# );
  $p5httpd_homedir ||= cwd;    # last resort
  $p5httpd_homedir = abs_path($p5httpd_homedir);
  $p5httpd_homedir =~ s#/$##;

  my $extra_config_dir;
  if ($config_dir) {
    $extra_config_dir = $config_dir;
  }
  elsif ($server_root) {
    $extra_config_dir = "$server_root/../config";
  }
  elsif ( -d "$p5httpd_homedir/config" ) {
    $extra_config_dir = "$p5httpd_homedir/config";
  }
  else {
    $extra_config_dir = $p5httpd_homedir;
  }
  my $extra_config_file = "$extra_config_dir/config_$OSNAME";
  if ( -r $extra_config_file ) {
    logmsg "Reading $extra_config_file";
    do $extra_config_file;
    $@ and logmsg "Something rotten in $extra_config_file: \n$@";
  }
  elsif ( -f $extra_config_file ) {
    logmsg "$extra_config_file exists but not readable: $!";
  }
  else {
    logmsg "looked for, but didn't find extra config in $extra_config_file";
  }

  # If $config_dir is still unset, set it now
  $config_dir ||= $extra_config_dir;
  push @INC, "$config_dir/modules";    # extra modules may be put here, and
  $ENV{PERL5LIB} = ( $ENV{PERL5LIB}? "$ENV{PERL5LIB}:$config_dir/modules" : "$config_dir/modules"); # ... let children know about this

  if ( not $server_root ) {
    $server_root = (
      -d "$p5httpd_homedir/html" ? "$p5httpd_homedir/html" : $p5httpd_homedir );
    logmsg "You didn't specify the server root directory ";
    logmsg "I'll use $server_root for now...";
  }
  $server_root =~ s#/$##;              # remove final slash from $basdir

  $p5httpd::server_root =
    $server_root;    # make this variable visible for CGI scripts

  $port ||= 80 unless $port;
  $password_file ||= "$config_dir/htpasswd";      # absolute path
  $mime_types    ||= "$config_dir/mime.types";    # absolute path
  $icondir       ||= 'icons';                     # relative to $server_root
  $cgi_scriptname_regexp ||= '\.cgi$';

  if ( $mime_types and open MIME, $mime_types ) {
    while (<MIME>) {                              # read list of mime types
      chomp;
      s/#.*//;                                    # ignore comments
      my ( $type, @suffixes ) = split;
      next unless @suffixes;
      foreach my $suffix (@suffixes) {
        $mime_types{".$suffix"} = $type; # e.g " $mime_types{.png} = "image/png"
      }
    }
    close MIME;
  }
  else {
    logmsg(
      (
        $mime_types
        ? "Couldn't read MIME types file $mime_types."
        : "No MIME types configured"
      )
      . " Using a minimal set instead"
    );
    %mime_types = (
      ".gif"  => "image/gif",
      ".jpg"  => "image/jpeg",
      ".htm"  => "text/html",
      ".html" => "text/html"
    );
  }

  if ($use_authentication) {    # read passwords
    open PASS, $password_file
      or log_and_die "Couldn't read password file $password_file: $!\n";
    while (<PASS>) {
      s/\s//g;
      next if /^#/;             # comments in a passwd file? Hmmm...
      my ( $name, $encrypted_password ) = split /:/;
      $encrypted_passwords{$name} = $encrypted_password
        if $encrypted_password;
    }
    close PASS;

    # initialise directory hashes
    foreach my $dir (@public_directories)  { $public{$dir}  = 1; }
    foreach my $dir (@private_directories) { $private{$dir} = 1; }
  }

  unless ( $when_to_fork == $never_fork ) {
    logmsg "Setting SIG{CHLD} to 'IGNORE'";
    $SIG{CHLD} = 'IGNORE'
      ; # We don't care about children's exit status, we just don't want zombies
  }

}

sub main_loop {

  # Standard Perl incantation for creating a server socket:
  my $tcp = getprotobyname('tcp');
  socket( Server, PF_INET, SOCK_STREAM, $tcp ) or log_and_die "socket: $!";
  setsockopt( Server, SOL_SOCKET, SO_REUSEADDR,
    pack( "l", 1 ) )    # to prevent "address in use" errors
    or $OSNAME =~ /EPOC/i or logmsg " Warning: setsockopt: $!";
  if ( not bind( Server, sockaddr_in( $port, INADDR_ANY ) ) ) {
    log_and_die(
      $port < 1024
      ? " bind: $! (ports below 1024 require root privs on unix-like systems)\n"
      : "bind: $!\n"
    );
  }
  listen( Server, SOMAXCONN ) or log_and_die " listen: $!";
  logmsg
    "Server started on port $port.\n\nPoint your browser at http://$HOSTNAME"
    . ( $port == 80 ? "" : ":$port" );

CONNECT:
  for ( ; accept( Client, Server ) ; close Client ) {

    my $remote_sockaddr = getpeername(Client);
    my ( undef, $iaddr ) = sockaddr_in($remote_sockaddr);
    my $peername = gethostbyaddr( $iaddr, AF_INET ) || "localhost";
    my $peeraddr = inet_ntoa($iaddr) || "127.0.0.1";

    my $local_sockaddr = getsockname(Client);
    my ( undef, $iaddr_local ) = sockaddr_in($local_sockaddr);
    $localname = gethostbyaddr( $iaddr_local, AF_INET ) || "localhost";
    my $localaddr = inet_ntoa($iaddr_local) || "127.0.0.1";

    $INPUT_RECORD_SEPARATOR =
      "\n";    # input record separator should be \n here (the default)
    $OUTPUT_AUTOFLUSH = 1;

    chomp( $_ = <Client> );    # get Request-Line
    my ( $method, $url, $proto, undef ) =
      split;                   # parse it

    if ( not $proto ) {        # Whoa! HTTP 0.9 here
      print Client
"<html><head></head><body> <H1>This server doesn't speak HTTP 0.9!</H1> </body></html>";
      next CONNECT;
    }
    $url =~ s#\\#/#g;          # rewrite bla\sub as bla/sub
    logmsg "<- $peername: $_";
    my ( $abs_path, undef, $arglist ) =
      ( $url =~ /([^?]*)(\?(.*))?/ );    # split at ?

# An "absolute path" in RFC 1945-speak denotes a file *relative* to the server root!
    if ( $abs_path !~ m#^/# ) {
      logmsg "Whoa! an absolute path should begin with a slash /";
      $abs_path = "/$abs_path";
    }

    my $path_info;
    if ( not $arglist and $abs_path =~ m#(.*?\.cgi)/(.+)#i ) {
      redirect("$1?$2");
      next CONNECT;
    }
    my $abs_path_escaped = $abs_path;    # keep a copy of filename with escapes
    $abs_path =~ s/%([\dA-Fa-f]{2})/chr(hex($1))/eg;    # %20 -> space

    fork_if_necessary($abs_path)
      and next CONNECT
      ; # if we have indeed forked, the child will handle the request and we can move on...

    if ( $method !~ /^(GET|POST|HEAD)$/ ) {
      logerr 501, "I don't understand method $method";
      exit if $I_am_child;
      next CONNECT;
    }

    my ( $user, $passphrase );
    $ENV{USER_AGENT} = $ENV{CONTENT_LENGTH} = $ENV{CONTENT_TYPE} = undef;
    while (<Client>)
    {    # gobble up all remaining headers and notice the relevant ones:
      s/[\r\l\n\s]+$//;
      /^User-Agent: (.+)/i              and $ENV{USER_AGENT}     = $1;
      /^Content-length: (\d+)/i         and $ENV{CONTENT_LENGTH} = $1;
      /^Content-type: (.+)/i            and $ENV{CONTENT_TYPE}   = $1;
      /^Authorization:\s+Basic\s+(.+)/i and $passphrase          = $1;

      if (/^HTTP-(.+?): (.+)/i)
      {    # any header like HTTP-Blah-Gurgle is put in BLAH_GURGLE
        my $environment_variable = uc($1);
        $environment_variable =~ s/-/_/g;
        $ENV{$environment_variable} = $2;
      }

      # We don't honour If-Modified-Since
      last if (/^$/);

    }

    if ($use_authentication) {
      $user = authorized( $abs_path, $passphrase );
      if ( not defined $user )
      {    # $abs_path is private, and authentication failed
        challenge( "p5httpd", $abs_path );
        exit if $I_am_child;
        next CONNECT;
      }
    }
    if ( -d "$server_root$abs_path" ) {
      unless ( $abs_path =~ m#/$# ) {    # does $abs_path end with a slash ?
        redirect("$abs_path/");          # no? redirect to $abs_path/
        exit if $I_am_child;
        next CONNECT;
      }

      # we can from now on assume that $abs_path ends with a slash

      my $do_listing = 1;
      foreach my $index (@index_filenames)
      {                                  # check for existence of an index page
        if ( -f "$server_root$abs_path$index" ) {
          $abs_path .= $index;
          $do_listing = 0;
          last;
        }
      }
      if ($do_listing) {                 # no index found, do directory listing
        directory_listing($abs_path);
        exit if $I_am_child;
        next CONNECT;
      }
    }    # if (-d "$server_root$abs_path"

    if ( not -r "$server_root$abs_path" ) {    # check for existence of abs_path
      logerr 404, "$abs_path: $!";
      exit if $I_am_child;
      next CONNECT;
    }

    print Client "HTTP/1.0 200 OK\n";          # probably OK by now

    my $mime_type = filetype($abs_path);

    my $handler = $handlers{$mime_type};

    if ($handler) { # call handler
      $arglist = "file=$abs_path";
      $abs_path = "/cgi-bin/$handler";
      $mime_type = "application/cgi";
      $url = "$abs_path?$arglist";
      $method = "GET";
    }

    if ( $mime_type eq "application/cgi" )
    {    # cf. the specification at http://hoohoo.ncsa.uiuc.edu/cgi/env.html
      $ENV{SERVER_SOFTWARE}   = "p5httpd/$version";
      $ENV{SERVER_NAME}       = $localname;
      $ENV{GATEWAY_INTERFACE} = "CGI/1.1";
      $ENV{SERVER_PROTOCOL}   = $proto;
      $ENV{SERVER_PORT}       = $port;
      $ENV{REQUEST_METHOD}    = $method;
      $ENV{PATH_INFO}         = $path_info;

      #     $ENV{PATH_TRANSLATED}   = Ehrrm....??
      $ENV{SCRIPT_NAME}     = $abs_path;
      $ENV{QUERY_STRING}    = $arglist;
      $ENV{REMOTE_HOST}     = $peername;
      $ENV{REMOTE_ADDR}     = $peeraddr;
      $ENV{AUTH_TYPE}       = ( $use_authentication ? "Basic" : "" );
      $ENV{REMOTE_USER}     = ( $use_authentication ? $user : "" );
      $ENV{SERVER_URL}      = "http://$localname:$port/";
      $ENV{SCRIPT_FILENAME} = "$server_root$abs_path";
      $ENV{REQUEST_URI}     = $url;
      $ENV{SERVER_ROOT} = $server_root;    # non-standard?

      if ( $method =~ /POST/ ) {
        logmsg
          "<- Content-length: $ENV{CONTENT_LENGTH}, type: $ENV{CONTENT_TYPE}";
      }
      cgi_run( $abs_path, $arglist, $method );
      exit if $I_am_child;
      next CONNECT;
    }


    cat $abs_path, $mime_type, $method || logerr 500, "$abs_path: $!";
    exit if $I_am_child;
    next CONNECT;
  }
  log_and_die "$$ Fatal error: accept failed: $!\n";  # This should never happen
}

#################### other subroutines ####################

# fork_if_necessary() inspects  $when_to_fork and forks when it thinks it should.
# This may involve keeping track of cgi script invocations when
# $when_to_fork == $fork_after_first_invocation
# Return value: 0 in child, when forking is not necessary, or after failure;
# child pid in parent

sub fork_if_necessary {
  my ($file) = @_;
  my $pid = 0;
  if (    # always fork, or second or later invocation of .cgi script?
    $when_to_fork == $fork_always
    or ( $when_to_fork != $never_fork
      and ( filetype($file) ne "application/cgi" or $cgi_urls{$file}++ ) )
    )
  {
    eval {$pid = fork()};
    if ( $@ or  $pid < 0 ) {
      warn
        "Couldn't fork now and won't try again (can your OS ever do it?): $@";
      $when_to_fork = $never_fork;
      return 0;
    }
    $I_am_child = 1 unless $pid;
  }
  return $pid;
}

# logmsg "Couldn't frob the gnargle: $!"; logs a time-stamped message,
# folowed by newline, to STDERR. No return value.

sub logmsg ($) {
  my ($text) = (@_);
  my $fulltime = localtime();
  my $PID = sprintf "%5d", $$;
  my ($hms) = ( $fulltime =~ /(\d\d:\d\d:\d\d)/ );
  my @text = split /\n/, $text;
  foreach my $line (@text) {
    print STDERR "$PID $hms $line\n";
  }
}

sub log_and_die ($) {
  my ($text) = (@_);
  logmsg "FATAL: $text";
  die "\n";
}

# logerr 404, "No gnargles here, sorry!"; signals error to browser,
# logging it to STDERR as well.  No return value.

sub logerr ($$) {
  my ( $code, $detail ) = @_;
  my %codes = (
    200 => 'OK',
    400 => 'Bad Request',
    403 => 'Access Denied',
    404 => 'Not Found',
    500 => 'Internal Server Error',
    501 => 'Not Implemented',
  );
  my $msg = "$code " . $codes{$code};
  logmsg "-> $msg $detail";
  print Client <<EOF;
    HTTP/1.0 $msg
    Content-type: text/html

    <html><body>
    <h1>$msg</h1>
    <p>$detail</p>
    <hr>
    <p><I>p5httpd/$version server at $localname port $port</I></p>
    </body></html>
EOF
}

# cat "relative/path", "text/html", $method; writes the appropriate
# response headers to STDOUT. If $method == GET (which is the default)
# then the file is dumped on STDOUT as well.

sub cat($$;$) {
  my ( $file, $mimetype, $method ) = @_;
  $method = "GET" unless $method;
  my $fullpath = "$server_root$file";

  my ( undef, undef, undef, undef, undef, undef, undef, $length, undef, $mtime )
    = stat($fullpath);
  $mtime = gmtime $mtime;
  my ( $day, $mon, $dm, $tm, $yr ) =
    ( $mtime =~ m/(...) (...) (..) (..:..:..) (....)/ );

  print Client "Content-length: $length\n";
  print Client "Last-Modified: $day, $dm $mon $yr $tm GMT\n";
  print Client "Content-type: $mimetype\n\n";
  my $sent = 0;
  if ( $method eq "GET" ) {
    local $INPUT_RECORD_SEPARATOR = undef;   # gobble whole files, but only here
    open IN, "<$fullpath" || return 0;
    my $content = <IN>;
    close IN;
    $sent = length($content);
    print Client $content;
  }
  logmsg "-> 200 OK $file: $sent bytes sent as $mimetype";
  return 1;
}

# cgi_run("relative/path.cgi", "encoded%20arglist", $method) changes to directory
# where script lives, and then either evals or executes it.

sub cgi_run {
  my ( $script, $arglist, $method ) = @_;
  my ($dir) = ( $script =~ /^(.*\/)/ );
  my $script_path = "$server_root$script";
  my $script_text;
  chdir "$server_root$dir"
    or return logerr 500, "Cannot chdir to $server_root$dir: $!";
  $script_path =~ s/[A-Z]://;

# command line decoding, cf description at http://hoohoo.ncsa.uiuc.edu/cgi/cl.html:
  local @ARGV;
  unless ( $arglist =~ /=/ ) {
    $arglist =~
      s/%([\dA-Fa-f]{2})/chr(hex($1))/eg;    # decode arglist, e.g. %20 -> space
    @ARGV = split /\s+/, $arglist;
  }
  my $file_tastes_like_perl = 1;
  if ( $eval_or_execute != $cgis_are_executed ) {

    open CGI, $script_path or return logerr 500, "Cannot read $script_path: $!";
    my ( $script_text, $nread );
    if ( $eval_or_execute == $only_perl_is_evaled ) {
      logmsg "sniffing and tasting $script...";
      $nread = read CGI, $script_text, 100, 0;    # taste first 100 bytes
      defined $nread
        or return logerr 500, "Read error reading $script_path: $!";
      if ( $script_text !~ /#!.*perl/i )
      {    # No #!/.../perl? Then it's not a perl script.
        logmsg "yeachh! $script doesn't taste like perl!";
        close CGI;
        $file_tastes_like_perl = 0;
      }
    }
    if ($file_tastes_like_perl) {
      {
        local $INPUT_RECORD_SEPARATOR = undef;    # gobble rest of $script
        $script_text .= <CGI>;
      }
      close CGI;
      logmsg "-> eval'ing $script_path";
      my $package_name = $script;  # most CGI's dont bother to set package name.
      $package_name =~    # mangle filename into package name in order to
        s/\W/_/g;         # avoid variable name clashes when in non-forking mode
      eval <<EOF;
        local *STDIN = *Client;
        local *STDOUT = *Client;
        package $package_name;
        no strict;
        $script_text
EOF
      $@ and logerr 500, "in $script:<br>  <pre>$@</pre>";
    }
  }
  if ( $eval_or_execute == $cgis_are_executed or not $file_tastes_like_perl ) {
    -x $script_path or logerr 500, "Cannot execute $script_path: $!";
    local $ENV{CHLD} = 'DEFAULT';

    logmsg "-> exec'ing $script_path";
    my ( $pid, $cgi_out, $cgi_in, $output, $errors );
    my $parent_pid = $PID;
    eval { $pid = open2( $cgi_out, $cgi_in, $script_path, "" ) }; # the extra "" avoids the shell
    if ($@) {    # we may be kid here from open2's fork(). Weird...
      logmsg "(NB: note my PID!) When trying to execute $script:";
      chomp($@);
      logmsg $@;
      exit 0 unless $PID == $parent_pid;
    }
    else {
      if ( $method =~ /POST/i ) {
        read( Client, $_, $ENV{CONTENT_LENGTH} );
        local $SIG{PIPE} = 'IGNORE';    # avoid choking on broken pipe
        print $cgi_in $_;               # .. when tring to talk to a dead kid.
      }
      close $cgi_in;
      {
        local $INPUT_RECORD_SEPARATOR = undef;    # slurp!
        $output = <$cgi_out>;
      }
      close $cgi_out;
      waitpid( $pid, 0 );
      if ( $output =~ m#^\r?Content-Type:.*?\r?\n\r?\n#mi or  $output =~/^\r?Status:\s+302/ ) {
        print Client $output;
      }
      else {    # Capturing scripts stderr with open3 would be just too painful
                # (deadlock problems) so we're almost as unhelpful as apache!
	print STDERR $output;
        logerr 500,
          "Premature end of script headers."
          . ( $? ? "<br> Status: $?" : "" )
          . "<br>Have a look at server log for stderr output of $script";
      }
    }
  }
  chdir $server_root;
}

sub directory_listing {
  my ($dir) = @_;
  $dir =~ s#//#/#g;
  chdir "$server_root$dir"
    or return logerr 500, "Cannot chdir to $server_root$dir: $!";
  my @files = glob("*");
  @files = sort @files;
  $dir eq "/" or @files = ( "..", @files );
  print Client <<EOF;
HTTP/1.0 200 OK
Content-type: text/html

   <html>
   <head><title>$dir</title></head>
   <body>
   <h1>$dir</h1>
   <pre>
EOF
  foreach my $file (@files) {
    print_direntry($file);
  }
  print Client <<EOF;
    </pre>
    <hr>
    <p><I>p5httpd/$version server at $localname port $port</I>
    </body>
    </html>
EOF
  logmsg "-> 200 OK listing $dir";
}

sub filetype {
  my ($relpath) = @_;
  $relpath eq '..' and return "folder/parent";
  -d $relpath and return "folder/normal";
  ( cwd . "/$relpath" ) =~ /$cgi_scriptname_regexp/i
    and return "application/cgi";
  my ($suffix) = ( $relpath =~ /(\.\w+)$/ );
  my $type = $mime_types{ lc($suffix) };
  $type ||= "text/plain";
  return $type;
}

sub print_direntry {
  my @months = qw(Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec);
  my ($file) = @_;
  my ( undef, undef, undef, undef, undef, undef, undef, $size, undef, $mtime ) =
    stat $file;
  my ( $icon, $type );
  if ($show_icons) {
    $type = filetype($file);
    $type =~ s/\//_/g;
    -r "$server_root/$icondir/$type.gif" or $type = "unknown";
    $icon = "$icondir/$type.gif";
    $icon = ( -r "$server_root/$icon" ? "<img src=\"/$icon\">" : "" );
  }
  my $filename = ( $file eq ".." ? "Parent directory" : $file );
  $filename = (
    length($filename) > 18
    ? sprintf( "%18.18s", $filename ) . ".."
    : $filename
  );
  $filename .= "/" if $type eq "folder_normal";
  my ( $x, $min, $hour, $mday, $mon, $year ) = localtime $mtime;
  $year += 1900;
  $min  = sprintf "%2.2d", $min;
  $hour = sprintf "%2.2d", $hour;
  my $date = "$mday-$months[$mon]-$year $hour:$min";
  my $spacing = " " x ( 25 - length($filename) );
  printf Client "%s <a href=\"%s\">%s</a>%s  %20.20s   %8.8s\n", $icon, $file,
    $filename, $spacing, $date, $size;
}

sub redirect {
  my ($redir) = @_;
  print Client "HTTP/1.0 301 Moved Permanently\nLocation: $redir\n\n";
  logmsg "-> 301 Moved Permanently to $redir";
}

sub challenge {
  my ( $realm, $file ) = @_;
  print Client
"HTTP/1.0 401 Access Denied\nContent-type: text/html\nWWW-Authenticate: Basic realm=\"$realm\"\n\n";
  logmsg "-> Authentication requested for $file";
}

sub authorized {
  my ( $file, $passphrase ) = @_;
  my $parent = $file;
  do {    # check whether $file is public or private
          # by stripping away final path components until
    return ""
      if $public{
      "$parent/"};    # either a public or a private directory is reached
    goto PROTECTED
      if $private{"$parent/"};    # "last" would test the wile clause once more
  } while ( $parent =~ s#/[^/]*$## );
PROTECTED:
  logmsg "checking password";
  $passphrase =~ tr#A-Za-z0-9+/##cd;     # remove non-base64 chars
  $passphrase =~ tr#A-Za-z0-9+/# -_#;    # convert to uuencoded format
  my $len = pack( "c", 32 + 0.75 * length($passphrase) );  # compute length byte
  my $decoded = unpack( "u", $len . $passphrase );         # uudecode and print
  my ( $name, $password ) = split /:/, $decoded;

  if ( my $encrypted_password = $encrypted_passwords{$name} ) {
    return $name
      if crypt( $password, $encrypted_password ) eq
      $encrypted_password;                                 # check password
  }
  return undef;                                            # failed
}

__END__


=head1 NAME

p5httpd - tiny perl http server

=head1 SYNOPSIS

path/to/p5httpd.pl (or click on the icon)

=head1 DESCRIPTION

p5httpd is a simple HTTP 1.0 server written as a single perl
file. Written for use on a hand-held machine, it should be useful on
any machine as a quick and dirty, non-secure webserver for occasional
use.

Understands PUT, GET, and HEAD, can do basic authentication and
directory listings. CGI scripts can be executed or, if they are perl
scripts, eval'ed.



=head1 INSTALLATION AND CONFIGURATION

p5httpd.pl is a single file, containing a small configuration section
at the beginning, and this POD documentation at the end. This single
file, unedited, is already functional, but it will be more useful if
you unzip the whole distribution and edit the first few lines of the
server program to adapt it to your installation

=head1 FORKING POLICY

Unix servers typically use fork() in order to be ready for the next
request as soon as possible, delegating the hard work to a child
process. This may result in better performance (e.g. when requesting a
page with a lot of images), but perl CGI scripts will have to load all
their modules every time they're run.

A non-forking server will run all scripts in the same interpreter
process, an thus will have to load the modules ony once. For
heavyweight modules like CGI.pm this may make a big difference.

p5httpd can be configured (with the config variable $when_to_fork) to
fork always, never, or always except the first time a particular
script is run.  This last policy combines the advantages of the
always-forking and never-forking policies, as the server (and hence
its children) will have the script's required modules loaded after its
first (non-forking) run. In this case, expensive re-initialisations
can also be avoided.

=head1 EVAL OR EXECUTE?


cgi scripts can be executed as a separate process, or they can be run
(eval'ed) in the same interpreter as the server, if they are written
in perl. You can configure the sever (with the config variable
$eval_or_execute) to always execute, or always eval cgi scripts. It
can also look at the script and try to find out whether it is perl (it
then looks for the slashbang pattern #!/.../perl).


=head1 SECURITY AND AUTHENTICATION

p5httpd should not be used when security is critical. It can only use
the "Basic" authentication scheme, where usernames and passwords are
sent unencrypted over the network. It uses the same htpasswd files as
apache (use the htpasswd (1) program, or
http://www.euronet.nl/~arnow/htpasswd/ to generate them).

A list of public directories and another list of private directories
(in the config variables @public_directories and @private_directories)
determines when authentication is requested: for any file access,
p5httpd climbs up the directory tree until it finds a directory in
either list (the public list is tried first)

=head1 PATH INFO

As a workaround for a bug in EPOC Opera (which will not reliably POST
to an URL of the form /path/to.cgi?args) any requests to
/path/to.cgi/args are redirected to /path/to.cgi?args. This is I<not>
path info as per HTTP/1.0, and PATH_INFO will not be set.


=head1 CGI SCRIPT PITFALLS WITH p5httpd

Depending on the forking policy,and whether cgi's are eval'ed or
executed, you may have to take some care when writing your scripts.
When all cgi's are executed, and/or when the server forks for evey
request, your scripts execute with "a clean slate" every time. This is
the setting to use whenever you use cgi's that normally run on
e.g. apache, at least initially, before you try the more dangerous
(but possibly faster) settings.

On the other extreme, when you evaluate your scripts and never fork(),
(which is the only setting that works on EPOC/psion), there are a
couple of things to watch out for:

=over 4





=item scope issues

All CGI scripts run in a separate namespace, derived from the script
name. Just as with e.g. mod_perl, package globals remain defined
across invocations. This may be very useful in some situations
(e.g. for preserving an expensive initialisation), but you should be
aware of it. Unless you know what you're doing, take the following
advice from the mod_perl FAQ:

I<Properly scope your variables. Stop and read that sentence
again. Conventional CGI scripts can be as sloppy with their namespace
as they want, since they are restarted anew for each request. Your
mod_perl script has a much longer lifetime (potentially as long as
your [...] server is running), and requires much more care. Scope
everything except long-lived variables with my() and use strict; so
Perl will demand that you recognize your global variables.>

I<Localize global variables. If you change any of Perl's global
variables (e.g. $/ to change the input record separator), or even your
own global variables remember to reset them or better still, always
localize global variables before using them, e.g. local($/) =
undef. If you can, reduce your dependency on global variables>


=item die() and exit()

If you call C<exit()> in your script, the whole server will quit
(C<die()> will just print an error message). CGI scripts may hang, or
even crash, the server. Filehandles remain open across invocations.

=item CGI.pm

If you use the C<CGI.pm> package, you have to use the (undocumented)
subroutine C<CGI::initialize_globals()> to get it to re-read the script
parameters.  If you don't, the script will only read them the first
time it runs.

=back

The server does a C<chdir> to a script's directory before running it,
and sets the environment variable SERVER_ROOT to the absolute pathname
of the server root directory.


=head1 REQUIRES

p5httpd needs perl 5.6.0 or newer It works
on machines that cannot fork() (like Psion handhelds) but it can use
fork() if available. Needs the IPC::Open2 module whenever a cgi should
be executed (not eval'ed). This module may only be present on
Unix-like systems.


=head1 CREDITS

Originally based on phttpd (pure perl httpd, (C) Paul Tchistopolskii
1998, 99 The Wiki packaged with this server is based on QuickiWiki (C)
Copyright 1999-2000 Ward Cunningham.

=head1 AUTHOR

Hans Lub. Bug reports to hlub@knoware.nl


=head1 COPYRIGHT

Copyright (c) 2002-2004 Hans Lub. This program is free software; you
can redistribute it and/or modify it under the same terms as
 Perl itself

=cut

# Local Variables:
# mode: cperl
# End:













