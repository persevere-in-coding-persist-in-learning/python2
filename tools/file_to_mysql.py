# -*- coding: UTF-8 -*-
import urllib
from urllib import quote
from urllib import unquote

with open("tag.txt", "r") as f:
    for line in f.readlines():
        a = line.split('  ')
        print ('update  tztag_tag_1136459105356091401_1 set tag_name=' + "'" + urllib.unquote(
            a[1].strip()) + "'" + ' where tag_id=' + "'" + a[0].strip()) + "';"
