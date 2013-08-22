Introduction
============

IPIP-NEO is essentially a professional grade psychological personality test
suite, which is used in research as well as actual clinical environments.

Motivation
==========

The current version suffers from a number of "technical" problems, like,

- It is written in Perl. Enough said.

- It uses very old-school CGI techniques.

- It has no features for collaboration and data analysis.


Requirements
=============

1. IPIP-NEO-ng should be able to work in OFFLINE mode.

   Many hospitals do not have internet or even network connectivity at all. In
   fact, majority of the hospitals actively avoid internet connectivity on
   internal systems for security and privacy reasons.

2. IPIP-NEO-ng should be PORTABLE.

   It should run EVERYWHERE possible (from old Windows XP systems to modern
   Linux systems).

   IPIP-NEO-ng tests should run on ALL browsers (including Internet Explorer 6).

3. IPIP-NEO-ng should have PERSISTENCE.

   It should be able to save test data and results.

4. IPIP-NEO-ng should have a TEST SUITE.

   In fact, a test suite should be implemented before the actual porting takes
   place. After all, we need to verify that the new port does not break
   anything.

Pros
====

1. This project is NOT a typical undergrad project (most of which are "toys"
   written to be thrown away). This project aims to delive a professional
   software which will be heavily used by researchers and health-care
   professionals all over the world.

2. You will get familiar with industry standard "tools" like Python, Git.
