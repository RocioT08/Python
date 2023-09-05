import welcome as w
import random

# import welcome
# from welcome import welcome_message

w.welcome_message("Data Design")


def calculateNums(a, b):
    c = a + b * random.uniform(1, 10);
    print(c);


calculateNums(5, 6);
calculateNums(7, 6)

"""
import html.parser
from html import parser
from html import *
"""

"""
import distutils.command.build
from distutils.command import build
from distutils.command import *
"""


def calculateSalary(hours, hWage, bonusApplied):
    salary = hours * hWage
    if (bonusApplied):
        salary *= 1.1
    return salary


print(calculateSalary(10, 11, True))



"""Write a function in Python (generate_fibonacci) to accept one 
integer argument (n) and generate the Fibonacci series of  n numbers. 
The series shall start at 1. 
"""

print(list(range(1,5))[0])


def generate_fibonacci(n):
    fibonacci = [1]

    if n<=1:
        return fibonacci
    else:
        fibonacci.append(1)

    for i in range(2,n):
        fibonacci.append(fibonacci[i-1]+fibonacci[i-2])

    return fibonacci

print(generate_fibonacci(7))


def generate_fib_number(n):
    if n == 1 or n == 2:
        return 1
    else:
        return generate_fib_number(n-1)+generate_fib_number(n-2)

def generate_fibonacci2(n):
    fib = []
    for i in range(1,n+1):
        fib.append(generate_fib_number(i))

    return fib;

print(generate_fibonacci2(7))


def calcualte_f_number(a,b,c):
    return (a+b)/c

#print(calcualte_f_number(5))

print(calcualte_f_number(5,6,2))


def calcualte_g_number(*numbs):
    return (numbs[0]+numbs[1])/numbs[2]

print(calcualte_g_number(5,6,2))
#print(calcualte_g_number(5,6))
#print(calcualte_g_number(5))

print(calcualte_f_number(b =18,c =3, a = 20))


def calcualte_h_number(**numbs):
    return (numbs["a"]+numbs["b"])/numbs["c"]

print(calcualte_h_number(b =18,c =3, a = 30))


def calcualte_f2_number(a: int = 1, b: int = 1, c: int = 1) -> float:
    """

    :param a:
    :param b:
    :param c:
    :return:
    """
    return (a+b)/c

print(calcualte_f2_number(b =18,c =3, a = 30))
print(calcualte_f2_number(b =18,c =3))


def myFunction():
    pass;


myLamda = lambda a,b,z : b*z/a
print("myLamda:",myLamda(3,5,7))