import random
import os

os.system("clear")
options = ('piedra', 'papel', 'tijeras')
computer_wins = 0
user_wins = 0
round = 1
while True:
  print('*' * 10)
  print('ROUND', round)
  print('*' * 10)
  print('computer_wins =>', computer_wins)
  print('user_wins =>', user_wins)
  user_option = input('piedra, papel o tijeras => ')
  user_option = user_option.lower()
  round += 1
  if user_option not in options:
    print('Esa opcion no es valida')
    continue
  computer_option = random.choice(options)
  print('User_option =>', user_option)
  print('Computer_option', computer_option)
  if user_option == computer_option:
    print('Empate!')
  elif user_option == 'piedra':
    if computer_option == 'tijeras':
      print('piedra gana a tijeras')
      print('user gano')
      user_wins += 1
    else:
      print('papel gana a piedra')
      print('computer gano')
      computer_wins += 1
  elif user_option == 'papel':
    if computer_option == 'piedra':
      print('papel gana a piedra')
      print('user gano')
      user_wins += 1
    else:
      print('tijeras gana a papel')
      print('computer gana')
      computer_wins += 1
  elif user_option == 'tijeras':
    if computer_option == 'papel':
      print('tijeras gana a papel')
      print('user gano')
      user_wins += 1
    else:
      print('piedra gana a tijeras')
      print('computer gano')
      computer_wins += 1
  if computer_wins == 2:
    print('El Rotundo Ganador Es La Computadora')
    break
  if user_wins == 2:
    print('El Rotundo Ganador Es El Usuario')
    break