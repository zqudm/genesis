#!/usr/bin/env python
from urllib2 import urlopen
from urllib2 import HTTPError
from bs4 import BeautifulSoup
from sys import argv
from os import system
import random
import time
import subprocess

p=subprocess.Popen(["git", "log" ],cwd="Avengers", stdout=subprocess.PIPE)

[out,err]= p.communicate();

#print out
