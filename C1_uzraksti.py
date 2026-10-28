# ----------------------------------------------------------------------
# C1. Atzīmju kopsavilkums
# ----------------------------------------------------------------------

# Kodā izveido sarakstu ar septiņām atzīmēm. Izvadi to skaitu, summu, vidējo, augstāko un zemāko. Visu kodu raksti pats.
#
# Šis fails ir tukšs. Visu kodu raksti pats zem šīs rindas.
# ----------------------------------------------------------------------                                                                                                Sarakstu, kurā glabā atzīmes, nosauc ar vārdu atzimju_saraksts.

atzimes = (8, 6, 3, 8, 5, 7, 1)
skaits = []
summa = []
augastakais = []
zemakais = []

skaits = len(atzimes)
print("Atzimes skaits:", skaits)

summa = sum(atzimes)
print("Atzimes summa ir :", summa)

videjais = sum(atzimes) / len(atzimes)
print("Videja atzime ir:", videjais)

augstakais = max(atzimes)
print("Augstaka atzime ir:", augstakais)

zemakais = min(atzimes)
print("Zemaka atzime ir:", zemakais)

