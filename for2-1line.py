# 출석번호가 1,2,3,4.. 앞에 100을 붙이기로 함 -> 101,102,103,104.

# students = [1,2,3,4,5] 
# print(students)
# students = [i+100 for i in students]
# print(students)

# 학생 이름을 길이로 변환
students = ["Iron man", "Thor", "I am groot"]

students = [len(i) for i in students] # i의 길이를 students에 집어넣겠다는 뜻
# students = [i.upper() for i in students]
print(students)