while True:
    print("\n--- Menu ---")
    print("1) Pershendetje")
    print("2) Shume e dy numrave")
    print("3) Ndihme")
    print("0) Dalje")
    print("------------")

    zgjedhja = input("Zgjidhni një veprim (0-3): ")

    if zgjedhja == '1':
        print("\nPërshendetje! Mirë se vini.")
        continue
    elif zgjedhja == '2':
        try:
            num1 = float(input("Jepni numrin e parë: "))
            num2 = float(input("Jepni numrin e dytë: "))
            print(f"Shuma është: {num1 + num2}")
        except ValueError:
            print("Hyrje e pavlefshme. Ju lutem jepni numra.")
        continue
    elif zgjedhja == '3':
        print("\n--- Ndihmë ---")
        print("Zgjidhni '1' për një përshëndetje.")
        print("Zgjidhni '2' për të mbledhur dy numra.")
        print("Zgjidhni '0' për të dalë nga programi.")
        continue
    elif zgjedhja == '0':
        print("Mirupafshim!")
        break
    else:
        print("Zgjedhje e pavlefshme. Ju lutem provoni përsëri.")
        continue
