a = input("Alegerti o valoare: ")
try:
    print(int(a))
    print(variabila_nedefinita)
except NameError as e:
    variabila_nedefinita = None
    print('Name error')
except ValueError:
    print("S-a intalnit o eroare")
    a = input("Alegeti alta valoare: ")
except Exception as e:
    print(e)
else:
    print("S-a executat cu succes")
finally:
    print("Se executa oricum")
print("A trecut de blocul de try-except", variabila_nedefinita)