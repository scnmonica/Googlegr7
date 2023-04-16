
def analizor_cnp(cnp):
    s = cnp[0]
    if s not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
        return False
    aa = int(cnp[1:3])
    if aa > 99:
        return False
    ll = int(cnp[3:5])
    if ll < 1 or ll > 12:
        return False
    zz = int(cnp[5:7])
    if zz < 1 or zz > 31:
        return False
    elif zz > 28 and ll == 2:
        if int(cnp[1]) not in [1, 2]:
            return False
        elif zz > 29:
            return False
    if zz > 30 and ll in [4, 6, 9, 11]:
        return False
    jj = int(cnp[7:9])
    if jj < 1 or jj > 52:
        return False
    nnn = int(cnp[9:12])
    if nnn < 1 or nnn > 999:
        return False
    c = int(cnp[12])
    control = [2, 7, 9, 1, 4, 6, 3, 5, 8, 2, 7, 9]
    suma = 0
    for i in range(0, 12):
        suma += control[i] * int(cnp[i])
    rezultat = suma % 11
    if rezultat == 10:
        rezultat = 1
    if rezultat != c:
        return False
    if len(cnp) != 13:
        return False

    return True

cnp = str(input("Introduceti CNP: "))
if analizor_cnp(cnp):
    print("CNP valid")
else:
    print("CNP invalid")