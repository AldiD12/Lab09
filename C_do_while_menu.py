while True:
    print("\n--- Menu ---")
    print("1) Pershendetje")
    print("2) Shume e dy numrave")
    print("3) Ndihme")
    print("0) Dalje")
    print("------------")

    zgjedhja = input("Zgjidhni nje veprim (0-3): ")

    if zgjedhja == '1':
        print("\nPershendetje! Mire se vini.")
        continue
    elif zgjedhja == '2':
        try:
            num1 = float(input("Jepni numrin e pare: "))
            num2 = float(input("Jepni numrin e dyte: "))
            print(f"Shuma eshte: {num1 + num2}")
        except ValueError:
            print("Hyrje e pavlefshme. Ju lutem jepni numra.")
        continue
    elif zgjedhja == '3':
        print("\n--- Ndihme ---")
        print("Zgjidhni '1' per nje pershendetje.")
        print("Zgjidhni '2' per te mbledhur dy numra.")
        print("Zgjidhni '0' per te dale nga programi.")
        continue
    elif zgjedhja == '0':
        print("Mirupafshim!")
        break
    else:
        print("Zgjedhje e pavlefshme. Ju lutem provoni perseri.")
        continue

