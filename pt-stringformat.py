#1
#d는 정수, s는 string, c는 character
print("I am %d years old." % 20) # % 뒤에 원하는 값 적기 . 20을 d위치에 넣겠다는 의미. d는 항상 정수만 가능 
print("나는 %s을 좋아해요." % "파이썬") 
print("Apple은 %c로 시작해요" % "A") 


#2
print("나는 {}살입니다." .format(20))
print("나는  {}색과 {}색을 좋아해요.".format("파란", "빨간"))


#3
# print("I am {age} years old, I like {color} color.".format(age=20, color="black"))


#4
age = 20
color = "pink"
print(f"I am {age} years old, I like {color} color.")