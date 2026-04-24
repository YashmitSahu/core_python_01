def readfile():
    file = open("../files/Hello.txt",'r')

    text = file.read()
    print(text)
    file.close()


readfile()