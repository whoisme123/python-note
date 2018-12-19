import sys
while True:
    print('who are you ?')
    name = input()
    if name != 'jon':
        print('查无此人')
        continue
    print('Hello jon. What is the password?')
    password = input()
    if password == 'z':
        print('登录成功')
        sys.exit(0)
    if password != 'z':        
        break
while True:
    password = input()
    if password != 'z':
        print('密码错误重新输入')
    if password == 'z':
        break
print('登录成功')

