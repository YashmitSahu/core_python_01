def writefile():
    file = open("../files/abc.txt","w")
    file.write("Hi\n")
    file.write("Hello Yashmit sahu\n")
    file.write("this is python file")
    print("file write successfully")
    file.close()

writefile()