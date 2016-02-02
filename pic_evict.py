import os, shutil

user = os.path.expanduser('~')
cur_dir = os.getcwd()
target_dir = (user + '/Pictures/')
f_ext = ['jpg','bmp','gif','png']

pics = [fn for fn in os.listdir(cur_dir)
        if any(fn.endswith(ext) for ext in f_ext)]

count = 0
for i in pics:
    count += 1
    print(i)

print("There are {} images in the current directory.".format(count))

print("Please select what to do next:")
print("1. Move to Pictures")
print("2. Delete")

option = input("\nOption: ")

if option == '1':
    for i in pics:
        shutil.move(i, target_dir)
        print("Pictures have been moved")
else:
    for i in pics:
        os.remove(i)

input("\nHit any key to exit...")