row1 = ["🥸","🥸","🥸"]
row2 = ["🥸","🥸","🥸"]
row3 = ["🥸","🥸","🥸"]

map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}\n")
position = input("Where do you want to put the treasure\n")

horizonal = int(position[0])
vertical = int(position[1])

selected_row = map[vertical -1]
selected_row[horizonal -1] = "X"

print(f"{row1}\n{row2}\n{row3}")