# This code will test various conditional staments


car = "Tesla"

# equality and inequality with strings
print (car == 'Tesla')
print (car != 'Tesla')

print ('\n')

# test using the lower method
print (car.lower() == 'tesla')
print (car.lower() == 'Tesla')

print ('\n')

# numerical test to check == != >= > <= <
number = 5
print (number == 5)
print (number != 5)
print (number  > 7)
print (7 >= number)
print (number < 7)
print (7 <= number) 

print ('\n')

# test using and and or
number_2 = 7
print (number == 5 and number_2 == 3)
print (number == 10 or number == 5)

print ('\n')

# test whether an item is or isn't in a list 
test_list = [1, 2, 3, 4, 5]

if 1 in test_list:
    print ("True")

if 6 not in test_list:
    print ("False")

