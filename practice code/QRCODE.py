import pyqrcode
import png
from pyqrcode import QRCode

s = "www.SHEIN.com"

url = pyqrcode.create(s)

url.png('myqr.png', scale = 6)

import qrcode

# =========================
# CHANGE THESE DETAILS
# =========================
upi_id = "pateldipen4657-1@okaxis"      # example: dipenpatel@oksbi
name = "Dipen Patel"           # receiver name
amount = "10000"                 # amount in INR (optional)
note = "Payment for services"  # note (optional)

# UPI payment URL
upi_url = f"upi://pay?pa={upi_id}&pn={name}&am={amount}&cu=INR&tn={note}"

# Generate QR Code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

qr.add_data(upi_url)
qr.make(fit=True)

# Create Image
img = qr.make_image(fill_color="white", back_color="black")

# Save QR Code
img.save("gpay_payment_qr.png")

print("✅ GPay Payment QR Code generated successfully!")
print("📁 File saved as gpay_payment_qr.png")


import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer
from qrcode.image.styles.colormasks import SolidFillColorMask

# ===== PAYMENT DETAILS =====
upi_id = "yourupiid@bank"     # example: dipen@oksbi
name = "Dipen Patel"
amount = "250"
note = "Shop Payment"

upi_url = f"upi://pay?pa={upi_id}&pn={name}&am={amount}&cu=INR&tn={note}"

# ===== CREATE QR OBJECT =====
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=12,
    border=4,
)

qr.add_data(upi_url)
qr.make(fit=True)

# ===== GENERATE DESIGN QR =====
img = qr.make_image(
    image_factory=StyledPilImage,
    module_drawer=RoundedModuleDrawer(),
    color_mask=SolidFillColorMask(
        back_color=(255, 255, 255),
        front_color=(0, 0, 0)   # change color if you want
    )
)

# ===== SAVE =====
img.save("design_upi_qr.png")

print("✅ Design UPI QR Code generated")
print("📁 File: design_upi_qr.png")
