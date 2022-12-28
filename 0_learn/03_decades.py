age = int(input('How old are you?\n'))

decades_float = age/10
print("You are " + str(decades_float) + " descdes old")

decades = age // 10
years = age % 10
print("You are " + str(decades) + " descdes and " + str(years) + " years old.")
