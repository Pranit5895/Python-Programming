# USE OF COLLECTIONS AND THE LIGHWEIGHT DATA STRUCTURE namedtuple
from collections import namedtuple
# DECLARE THE STRUCTURE OF THE BOX DATA STRUCTURE
Box = namedtuple("Box", "color weight content_breakable")

# INITIALIZE SOME BOXES
b1 = Box("Red", 10, False)
b2 = Box("Blue", 20, True)
b3 = Box("Green", 40, False)

# CREATE A BOXES LIST AND POPULATE IT WITH SOME VAUES
Boxes = []
Boxes.append(Box("Red", 8, True))
Boxes.append(Box("Blue", 11, True))
Boxes.append(Box("Green", 15, False))
Boxes.append(Box("Yellow", 16, True))
Boxes.append(Box("Red", 29, False))
Boxes.append(Box("Blue", 56, True))
Boxes.append(Box("Red", 5, False))

# DECLARE VARIABLES TO COUNT THE NUMBER OF BOXES
num_of_red_boxes = 0
num_of_blue_boxes = 0
num_of_other_boxes = 0

# USE A FOR LOOP TO COUNT THE BOXES
for box in Boxes:
    if box.color == 'Red':
        num_of_red_boxes = num_of_red_boxes + 1
    elif box.color == 'Blue':
        num_of_blue_boxes = num_of_blue_boxes + 1
    else:
        num_of_other_boxes = num_of_other_boxes + 1

print(num_of_red_boxes)
print(num_of_blue_boxes)
print(num_of_other_boxes)
