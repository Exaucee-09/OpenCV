import cv2

#Read input image
image=cv2.imread('./assignment-001-given.jpg')

#Text properties
text = 'RAH972U'
font = cv2.FONT_HERSHEY_SIMPLEX
scale = 2
thickness = 5
text_color = (0, 255, 0)
box_color = (0,0,0)
padding = 3
alpha = 0.5

#calculating the text size and position
(img_height, img_width, _) = image.shape
(text_width, text_height), baseline = cv2.getTextSize(text, font, scale, thickness)

text_x = img_height - text_width
text_y = text_height + 120 # 110px padding from the top

#Coordinates for the background box
top_left = (text_x - padding, text_y - text_height - padding)
bottom_right = (text_x + text_width + padding, text_y + baseline + padding)

#Create copy of the image for transparency effect
overlay = image.copy()

#Draw the textbox on the overlay
cv2.rectangle(overlay, top_left, bottom_right, box_color, -1)

cv2.addWeighted(overlay, alpha, image, 1 - alpha, 0, image)

cv2.putText(image, text, (text_x, text_y), font, scale, text_color, thickness)

#Draw a green rectangle showing the number plate
cv2.rectangle(image,(265,190),(987,922),(0,255,0),4)

#Display the image
cv2.imshow('Result image', image)
cv2.waitKey(0)
cv2.imwrite("assignment-001-result.jpg", image)
cv2.destroyAllWindows()
