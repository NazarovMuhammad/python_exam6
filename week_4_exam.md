# EXAM FOR WEEK 2
## RULES:
> No interner, no help to each other!
> Make one file and place all your work there (e.g. odina_kholiqov.py)
> Send the file at 
> You have 2 hours only


### 1 Question
Random Lottery Pick. Generate 100 random lottery tickets and pick two lucky tickets from it as a winner.
Случайный лотерейный выбор. Создайте 100 случайных лотерейных билетов и выберите из них два счастливых билета в качестве победителя.
    Note you must adhere to the following conditions(что необходимо соблюдать следующие условия:):
    The lottery number must be 10 digits long(Номер лотереи должен состоять из 10 цифр).
    All 100 ticket number must be unique(Все 100 номеров билетов должны быть уникальными).


### 2 Question
Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.
Напишите программу, которая принимает из консоли последовательность чисел, разделенных запятыми, и генерирует список и кортеж, содержащий каждое число.
Input:
34,67,55,33,12,98
Output: 
['34', '67', '55', '33', '12', '98']
('34', '67', '55', '33', '12', '98')


### 3 Question
Create a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.
Создайте генератором, который может перебирать числа, кратные 7, в заданном диапазоне от 0 до n.
Input:
n = 30
Output:
7 14 21 28

### 4 Question
Write a Python program to create a calculator class. Include methods for basic arithmetic operations. / Напишите программу на Python для создания класса калькулятора. Включите методы для основных арифметических операций.

### 5 Question
Write a Python program to create a person class. Include attributes like name, country and date of birth. Implement a method to determine the person's age. Use incapsulation methods as well. / Напишите программу на Python для создания класса человека. Включите такие атрибуты, как имя, страна и дата рождения. Реализуйте метод определения возраста человека. Также используйте методы инкапсуляции.

### 6 Question
Write a Python program to create a class representing a shopping cart. Include methods for adding and removing items, and calculating the total price. / Напишите программу на Python, чтобы создать класс, представляющий корзину покупок. Включите методы добавления и удаления элементов, а также расчета общей цены.

### 7 Question
Write a Python program to create a decorator that prints the arguments and return value of a function. / Напишите программу на Python, чтобы создать декоратор, печатающая аргументы и возвращаемое значение функции.

### 8 Question
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order. / Учитывая целочисленный массив nums и целое число k, верните k наиболее часто встречающихся элементов. Вы можете вернуть ответ в любом порядке.

#### Example 1:
    Input: nums = [1,1,1,2,2,3], k = 2
    Output: [1,2]

#### Example 2:
    Input: nums = [1], k = 1
    Output: [1]

### 9 Question
Write a Python class Restaurant with attributes like menu_items, book_table, and customer_orders, and methods like add_item_to_menu, book_tables, and customer_order. / Напишите класс Restaurant на Python с такими атрибутами, как menu_items, book_table и customer_orders, а также такими методами, как add_item_to_menu, book_tables и customer_order.

The class can have the following methods / Класс может иметь следующие методы:

    Add items to the menu / Добавление позиции в меню
    Make table reservations / Бронирование столика
    Take customer orders / Прием заказа клиента
    Print the menu / Печать меню
    Print table reservations / Печать забранированных столиков
    Print customer orders / Печать заказов клиентов

Note: Use dictionaries and lists to store the data. / Для хранения данных используйте словари и списки.


### 10 Question
Find palindromes. A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers. Given a string s, return true if it is a palindrome, or false otherwise. / Найдите палиндромы. Фраза является палиндромом, если после преобразования всех прописных букв в строчные и удаления всех небуквенно-цифровых символов она читается одинаково и вперед, и назад. Буквенно-цифровые символы включают буквы и цифры. Учитывая строку s, верните true, если это палиндром, или false в противном случае.

#### Example 1:
    Input: s = "A man, a plan, a canal: Panama"
    Output: true
    Explanation: "amanaplanacanalpanama" is a palindrome.

#### Example 2:
    Input: s = "race a car"
    Output: false
    Explanation: "raceacar" is not a palindrome.

#### Example 3:
    Input: s = " "
    Output: true
    Explanation: s is an empty string "" after removing non-alphanumeric characters.
    Since an empty string reads the same forward and backward, it is a palindrome.

