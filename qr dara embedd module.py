import qrcode

# The data to be embedded in the QR code
data = input("enter the data you want to be embedded in qrcode : ")

# Generate the QR code
qr = qrcode.QRCode(
    version=None,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(data)
qr.make(fit=True)

# Create an image from the QR code
img = qr.make_image(fill_color="black", back_color="white")

# Save the image
img.save("qr_code.png")
