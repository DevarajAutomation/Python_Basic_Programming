import os
import tracemalloc

tracemalloc.start()

file=open("/workspaces/Python_Basic_Programming/Basics_of_python/my_file.txt",'r') 

print(file.read())

current,peak=tracemalloc.get_traced_memory()

print(current,peak)