import matplotlib.pyplot as plt

mahsulotlar = ["Non", "Sut", "Tuxum", "Yog'", "Shakar"]
sotuv = [45, 30, 60, 20, 35]

plt.bar(mahsulotlar, sotuv, color="purple")
plt.title("Do'konda bir haftada sotilgan mahsulotlar soni")
plt.xlabel("Mahsulotlar")
plt.ylabel("Sotuv soni")
plt.show()

eng_kop = mahsulotlar[sotuv.index(max(sotuv))]
eng_kam = mahsulotlar[sotuv.index(min(sotuv))]
print(f"Eng ko'p sotilgan: {eng_kop}, Eng kam sotilgan: {eng_kam}")