# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

text = "Привет, меабв! аааа вабв вабвб аааб, пабв абв"

text = text.split()

text_new = []
for i in range(len(text)):
    if "абв"  not in text[i]:
        text_new.append(text[i])
print(" ".join(text_new))