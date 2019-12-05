i = 11
while i <= 20:
    print(i)
    i += 1
else:
    print("i is no longer less then 20")
j = 11
while j > 10:
    if j == 18:
        break
    j += 1
    if j == 16:
        continue
    print(j)
