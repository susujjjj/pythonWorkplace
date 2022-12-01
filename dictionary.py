#{} 
cabinet = {3:"유재석", 100: "김태호"}
print(cabinet[3]) #유재석
print(cabinet[100]) #김태호

print(cabinet.get(3)) #유재석

print(cabinet[5])  #error 
print(cabinet.get(5))  #none 
print(cabinet.get(5, "사용가능")) #사용가능
print("hi")

#어떤 값이 있는지 확인 할수있다. 
print(3 in cabinet) #True
print(5 in cabinet) #False
