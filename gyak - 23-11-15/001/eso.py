#Dobany Norbert 2023-11-15
print("Dobany Norbert 2023-11-15")

print("Adja meg a heti és múltheti csapadék mennyiségeket mm-ben")
most=float(input("Heti csapadék mennyiség: "))
elozo=float(input("Múltheti csapadék mennyiség: "))


if most==elozo:
    print("A két mennyiség megegyezik")
elif most>elozo:
    print("A héten több eső esett")
else:
    print("A múlthéten több eső esett")


