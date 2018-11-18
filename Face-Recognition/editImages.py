import cv2

# Reads image as a color image
img = cv2.imread('twitter_logo.png', cv2.IMREAD_COLOR)

# Looking at specific pixels...
px = img[55,55]

# Changes a pixel
img[55, 55] = [255, 255, 255]

px = img[55, 55]
print(px)

# Modifies a whole region
# Draws a white box in the region 500:600 -> 500:600
img[500:600, 500:600] = [255, 255, 255]


# Cool areas on the image
print(img.shape)
print(img.size)
print(img.dtype)

# Getting part of the logo to reshape
logo = img[100:300, 100:300]
img[0:200, 0:200] = logo

# Putting text on the image
font = cv2.FONT_HERSHEY_TRIPLEX
cv2.putText(img, 'Twitter', (125, 515), font, 3, (255, 200, 200), 8, cv2.LINE_AA)

# Shows edited image until escape is tapped on keyboard.
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()