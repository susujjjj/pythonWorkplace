# Quiz) 당신의 학교 파이썬 코딩대회 주최한다
# 참석률을 높이기위해 댓글 이벤트를 진행하기로 함
# 댓글 작성자들 중 추첨을 통해 1명은 치킨, 3명은 커피쿠폰을 받게됨.
# 추첨 프로그램을 작성하라

# 조건1: 편의상 댓글은 20명이 작성하였고 아이디는 1-20 이라고 가정
# 조건2: 댓글 내용과 상관없이 무작위로 추첨하되 중복 불가
# 조건3: random모듈의 shuffle과 sample을 활용

# (출력 예제)
# == 담청자 발표 ==
# 치킨 당첨자: 1
# 커피 당첨자: [2, 3, 4]
# == 축하합니다 ==

# (활용 예제)
# from random import *
# list = [1,2,3,4,5]
# # print(list)
# # shuffle(list)
# # print(list)
# print(sample(list,1)) # 리스트중에서 1개를 무작위로 뽑음

from random import *

users = range(1, 21) #1부터 21직전, 즉, 1부너20까지 숫자를 생성
print(type(users))  #<class 'range'> 라고나오는데
#range는 list가 아니라서 list에서 쓰고자 하는 함수를 쓸수없어 이럴땐
users = list(users)  #users는 list라고 하고 users라고 해주면되요 
print(type(users))#<class 'list'>
#그러면 range타입이던 uses가 list로변환되어서 users에 저장되는거임



print(users)
shuffle(users)
print(users)

winners = sample(users, 4) #4명중에서 1명은 치킨, 3명은 커피

print(" -- 당첨자 발표 -- ")
print(" 치킨 당첨자 : {0}".format(winners[0]))
print(" 커피 당첨자 : {0}".format(winners[1:])) #1,2,3 인덱스에 있는걸 가져옴
print(" -- congrats -- ")