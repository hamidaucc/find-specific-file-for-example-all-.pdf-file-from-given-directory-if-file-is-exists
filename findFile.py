import os
'''
find specific file for example all .pdf file from given directory
if file is exists
'''
def findFile(path):
    for i in os.listdir(path):
        if i.endswith(".pdf"):
            print(i)


x="pathToFolder"
findFile(x)
