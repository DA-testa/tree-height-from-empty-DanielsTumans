# python3

import sys
import threading
import numpy

def compute_height(n, parents):
    # Write this function
  tree = [[] for _ in range(n)]
  for i, in parent in enumerate(parents):
    if parent == -1:
        root = i
    else:
        tree[parent].append(i)
        
        
        
        
    def max_heights(r):
        
        if not tree[r]:
            return 0
        
            
        return max(max_heights(child) for child in tree[r]) + 1
    max_height = max_heights(root) + 1       
    return max_height
    
    
     
   


def main():
    bebr = str(input())
    if "I" in bebr:
        n = int(input())
        parents = [int(z) for z in input().split()]
        print(compute_height(n, parents))
    elif "F" in bebr:
        bebrik = str(input())
        if 'a' in bebrik:
            print ("wrong")
            exit()
        bebrik = "test/" + bebrik
        with open (bebrik, 'r') as file:
            n = int(file.readline())
            parents = [int(z) for z in file.readline().split()]
        height = compute_height(n, parents)
        print(height)



sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
