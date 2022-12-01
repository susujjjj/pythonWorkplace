#print("대기번호 : 1")
#print("대기번호 : 2")
#print("대기번호 : 3")
#print("대기번호 : 4")



for waiting_num in range(5): # 5미만까지, 즉 0 ~4까지 
  print("대기번호: {0}".format(waiting_num))
  
  #range(1, 6)  ->  1,2,3,4,5
  
  
starbucks = ["아이언맨", "토르", "아아엠 그루트"]
for customer in starbucks: 
  print("{0}, 커피가 준비되었습니다.".format(starbucks))