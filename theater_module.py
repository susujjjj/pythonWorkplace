#일반 가격 
def price(people):
  price("{0}명 가격은 {1}원 입니다".format(people, people * 10000))
  
#조조 할인 가격 
def price_morning(people):
  price("{0}명 가격은 {1}원 입니다".format(people, people * 6000))
  
#군인 할인 가격
def price_soldier(people):
  price("{0}명 군인 할인 가격은 {1}원 입니다".format(people, people * 4000))
  

