import os
import datetime
import shutil
import subprocess
import sys
from os import walk

targetDirectory = "yourDirectoryHere"
os.chdir(targetDirectory)
filenames = next(walk("."), (None, None, []))[2]

def modification_date(filename):
    t = os.path.getmtime(filename)
    return datetime.datetime.fromtimestamp(t)

for file in filenames:
    timestamp = str(modification_date(file))
    year = timestamp[0:4]
    month = datetime.datetime.strptime(timestamp[5:7], "%m").strftime("%B")

    if not os.path.exists(year):
        os.makedirs(year)
    if not os.path.exists(year+"/"+month):
        os.makedirs(year+"/"+month)

    shutil.move("./" + file, year+"/"+month + "/" + file)