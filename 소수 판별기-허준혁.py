#숫자 입력 받고 숫자가 소수인지 판별하기
def check_prime_num(x):
  for i in range(2, x):
    if x % i == 0:
        return False
    return True

while True:
  try:
      number = int(input('판별할 자연수를 입력하세요:'))
      if number <= 0:
        print("0과 이하는 입력하실 수 없습니다.")
      elif number == 1:
        print("1이외의 정수를 입력해 주시길 바랍니다.")
      else:
        print(check_prime_num(number))
        break

  except ValueError:
    print("정수를 입력해주세요")


