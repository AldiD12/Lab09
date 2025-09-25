count = 0
total_sum = 0.0
min_val = None
max_val = None

print("Jepni numra një nga një. Shkruani 'stop' për të përfunduar.")

while True:
    txt = input("> ")
    
    if txt.lower().strip() == 'stop':
        break
    
    try:
        num = float(txt)
    except ValueError:
        print("Vlerë e pavlefshme")
        continue  
    count += 1
    total_sum += num
    
    if min_val is None or num < min_val:
        min_val = num
    if max_val is None or num > max_val:
        max_val = num

print("\n--- Përmbledhja Statistikore ---")
if count == 0:
    print("Nuk u dhanë të dhëna.")
else:
    mesatarja = total_sum / count
    print(f"Numri i vlerave (Count): {count}")
    print(f"Vlera Minimale (Min): {min_val}")
    print(f"Vlera Maksimale (Max): {max_val}")
    print(f"Mesatarja: {mesatarja:.2f}")
