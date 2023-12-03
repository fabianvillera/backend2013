for number in range (1,101):
    if number%3 == 0:
        print("fiz")
    elif number % 5 == 0:
      print('buzz')
    elif number%5 == 0  and number% 3 == 0:
       print('fizBuss')
    else :
       print(number)