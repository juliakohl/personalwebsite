# a = 5
# b = 10

# print(a + b)
# print(a * b)
# print(a / b)
# # Exponentiation
# print(a ** b)
# # Modulo
# print ( 5 % 3)
# # Floor
# print ( 5 // 2)


# for i in range(0,10):
#     print(i)
#     if (i == 7):
#         break
# else:
#     print('else Zweig')



# b1 = [('Erstens', 'Zweitens', 'Drittens'), ('Viertens', 'Fünftens', 'Sechstens'), ('Siebtens', 'Achtens')]
# res = [y for x in b1 for y in x]
# print(res)
    
# def getNumber():
#     for i in range (1, 10):
#         return i
# def getNum():
#     for i in range(1, 10):
#         yield i
# print(getNum())
# print(getNumber())
# print(getNumber())
# for i in numberGenerator():
#     if (i == 20):
#         break
#     print(i)

# def getSquares():
#     squares = [x*x for x in range(20) if x % 2 == 0 ]
#     return squares
# res = getSquares()
# print(res)

# try:
#     3 / 0
# except:
#     print('Das hat nicht funktioniert')
# try:
#     print("Anna" + str(3))
# except Exception as e:
#     print(e)

# try:
#     liste = ['TestString','ZweiterString']
#     print(liste)
#     liste[1] = 'o'
#     print(liste)
#     print(type(liste))
# except Exception as ex:
#     print(ex)

# def class user(self):
#     def __init__(name, age, job):
#         self.n = name
#         self.a = age
#         self.j = job

#     def getDetails(self):
#         details = [self.n, self.a, self.j]
#         return details

# user1 = new user("Hans", 20, "Klempner")
# user1.getDetails()

# eins = "eins"
# zwei = "eins"

# # set1 = set()

# # set1 = {'eins', 'zwei', 'drei'}

# # print(set1)
# # print(id(set1))

# # set1("jhvj")

# # print(set1)
# # print(id(set1))


# print(id(eins))
# print(id(zwei))
# eins = "neue eins"
# print(id(eins))
# print(id(zwei))
# import requests
# from pprint import pprint



# # HTTP Request ausführen und Response abholen
# response = requests.get('https://api.chucknorris.io/jokes/random')
# print(response)

# # JSON extrahieren
# j = response.json()
# print(j['value'])
# #pprint(vars(response))
import urllib.request
from bs4 import BeautifulSoup
import math
import csv


url = "https://www.fhws.de "

response = urllib.request.urlopen(url)

print(response)


html = response.read()




# "BeautifulSoup" Objekt erzeugen
# Der zweite Parameter ('html5lib') im Konstruktur gibt an, welcher HTML Parser verwendet werden soll
# um im zweiten Schritt mittels get_text() nur den Text zu extrahieren und alle HTML
# Elemente zu "loeschen"
# Achtung: Nicht für den Produktiveinsatz geeignet, da nicht alle Woerter richtig erkannt werde
soup = BeautifulSoup(html, 'html5lib')


words = soup.text.split()

# Zählen der Häufigkeiten
haeufigkeiten = {}

for word in words:
    try:
        haeufigkeiten[word] = haeufigkeiten[word] + 1
    except Exception as e:
        haeufigkeiten[word] = 1


# WDF berechnen
wdf = {}
for word in words:
    wdf[word] = math.log2(haeufigkeiten[word] + 1) / math.log2(len(haeufigkeiten))

# Alle Daten vorhanden

# Ausgabe
for key in haeufigkeiten:
    #print(key, haeufigkeiten[key])
    # print("{0:<50}{1}\t{2}".format(x, tf[x], wdf[x]))
    print("{0:<50}{1}\t{2}".format(key, haeufigkeiten[key], wdf[key]))



# CSV Output
with open('tfwdf.csv', mode='w') as f:
    tfWriter = csv.writer(f, delimiter = '|', quotechar='"')
    for key in haeufigkeiten:
        tfWriter.writerow( [key, haeufigkeiten[key], wdf[key] ] ) 