
with open("./sample-ggplot.png", 'rb') as f:
    img = f.read()
    with open('/job/output-files/my-image.png', 'wb') as f2:
        f2.write(img)
