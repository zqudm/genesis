#!/usr/bin/env python
import MySQLdb
from sys import argv
from urllib2 import urlopen
from bs4 import BeautifulSoup
import getopt
from os import system, path,chdir, getcwd
from repo_handler import prepare_casedir
import zipfile




def get_dir_of_zip(zipf):

     zf = zipfile.ZipFile(zipf, 'r')
     maindir = zf.namelist()[0];
 
     return maindir.split("/")[0]


def get_name_of_project(url):
    comps = url.split("/")
    return comps[len(comps)-1];


def showcases(numid,o):
  host = "127.0.0.1";
  user = "root";
  passwd = "genesis";
  if (o=="--np"):
      t = "for_npe_test";
  if (o == "--host"):
      host = a;
  if (o == "--user"):
      user = a;
  if (o == "--passwd"):
      passwd = a;
  if (o == "--oobcase"):
      t = "for_oob_test";
  if (o == "--ccecase"):
      t = "for_cce_test";
  
  db = MySQLdb.connect(user = user, host = host, passwd = passwd, db = "genesis");
  c = db.cursor();
  c.execute("""SELECT patcht.id, patcht.github_prepatch_rev, patcht.github_postpatch_rev, \
            application.github_url FROM (SELECT * from patch where """ + t + """ = 1) as patcht \
            LEFT JOIN application ON patcht.app_id = application.id;""");
  case_id = int(numid);
  #ioutdir = args[1];
  if (case_id <= 0):
      print "Must be a positive id!";
      exit(1);
  if (case_id > c.rowcount):
      print "Maximum case id: ", c.rowcount;
      exit(1);
  #system("rm -rf " + args[1]);
  #system("mkdir " + args[1]);
  cnt = 0;
  for row in c:
      cnt += 1;
      if (case_id != cnt):
          continue;
      patchid = row[0];
      prerev = row[1];
      postrev = row[2];
      url = row[3];
      print  patchid,prerev,postrev,url 
      #system("wget --spider https://github.com" + repoaddr + "/archive/master.zip")
      soup = BeautifulSoup(urlopen(url), 'lxml');
      #for link in soup.find_all('a',href=True, text='Download ZIP'):
      #  linkstr = link['href'];
      #  print linkstr
      link = soup.find_all('a')
      for l in link:
          content =l.string
          if not content is None:
                  title = content.strip()
                  if title =='Download ZIP':
                     href= l['href']
                     break;
      prefix= href[href.index("archive"):len(href)]
      zipname= href[href.rfind("/")+1:len(href)];
      #zipname= href[href.rfind('/',len(href),0),len(href)]
      linkall = url+"/"+prefix    #print index(content, 'Zip')          
      ret = system("wget --spider "+ linkall+ "  1>/dev/null 2>&1");
      ##print ret;
      if ret ==0:
          down_ret = system("wget " + linkall );
          if down_ret != 0:
              down_ret = system("wget " + linkall);
              if down_ret !=0:
                  print "download zip failed "
                  exit(0);
      print zipname;        
      #exit(0);
      #print get_dir_of_zip(zipname);
      #print get_name_of_project(url);

    
      project_dir=get_dir_of_zip(zipname);

      if path.exists(project_dir):
           ret = system("rm  "+ zipname);
        
           db.close();
           return;



      system("unzip " + zipname );
      #ret = system("rm  "+ zipname);
      #print ret;
      #exit(0);
      ret = system("git clone --bare " + url);
      if ret !=0:
          ret = system("git clone --bare " + url);
          if ret!=0:
              print "git clone --bare failed"
              exit(0);
      
      project_dir=get_dir_of_zip(zipname);
      gitdir =  project_dir +"/.git";
      system("mkdir "+gitdir)
      
      baregit = get_name_of_project(url)+".git";
      
      ret = system("cp -rf " +  baregit +"/*  " + gitdir)

      system("rm -rfd "+ baregit);
      ret = system("rm  "+ zipname);

      orig_dir = getcwd();
      chdir(project_dir);
      system("git init")
      system("git reset --hard  " +  postrev[0:7]);
      chdir(orig_dir)
      


            

      

  db.close();
num_np = [1, 4, 5, 6,7,11,12,13,14,15,16,17,18,19,20];
num_oob =[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13 ]
#num_cc = [1,3,4,5,6,7,8,9,10,11,12,13,14,15,16];
num_cc = [1,3,4,5,6,7,8,9,10,11,12,15];

#showcases(num_cc[11],"--ccecase");

for i in num_np:
    showcases(i,"--np");

for i in num_oob:
    showcases(i,"--oobcase");

for i in num_cc:
    showcases(i,"--ccecase");



