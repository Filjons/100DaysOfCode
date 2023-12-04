import colorgram
colors = colorgram.extract("C:\\Users\\filjon\\OneDrive - Mildef\\Dokument\\Code\\100DaysOfCode\\Day 18\\painting\\my_image.jpg", 30)

rgp_colors = []
for color in colors:
    rgp_colors.append((color.rgb.r, color.rgb.g, color.rgb.b))

print(rgp_colors)