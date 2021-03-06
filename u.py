#!/usr/local/bin/python
#encoding:utf8
import os
import sys

def update_git (msg):
    print 'try to push to github'
    site_path = os.path.dirname(os.path.abspath(__file__))

    os.chdir(site_path)
    print os.popen('jekyll build').read()

    os.chdir('_site')
    cmds = ['git add --all', 'git commit -m "%s"' %msg, 'git push -u origin master']

    for i in cmds:
        print os.popen(i).read()
      

if __name__ == "__main__":
    if len(sys.argv)==1:
      msg = 'git update'
    else:
      msg = sys.argv[1]
    update_git(msg)
