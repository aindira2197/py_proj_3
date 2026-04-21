# Matn kiritish
matn = input("Matn kiriting: ")

# Unli harflar ro‘yxati
unlilar = "aeiouAEIOU"

# Sanash uchun o‘zgaruvchi
soni = 0

# Har bir belgini tekshiramiz
for harf in matn:
    if harf in unlilar:
        soni += 1

# Natijani chiqaramiz
print("Unli harflar soni:", soni)
