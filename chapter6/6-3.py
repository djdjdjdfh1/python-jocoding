def get_total_page(m, n):
    if m % n == 0:
        return m // n
    else:
        return m // n + 1

print(get_total_page(5,10))
print(get_total_page(15,10))
print(get_total_page(20,10))
print(get_total_page(30,10))
