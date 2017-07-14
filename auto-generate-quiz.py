#!- encoding = utf-8 -!

'''
Author: Dou Liyou
Program Time: 2017-07-14
Version: 1.0

Script using: 
'''

import random
import operateDocx

'''
define a method called 'calculate' with 3 parameters: number1, number2 and expression.
the method calculate depend on the expression, this version only support '+' , '-'
other expression will return None
'''

def calculate(Operator,number1,number2):
    if Operator == '+':
        return number1 + number2
    if Operator == '-':
        return number1 - number2
    return -1


def cal(exp):
    if exp.__len__() == 3:
        return calculate(exp[0],exp[1],exp[2])
    if exp.__len__() == 5:
        tmpValue = calculate(exp[0],exp[2],exp[3])
        return calculate(exp[1],tmpValue,exp[4])

'''
this method is used to produce a random int which is between 'begin' and 'end'.

'''
def makeRandomInt(begin,end):
    if begin <= end:
        return random.randint(begin,end)
    else:
        return 0


'''
this method is used to produce a operator optionally. which should be '+' or '-'
'''
def makeRandomOper():
    exp = ['+','-']
    index = random.randint(0,1)
    return exp[index]


'''
this method can produce a list which contains one operator and two numbers.

'''
def generateExpression():
    exp = []
    exp.append(makeRandomOper())
    exp.append(makeRandomInt(0,99))
    exp.append(makeRandomInt(0,99-exp[1]))
    if exp[0]=='+':
        return exp
    if exp[0]=='-':
        if exp[1]>exp[2]:
            return exp
        else:
            two = exp.pop(1)
            one = exp.pop(1)
            exp.append(one)
            exp.append(two)
            return exp


def generateThreeExp():
    exp = []
    exp.append(makeRandomOper())
    exp.append(makeRandomOper())
    exp.append(makeRandomInt(0,99))
    exp.append(makeRandomInt(0,abs(99-exp[2])))
    exp.append(makeRandomInt(0,abs(99-exp[2]-exp[3])))
    if (exp[0] == '+') & (exp[1] == '+'):
        return exp
    else:
        if (exp[2]>exp[3]) & (exp[3]>exp[4]):
            testValue = cal(exp)
            if testValue < 0:
                exp[2] = exp[2] + abs(testValue)
                print exp
            return exp
        else:
            for i in range(2,3):
                for j in range(i+1,5):
                    if exp[i]< exp[j]:
                        tmp = exp[i]
                        exp[i]= exp[j]
                        exp[j]=tmp
            # be sure the return value is negative number, modify the first number, confirm it's big enough.
            testValue = cal(exp)
            if testValue < 0:
                exp[2] = exp[2] + abs(testValue)
                print exp
            return exp



'''
this method format a expression to style which can be read by a pupil
'''
def formatExpression(exp):
    if exp.__len__() == 3:
        return str(exp[1])+''+exp[0]+' '+str(exp[2])+ ' '+ '='+'  '
    if exp.__len__() == 5:
        return str(exp[2]) + '' + exp[0] + '' + str(exp[3]) +  ' '+ exp[1] + ' '+ str(exp[4]) + ' '+ '=' + '  '


'''
this method produce a quiz and return quiz as a list.
e.g: [[exp1,exp2,exp3],[res1,res2,res3]]
'''
def generateQuiz(amout):
    quiz = []
    expression = []
    results = []
    quiz.append(expression)
    quiz.append(results)
    for i in range(amout):
        r = random.randint(0,1)
        if r == 0:
            exp = generateExpression()
        else:
            exp = generateThreeExp()
        fexp =formatExpression(exp)
        result = cal(exp)
        expression.append(fexp)
        results.append(result)
    return quiz


if __name__=="__main__":
    print 'auto generate quiz starts ...'
    # print makeRandomOper()
    # exptmp = generateExpression()
    # print exptmp
    # print formatExpression(exptmp)
    # print calculate(exptmp[0],exptmp[1],exptmp[2])
    # print generateQuiz(5)

#####generate 2 number expression.

    amountOfQuiz = 3000

    myQuiz = generateQuiz(amountOfQuiz)
    operateDocx.writeDocx(myQuiz,'quizs.docx')
    print 'quiz generated! '

#### test generateThreeExp
    # exp = generateThreeExp()
    #
    # print formatExpression(exp)
    # print 'result is : '+ str(cal(exp))