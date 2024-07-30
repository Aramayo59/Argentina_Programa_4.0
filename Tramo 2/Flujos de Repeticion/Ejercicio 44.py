
A = int(input("Ingrese el primer número entero positivo (A): "))
B = int(input("Ingrese el segundo número entero positivo (B): "))


producto = 0

for _ in range(B):
    producto += A


print(A, "*", B, "=", producto, "(suma de", A, "sumado", B, "veces)")
