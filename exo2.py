# Fonction récursive devinRec
def devinRec(a, b):
    if a < b:
        return 0
    else:
        return 1 + devinRec(a - b, b)

# Fonction récursive factorielle
def factorielle(a):
    if a == 0 or a == 1:
        return 1
    else:
        return a * factorielle(a - 1)

# utilisation de la fonction devinRec
a = 10
b = 4
result = devinRec(a, b)
print(f"La division entière de {a} par {b} est : {result}")

# utilisation de la fonction factorielle
n = 6
fact = factorielle(n)
print(f"La factorielle de {n} est : {fact}")
