while True:
    try:
        n_str = input("Jepni një numër të plotë jo-negativ (n >= 0): ")
        n = int(n_str)
        if n >= 0:
            break
        else:
            print("Ju lutem jepni një numër jo-negativ.")
    except ValueError:
        print("Ju lutem jepni një numër të vlefshëm të plotë.")

shuma = 0
faktoriali = 1

for i in range(1, n + 1):
    shuma += i
    faktoriali *= i

print(f"\nRezultatet për n = {n}:")
print(f"Shuma (S = 1 + 2 + ... + {n}) është: {shuma}")
print(f"Faktoriali ({n}!) është: {faktoriali}")
