
cabinet = {"A-3": "유재석" , "B-100": "김태호"}
print(cabinet["A-3"]) #유재석
print(cabinet["B-100"]) #김태호

#새 손님
print(cabinet)
cabinet["A-3"] = "김종국" #김종국
cabinet["C-20"] = "조세호" #캐비넷에 C-20이라는 키를 만들고 조세호라는 값을 만든거  
print(cabinet)


#간 손님
del cabinet["A-3"]
print(cabinet)


#key들만 출력
print(cabinet.keys()) #dict_keys(['B-100', 'C-20'])
print(cabinet.values()) #dict_values(['김태호', '조세호'])

#key, value 쌍으로 출력하려면 
print(cabinet.items()) 
# dict_items([('B-100', '김태호'), ('C-20', '조세호')])


#모든값 싹다 지우기
cabinet.clear()
print(cabinet)

