PIN_KORREKT = "2580"
perpjekje_te_mbetura = 3
hyrje_e_lejuar = False

while perpjekje_te_mbetura > 0:
    pin_i_dhene = input(f"Jepni PIN-in ({perpjekje_te_mbetura} përpjekje të mbetura): ")
    if pin_i_dhene == PIN_KORREKT:
        print("Hyrje e lejuar")
        hyrje_e_lejuar = True
        break
    else:
        perpjekje_te_mbetura -= 1
        if perpjekje_te_mbetura > 0:
            print(f"PIN i gabuar. Ju kanë mbetur {perpjekje_te_mbetura} përpjekje.")

if not hyrje_e_lejuar:
    print("Karta u bllokua")
else:

    while True:
        try:
            n_str = input("\nJepni një numër të plotë jo-negativ (n >= 0): ")
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
