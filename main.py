'''

Programming HW 3 - Name Game

Description: Implement a program that can produce a verse of the "Name Game" song given an input name.

Developer Name(s): Salma Gitesatani

Date: 11/28/2022

'''

##########################################
# IMPORTS:
#   modules needed for program
##########################################


##########################################
# FUNCTIONS:
#   functions useful to main program
##########################################
#code goes here

def name_game(name):
    '''Prints one verse of the name game using the given name.'''
name= "Catherine"
vowel= 'aeiou'
if name[0].lower() in vowel and name[1].lower() in vowel:
  '''Checks if inputted name has a vowel in the first and second character'''
  '''Hacker Portion'''
  print(name.upper())
  print(name+", "+name+", bo-B"+name)
  print("banana fana fo-F"+name)
  print("fee-fi-mo-M"+name)
  print(name+"!")
else:
  print(name.upper())
  print(name+", "+name+", bo-B"+name[1:len(name)])
  print("Banana-fana fo-F"+name[1:len(name)])
  print("Fee-fi-mo-M"+name[1:len(name)])
  print(name+"!")
  
name= "Patrick"
vowel= 'aeiou'
if name[0].lower() in vowel and name[1].lower() in vowel:
  '''Checks if inputted name has a vowel in the first and second character'''
  '''Hacker Portion'''
  print(name.upper())
  print(name+", "+name+", bo-B"+name)
  print("banana fana fo-F"+name)
  print("fee-fi-mo-M"+name)
  print(name+"!")
else:
  print(name.upper())
  print(name+", "+name+", bo-B"+name[1:len(name)])
  print("Banana-fana fo-F"+name[1:len(name)])
  print("Fee-fi-mo-M"+name[1:len(name)])
  print(name+"!")

name= "Nery"
vowel= 'aeiou'
if name[0].lower() in vowel and name[1].lower() in vowel:
  '''Checks if inputted name has a vowel in the first and second character'''
  '''Hacker Portion'''
  print(name.upper())
  print(name+", "+name+", bo-B"+name)
  print("banana fana fo-F"+name)
  print("fee-fi-mo-M"+name)
  print(name+"!")
else:
  print(name.upper())
  print(name+", "+name+", bo-B"+name[1:len(name)])
  print("Banana-fana fo-F"+name[1:len(name)])
  print("Fee-fi-mo-M"+name[1:len(name)])
  print(name+"!")

name= "Abby"
vowel= 'aeiou'
if name[0].lower() in vowel:
  '''Checks if inputted name has a vowel in the first and second character'''
  '''Hacker Portion'''
  print(name.upper())
  print(name+", "+name+", bo-B"+name.lower())
  print("Banana-fana fo-F"+name.lower())
  print("Fee-fi-mo-M"+name.lower())
  print(name+"!")
else:
  print(name.upper())
  print(name+", "+name+", bo-B"+name[1:len(name)])
  print("Banana-fana fo-F"+name[1:len(name)])
  print("Fee-fi-mo-M"+name[1:len(name)])
  print(name+"!")

name= "Bart"
vowel= 'aeiou'
if name[0].lower() in vowel:
  '''Checks if inputted name has a vowel in the first and second character'''
  '''Hacker Portion'''
  print(name.upper())
  print(name+", "+name+", bo-B"+name.lower())
  print("Banana-fana fo-F"+name.lower())
  print("Fee-fi-mo-M"+name.lower())
  print(name+"!")
else:
  print(name.upper())
  print(name+", "+name+", bo-"+name[1:len(name)])
  print("Banana-fana fo-F"+name[1:len(name)])
  print("Fee-fi-mo-M"+name[1:len(name)])
  print(name+"!")

name= "Moses"
vowel= 'aeiou'
if name[0].lower() in vowel:
  '''Checks if inputted name has a vowel in the first and second character'''
  '''Hacker Portion'''
  print(name.upper())
  print(name+", "+name+", bo-B"+name.lower())
  print("Banana-fana fo-F"+name.lower())
  print("Fee-fi-mo-M"+name.lower())
  print(name+"!")
else:
  print(name.upper())
  print(name+", "+name+", bo-B"+name[1:len(name)])
  print("Banana-fana fo-F"+name[1:len(name)])
  print("Fee-fi-mo-"+name[1:len(name)])
  print(name+"!")

name= "Francis"
vowel= 'aeiou'
if name[0].lower() in vowel:
  '''Checks if inputted name has a vowel in the first and second character'''
  '''Hacker Portion'''
  print(name.upper())
  print(name+", "+name+", bo-B"+name.lower())
  print("Banana-fana fo-F"+name.lower())
  print("Fee-fi-mo-M"+name.lower())
  print(name+"!")
else:
  print(name.upper())
  print(name+", "+name+", bo-B"+name[1:len(name)])
  print("Banana-fana fo-"+name[1:len(name)])
  print("Fee-fi-mo-M"+name[1:len(name)])
  print(name+"!")
  '''Code will print out name without first letter if there is no vowel in first and second character'''
  

##########################################
# MAIN PROGRAM:
#   beginning of running program
##########################################
#leave the following alone




