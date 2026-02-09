# is_logged_in = True
# has_admin_rights = False
# account_locked = True

# has_access = is_logged_in and has_admin_rights and not account_locked

# if has_access:
#     print('Access Granted')
# else:
#     print('Access Denied')

# is_logged_in = True
# has_admin_rights = True
# account_locked = False

# has_access = is_logged_in and has_admin_rights and not account_locked

# if has_access:
#     print('Access Granted')
# else:
#     print('Access Denied')


# -- Lsit --
#    0  1  2  3  4   5  6
#   -7 -6 -5 -4 -3  -2 -1
x = [1, 2, 4, 5, 7, 42, 3]

# print(x[5])
# print(x[-2])
# 1, 2, 4, 5
# print(x[0:4])
# print(x[:4])

# 4, 5,
# print(x[2:4])

# print(x[::2])
# print(x[::-1])
# print(x[::-2])

# print(x[2:4][::-1])
# print(x[3:1:-1])

# print(x[-3:])
# print(x[-10:])
# print(x[:156])

#    0  1  2  3  4   5  6
#   -7 -6 -5 -4 -3  -2 -1
x = [1, 2, 4, 5, 7, 42, 3]

# x[1] = 'two'
# # print(x) 
# x[1] = 2
# x[len(x):] = [-8,-9,-10]
# print(x)
# x[2:4] = [-6, -6]
# print(x)
# x[2:4] = []
# print(x)
# del x[0]
# print(x)

#    0  1  2  3  4   5  6
#   -7 -6 -5 -4 -3  -2 -1
# x = [1, 2, 4, 5, 7, 42, 3]

# x.append('text')
# print(x)
# x.append([1,2,3,4])
# print(x)
# x += [1,2,3,4]
# print(x)
# # x.sort()
# print(x)
# x = [1, 2, 4, 5, 7, 42, 3]
# x.sort()
# print(x)

# x = ['a', 'b', 'A', 'c']
# x.sort()
# print(x)

# if 'a' > 'A':
#     print('a')
# else:
#     print('A')

# x = ord('c')
# print(x)

# x = chr(128013)
# print(x)


#    0  1  2  3  4   5  6
#   -7 -6 -5 -4 -3  -2 -1
# x = [1, 2, 4, 5, 7, 42, 3, 4, 4, 4]

# # idx = x.index(42)
# # print(idx)

# # idx = x.index(42456)
# # print(idx)
# couns =x.count(4576)
# print(couns)


# x = [1,2,3]
# y = x * 3
# print(y)


# x = (1,)
# x = (1, 2, 3, 4, 5, 6, 7, 8, 12)
# x[2] = 'd' # this gives an error​
# z = (x + y,) # Including a comma indicates that the parentheses denote a tuple​
# x = (1, "two", 4.0, ["a", "b"], (5, 6))


x = [1, 2, 3, 4] 
y = tuple(x) # converting from list to tuple​
x = list(y) # and back
