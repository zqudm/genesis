#!/usr/bin/env python
from urllib2 import urlopen
from bs4 import BeautifulSoup
from sys import argv
from os import system
import random
import time

#def resolve_redirects(url):
#        try:
#            return urllib2.urlopen(url).geturl()
#            except HTTPError:
#               time.sleep(5)
#               return urllib2.urlopen(url).geturl()
def fetchProjectList(lang, size, page):
    ret = []
    tt = []
    #url_str = "https://github.com/search?o=desc&p=" + str(page) + "&l="+ lang + \
    #    "&size>" + str(size) + "&q=NOT+android"+ \
    #    "&ref=searchresults&s=stars&type=Repositories";
    url_str= " https://github.com/search?l=Java&o=desc&p="+str(page)+"&q=NOT+ANDROID++stars%3A%3E1000+language%3AJava&s=stars&type=Repositories";    
    # https://github.com/search?l=Java&o=desc&q=NOT+android in name &s=stars&type=Repositories&size%3E1000
    soup = BeautifulSoup(urlopen(url_str), 'lxml');
    #f = open(outdir + "/p" + str(i) + ".html", "w");
    #print >> f, dd
    #f.close();

    #print url_str
    
    # The hacky pattern is that the user_name/project_name will appear three
    # times in a row, and the last time starts with "/". It might be invalid
    # if github updates its webpage layout
    lastlink1 = ""
    lastlink2 = ""
    for link in soup.find_all('a'): 

        linkstr = link.get('href');
            
        if len(linkstr)<2:
            continue;
        if linkstr[0] == "/":
            #ret.append(linkstr); 
            ress = linkstr.split("/");
            if len(ress)==3 and link.get("class")[0] == "v-align-middle":
              clas= link.get("class");
              ret.append(linkstr)
              #tt.append(clas[0]);
        #      
             #print linkstr;
        #return
        #if len(linkstr) < 2:
        #    continue;
        #if (len(lastlink1) >= len(linkstr)) and \
        #   (len(lastlink2) >= len(linkstr)):
        #    if linkstr[0] == "/":
        #        if lastlink1[0:len(linkstr)-1] == linkstr[1:len(linkstr)]:
        #            if lastlink2[0:len(linkstr)-1] == linkstr[1:len(linkstr)]:
        #                if linkstr != "/":
        #                    ret.append(linkstr)
        #lastlink2 = lastlink1
        #lastlink1 = linkstr
    return ret

assert( len(argv) > 1);
outdir = argv[1];
system("rm -rf " + outdir);
system("mkdir " + outdir);
random.seed(53);
for i in range(80, 92):
    print "Fetching page " + str(i);
    l = fetchProjectList("Java", "1000", i);
    f = open(outdir + "/p" + str(i) + ".txt", "w");
    for addr in l:
        print >> f, addr;
    f.close();

    time.sleep(random.uniform(30, 150));
