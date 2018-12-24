#!/usr/bin/env python
import os
from os import system
import MySQLdb
from sys import argv
import getopt
from repo_handler import create_repo_handler

def unmarshal_reponame(reponame):
    ret = "";
    if (reponame[0] != "_"):
        repos = reponame;
    else:
        repos = reponame[1:];
    for c in repos:
        if (c == "_"):
            ret +="/";
        else:
            ret += c;
    return ret;

#opts, args = getopt.getopt(argv[1:], "", ["dbhost=", "passwd=", "user=", "github-user=", "github-passwd=", "nomsg"]);
dbhost = "127.0.0.1";
user = "root";
passwd = "genesis";
github_user = "";
github_passwd = "";
nomsg = False;
#for (o, a) in opts:
#    if (o == "--dbhost"):
#        dbhost = a;
#    if (o == "--passwd"):
#        passwd = a;
#    if (o == "--user"):
#        user = a;
#    if (o == "--github-user"):
#        github_user = a;
#    if (o == "--github-passwd"):
#        github_passwd = a;
#    if (o == "--nomsg"):
#        nomsg = True;
#
#d = args[0];
res = {};
revset = set();
#for root, dirs, files in os.walk(d):
#    for fname in files:
#        if (fname.find("_revs") == -1):
#            continue;
#        f = open(root + "/" + fname);
#        lines = f.readlines();
#        rurl = fname[0:len(fname) - 5];
#        res[rurl] = [];
#        for line in lines:
#            if not (line.strip() in revset):
#                res[rurl].append(line.strip());
#                revset.add(line.strip())
#        f.close();
#
#diff = 0;
conn = MySQLdb.connect(user = user, host = dbhost, passwd = passwd, db = "genesis");

cursor = conn.cursor()
databases = ("show tables")
cursor.execute(databases)
#for (databases) in cursor:
#         print databases[0]
#
result = cursor.fetchall()

for i in range(len(result)):
        print(result[i])
sql = "SELECT * FROM application" 
cursor.execute(sql)  
results = cursor.fetchall()  
print len(results);
sql = "SELECT * FROM patch" 
cursor.execute(sql)  
results = cursor.fetchall()  
print len(results);
for j in range(len(results)):
      if '9e7b13' in results[j][2]:
          print results[j];
          
      
sql = "SELECT * FROM testcase" 
cursor.execute(sql)  
results = cursor.fetchall()  
print len(results);


conn.close();

