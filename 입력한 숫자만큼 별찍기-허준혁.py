while True:
  try:
    n = int(input())
    if n <= 0:
      print("0 이하 숫자는 입력 불가능합니다.")
      continue
    else:
      str = '*'
      for i in range(1, n + 1):
        print(str)
        str += '*'
    break
  except ValueError:
    print("소수점 이하는 입력 불가능 합니다.")
