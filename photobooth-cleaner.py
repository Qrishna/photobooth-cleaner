#!/usr/bin/env python
import os
import glob
import shutil
import getpass

user = getpass.getuser()

TARGET_DIR = "/Users/%s/Pictures/Photo Booth Library/Pictures/" % user
TARGET_EXT = "*.jpg"
my_pics = glob.glob(TARGET_DIR + TARGET_EXT)

for pic in my_pics:
    name = TARGET_DIR + "-".join(pic.split("/")[-1].split(" "))
    shutil.move(pic, name)

os.system("cd /Users/%s/Pictures/Photo\ Booth\ Library/Pictures/ && mogrify -flop *.jpg" % user)

