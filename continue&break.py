absent = [2, 5] #만약 2번 5번학생이 결석
no_book = [7] #7번 학생  책을깜빡했음

for student in range(1, 11): #1,2,3,4,5,6,7,8,9,10 1번부터 10번까지의 출석번호가 있다고 가정해보겠다
  if student in absent: #반복중인 학생이 결석을 했다면 . 이 absent 리스트 속에 포함되는지를 보는거임
    #결석을 했다면! continue를 쓴다
    continue
  elif student in no_book:
    print("오늘수업 여기까지. {0}는 교무실로 따라와.".format(student))
    break
  print("{0}, 책을 읽어봐".format(student))
  #continue를 만나게되면 그 밑에 있는 문장을 실행하지 않고 다음 반복으로 이어서 하는거에요 즉, 
  #1번으로 하다가 2번으로 가야되는데 2번 continue 즉, 스킵하고 3번가는거임 
  
  #즉! continue는 아래에 있는 문장을 더이상 실행시키지 않고 다음 반복으로 계속 진행하도록 하라 라는 명령어다