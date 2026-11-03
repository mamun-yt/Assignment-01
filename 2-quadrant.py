
x = float(input("Enter the x coordinate: "))
y = float(input("Enter the y coordinate: "))


if x > 0 and y > 0:
    print("The point is in the 1st quadrant.")
elif x < 0 and y > 0:
    print("The point is in the 2nd quadrant.")
elif x < 0 and y < 0:
    print("The point is in the 3rd quadrant.")
elif x > 0 and y < 0:
    print("The point is in the 4th quadrant.")
elif x == 0 and y == 0:
    print("The point is at the origin.")
elif x == 0:
    print("The point lies on the y-axis.")
else:
    print("The point lies on the x-axis.")
