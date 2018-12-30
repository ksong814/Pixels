
import turtle

# creates a turtle (pen) an sets the speed (where 0 is fastest and 10 is slowest)
# The colors can be set through their names or through hexadecimal codes, use hex for accuracy
myPen = turtle.Turtle()
myPen.speed(0)
myPen.color("#000000")
turtle.delay(0)

# setting out box sizes to the n sq pixels per box
boxSize = 10
 

# myPen.setheading(n) points pen to given angle direction.
# where n queals the angle.
# 0 points to the right, 90 to go up, 180 to go to the left 270 to go down

# Positions myPen in top left area of the screen
# This should change according to the image size you want to make and the size of your boxes ("pixels")
# This canvas is currently set to 200*200 pixels or a 20x20 box of 10 sq pixels each
myPen.penup()
myPen.forward(-150)
myPen.setheading(90)
myPen.forward(150)
myPen.setheading(0) 

# This function draws a box by drawing each side of the square and using the fill function
def box(intDim):
    myPen.begin_fill()
    # 0 deg.
    myPen.forward(intDim)
    myPen.left(90)
    # 90 deg.
    myPen.forward(intDim)
    myPen.left(90)
    # 180 deg.
    myPen.forward(intDim)
    myPen.left(90)
    # 270 deg.
    myPen.forward(intDim)
    myPen.end_fill()
    myPen.setheading(0)  

 
# You will save your drawings as lists.
# This first list stores the color values
pallet_1 = ["#FFFFFF" , "#FFFF00" , "#000000" , "#61380B" , "#F4FA58"]
# Your drawings are stored using a "list of lists" where each value within every list
# element is the index of the color in the pallet list
# Banana
pixels_1 = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
pixels_1.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
pixels_1.append([0,0,0,0,0,0,0,0,2,2,0,0,0,0,0,0])
pixels_1.append([0,0,0,0,0,0,2,2,3,3,2,0,0,0,0,0])
pixels_1.append([0,0,0,0,0,2,4,1,2,2,0,0,0,0,0,0])
pixels_1.append([0,0,0,0,2,4,4,1,2,0,0,0,0,0,0,0])
pixels_1.append([0,0,0,2,4,4,1,2,0,0,0,0,0,0,0,0])
pixels_1.append([0,0,2,4,4,4,1,2,0,0,0,0,0,0,0,0])
pixels_1.append([0,0,2,4,1,1,2,0,0,0,0,0,0,0,0,0])
pixels_1.append([0,0,2,4,4,1,2,0,0,0,0,0,0,0,0,0])
pixels_1.append([0,0,0,2,4,1,1,2,2,2,0,0,0,0,0,0])
pixels_1.append([0,0,0,0,2,4,1,3,2,0,0,0,0,0,0,0])
pixels_1.append([0,0,0,0,0,2,2,2,0,0,0,0,0,0,0,0])
pixels_1.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
pixels_1.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
pixels_1.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])

# Mario
pallet_2 = ["#4B610B" , "#FAFAFA" , "#DF0101" , "#FE9A2E"]
pixels_2 = [[1,1,1,1,2,2,2,2,2,2,2,2,1,1,1,1]]
pixels_2.append([1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,1])
pixels_2.append([1,1,1,0,0,0,3,3,3,3,3,0,3,1,1,1])
pixels_2.append([1,1,0,3,0,3,3,3,3,3,3,0,3,3,3,1])
pixels_2.append([1,1,0,3,0,0,3,3,3,3,3,3,0,3,3,3])
pixels_2.append([1,1,0,0,3,3,3,3,3,3,3,0,0,0,0,1])
pixels_2.append([1,1,1,1,3,3,3,3,3,3,3,3,3,3,1,1])
pixels_2.append([1,1,1,0,0,2,0,0,0,0,2,0,1,1,1,1])
pixels_2.append([1,1,0,0,0,2,0,0,0,0,2,0,0,0,1,1])
pixels_2.append([0,0,0,0,0,2,2,2,2,2,2,0,0,0,0,0])
pixels_2.append([3,3,3,0,2,3,2,2,2,2,3,2,0,3,3,3])
pixels_2.append([3,3,3,3,2,2,2,2,2,2,2,2,3,3,3,3])
pixels_2.append([3,3,3,2,2,2,2,1,1,2,2,2,2,3,3,3])
pixels_2.append([1,1,1,2,2,2,1,1,1,1,2,2,2,1,1,1])
pixels_2.append([1,0,0,0,0,1,1,1,1,1,1,0,0,0,0,1])
pixels_2.append([0,0,0,0,0,1,1,1,1,1,1,0,0,0,0,0])

# Tina ~ :) 
pallet_tina = ['#FFFFFF' , '#000000' , '#F5DEB3' , '#FFFF00' , '#00BFFF']
				#white		#black		#beige		#yellow		#blue
pixels_tina = [[0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0]]
pixels_tina.append([0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0])
pixels_tina.append([0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0])
pixels_tina.append([0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0])
pixels_tina.append([0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0])
pixels_tina.append([0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0])
pixels_tina.append([0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0])
pixels_tina.append([0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0])
pixels_tina.append([0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0])
pixels_tina.append([0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0])
pixels_tina.append([0,0,1,1,1,1,1,1,1,3,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0])
pixels_tina.append([0,0,1,1,1,1,1,1,1,1,3,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0])
pixels_tina.append([0,0,1,1,1,1,1,1,1,1,1,3,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0])
pixels_tina.append([0,0,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,2,1,1,2,1,1,2,1,1,1,0,0,0,0])
pixels_tina.append([0,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,1,1,1,0,0,0,0])
pixels_tina.append([0,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,1,1,1,0,0,0,0])
pixels_tina.append([0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,1,1,1,1,1,0,0,0])
pixels_tina.append([0,1,1,1,1,1,1,1,1,1,1,1,2,1,0,0,0,0,0,0,1,1,1,0,0,0,0,0,1,0,0])
pixels_tina.append([0,1,1,1,1,1,1,1,1,1,1,1,2,1,0,0,0,0,0,0,1,2,1,0,0,0,0,0,1,0,0])
pixels_tina.append([0,1,1,1,1,1,1,1,1,1,1,1,2,1,0,0,0,1,0,0,1,2,1,0,0,1,0,0,1,0,0])
pixels_tina.append([0,1,1,1,1,1,1,1,1,1,1,1,2,1,0,0,0,0,0,0,1,2,1,0,0,0,0,0,1,0,0])
pixels_tina.append([0,1,1,1,1,1,1,1,1,1,1,1,2,2,1,0,0,0,0,1,2,2,2,0,0,0,0,1,0,0,0])
pixels_tina.append([0,1,1,1,1,1,1,1,1,1,1,1,2,2,2,1,1,1,1,2,2,2,2,1,1,1,1,0,0,0,0])
pixels_tina.append([0,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,1,2,2,1,0,0,0,0])


# This function takes a pallet and pixel list (matrix) to draw the picture
def draw(pallet, pixels):
	myPen.setheading(0)
	for row in pixels: 
		for color in row:
			myPen.color(pallet[color])
			box(boxSize)
			myPen.forward(boxSize)
			myPen.penup()
		myPen.setheading(180)
		myPen.forward(len(row) * boxSize)
		myPen.setheading(270)
		myPen.forward(boxSize)
		myPen.setheading(0)



def main():
	draw(pallet_tina,pixels_tina)
	# Need this to prevent window from closing!!!!
	turtle.done()

main()