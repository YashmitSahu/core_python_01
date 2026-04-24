import shutil

source = "C:/Users/PC/OneDrive/Desktop/io/tree.jpg";
target = "C:/Users/PC/OneDrive/Desktop/op/tree.jpg";


shutil.copyfile(source,target)
print(source +" is copied to " + target)