AUTHOR = 'DeepFreeze'
import base64

print("Enter the b64 code to decode")
s = raw_input(">> ")
print(base64.b64decode(s))