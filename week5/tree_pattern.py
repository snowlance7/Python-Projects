print("Tree Pattern\n")
branches = int(input("Enter the number of branches: "))

def printTree(maxN):
    def tree(n):
        if n > 0:
            tree(n-1)
            print(n,"*" * n * maxN)
            tree(n-1)
    tree(maxN)

printTree(branches)