from yubico_client import Yubico

CLIENT_ID = '113566'
yubico = Yubico(CLIENT_ID)

otp = otp_entry.get()  # Replace with your actual CTkEntry reference

try:
    if yubico.verify(otp):
        print("OTP valid!")
    else:
        print("OTP invalid.")
except Exception as e:
    print("Validation error:", e)