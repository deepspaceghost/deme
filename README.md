# Deme
- ----

Deme (short for Demeter) is an exercise in a natural language processing
and computational linguistics. Current development is focused on increasing
Deme's ability to interact with human language. Features in development are
labeled as "[name]-deme-feature."

## Table of Contents
-- ----- -- --------

- [Getting Started](#getting-started)

## Getting Started
-- ------- -------

First, get the code on your system. The simplest method is via git ([git installation instructions](https://gist.github.com/derhuerst/1b15ff4652a867391f03)):
- `cd ~/`
- `git clone https://github.com/deme-app/deme-app.git`
- `cd deme-app`
- `bash dev_setup.sh` (still a work in progress)

This script sets up dependencies and a [virtualenv][about-virtualenv]. If running in an environment besides Ubuntu/Debian, Arch, or Fedora you may need to manually install packages as instructed by dev_setup.sh.

[about-virtualenv]:https://virtualenv.pypa.io/en/stable/

NOTE: The default branch for this repository is "main", which should be considered a work-in-progress. It's also the most stable version.

## REQUIREMENTS
-- ------------

* discord.py==1.7.1
* Flask==1.1.2
* geopy==2.1.0
* google==3.0.0
* python-dotenv==0.17.1
* randfacts==0.5.0
* requests==2.25.1


## MAINTAINER(S)
-- -----------

Current maintainer(s):
* deepspaceghost - https://github.com/deepspaceghost
