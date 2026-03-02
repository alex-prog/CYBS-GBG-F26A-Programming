# Date: 02-Mar-2026

# file_path = 'my_file.txt'
# file_obj = open(file_path, 'r')

# # print(file_obj)

# # ln = file_obj.readline()
# # print(ln)
# # ln = file_obj.readline()
# # print(ln)

# lns = file_obj.readlines()
# print(lns)
# for ln in lns: 
#     print(ln, end='')

# ----------------------------------
from pathlib import Path

# file_path = Path(r'C:\coag_temp\_F2026\1sem_prog\CYB-F26A-code\my_file.txt')
# # file_obj = open(file_path, 'r')

# # print(file_obj.readlines())
# print(file_path.cwd())  

# cwd = Path.cwd()
# file_path = cwd.joinpath('my_file.txt')
# file_obj = open(file_path, 'r')
# print(file_obj.readlines())

cwd = Path.cwd()
print(cwd)
file_path = cwd.joinpath('test.txt')
# f_obj = open(file_path, 'r')
# print(f_obj.readline())
# f_obj.close()

# with open(file_path, 'r') as f_obj:
#     for x in f_obj:
#         print(x, end='')

# with open('test.txt', 'a') as f_obj:
#     f_obj.write('Hello from python\n')

# print('-'*30)
# with open(file_path, 'r') as f_obj:
#     for x in f_obj:
#         print(x, end='')

# with open('test2.txt', 'w') as f_obj:
#     f_obj.write('Hello from python AGAIN\n')

#---------------------------------------------------
import os

file_path = 'numbers2.txt'
isFile = os.path.exists(file_path)
if isFile:
    with open(file_path, 'r+') as f:
        lns = f.readlines()
        run_count = int(lns[-1])
        new_count = run_count + 1
        f.write(f'{new_count}\n')
else:
    with open(file_path, 'w') as f:
        f.write(f'0\n')