# 23-Feb-2026

a = 100
b = 100
c = 3

# if a >= b and a >= c:
#     print(f'{a=}')
# elif b >= a and b >= c:
#     print(f'{b=}')
# else:
#     print(f'{c=}')

# print(max(a,b,c))

# request_line = 'HTTP/0.9'
# match request_line:
#     case 'HTTP/0.9':
#         print('You need to upgrade your browser; we do not support version 0.9')
#         exit(-30)
#     case 'HTTP/1.0':
#         print('You are running version 1.0 therefore non-persistent')
#     case 'HTTP/1.1':
#         print('You are running version 1.1 therefore persistent')
#     case other:
#         print(f'{other} is not a valid HTTP version')
#         exit('Bye!')


# x = 420
# match x:
#     case 0:
#         print('it is 0')
#     case 100:
#         print('it is 100')
#     case 42:
#         print('it is the answer')
#     case de:
#         print(f'it is {de}')
    
# alert_timer = 5
 
# print("Security Alert: System will lock in:")
# while alert_timer > 0:
#     print(f"{alert_timer} seconds...")
#     alert_timer -= 1
 
# print("System locked!")


# c = 0
# while c < 101:
#     print(c)
#     c = c + 1 # c += 1


# print('Bye!')

# x = 'BobIsHere'
# idx = 0
# while idx < len(x):
#     print(x[idx])
#     idx += 1

# x = 'helo1234'
# is_digit = x.isdigit()
# print(f'{x=}, is digit:{is_digit}')

# x = '1234'
# is_digit = x.isdigit()
# print(f'{x=}, is digit:{is_digit}')

# x = '1234b'
# is_digit = x.isdigit()
# print(f'{x=}, is digit:{is_digit}')


# x = 'BobIsHere89'
# for char in x:
#     is_digit = char.isdigit()
#     print(f'{char=}, is digit:{is_digit}')


# print('\nScanning IP range:')
# for i in range(1, 254):
#     print(f'192.168.1.{i} - checking...')


# x = list(range(0,101))
# # print(x)
# x = list(range(0,101,2))
# print(x)

# x = [1,5,3,6,2,9,2,4,6,8]
# for el in x:
#    print(el) 

# x = [1,5,3,6,2,9,2,4,6,8]
# for i in range(0, len(x)):
#    print(i, x[i]) 


# somelist = [(1, 2), (3, 7), (9, 5)]
# result = 0
# for x in somelist:# tuple unpacking
#     print(x)
#     print(x[0], x[1])
#     # result += x * y # the same as result = result + (x * y)
# # print(result) # 68


# somelist = [(1, 2), (3, 7), (9, 5)]
# result = 0
# for x, y in somelist:# tuple unpacking
#     print(x, y)
#     # result += x * y # the same as result = result + (x * y)
# # print(result) # 68