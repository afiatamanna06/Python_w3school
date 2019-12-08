flowers = ["Rose", "Jesmin", "Tuberose"]
print(flowers[0])
flowers[2] = "Marygold"
print(flowers)
print(len(flowers))
for x in flowers:
    print(x)
flowers.append("Tuberose")
print(flowers)
flowers.remove("Marygold")
print(flowers)
flowers.reverse()
print(flowers)
vehicles = ["Car", "Bus"]
flowers.extend(vehicles)
print(flowers)
