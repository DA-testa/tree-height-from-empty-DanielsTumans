# python3
# 221RDB190DanielsTumans
import sys
import threading

def compute_height(n, parents):
    tree = [[] for _ in range(n)]
    for i, parent in enumerate(parents):
        if parent == -1:
            root = i
        else:
            tree[parent].append(i)
            
    def height(node):
        if not tree[node]:
            return 0
        return max(height(child) for child in tree[node]) + 1
    
    max_height = height(root) + 1
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
            print("Error")
            exit()
        bebrik = "test/" + bebrik
        with open(bebrik, 'r') as file:
            n = int(file.readline())
            parents = [int(z) for z in file.readline().split()]
        height = compute_height(n, parents)
        print(height)

sys.setrecursionlimit(10**7)
threading.stack_size(2**27)
threading.Thread(target=main).start()
