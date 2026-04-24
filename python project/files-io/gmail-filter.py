import re

def readLine():

    input_file = open(r"C:\\Users\\PC\\OneDrive\\Desktop\\gmail.txt",'r')
    yahoo_output_file =open(r"C:\\Users\\PC\\OneDrive\\Desktop\\yahoocorrect.txt",'w')
    gmail_output_file = open(r"C:\\Users\\PC\\OneDrive\\Desktop\\gmailcorrect.txt",'w')
    outlook_output_file= open(r"C:\Users\PC\OneDrive\Desktop\outlookcorrect.txt",'w')

    for line in input_file:
        if "@gmail.com" in line:
            gmail_output_file.write(line)
        elif "@yahoo.com" in line:
            yahoo_output_file.write(line)
        elif "@outlook.com" in line:
            outlook_output_file.write(line)

    input_file.close()
    gmail_output_file.close()
    yahoo_output_file.close()
    outlook_output_file.close()

readLine()