# 행, 열값 받아서 규칙에 맞춰 값 출력하기
while True:
  try:
    m = int(input())  #행의 역할
    n = int(input())  #열의 역할
    a = 1
    if m < 0 or n < 0:
      print("음수는 입력할 수 없습니다.")
    else:
      for i in range(1, m + 1):
        print(a, end = "")
        a += 1
        b = a
        for j in range(1, n):
          print(b, end = "")
          b += 1
        print()
      break
  except ValueError:
    print("에러입니다.")
