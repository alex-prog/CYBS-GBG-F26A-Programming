#Date: 24-Feb-2026

# def password_checker(password, minimum_length):
#     if 64 >= minimum_length >= 6:
#         pass
#         # print('ok')
#     else:
#         print('min not ok (6-64)')
#         exit()
    
#     if len(password) > minimum_length:
#         print('pass ok')
#     else:
#         print('too short')

# # password_checker('aa', 3)
# password_checker('aabbccdddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd', 7)
# password_checker('aa', 69)



# def add_numbers(a, b) -> int:
#     total = a + b
#     return total

# x = add_numbers(20, 30)
# print(x, type(x))


# print(isinstance("kk", int))
# print(isinstance("kk", str))
# print(isinstance(["kk"], list))


# def string_checker(string) -> bool:
#     if isinstance(string, str):
#         return True
#     else:
#         return False
    
# password1 = 12345
# password2 = '12345'

# print(f'Is password1 string? {string_checker(password1)}')
# print(f'Is password2 string? {string_checker(password2)}') #formatted-string - Abdullah G. Husk

# print(5/0)

# try:
#     print(5/0)
# except Exception as e:
#     print('wow', e)

# print('This is vary important line')


# try:
#     print(5/0)
#     x = "cyber"
#     x = int(x)
# except ZeroDivisionError: 
#     print("You can't divide by zero")
# except:
#     print("Some other general error")


try:
    # print(5/0)
    x = "cyber"
    x = int(x)
except Exception as abdulah:
    print("Some other general error: ", abdulah)