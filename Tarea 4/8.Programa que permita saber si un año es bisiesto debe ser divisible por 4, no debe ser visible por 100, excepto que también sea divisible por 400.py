print("""
 ____    ___   ____   _          ___   _____   ___    ___
|___ \  / _ \ |___ \ / |        / _ \ |___ /  / _ \  ( _ ) 
  __) || | | |  __) || | _____ | | | |  |_ \ | | | | / _ \      
 / __/ | |_| | / __/ | ||_____|| |_| | ___) || |_| || (_) |
|_____| \___/ |_____||_|        \___/ |____/  \___/  \___/
""")
n1 = int(input("Introduce el año: "))

if(n1 % 4 == 0 and n1 % 100 == 0 and n1 % 400 == 0):
    print("Es bisiesto")
elif(n1 % 4 == 0 and n1 % 100 != 0):
    print("Es bisiesto")
else: print("No es bisiesto")    