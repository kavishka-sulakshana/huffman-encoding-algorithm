import heapq


class tree_node:
    def __init__(self, freqency, symbol, left=None, right=None):
        self.freqency = freqency
        self.symbol = symbol
        self.left = left
        self.right = right
        self.huffmanCode = ''

    def __lt__(self, other):
        return self.freqency < other.freqency


huffman_table = {}


def huffTable(tree_node, val=''):
    newVal = val + str(tree_node.huffmanCode)
    if tree_node.left:
        huffTable(tree_node.left, newVal)
    if tree_node.right:
        huffTable(tree_node.right, newVal)
    if not tree_node.left and not tree_node.right:
        if tree_node.symbol == " ":
            print("|\t space \t|", newVal, "\t")
        else:
            print("|\t", tree_node.symbol, "\t\t|", newVal, "\t")
        huffman_table[tree_node.symbol] = newVal


def get_mapped_list(msg):
    arr = {}
    for k in msg:
        if k not in arr:
            arr[k] = 1
        else:
            arr[k] = arr[k] + 1
    return arr


def make_tree(chars, freq):
    tree_nodes = []
    for x in range(len(chars)):
        heapq.heappush(tree_nodes, tree_node(freq[x], chars[x]))

    while len(tree_nodes) > 1:
        left = heapq.heappop(tree_nodes)
        right = heapq.heappop(tree_nodes)
        left.huffmanCode = 0
        right.huffmanCode = 1
        new_tree_node = tree_node(left.freqency+right.freqency, left.symbol+right.symbol, left, right)
        heapq.heappush(tree_nodes, new_tree_node)
    return tree_nodes[0]


message = input("Enter the secret message : ")
mapped_list = get_mapped_list(message)
chars = list(mapped_list.keys())
freqency = list(mapped_list.values())
huffman_tree = make_tree(chars, freqency)
print("\nThis is the table of huffman : \n_____________________")
huffTable(huffman_tree)
print("---------------------\n")
encoded_msg = ""
for i in message:
    encoded_msg = encoded_msg + (huffman_table[i]+" ")
print("Encoded Message : \n{}\n".format(encoded_msg))
print("\ntotal no of characters in message : ", len(message))
print("Total no of bits want in ASCII : ", len(message) * 8)
huffmanCodeSize = 0
for x, y in mapped_list.items():
    huffmanCodeSize = huffmanCodeSize + y * len(huffman_table[x])
print("After Huffman coding, total number of bits needed :", huffmanCodeSize)
print("Number of bits that were saved : ", len(message) * 8 - huffmanCodeSize)


