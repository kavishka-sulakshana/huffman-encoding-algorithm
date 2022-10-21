def get_min(dataset):
    mx = -1
    max_key = ""
    for i, v in dataset.items():
        if v[2] > mx:
            mx = v[2]
            max_key = i
    return max_key


def print_list(dicti):
    for x, y in dicti.items():
        print("\t{} --- {} --- {}".format(x, y[0], y[1]))


# item_list = {
#     'Apple': [1, 1050],
#     'Banana': [6, 600],
#     'Papaya': [8, 400],
#     'Watermelon': [5, 1500],
#     'Orange': [4, 800],
#     'Potato': [6, 1800],
#     'Carrot': [1, 300],
#     'Egg Plant': [2, 600],
#     'Beetroot': [3, 600],
#     'Ladies\' Fingers': [5, 1000]
# }
# maximum_amount = 30

item_list = {}
maximum_amount = int(input("Enter maximum weight amount : "))
inp1 = int(input("How many items you have to choose :"))
if inp1 > 0:
    for count in range(inp1):
        print("Item", count+1)
        inp2 = input("\tEnter item name :")
        inp3 = int(input("\tEnter their total weight : ".format(inp2)))
        inp4 = int(input("\tEnter their total price : "))
        if inp3 < 0:
            item_list[inp2] = [0, inp4]
        else:
            item_list[inp2] = [inp3, inp4]


for item in item_list.values():
    div = item[1] / item[0]
    item.append(div)

max_price = 0
max_weight = 0
selected_list = {}
current_amount = 0
j = 1

while current_amount < maximum_amount:
    a = get_min(item_list)
    if (item_list.get(a)[0] + current_amount) <= maximum_amount:
        current_amount = current_amount + item_list.get(a)[0]
        price = item_list.get(a)[1]
        weight = item_list.get(a)[0]
        selected_list[a] = [weight, price]
        item_list.pop(a)
    else:
        possible_amount = maximum_amount - current_amount
        current_amount = maximum_amount
        price = (possible_amount / item_list.get(a)[0])*item_list.get(a)[1]
        selected_list[a] = [possible_amount, price]
        item_list.pop(a)
        break

print("\nThis is selected item-list : ")
print_list(selected_list)

for m in selected_list.values():
    max_weight = max_weight + m[0]
    max_price = max_price + m[1]

print("\nmax price -> Rs:{}\nmax weight -> {}kg\n".format(max_price, max_weight))