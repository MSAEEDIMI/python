file=open("/home/mohammad/Desktop/a1.html","r")
file=file.read()

def stringSprator(file,a,h):
    file=file.split()
    fp=[]
    p=[]
    for i in file:
        if a in i:
            p.append(i)
    for i in range(len(p)):
        b=p[i]
        if "h"in a:
            b=b[b.index(a)+4:b.index(h)]
            if "p"in b: 
                b=str(b).split("<p>")[0]   
        elif "<p"in a:
            b=b[b.index(a)+3:b.index(h)]
            if "<h"in a:
                b=str(b).split(a)[0]
        fp.append(b) 
    print(fp)    

stringSprator(file,"<h1>","</h1>")
stringSprator(file,"<p>","</p>")
