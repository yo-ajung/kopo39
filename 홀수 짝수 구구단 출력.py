#홀수만 출력
a = 1
while a <= 9:
  i = 1
  while i <= 9:
      print(str(a) + 'X'+str(i) + '=' + str(i*a))
      i += 2
  a += 2



#짝수만 출력
a = 2
while a <= 9:
  i = 2
  while i <= 9:
    print(str(a) + 'X'+str(i) + '=' + str(i*a))
    i += 2
  a += 2  
