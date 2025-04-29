def gugu(number):
    list = []
    count = 1
    while count < 10:
        list.append(2 * count)
        count += 1
    return list

result = gugu(2)

print(result)