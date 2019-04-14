num = 1
count = 1
total = int(input('please input a num: '))
while count <= total:
    print(' ' * (total - count), '*' * num)
    num += 2
    count += 1
