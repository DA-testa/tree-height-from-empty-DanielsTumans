# python3

import sys
import threading
import numpy

def compute_height(n, parents):
    # Write this function
  tree = [[] for _ in range(n)]
  for i, in range(n):
    if parents[i] == -1:
        root = i
    else:
        tree[parents[i]].append(i)
        
        
        
        
   def max_height(r):
        height = 1
        if not tree[r]:
            return height
        else:
            for child in tree[r]:
                height = (height, max_height(child))
            return height+1
    return max_height(root)
    
    
     
   


def main():
    bebr = input
    if "I" in bebr:
        n = int(input())
        parents = [int(z) for z in input().split()]
        print(compute_height(n, parents))
    elif "F" in bebr:
        filer = input()
        if 'a' in file:
            print ("wrong")
        bebr = "test/" + bebr
        with open (bebr, 'r') as file
            n = int(file.readline())
            parents = [int(x) for x in file.readline().split()]
        height = compute_height(n, parents)
        print(height)



sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
