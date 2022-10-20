class TreeNode:
    def __init__(self, freq, character, left, right, alt):
        self.frequency = freq
        self.character = character
        self.left = left
        self.right = right
        self.c = alt

    def __lt__(self, other):
        return self.frequency < other.frequency


def get_mapped_list(msg):
    arr = {}
    for k in msg:
        if k not in arr:
            arr[k] = 1
        else:
            arr[k] = arr[k] + 1
    return arr


def get_class_list(arr):
    class_list = []
    arr_list = arr.keys()
    for m in arr_list:
        class_list.append(TreeNode(arr[m], m, None, None, True))
    return class_list


def find_min(arr):
    min1 = 0
    min2 = 0
    for k in range(len(arr)):
        if arr[k] < arr[min1]:
            min1 = k
    arr[min1].c = False
    if min1 == 0:
        min2 = 1
    for j in range(len(arr)):
        if arr[j].c and (arr[j] < arr[min2]) and min1 != 0:
            min2 = j

    arr[min1].c = True
    return [arr[min1], arr[min2]]


def create_tree(class_list):
    while len(class_list) > 1:
        values = find_min(class_list)
        f_node = values[0]
        s_node = values[1]
        new_freq = f_node.frequency + s_node.frequency
        class_list.remove(values[0])
        class_list.remove(values[1])
        new_node = TreeNode(new_freq, None, f_node, s_node, True)
        class_list.append(new_node)
    return class_list[0]


huffmanCodeIndex = {}


def traverse(tree, n=1, string=""):
    if tree.left is not None:
        traverse(tree.left, n + 1, string + "0")
    if tree.right is not None:
        traverse(tree.right, n + 1, string + "1")
    if tree.character is not None and tree.character != " ":
        print("|\t", tree.character, "\t\t|", string, "\t")
    elif tree.character == " ":
        print("|\t space", "\t|", string, "\t")
    huffmanCodeIndex[tree.character] = string


# message = 'Betty Butter Bought Some Butter'
message = input("Enter the secret message : ")
mapped_list = get_mapped_list(message)
converted_list = get_class_list(mapped_list)
if len(converted_list) > 1:
    minHeap = create_tree(converted_list)
    print("\nThis is the table of huffman : \n_____________________")
    traverse(minHeap)
    print("---------------------\n")
    print("Encoded Message : ")
    for i in message:
        print(huffmanCodeIndex[i], end=" ")
    print("\ntotal no of characters in message : ", len(message))
    print("Total no of bits want in ASCII : ", len(message) * 8)
    huffmanCodeSize = 0
    for x, y in mapped_list.items():
        huffmanCodeSize = huffmanCodeSize + y * len(huffmanCodeIndex[x])
    print("After Huffman coding, total number of bits needed :", huffmanCodeSize)
    print("Number of bits that were saved : ", len(message) * 8 - huffmanCodeSize)

else:
    print(converted_list[0].character, "\t", 1)
