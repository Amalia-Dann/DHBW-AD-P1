def makeTree(height: int):
    global tree
    # Make the top of the tree
    tree = "      " + " " * height +"*" + "\n"
    for i in range(1, height):
        leftTree(i, height)
        rightTree(i)

def leftTree(currentLevel: int, height: int):
    global tree
    tree += "  "*(height-currentLevel-1) + "~@" * currentLevel
    tree = tree[:-1]

def rightTree(currentLevel: int):
    global tree
    tree += "@~" * currentLevel
    tree += "\n"


# Call the function to print the tree
def main():
    global tree
    height = 9
    makeTree(int(height))
    print(tree)
    print("           |||||||||")
    print("           |||||||||")
    print("           |||||||||")

main()
