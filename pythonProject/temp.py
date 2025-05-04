import time
import hmac
import hashlib
import base64
import struct

def generate_totp(email, time_step=30, digits=10):
    secret = (email + "HENNGECHALLENGE004").encode('utf-8')
    t = int(time.time()) // time_step
    msg = struct.pack('>Q', t)
    hmac_digest = hmac.new(secret, msg, hashlib.sha512).digest()
    offset = hmac_digest[-1] & 0x0F
    code = struct.unpack(">I", hmac_digest[offset:offset+4])[0] & 0x7FFFFFFF
    return str(code % (10 ** digits)).zfill(digits)

# Example usage:
email = 
print(generate_totp(email))
