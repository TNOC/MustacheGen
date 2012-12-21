Mustache Generator
===========

About
------
A command line tool to join a config file with a mustache template

Usage
------
MustacheGen -c /path/to/config.json -t /path/to/template.ms > output.ext

Config Files
------
The configuration files should contain JSON data.

Template Files
------
The template files should be writen in Mustache template format, click [here](http://mustache.github.com/) for documentation

##Implementation##
This project uses the [Python Implementation](https://github.com/defunkt/pystache) of Mustache to generate output

Dependencies
--------

###pystache###

Platform
--------
<b>Language</b>:Python

###Testing Environment###

####1####
- <b>Operating System</b>: OSX Mountain Lion
- <b>Python Version</b>: Python 2.7.2
