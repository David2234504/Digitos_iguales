print("-------------------------------------")
print("---------Digitos iguales-------------")
print("-------------------------------------")

# input
n = int(input("Digite un numero: "))
 
# processing
if -10 <= n <= 10:
    rta = "El numero no tiene mas de dos digitos"
else:
    d = abs(n) % 100
    l = d % 10
    p = d // 10
    if l == p:
        rta = "Los ultimos dos digitos son iguales"
    else:
        rta = "Los ultimos dos digitos son diferentes"

# output
print("-------------------------------------")
print(str(rta))
print("-------------------------------------")

