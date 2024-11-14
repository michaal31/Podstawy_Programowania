kwota = float(input("Podaj kwotę: "))

vat_procent = 23

vat_kwota = kwota * vat_procent / 100

print(f"Kwota: {kwota:.2f} zł")
print(f"VAT (23%): {vat_kwota:.2f} zł")