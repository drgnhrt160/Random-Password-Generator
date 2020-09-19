import random


def shuffle(string):
  tempList = list(string)
  random.shuffle(tempList)
  return ''.join(tempList)

uppercaseLetter1=chr(random.randint(65,90)) #Generate a random Uppercase letter (based on ASCII code)
uppercaseLetter2=chr(random.randint(65,90)) #Generate a random Uppercase letter (based on ASCII code)
lowercaseLetter1=chr(random.randint(97,122)) #Generate a random lowercase letter
lowercaseLetter2=chr(random.randint(97,122)) #Generate a random lowercase letter
specialChar1=chr(random.randint(33,47)) #Generate a random special character
specialChar2=chr(random.randint(33,47)) #Generate a random special character
number1=chr(random.randint(48,57)) #generate a random number
number2=chr(random.randint(48,57)) #generate a random number
password = uppercaseLetter1 + uppercaseLetter2 + lowercaseLetter1 + lowercaseLetter2 + specialChar1 + specialChar2 + number1 + number2
password = shuffle(password)

#Ouput
print(password)
