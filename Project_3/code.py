# Generating a random password that takes password length as input
# and prints a random password of that length


import secrets
import string

pool_of_digits = string.ascii_letters+string.digits+string.punctuation

print("--------------Password Generator---------------\n")
while True:
  input_value = int(input("If you want to proceed generating password press '1' or to end press '0'\n"))
  if input_value != 0 and input_value != 1:
   print("Only 0 or 1 allowed!!")
   continue
  break
while input_value != 0:   
   list_new=[]
   input_digit= int(input("Enter the length of Password:\n"))
   for i in range(input_digit):
    str=secrets.choice(pool_of_digits)
    list_new.append(str)
   updated_string="".join(list_new)
   print("Password is:  ",updated_string)  
   input_value = int(input("To create another password press '2' or press '0' to end.\n"))

  

