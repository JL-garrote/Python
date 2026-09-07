a = 0

a = int(input("Introduce el primer numero a multiplicar \n"))
b = int(input("Introduce el numero de veces a multiplicar \n"))

for i in range(b + 1):
    print(f"La multiplicacion {a} * {i} =" , a * i , "\n")

