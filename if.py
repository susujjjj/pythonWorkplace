# weather = input("how's the weather today?")
# if weather == "rainy" or weather == "snowy":
#   print("take an umbrella")
# elif weather == "fine dust":
#   print("take a mask")
# else:
#   print("nothing to take!")


#2
temp = int(input("What's the temperature today?"))
if 30 <= temp:
  print("too hot. don't go out!")
elif 10 <= temp and temp < 30:
  print("fine!")
elif 0 <= temp < 10:
  print("bring your coat")
else:
  print("too cold. it is dangerous out of blanket!")