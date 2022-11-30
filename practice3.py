python = "Python is Amazing"
print(python.lower())
print(python.upper())
print(python[0].isupper())
print(len(python))
print(python.replace("Python", "Java"))

index = python.index("n")
print(index) #5 출력. 5번째위치 
index = python.index("n", index+1) #15
#index+1에서는 두번째 n을 찾음. 따라서 Amazing에있는 n 을찾게됨
print(index)

print(python.find('Java'))#find에서는 java는 없으니까 -1을 출력함
print(python.index('Java'))#index에서는 java는 없으니까 error호출함 


print(python.count('n'))