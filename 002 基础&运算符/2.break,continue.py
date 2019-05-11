# while True:
#     print('hello')
#     while True:
#         print(666)
#         break

# while True:
#     print('hello')
#     while True:
#         print(666)
#         break
#     break

# count = 1
# while count <= 10:
#     if count == 7:
#         pass
#     else:
#         print(count)
#     count += 1

# count = 1
# while count <= 10:
#     if count == 7:
#         count += 1
#         continue
#     print(count)
#     count += 1

count = 0
while True:
    count += 1
    if count == 7:
        continue
    print(count)
    if count > 10:
        break


