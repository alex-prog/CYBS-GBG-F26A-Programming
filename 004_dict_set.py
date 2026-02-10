# 10-Feb-2026
# Ex. from last time

# my_list = [0,1,2,3,4,5,6,7,8]

# print(my_list)
# print(f'My list is: {my_list}.')
# print('My list is: ' + str(my_list))
# print('My list is:', my_list, '.')

# print(f'{my_list=}')
# print(f'{my_list*2}')
# x = f'This is my formatted string, {(3%2)=}'
# print(x)

# print(f'2. Print the first element of the list: {my_list[0]}')
# print(f'3. Print the last element of the list: {my_list[-1]}')
# print(f'4. Print the first 4 elements: {my_list[:4]}')

# second_list = my_list[-3:]
# print(second_list)

# -----------------------------------------------

# my_list = ['cyber']
# print(type(my_list))
# my_list.append(2)
# my_list.append(1)
# my_list.append(3)

# print(my_list)

# my_list.append('cyber')
# print(my_list)
# print(my_list.index('cyber'))
# del my_list[0::4] 
# print(my_list)
# my_list.sort(reverse=True)
# print(my_list[::-1])

# ips = ['189.19.202.26', '124.124.86.154', '111.123.147.92', '191.194.49.89', '191.194.49.89', '3.100.186.196', '17.102.131.131', '170.40.162.9', '66.23.103.242', '203.207.124.71', '3.100.186.196', '170.194.124.70', '3.100.186.196', '161.240.120.16', '37.161.17.14', '3.100.186.196', '144.182.46.41', '3.100.186.196', '67.180.5.237', '182.44.178.202']

# ips.append('8.8.8.8')
# # ips += ['1.1.1.1']
# print(ips)
# print(f'Total entries: {len(ips)}')
# print(f"last 5: {ips[-5:]}")

# print(f'Counts of \'3.100.186.196\': {ips.count('3.100.186.196')}')

# ---------------------------------------------------------
# x = (1,2,3,4,5, "Sebastian")
# x = list(x)
# x.append('Alex')
# x = tuple(x)
# print(x)

# x = (1,2,3,4,5, "Sebastian")
# x = x + ('Alex', )
# print(x)

# d = {"te1": 'Sebi', 'te2': 'Alex'}
# d['name'] = 'Bob'
# print(d)
# print(len(d))
# print(len(d['te2']))

# print('te2' in d)

# d = {'a':[1,2], 'b':[4,5]}
# print(d)
# print('b' in d)
# print(5 in d['b'])
# print(d['b'])

# d[8] = 42
# print(d)
# d[(1,2)] = 'bob'
# print(d)

# my_list = [1,2,3]
# d = {'a': my_list, 'b': [2,1]}
# print(d)
# my_list = 'wow'
# print(d)

d = {'a':12, 'b':4, 'c':16}
print(d.keys())
print(d.values())
print(d.items())

for it in d.items():
    print(it)
