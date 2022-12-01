# #while
# customer = "토르"
# index=5
# while  index >= 1:
#   print("{0}, 커피가 준비 되었습니다. {1}번 남았어요".format(customer, index))
#   index -= 1 #불렀으면 1개씩 줄여나가기
#   if index == 0:
#     print("커피는 폐기처분되었습니다")
#     # 5 4 3 2 1 번남고 0번째와서 커피 폐기처분하고 while문을 빠져나왔습니다 
    

customer = "토르"
person = "Unknown"

while person != customer:
  print("{0}, 커피가 준비 되었습니다.".format(customer))
  person = input("이름이 어떻게 되세요? ")
  #토르가 오면 반복문 탈출