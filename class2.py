class Unit: 
  def __init__(self, name, hp, damage): 
    self.name = name
    self.hp = hp
    self.damage = damage
    print("{0} 유닛이 생성 되었습니다.".format(self.name))
    print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))
    
# marine1 = Unit("마린", 40, 5)
# marine2 = Unit("마린", 40, 5)
# tank = Unit("탱크", 150, 35) # name hp damage

# 레이스: 공중 유닛, 비행기, 클로킹 (상대방에게 보이지 않음)
wraith1 = Unit("레이스", 80, 5)
print("유닛 이름: {0}, 공격력: {1}".format(wraith1.name, wraith1.damage))

# 마인드 컨트롤: 상대방 유닛을 내것으로 만듣는것 (빼앗음)
wraith2 = Unit("빼앗은 레이스", 80, 5)
wraith2.clocking = True

if wraith1.clocking == True:
  print("{0}는 현재 클로킹 상태입니다".format(wraith2.name))
  #'Unit' object has no attribute 'clocking'
  
  #이런식으로 클래스 외부에서 내가 원하는 어떤 변수에 대해서
  #확장 할수도있고 그확장된 변수는 내가 확장한 객체에 대해서만 적용이 되고
  #기존에 있던 다른 객체에는 적용이 안된다는점 