f = open("deletefile.txt", "w")
f.write("Me cute :p ")
f.close()


import os
if os.path.exists("deletefile.txt"):
    os.remove("deletefile.txt")
else:
    print("No file named after the name")


import os
os.mkdir("myfolder")


import os
os.rmdir("myfolder")

