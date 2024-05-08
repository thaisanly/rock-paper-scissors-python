ar = ["a", "b", "c", "d", "e"]
item = "d"
item_index = ar.index(item)

head = []
tail = []

limit = (len(ar) - 1) // 2

if item_index + limit > len(ar) - 1:

    current_index = item_index + 1

    while True:

        if current_index == item_index:
            break

        if current_index >= len(ar) - 1:
            current_index = 0

        if len(tail) < limit:
            tail.append(ar[current_index])
        else:
            head.append(ar[current_index])

        current_index += 1

else:

    for i in range(0, len(ar)):
        if i == item_index:
            continue
        if i >= item_index and len(tail) < limit:
            tail.append(ar[i])
        else:
            head.append(ar[i])

print(head, tail)
