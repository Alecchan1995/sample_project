import os
def newfile(name = "none"):
    pa = os.path.dirname(__file__)
    if os.path.exists(pa+"/"+name):
        print("these has this file")
    else:
        os.system("mkdir "+name)
        print("build the file is finish")

def filemove(name = "none"):
    pa = os.path.dirname(__file__)
    if os.path.exists(pa + "/" + name):
        os.rmdir(pa+"/"+name)
        print("finish to delete")
    else:
        print("these has not this file")

def changepath(name):
    path = os.getcwd()
    path = path+"/"+name
    os.chdir(path)



