#subway 1 = 10
#subway 2 = 20
#subway 3 = 30


subway = [10, 20, 30]
print(subway)

subway = ["john", "ray", "kate"]
print(subway)

"ray는 몇번째 칸에 타고 있는가?"
print(subway.index("ray")) # 1


#  haha 가 다음 정거장에서 다음칸에 탐
subway.append("haha")
print(subway)

#vivian을 john과 ray사이에 태워봄
subway.insert(1, "vivian") #index , 객체 
print(subway)


#지하철에 있는 사람을 한명씩 뒤에서 써냄
print(subway.pop())
print(subway)

#정렬도 가능
num_list = [5,2,4,3,1]
num_list.sort()
print(num_list) # [1, 2, 3, 4, 5]

#뒤집기 가능
num_list.reverse()
print(num_list)  #[5, 4, 3, 2, 1]

# 모두 지우기
num_list.clear()
print(num_list) #[]

#다양한 자료형과 함께 사용 가능
num_list = [5,2,4,3,1]
mix_list = ["조세호", 20, True]
# print(mix_list) #['조세호', 20, True] 

#리스트끼리 확장도 가능
num_list.extend(mix_list)
print(num_list) #[5, 2, 4, 3, 1, '조세호', 20, True]