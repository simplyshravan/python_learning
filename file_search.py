import os

def find(name, path):
    for root, dirs, files in os.walk(path):
      if name in files:
##        print(root,dirs,files)
             print(os.path.join(root, name))

inp=input("enter the path : ")
inp1=input("enter the filename : ")
find(inp1,inp)

