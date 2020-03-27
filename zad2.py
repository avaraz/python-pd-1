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
  print(a, "+", b, "=", a+b)
elif dzialanie == "2":
  print(a, "-", b, "=", a-b)
elif dzialanie == "3":
  print(a, "*", b, "=", a*b)
elif dzialanie == "4":
  print(a, "/", b, "=", a/b)
elif dzialanie == "5":
  print(a, "/", b, "=", a//b, "reszta:", a%b)
elif dzialanie == "6":
  print(a, "^", b, "=", a**b)
else:
  print("Nieprawidłowy numer działania.")
