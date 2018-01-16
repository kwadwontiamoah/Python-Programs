def numberLines(file):
    somefile=open(file,"r")
    newfile=open("other.txt","w")
    linecounter=1
    for aline in somefile:
        newfile.write(str(linecounter)+" "+aline+"\n")
        linecounter=linecounter + 1
