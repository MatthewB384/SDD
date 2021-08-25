#This gets the user to enter something, and tells them if it is a number or not

your_input = input('Enter something: ')


def print_the_input():
  print('Your input is', your_input)
  

def say_if_input_is_a_number():
  try:
    your_input = float(your_input) #if they type something that isnt a number this breaks and sends them to the except bit
    print('Your input is a number!')
  except:
    print('Your input is not a number!')
    

print_the_input()
say_if_input_is_a_number()
