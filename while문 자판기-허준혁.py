while True:
  try:   
    print("===================================================================")
    print('음료목록 1.오렌지주스(100원), 2.커피(200원), 3.콜라(300원), 99.종료')
    print("===================================================================")
    coin = int(input('동전을 넣으세요.'))
    if coin <= 0 :
      print("동전이 넣지 않았습니다. 다시 넣어주세요")
      continue

    drink = int(input('음료를 고르세요.\n'))
    if drink == 1:
      #오렌지 주스가 100원이다.
      if coin >= 100:
        remain = coin - 100
        print("오렌지 주스가 나옵니다.")
        print("거스름돈은 {}원입니다.".format(remain))
        coin = 0
      else:
        remain = coin
        print("금액이 부족합니다.")
        print("{}원이 반환됩니다.".format(remain))
        coin = 0

    elif drink == 2:
      #커피는 200원이다.
      if coin >= 200:
        remain = coin - 200
        print("커피가 나옵니다.")
        print("거스름돈은 {}원입니다.".format(remain))
        coin = 0
      else:
        remain = coin
        print("금액이 부족합니다.")
        print("{}원이 반환됩니다.".format(remain))
        coin = 0

    elif drink == 3:
      #콜라는 300원이다.
      if coin >= 300:
        remain = coin - 300
        print("콜라가 나옵니다.")
        print("거스름돈은 {}원이 나옵니다." .format(remain))
      else:
        remain = coin
        print("금액이 부족합니다.")
        print("{}원이 반환됩니다.".format(remain))
        coin = 0

    elif drink == 99:
      remain = coin
      print("주문을 종료합니다.")
      print("{}원이 반환됩니다.".format(remain))
      coin = 0
      break

    else:
      remain = coin
      print("없는 메뉴입니다. 다시 입력해주세요")
      print("{}원이 반환됩니다.".format(remain))
      
  except ValueError:
    print("소수점 이하의 값은 입력하실 수 없습니다.")
