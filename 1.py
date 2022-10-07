Name = input("Введите имя ")
Surname = input("Введите фамилию ")
Year = int(input("Введите год рождения "))
print(Name+"_"+Surname+"_"+str(Year))
Name, Surname = Surname, Name
Year = Year + 60
print(Name+"_"+Surname+"_"+str(Year))
