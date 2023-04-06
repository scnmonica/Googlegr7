a = 2
b = 2
c = 3
# mesaj, d = "a egal cu b", 0
# if a < b and (d := a + b) and d < a:
#    mesaj = "a mai mic decat b"
# elif a > b and (d := a - b) and d < a:
#    mesaj = "a mai mare decat b"
# elif a < c and (d := a + c) and d < a + b + c:
#    mesaj = "a mai mic decat c"
# print(f"Mesaj: {mesaj}")
# print(f"d: {d}")

rezultatul = a if a < b else b
print(rezultatul)
