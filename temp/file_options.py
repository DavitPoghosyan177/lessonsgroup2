import os

def go_file(a):
    os.chdir(a)        
    f=os.listdir()
    return f
def open_file(a,b):
    f=open(a,'w')
    c=f.write(b)
    f.close()
    return c
def file_watch(a):
    e=''
    for i in range(len(a)):
        b=open(a[i],'r')
        c=b.read()
        b.close
        e+=a[i]+'->'+c+'\n'
    return e
def main():
    filename= "/home/davit/Desktop/temp/test"
    nfile=go_file(filename)
    see=file_watch(nfile)
    open_file('/home/davit/Desktop/temp/result.txt',see)
main()    
         