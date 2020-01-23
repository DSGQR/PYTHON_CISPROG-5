num1 = input('Enter a number: ')
num2 = num1 + 1
print(num2)

### ------ Output ------ ###
# Traceback (most recent call last):
#   File "main.py", line 2, in <module>
#     num2 = num1 + 1
# TypeError: can only concatenate str (not "int") to str

### ------ Explinaiton ------ ###
# I received a type error. The program thinks I am trying to cancatenate 
# two different data types. Cancatenation can only be done with strings and
# not inters. 