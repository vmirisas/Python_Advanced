# these are 2 ways to print the first 100 odd numbers

my_list = []
i = 0

while len(my_list) < 100:
    if (i % 2) != 0:
        my_list.append(i)
        i += 1
    else:
        i += 1

print(len(my_list))
print(my_list)

list2 = []
for i in range(1, 200, 2):
    list2 += [i]

print(list2)
print(sum(my_list) == sum(list2))
