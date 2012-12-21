Mustache Generator
===========

About
------
A command line tool to join a config file with a mustache template

Usage
------

```
$ MustacheGen.py --help
Usage: MustacheGen.py [options]

Options:
  -h, --help            show this help message and exit
  -c FILE, --config=FILE
                        load the config from the FILE
  -t FILE, --template=FILE
                        load the template from the FILE
  -q, --quiet           don't print status messages to stdout
```

###Example###

```
MustacheGen -c /path/to/config.json -t /path/to/template.ms > output.ext
```


Config Files
------
The configuration files should contain JSON data.

###Examples###

####people.json####
```
{
    "people": [
        {
            "name": "Joe",
            "dob": {
                "month": 3,
                "day": 11,
                "year": 1880
            }
        },
        {
            "name": "Dirt",
            "dob": {
                "month": 7,
                "day": 4,
                "year": 1671
            }
        }
  ]
}

```

Template Files
------
The template files should be writen in Mustache template format, click [here](http://mustache.github.com/) for documentation

###Examples###

####people.ms####
```
{{#people}}
Hi {{name}}, your date of birth is {{dob.month}}/{{dob.day}}/{{dob.year}}
{{/people}}

```

Dependencies
--------

###pystache###

This project uses the [Python Implementation](https://github.com/defunkt/pystache) of Mustache to generate output

Platform
--------
<b>Language</b>:Python

###Testing Environment###

####1####
- <b>Operating System</b>: OSX Mountain Lion
- <b>Python Version</b>: Python 2.7.2
