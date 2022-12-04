# import theater_module
# theater_module.price(3) #3명이서 영화보러 갔을 때 가격
# theater_module.price_morning(4) #4명이서 조조할인 영화보러갔을때
# theater_module.price_soldier(5) #5명의 군인이 영화보러 갔을 때


#as 뒤에 별명붙이기. theater_module은 기니까..!
# import theater_module as mv 
# mv.price(3)
# mv.price_morning(4)
# mv.price_soldier(5)


#theater_module 여기 모듈에 있는 모든것을 사용하겠다는의미. 
# from theater_module import *
# price(3)
# price_morning(4)
# price_soldier(5)

from theater_module import price_soldier as price
price(5) #price_soldier의 내용을 price처럼 쓰는것을 의미