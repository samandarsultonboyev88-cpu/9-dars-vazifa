import matplotlib.pyplot as plt

hafta = [1, 2, 3, 4, 5, 6, 7]
ish_soati = [5, 6, 8, 7, 6, 4, 3]

plt.plot(hafta, ish_soati, marker="o", color="teal")
plt.title("Kunlik ish soatlari")
plt.xlabel("Kunlar")
plt.ylabel("Soat")
plt.grid(True)
plt.savefig("natija.png")
plt.show()