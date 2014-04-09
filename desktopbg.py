#! /usr/bin/env python

import urllib2
from subprocess import call
from BeautifulSoup import BeautifulSoup

soup = BeautifulSoup(urllib2.urlopen('http://xkcd.com/'))

# scrape the page. look for the div with id="comic". get the src from the image tag.
comicsrc = soup.find('div', attrs={'id':'comic'})('img')[0]['src']

# wget the image. save it as desktop.png
call(['wget', '-O', '/home/ben/bin/desktopbg/desktopbg.png', comicsrc])

# set the desktop background using xfconf-query
mon0cmd = 'xfconf-query -c xfce4-desktop -p /backdrop/screen0/monitor0/image-path -s ""'.split()
mon1cmd = 'xfconf-query -c xfce4-desktop -p /backdrop/screen0/monitor1/image-path -s ""'.split()
call(mon0cmd)
call(mon1cmd)

# set the desktop background using xfconf-query
mon0cmd = 'xfconf-query -c xfce4-desktop -p /backdrop/screen0/monitor0/image-path -s /home/ben/bin/desktopbg/desktopbg.png'.split()
mon1cmd = 'xfconf-query -c xfce4-desktop -p /backdrop/screen0/monitor1/image-path -s /home/ben/bin/desktopbg/desktopbg.png'.split()
call(mon0cmd)
call(mon1cmd)
