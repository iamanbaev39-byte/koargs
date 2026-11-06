def lugatni_chiqar(**lugat):
    print("Lug'at:")
    for soz, tarjima in lugat.items():
        print(f"{soz} — {tarjima}")


lugatni_chiqar(
    apple="olma",
    book="kitob",
    school="maktab",
)