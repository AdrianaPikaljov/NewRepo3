# #1 ulesanne
print("tere, maailm!")
nimi=input("kirjuta oma nimi: ").capitalize()
vanus=int(input("kirjuta oma vanus: "))
print("tere, maailm! tervitan sind",nimi,"!", "sa oled", vanus, "aastat vana.")

#2 ulesanne
vanus= 18
eesnimi= "jaak"
pikkus=16.5
kas_käib_koolis = True
print(type(vanus))
print(type(eesnimi))
print(type(pikkus))
print(type(kas_käib_koolis))

print(f"Muutuja {vanus} on {type(vanus)}")
print(f"Muutuja feesnimis on {type(eesnimi)}")
print(f"Muutuja {pikkus} on {type(pikkus)}")
print(f"Muutuja {kas_käib_koolis} on {type(kas_käib_koolis)}")
#Mis võimalus veel peale True oleks viimast muutujat väärtustada?
kas_käib_koolis = False

#3 ulesanne
from random import *
kommid=randint(10,100)
print("laual on", kommid ,"kommi")
ukrali_kommid=int(input("mitu kommi soovid votta?: "))
alles_kommi= kommid - ukrali_kommid
print("laual on nyyd alles", alles_kommi , "kommi" )

# #4 ulesanne 
from math import *
puu_umbermoot= float(input("kirjuta puu umbermoot: "))
labimoot= puu_umbermoot / pi
print("puu läbimõõt on",labimoot , "meetrit.")

#5 ulesanne
from math import *
n=float(input("sisesta maatukki pikkus: "))
m=float(input("sisesta maatukki laius: "))
diagonaal=sqrt (n**2 + m**2)
print("maatukki diagonaal on", diagonaal, "meetrit" )

#6 ulesanne
aeg = float(input("Mitu tundi kulus sõiduks? "))
teepikkus = float(input("Mitu kilomeetrit sõitsid? "))
kiirus = teepikkus / aeg
print("Sinu kiirus oli " + str(kiirus) + " km/h")

#7 ulesanne
print("sisesta 5 taisarvu")
arv1=int(input("esimene arv: "))
arv2=int(input("teine arv: "))
arv3=int(input("kolmas arv: "))
arv4=int(input("neljas arv: "))
arv5=int(input("viies arv: "))
aritmeetiline=(arv1 + arv2 + arv3 + arv4 + arv5)/5
print("antud arvude aritmeetiline keskmine on", aritmeetiline)

#8 ulesanne
print("    @..@")
print("   (----)")
print("  ( \__/ )")
print("   ^^ "" ^^  ")

#9 ulesanne
a=int(input("sisesta kolmnurga külg a: "))
b=int(input("sisesta kolmnurga külg b: "))
c=int(input("sisesta kolmnurga külg c: "))
umbermoot=a+b+c
print("kolmnurga ümbermõõt on", umbermoot)

#10 ulesanne
pitsa_hind=12.90
jootraha=0.10 * pitsa_hind

sobrad=int(input("kui palju inimest söövad pitsat?: "))
maksma= (pitsa_hind + jootraha) / sobrad
print("igauks peab maksma", maksma, "€")
