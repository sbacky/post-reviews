#!/usr/bin/env python3

import os
import requests
import sys
import json

def getInfo(fullPath):
    '''Get data from text file and save into a dictionary with keys title, name, date, feedback'''
    txt = open(fullPath, "r")
    post = {}
    post["title"] = txt.readline().strip()
    post["name"] = txt.readline().strip()
    post["date"] = txt.readline().strip()
    post["feedback"] = txt.read().strip()
    txt.close()
    return post

def postInfo(d):
    '''Post info stored in dictionary to http://35.225.76.124/feedback'''
    url = "http://35.225.76.124/feedback/"
    js = json.dumps(d)
    response = requests.post(url, data=js)
    print(response.status_code)

def dirCheck(dir):
    '''Returns True if obj at dir is a directory'''
    return os.path.isdir(dir)

def main():
    dir = sys.argv[1]

    if not dirCheck(dir):
        print("Not a valid directory: {}".format(dir))
        sys.exit(1)

    allFiles = os.listdir(dir)
    if len(allFiles) < 1:
        print("There are no files in dir: {}".format(dir))
        sys.exit(1)

    txtFiles = []
    for file in allFiles:
        if file.endswith(".txt"):
            txtFiles.append(file)

    if len(txtFiles) < 1:
        print("There are no text files in dir: {}".format(dir))
        sys.exit(1)

    for tFile in txtFiles:
        fullPath = os.path.join(dir, tFile)

        post = getInfo(fullPath)
        postInfo(post)

if __name__ == "__main__":
    main()
