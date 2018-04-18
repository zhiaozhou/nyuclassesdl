[![PyPI version](https://badge.fury.io/py/nyuclassesdl.svg)](https://badge.fury.io/py/nyuclassesdl)

nyuclassesdl
=====
_Developer: Zhiao Zhou ([@zhiaozhou](https://github.com/zhiaozhou) | <zz1749@nyu.edu> | [Linkedin](https://www.linkedin.com/in/zhiaozhou/))_ 

nyuclassesdl is a python library for automatically downloading files from NYU Classes learning management system. And it's only available to NYU students or faculties.

Now it can only download every file of all of your classes just like a git clone

Dependencies
=============
pgmpy has following non optional dependencies:
- Python 2.7 or Python 3
- argparse 
- selenium 
- urllib
- Geckodriver for Firefox users

Installation
=============
Using pip:
```
$ pip install nyuclassesdl
```

Or for installing the latest codebase:
```
$ git clone https://github.com/zhiaozhou/nyuclassesdl.git
$ cd nyuclassesdl/
$ python setup.py install
```

Documentation and usage
=======================

Now this package can be only used with a Firefox browser installed.

Then you will have to install Geckodriver from [Geckodriver/releases](https://github.com/mozilla/geckodriver/releases) and then put the executable file inside the root folder of your Firefox directory (Ex. C:\Program Files\Mozilla Firefox\)

For Mac users, put it under usr/local/bin

Then after installing the package using pip
you can start to use it by typing nyuclassesdl [argument]

| Argument | Description |
| :--: | :--: |
| --MFA | choose a way for MFA: now only "duo" is supported |
| --dir | choose a directory to download the files(Optional) |
| --un | NYU netid |
| --ps | NYU password |

License
=======
NYU-Classes-downloader is released under MIT License.