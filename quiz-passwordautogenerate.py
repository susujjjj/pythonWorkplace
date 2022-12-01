#Quiz) 사이트 별로 비번 만들어주는 프로그램을 작성하시오

#예) http://naver.com
#rule1: http:// 부분 제외 -> naver.com
#rule2: 처음 만나는점(.) 이후 부분은 제외  -> naver
#rule3: 남은 글자중 처음 세자리 + 글자갯수 + 글자 내 'e'갯수 + "!"로 구성
#              (nav)          (5)          (1)          (1)
# generated password: nav51!

url = "http://naver.com"
my_str = url.replace("http://", "") #규칙1
#print(my_str)
my_str = my_str[:my_str.index(".")] #규칙
 # my_str[0:5] -> 0 ~ 5 직전까지. (0, 1, 2, 3, 4)
# print(my_str)
password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
print("{0}의 비밀번호는 {1}입니다.".format(url, password))

