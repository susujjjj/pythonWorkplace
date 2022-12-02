#일반유닛
class Unit: 
  def __init__(self, name, hp, damage): 
    self.name = name
    self.hp = hp
    self.damage = damage
    print("{0} 유닛이 생성 되었습니다.".format(self.name))
    print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))
    

#공격유닛 나타내는 클래스 
class AttackUnit: #self는 자기자신을 의미.
  def __init__(self, name, hp, damage): 
    self.name = name # 그냥 name 은 인자로 받은 name을 쓴다는것
    self.hp = hp
    self.damage = damage 
  
  def attack(self, location): #메소드 앞에는 항상 이 self를 무조건 적어야함
    print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]"\
      .format(self.name, location, self.damage)) 
    #location은 인자로받은 location을 쓰고. 나머지 self.들은 자기 자신에 있는 멤버변수의 값을 출력하는거즉 위에서 정의된 self.name, self.damage를 쓰는것  
    
  def damaged(self, damage):
    print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
    self.hp -= damage
    print("{0}: 현재 체력은 {1}입니다.".format(self.name, self.hp))
    if self.hp <= 0:
      print("{0}: 파괴되었습니다.".format(self.name))
      
      
#메딕: 의무병 . 다친사람 치료해주는 군인 그래서 공격력이없음 

#파이어백: 공격 유닛, 화영방사기가지고있음
firebat1 = AttackUnit("파이어뱃", 50, 16)
firebat1.attack("5시")

#25의 공격을 받았다고 가정하기
#공격 2번 받는다고 가정
firebat1.damaged(25)
firebat1.damaged(25)