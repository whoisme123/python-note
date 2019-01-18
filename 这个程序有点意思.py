import random

def getAnswer(answerNumber):
    if answerNumber == 1:
        return ' 李雪智障'
    elif answerNumber == 2:
        return '李雪聪明'
    elif answerNumber == 3:
        return '李雪'
    elif answerNumber == 4:
        return '李雪美丽'
r = random.randint(1, 4)
forturn = getAnswer(r)
print(forturn)
