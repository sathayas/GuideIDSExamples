import base64

# input html file
in_html = 'Chapter4-DataUnderstanding-Python.html'

# output file base
fOutBase = 'foo-'
# output file extension
fOutExt = '.png'

# list of image lines
img_lines =[]


# opening the HTML file
fHTML = open(in_html, 'r')

# loop to read the HTML file, line by line
line = fHTML.readline()
while line:
    # checking if the image line
    if line.startswith('<img src="data:image/png;base64,'):
        # text processing
        line = line.strip().replace('<img src="data:image/png;base64,','')
        # saving the base64 string
        img_lines.append(line)
    line = fHTML.readline()

fHTML.close()


# number of images
nImg = len(img_lines)

for i in range(nImg):
    img_data = str.encode(img_lines[i])
    fImageOut = fOutBase + str(i+1) + fOutExt

    with open(fImageOut, "wb") as fh:
        fh.write(base64.decodebytes(img_data))
