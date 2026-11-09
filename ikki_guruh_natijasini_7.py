import matplotlib.pyplot as plt

testlar = [1, 2, 3, 4, 5]
guruh_a = [65, 70, 75, 80, 85]
guruh_b = [60, 72, 70, 88, 90]

plt.plot(testlar, guruh_a, label="Guruh A", color="blue", marker="o")
plt.plot(testlar, guruh_b, label="Guruh B", color="red", marker="x")
plt.title("Ikki guruhning test natijalari")
plt.xlabel("Testlar")
plt.ylabel("Ballar")
plt.legend()
plt.grid(True)
plt.show()