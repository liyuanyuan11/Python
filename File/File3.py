txtFile=open("/Users/chenchaoyang/Desktop/python/content/content.txt","r")
while True:       
    line=txtFile.readline()
    if not line:
        break
    else:
        print(line)
txtFile.close()