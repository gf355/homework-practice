num1 = float(input('Enter a number: '))
num2 = float(input('Enter a number: '))
num3 = float(input('Enter a number: '))
if (num1 > num2) and (num1 > num3):
  print('The first number is the biggest number.')
elif (num2 > num1) and (num2 > num3):
  print('The second number is the biggest number.')
elif (num3 > num1) and (num3 > num2):
  print('The third number is the biggest number.')
else:
  print('There is not a single biggest number.')
