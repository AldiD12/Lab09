PIN_KORREKT = "2580"
perpjekje_te_mbetura = 3
hyrje_e_lejuar = False

while perpjekje_te_mbetura > 0:
    pin_i_dhene = input(f"Jepni PIN-in ({perpjekje_te_mbetura} perpjekje te mbetura): ")
    if pin_i_dhene == PIN_KORREKT:
        print("Hyrje e lejuar")
        hyrje_e_lejuar = True
        break
    else:
        perpjekje_te_mbetura -= 1
        if perpjekje_te_mbetura > 0:
            print(f"PIN i gabuar. Ju kane mbetur {perpjekje_te_mbetura} perpjekje.")

if not hyrje_e_lejuar:
    print("Karta u bllokua")
else:

    while True:
        try:
            n_str = input("\nJepni nje numer te plote jo-negativ (n >= 0): ")
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

