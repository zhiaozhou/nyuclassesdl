[![PyPI version](https://badge.fury.io/py/nyuclassesdl.svg)](https://badge.fury.io/py/nyuclassesdl)

nyuclassesdl
=====
_Developer: Zhiao Zhou ([@zhiaozhou](https://github.com/zhiaozhou) | <zz1749@nyu.edu> | [Linkedin](https://www.linkedin.com/in/zhiaozhou/))_ 

nyuclassesdl is a python library based on Python Selenium package for automatically downloading files from NYU Classes learning management system. And it's only available to NYU students or faculties.

Now it can only download every file of all of your classes just like a git clone

Dependencies
=============
pgmpy has following non optional dependencies:
- Python 2.7 or Python 3
- argparse 
- selenium 
- urllib
- Geckodriver for Firefox users
- Chromedriver for Chrome users

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

Now this package can be only used with a Chrome browser installed. (Firefox is not supported due to some bugs inside Geckodriver)

Then you will have to install Geckodriver from [Geckodriver/releases](https://github.com/mozilla/geckodriver/releases) if you are using Firefox or chromedriver from [Chromedriver](https://sites.google.com/a/chromium.org/chromedriver/downloads) and then put it in a specific directory

Then after installing the package using pip
you can start to use it by typing nyuclassesdl [argument]
If you don't understand plz check the example gif below

| Argument | Description |
| :--: | :--: |
| --MFA | choose a way for MFA: now only "duo" is supported |
| --dir | choose a directory to download the files(Optional) |
| --un | NYU netid |
| --ps | NYU password |
| --browser | Your choice of browser used here (Optional since the default is chrome) |
| --cls | You can now select a class to download its files instead of downloading all (Optional if None you will download all) |
| --exe | The path of your driver executable file (Ex. "D:/googledriver.exe") |

![example](example.gif)

License
=======
NYU-Classes-downloader is released under MIT License.