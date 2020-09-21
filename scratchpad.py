while True:
  print('enter your age')

  age = input()

  try:
    age = int(age)
  
  except: 
    print('please use numeric digits')
    continue

  if age < 1:
    print('please enter a positive number')
    continue

  break

print(f'your age is {age}')
