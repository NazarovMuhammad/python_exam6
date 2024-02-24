# ### 1 Question
# Random Lottery Pick. Generate 100 random lottery tickets and pick two lucky tickets from it as a winner.
# Случайный лотерейный выбор. Создайте 100 случайных лотерейных билетов и выберите из них два счастливых билета в качестве победителя.
#     Note you must adhere to the following conditions(что необходимо соблюдать следующие условия:):
#     The lottery number must be 10 digits long(Номер лотереи должен состоять из 10 цифр).
#     All 100 ticket number must be unique(Все 100 номеров билетов должны быть уникальными).

### 1 Answer

# import random
# lists = []
# c = 100
# for i in range(1,c+1):
#     a = random.randint(1000000000,9999999999)
#     lists.append(a)
# v = random.choices(lists,k = 2)    
# print(v)    










# ### 2 Question
# Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.
# Напишите программу, которая принимает из консоли последовательность чисел, разделенных запятыми, и генерирует список и кортеж, содержащий каждое число.
# Input:
# 34,67,55,33,12,98
# Output: 
# ['34', '67', '55', '33', '12', '98']
# ('34', '67', '55', '33', '12', '98')

### 2 Answer
# a = input().split()
# listss = []
# for i in a:
#     c = str(i)
#     listss.append(c)
# tupless = tuple(listss)

# print(listss)
# print(tupless)










# ### 3 Question
# Create a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.
# Создайте генератором, который может перебирать числа, кратные 7, в заданном диапазоне от 0 до n.
# Input:
# n = 30
# Output:
# 7 14 21 28


### 3 Answer
# def cratniy(n):
#     for i in range(1,n+1):
#         if i%7 == 0:
#             yield i
# a = int(input())
# c = cratniy(a)
# for i in c:
#     print(i,end=" ")













# ### 4 Question
# Write a Python program to create a calculator class. Include methods for basic arithmetic operations. 
# Напишите программу на Python для создания класса калькулятора. Включите методы для основных арифметических операций.

### 4 Answer
# class Calculator:
    
    
#     def __init__(self,a,b):
#         self.a = a
#         self.b = b
    
#     def jam(self):
#         return self.a + self.b
        
#     def tarh(self):
#         return self.a - self.b
    
#     def zarb(self):
#         return self.a * self.b
    
#     def taqsim(self):
#         return self.a / self.b
    
#     def mod(self):
#         return self.a % self.b

# a = int(input("Enter number: "))
# c = input("Enter symbol: ")
# b = int(input("Enter number: "))
# calc = Calculator(a,b)
# if c == "+" :
#     print(calc.jam()) 
# elif c == "-":
#     print(calc.tarh())
# elif c == "*":
#     print(calc.zarb())
# elif c == "/":
#     print(calc.taqsim())
# elif c == "%":
#     print(calc.mod())            
        










# ### 5 Question
# Write a Python program to create a person class. Include attributes like name, country and date of birth. Implement a method to determine the person's age. Use incapsulation methods as well.
# Напишите программу на Python для создания класса человека. Включите такие атрибуты, как имя, страна и дата рождения. Реализуйте метод определения возраста человека. Также используйте методы инкапсуляции.

### 5 Answer
# class Person:
    
#     def __init__(self,name,country,birthday):
#         self.name = name
#         self.country = country
#         self.birthday = birthday
        
#     def __get__(self):
#         return f"{self.name} {self.country} {2024-self.birthday}"    
    
# Muhammad = Person("Muhammad","Tajikistan",2007)
# print(Muhammad.__get__())  












# ### 6 Question
# Write a Python program to create a class representing a shopping cart. Include methods for adding and removing items, and calculating the total price.
# Напишите программу на Python, чтобы создать класс, представляющий корзину покупок. Включите методы добавления и удаления элементов, а также расчета общей цены.  








# ### 7 Question
# Write a Python program to create a decorator that prints the arguments and return value of a function. 
# Напишите программу на Python, чтобы создать декоратор, печатающая аргументы и возвращаемое значение функции.
# def Say_hello(func):
#     def wrapper():
#         print("hello")
#         func
#         return wrapper
#     return Say_hello    

# @Say_hello
# def Name():
#      print ("MUhammad")


# Name()






# ### 8 Question
# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order. / Учитывая целочисленный массив nums и целое число k, верните k наиболее часто встречающихся элементов. Вы можете вернуть ответ в любом порядке.

# #### Example 1:
#     Input: nums = [1,1,1,2,2,3], k = 2
#     Output: [1,2]

# #### Example 2:
#     Input: nums = [1], k = 1
#     Output: [1]


a = input().split()
for i in a:
    













