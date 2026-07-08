## Question 1: Print Numbers 1 to 10

for i in range(1,11):
    print(f'Value : {i}')

## Question 2: Iterate Over a List

list_values = list(input('Enter the values : '))

for i in list_values:
    print(f'List sequesnce : {i}')

## Question 3: Print Even Numbers 1 to 20

for i in range(1,21):
    if i % 2 == 0:
        print(f'Even number : {i}')
## Question 4: Sum Numbers in a List
'''
list_value = list(int(input('Enter the list values : ')))
new_list = int(list_value)
sum_total = 0

for i in new_list:
    sum_total += i
    print(sum_total)
print(f'Total : {sum_total}')'''

my_list = [1, 2, 3, 4, 5]  # Example list
total = 0
for number in my_list:
    total += number
print(total)

## Question 5: Iterate Over a String
string_value = 'Hello World'

for i in string_value:
    print(f'Sequence of string letters : {i}')
## Question 6: Print Reverse of a String
string_value = 'Hello World'

for i in reversed(string_value):
    print(i)
## Question 7: List of Squares 1 to 10

for i in range(1,11):
    print(i**2)

## Question 8: Count 'a' in a String

text = 'Hello world arnorld is arnold'
cnt = 0
for i in text:
    if i == 'a':
        cnt += 1
print(f'Total a count in the text : {cnt}')

## Question 9: Iterate Over Dictionary

my_dict = {'a': 1, 'b': 2, 'c': 3}  # Example dictionary
for key, value in my_dict.items():
    print(f"{key}: {value}")

## Question 10: Find Minimum Value in a List
my_list = [5, 3, 2, 8, 1]  # Example list
min_value = float('inf')
print(min_value)
for number in my_list:
    if number < min_value:
        min_value = number
print(min_value)
     