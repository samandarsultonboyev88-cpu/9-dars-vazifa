import matplotlib.pyplot as plt

tillar = ["Python", "C", "JavaScript", "Java"]
o_quvchilar = [15, 8, 12, 5]

plt.pie(o_quvchilar, labels=tillar, autopct='%1.1f%%', startangle=90)
plt.title("Sinf o'quvchilarining sevimli dasturlash tillari")
plt.show()