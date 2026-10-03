#This is how we format string or insert variables within the string using the format method in the python but inn this method we need to be careful abt the placement of variables
letter = "My name is {} and I am from {}"

name = "Faheem Sajid"
country = "Pakistan"

print(letter.format(name,country))
print(letter)

#This is another method but here we need to be careful abt the placement of 0 and 1
letter = "My name is {0} and I am from {1}"

name = "Faheem Sajid"
country = "Pakistan"

print(letter.format(name,country))
print(letter)

#This is how we can do it using f-string
name = "Faheem Sajid"
country = "Pakistan"
letter1 = f"My name is {name} and I am from {country}"

print(letter1)

letter2 = f"My name is {{name}} and I am from {{country}}" #Double curly braces will be used when we want the same line to be printed
print(letter2)

