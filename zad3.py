a,b = float(input("Podaj 2 liczby:")), float(input())
print("Twoje liczby to:", a, b)
print("Wybierz numer działania: ")
print("1. Dodawanie")
print("2. Odejmowanie")
print("3. Mnożenie")
print("4. Dzielenie bez reszty")
print("5. Dzielenie z resztą")
print("6. Potęgowanie")
dzialanie = input()
if dzialanie == "1":
  a+=b
  print("Dodawanie wynosi:", a)
elif dzialanie == "2":
  a-=b
  print("Odejmowanie wynosi:", a)
elif dzialanie == "3":
  a*=b
  print("Mnożenie wynosi:", a)
elif dzialanie == "4":
  a/=b
  print("Dzielenie wynosi:", a)
elif dzialanie == "5":
  a//=b
  print("Dzielenie wynosi:", a)
elif dzialanie == "6":
  a**=b
  print("Potęgowanie wynosi:", a)
else:
  print("Nieprawidłowy numer działania.")