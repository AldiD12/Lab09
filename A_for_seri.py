while True:
    try:
        n_str = input("Jepni nje numer te plote jo-negativ (n >= 0): ")
        n = int(n_str)
        if n >= 0:
            break
        else:
            print("Ju lutem jepni nje numer jo-negativ.")
    except ValueError:
        print("Ju lutem jepni nje numer te vlefshem te plote.")

shuma = 0
faktoriali = 1

for i in range(1, n + 1):
    shuma += i
    faktoriali *= i

print(f"\nRezultatet per n = {n}:")
print(f"Shuma (S = 1 + 2 + ... + {n}) eshte: {shuma}")
print(f"Faktoriali ({n}!) eshte: {faktoriali}")

