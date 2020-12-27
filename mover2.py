import os
import shutil

dir_in = input('pls enter your directory url: ')
dir_dst = input('pls enter your dst directory url: ')

print(dir_in)
entries = os.listdir(dir_in)
print(entries)
filename = entries

for i in filename:

    file = i
    print(file)
    strip = file.split('.')
    if strip[1] == 'jpg':
        print('found jpeg file')
        src_file = dir_in + '/' + file
        get_size = os.path.getsize(src_file)
        print(get_size)
        # file_stats = os.stat(file)
        # print(f'File Size in Bytes is {file_stats.st_size}')
        # print (src_file)
        shutil.move(src_file, dir_dst)
    else:
        print('not found')
