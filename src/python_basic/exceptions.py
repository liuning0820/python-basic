#coding:UTF-8

try:
    file_handle= open("datafile.txt", "w")
    file_handle.write("This is some data to dump into the file")
    print("Wrote some data to the file")
except FileNotFoundError:
    print("Unable to find the file.")
except IOError:
    print("Exception caught: Unable to write to datafile.txt")
else:
    print("File written to successfully")
    file_handle.close()






