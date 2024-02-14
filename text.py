import os
def create_file(filename):
    try:
        with open(filename,'w') as file:
          file.write("this is an example of create file")
          print("file is created "+filename)
    except IOError:
       print("can not print the filename" +filename)

def append_file(filename,text):
    try:
        with open(filename,'a') as file:
          file.write(text)
          print("file is appended "+filename)
    except IOError:
       print("can not append the filename" +filename)

def open_file(filename):
    try:
        with open(filename,'r') as file:
          data = file.readlines()
          print(data)
          print("file is read successfully "+filename)
    except IOError:
       print("can not open the filename" +filename)

def rename_file(filename,new_filename):
    try:
          os.rename(filename, new_filename)
          print("file is renamed from " + filename  + " successfully " + new_filename)
    except IOError:
       print("can not open the filename" +filename)




filename = 'example.txt'
new_filename = 'changed.txt'
create_file(filename)
append_file(filename,"new text added")
open_file(filename)
rename_file(filename, new_filename)
      
