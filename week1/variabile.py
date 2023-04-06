# a = '0'
# a += '3'  concatenare de stringuri
# print(a)

nr_mere = 2
nr_pere = 3
# mesaj = f"Ana are {nr_mere} mere si {nr_pere} pere"
# mesaj = "Ana are {0} mere si {1} pere".format(nr_mere, nr_pere)
# mesaj = "Ana are " + str(nr_mere) + " mere si " + str(nr_pere) +" pere"
# mesaj = f"Ana are '{nr_mere}' mere si '{nr_pere}' pere"   la fel pentru ghilimele duble
# mesaj = f"Ana are \"{nr_mere}\" mere si \"{nr_pere}\" pere"  eroare fara \
# mesaj = f"Ana are \"{nr_mere}\" mere si \n \"{nr_pere}\" pere"
# si pere""" si ghilimele simple
mesaj = '''\tAna are mere
si pere'''  # tab
print(mesaj)