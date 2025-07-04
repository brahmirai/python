#radom password generator
import random
upper_case="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower_case="abcdefghijklmnopqrstuvwxyz"
number="1234567890"
symbole='!@#$%^&*()_+-=[]{}|;:,.<>?'
all_character=upper_case+lower_case+number+symbole
length= 10
password="".join(random.sample(all_character,length))
print("your password is:",password)
