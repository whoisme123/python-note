name = ''
while not name:
    print('Enter your name')
    name = input()
print('你们有多少客人?(请输入数字)')
while True:
    x = input(':')
    if x.isdigit():
        break
    else:
        print('请输入数字')
print('确保有足够的空间接待所有的客人.')
print('Done')

