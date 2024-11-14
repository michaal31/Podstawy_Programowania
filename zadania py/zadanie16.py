
cena_produktu = float(input("Podaj cenę produktu: "))
rabat = float(input("Podaj rabat w procentach: "))
cena_po_rabacie = cena_produktu * (1 - rabat / 100)
roznica = cena_produktu - cena_po_rabacie


print(f"Cena produktu: {cena_produktu:.2f} zł")
print(f"Rabat: {rabat:.2f}%")
print(f"Cena po rabacie: {cena_po_rabacie:.2f} zł")
print(f"Różnica: {roznica:.2f} zł")
