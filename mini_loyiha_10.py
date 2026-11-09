import matplotlib.pyplot as plt

ismlar = ["Ali", "Vali", "Sardur", "Malika", "Aziza", "Jasur"]
ballar = [78, 92, 65, 88, 95, 73]

plt.bar(ismlar, ballar, color="skyblue")
plt.title("O'quvchilar natijalari tahlili")
plt.xlabel("O'quvchilar")
plt.ylabel("Ballar")
plt.grid(axis='y', linestyle='--')
plt.savefig("oquvchilar_natijasi.png")
plt.show()

print(f"Eng yuqori ball: {max(ballar)}, Eng past ball: {min(ballar)}")
print(f"O'rtacha ball: {sum(ballar) / len(ballar)}")