import sys
print("python", "java", file=sys.stdout)
print("python", "java", file=sys.stderr)

scores = {"math": 20, "english": 50, "coding": 80}
for subject, score in scores.items():
  #우리가 딕셔너리 쓸때에는 key와 value쌍으로 튜플로 보내줍니다
  # print(subject, score)
  print(subject.ljust(8), str(score).rjust(4), sep=":")
  #왼쪽정렬하는데 총 8칸 공간 확보한 상태에서 왼쪽으로 정렬해달라는것임
  
# math    :  20
# english :  50
# coding  :  80



#은행 대기순번표
# 001, 002, 003, ... 
for num in range(1, 21):
  print("대기번호 : "+ str(num).zfill(3)) #3크기만큼의 공간을 확보하고, 나머지 빈공간만큼은 0으로채워달라는 의미

answer = input("아무 값이나 입력하세요 : ")
print("입력하신 값은 " + answer + "입니다.")
