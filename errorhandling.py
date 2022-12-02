# try:
#   print("나누기 전용 계산기입니다.")
#   num1 = int(input("첫 번째 숫자를 입력하세요 : "))
#   num2 = int(input("두 번째 숫자를 입력하세요 : "))
#   print("{0} / {1} = {2}".format(num1, num2, int(num1/num2)))
# except ValueError: #뭔가 문제가 있을때 except부분을 찾아요 찾아서 위에서 발생하는 오류에 해당하는 부분이 있으면은 ValueError가 발생했다고하면 그 내부에 있는 명령을 실행함 
#   print("에러! 잘못된 값을 입력하였습니다.") #에러면 이렇게 예외처리해줌  
# # 6 / 0 은 ZeroDivisionError: division by zero 에러나니까 또 예외처리해주기
# except ZeroDivisionError as err:
#   print(err) #division by zero

try:
  print("나누기 전용 계산기입니다.")
  nums = []
  nums.append(int(input("첫 번째 숫자를 입력하세요 : ")))
  nums.append( int(input("두 번째 숫자를 입력하세요 : ")))
  print("{0} / {1} = {2}".format(nums[0], nums[1], nums[2]))
except ValueError: #뭔가 문제가 있을때 except부분을 찾아요 찾아서 위에서 발생하는 오류에 해당하는 부분이 있으면은 ValueError가 발생했다고하면 그 내부에 있는 명령을 실행함 
  print("에러! 잘못된 값을 입력하였습니다.") #에러면 이렇게 예외처리해줌  
# 6 / 0 은 ZeroDivisionError: division by zero 에러나니까 또 예외처리해주기
except ZeroDivisionError as err:
  print(err) #division by zero
except Exception as err: #그외 나머지에서
  print("알 수 없는 에러가 발생하였습니다.")
  print(err)