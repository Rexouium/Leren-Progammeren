Aantalcroissantjes = int(input("Hoeveel croissantjes"))
Aantalstokbroden = int(input("Hoeveel stokbroden"))
Aantalkortingsbonnen = int(input("Hoeveel kortingsbonnen"))

Item1 = "croissantjes"
Item1prijs = 0.39

Item2 = "stokbroden "
Item2prijs = 2.78 

Item3 = "kortingsbonnen"
Item3prijs = 0.50

totaalPrijs = (Aantalcroissantjes * Item1prijs) + (Aantalstokbroden * Item2prijs - (Aantalkortingsbonnen * Item3prijs))

print("De feestlunch kost je bij de bakker",totaalPrijs, "euro voor de", Aantalcroissantjes, "croissantjes en de", Aantalstokbroden, "stokbroden als de", Aantalkortingsbonnen," kortingsbonnen nog geldig zijn")
# git debugg?