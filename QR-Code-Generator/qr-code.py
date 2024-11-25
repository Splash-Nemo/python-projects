import qrcode as qr
img= qr.make("https://www.geeksforgeeks.org/")

img.save("gfg.png")