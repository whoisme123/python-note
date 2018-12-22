'''
def spam():
    egg = 23
    ban()
    print(egg)
def ban():
    ham = 11
    egg = 33

spam()
'''

'''
def spam():
    egg = 'spam local '
    print(egg)

def bacon():
    egg = 'bacon local'
    print(egg)
    spam()
    print(egg)

egg = 'zzz'
bacon()
print(egg)

'''
'''
def spam():
    global eggs
    eggs = 'spam'
def bacon():
    egg = 'bacon local'    
eggs = 'sdada'
spam()
print(eggs)

'''
'''
def spam():
    print(eggs)
    eggs = 'spam local'

eggs = 'global'
spam()

'''
'''


#以下为ZeroDivisionError.py

def spam(divibeBy):
    try:
        return 42 / divibeBy
    except:
        print('错误')

print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))

'''

'''
def spam(zzz):
    return 42 / zzz
try:
    print(spam(2))
    print(spam(12))
    print(spam(0))   
    print(spam(1))  #一旦到了except就不会返回到try
except:
    print('错误')

'''

'''
#猜数游戏。
import random
sNumber = random.randint(1, 20)
print('数字在1到20之间')

#让玩家猜测6次
for guessTk in range(1, 7):
    print('猜一猜')
    guess = int(input())
    
    if guess < sNumber:
        print('你猜的太小了')
        continue
    elif guess > sNumber:
        print('你猜的太大了')
        continue
    else:
        break  #这个条件是正确的猜测

if guess == sNumber:
    print('恭喜你！ 你猜这个的数字是' + str(guessTk) + '次！' )
else:
    print('不，我想的数字是' + str(sNumber))


'''

import sys

def collatz(number):
    if number % 2 == 0:
         print(number // 2)
         return number//2
    else:
        print(3*number+ 1)
        return number*3 + 1

print('请输入一个整数')
try:
    number = int(input())
    while number != 1:
        number = collatz(number) 
except:
    print('请输入整数')
    sys.exit()
    
    
'''
def collatz(number):
	if number%2==0:
		print(number//2)
		return number//2
	else:
		print(number*3+1)
		return number*3+1
		
 
while True:
	print('input a number')
	try :
		num=int(input())
	except ValueError:
		print ('Error:Invalid argument.')
		continue
	while num!=1:
		num=collatz(num)
	if num == 1:
		break
'''

































































































