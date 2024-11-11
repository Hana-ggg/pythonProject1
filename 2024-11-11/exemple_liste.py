liste = []
tuple = ()
dice = {}


print(type(liste))
print(type(tuple))
print(type(dice))

#ajoute element 0 à la liste
print(liste)
liste.append(0)
print(liste)

#ajoute element 0 à la tuple
liste_temporaire = list(tuple)
print(liste_temporaire)
liste_temporaire.append(0)
tuple = ()

tupleUn = (1,2,"test",(3,4,5))
print(tupleUn[1],tupleUn[2],tupleUn[3],tupleUn[3][0])

animaux={'a':'Chien','b':'Chat','c':'Souris'}
print(animaux['a'],
animaux.keys(),
animaux.values(),
animaux.items())
print(animaux.pop('b'))
print(animaux)
=> Chien dict_keys(['a', 'b', 'c']) dict_values(['Chien', 'Chat', 'Souris']) dict_items([('a', 'Chien'), ('b', 'Chat'), ('c', 'Souris')])
Chat
{'a': 'Chien', 'c': 'Souris'}
