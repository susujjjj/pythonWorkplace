gun = 10

def checkpoint(soldiers): 
  #gun = 20 #여기께 쓰임
  global gun #전역 공간에 있는 gun사용 10
  gun = gun - soldiers
  print("[함수 내] 남은 총: {0}".format(gun))
  
  
def checkpoint(gun, soldiers):
  gun = gun - soldiers
  print("[함수 내] 남은 총: {0}".format(gun))
  return gun
  
print("전체 총 : {0}".format(gun))
# checkpoint(2) # 2명이 경계근무 나감 
gun = checkpoint(gun, 2)
print("남은 총 : {0}".format(gun))