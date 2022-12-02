#일반유닛
class Unit: 
  def __init__(self, name, hp): 
    self.name = name
    self.hp = hp
    # self.damage = damage  #메딕은 공격력이없으니깐 삭제 

#공격유닛 나타내는 클래스 
#근데 위 Unit의 name, hp랑, 아래 name, hp겹친다.? 이럴때 우리가 inheritance를 쓸수있는데
#상속은 말그대로 물려받는것을 의미.
#그래서 Unit이라는 클래스의 내용을 상속 받아서 attack unit을 만드는거에요
#그러면 Unit에 있는 이 멤버변수와 메소드는 그대로 어택에서 쓸수있음
class AttackUnit(Unit): #self는 자기자신을 의미.
  #그러면 공격Unit은 일반Unit클래스를 상속받아서 만들어진거고 
  #이때는 self.name 따로 정의해줄 필요가읎음
  def __init__(self, name, hp, damage): 
    Unit.__init__(self, name, hp)
    # self.name = name # 그냥 name 은 인자로 받은 name을 쓴다는것
    # self.hp = hp
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


#드랍쉽: 공중유니, 수송기. 마린/ 파이어백/ 탱크를 수송. 공격 없음
#날수 있는 기능을 가진 클래스 
class Flyable:
  def __init__(self, flying_speed):
    self.flying_speed = flying_speed
  def fly(self, name, location):
    print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]"\
      .format(name, location, self.flying_speed))
    
#공중 공격 유닛 클래스
class FlyableAttackUnit(AttackUnit, Flyable):
  def __init__(self, name, hp, damage, flying_speed):
    AttackUnit.__init__(self, name, hp, damage) 
    Flyable.__init__(self, flying_speed)
    
#발키리: 공중 공격 유닛, 한번에 14발 미사일 발사
valkyrie = FlyableAttackUnit("발키리", 200, 6, 5)
valkyrie.fly(valkyrie.name, "3시")
