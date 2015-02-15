from PIL import Imagedef resize_img(im):  if(im.size[0] > MAX_SIZE or im.size[1] > MAX_SIZE):    minimum = min(im.size[0], im.size[1])    if(minimum == im.size[0]):      ratio = float(im.size[0]) / im.size[1]      width = int(ratio * MAX_SIZE)      height = MAX_SIZE    else:      ratio = float(im.size[1]) / im.size[0]      width = MAX_SIZE      height = int(ratio * MAX_SIZE)    return im.resize((width, height))  return imdef trace_img(im, out, outfile):  num = 0  for i in range(im.size[0]):    pixel = im.getpixel((i, 0))    for j in range(im.size[1]):      pix = im.getpixel((i, j))      if(pix != pixel):        pixel = pix        out.putpixel((i, j), 0)  for i in range(im.size[1]):    pixel = im.getpixel((0, i))    for j in range(im.size[0]):      pix = im.getpixel((j, i))      if(pix != pixel):        pixel = pix        out.putpixel((j, i), 0)def write_to_file(outfile, out):  num = 0.0  for i in range(out.size[1]):    for j in range(out.size[0]):      pix = out.getpixel((j, i))      if(pix == 0):        channel1 = float(i) / out.size[1] * 2 - 1        channel2 = float(j) / out.size[0] * 2 - 1        outfile.write(str(num / SAMPLE_RATE) + "\t" + str(channel1) + "\t" + str(channel2) + "\n")        num+=1filename = raw_input("Enter input file name: ")outfile = raw_input("Enter output file name: ")im = Image.open(filename)im = im.convert("1")MAX_SIZE = 1000SAMPLE_RATE = 44100im = resize_img(im)print im.sizeout = Image.new("1", im.size, "white")outfile = open(outfile, "wb")outfile.write("; Sample Rate " + str(SAMPLE_RATE) + "\n")outfile.write("; Channels 2\n")trace_img(im, out, outfile)write_to_file(outfile, out)outfile.close()im.show()out.show()