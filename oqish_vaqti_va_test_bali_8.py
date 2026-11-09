import matplotlib.pyplot as plt

soat = [1, 2, 3, 4, 5, 6, 7]
ball = [40, 48, 55, 65, 72, 85, 90]

plt.scatter(soat, ball, color="red", s=50)
plt.title("O'quvchilarning kunlik tayyorlanish vaqti bilan test ballari")
plt.xlabel("Kunlik o'qish vaqti (soat)")
plt.ylabel("Test bali")
plt.grid(True)
plt.show()