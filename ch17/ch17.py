from PIL import ImageColor, Image
print("Hello, world!")
# PIL = python imaging library
print('red: ' + str(ImageColor.getcolor('red','RGBA')))
# print('blue: ' + str(ImageColor.getcolor('blue','RGBA')))
# print('green: ' + str(ImageColor.getcolor('green','RGBA')))
# print('chocolate: ' + str(ImageColor.getcolor('chocolate','RGBA')))
filename = 'zophie.png'
print("filename: %s" % filename)
try:
	catIm = Image.open(filename)
except ValueError:
	print("open of %s failed" % filename)
# print("size " + str(catIm.size))
# width, height = catIm.size
# print("width %s height %s" % (str(width), str(height)))
# print("%s %s %s" % (catIm.filename, catIm.format, catIm.format_description))
# catIm.save('zophie.jpeg')
faceIm = catIm.crop((355,345,565,560))
# croppedIm.save('cropped.png')

# catCopyIm = catIm.copy()
# catCopyIm.paste(faceIm,(0,0))
# catCopyIm.paste(faceIm,(400,500))
# catCopyIm.save('pasted.png')

catImWidth, catImHeight = catIm.size
faceImWidth, faceImHeight = faceIm.size
catCopyTwo = catIm.copy()
for left in range(0, catImWidth, faceImWidth):
	for top in range(0, catImHeight, faceImHeight):
		print(left,top)
		catCopyTwo.paste(faceIm, (left,top))
catCopyTwo.save('tiled.png')