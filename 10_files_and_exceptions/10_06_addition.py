# this program will use try except to make sure the user inputs numbers.

numOne = ('What is the first number you want to add:')
numTwo = ('What is the second number you want to add:')

num_one = input(numOne)
   
num_two = input(numTwo)
    
try: 
    answer = int(num_one) + int(num_two)
except ValueError:
    print("You need to 2 numbers!")
else:
    print(f' The answer is {answer}')

