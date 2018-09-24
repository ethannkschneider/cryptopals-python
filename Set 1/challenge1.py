import base64
import binascii

def hex_to_base64(hex_str):
  raw = binascii.unhexlify(hex_str)
  encoded = base64.b64encode(raw)
  return encoded

# TESTS
def run_test():
  hex = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
  b64 = "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"

  result = hex_to_base64(hex)
  print("Are they equal: %s" % (b64 == result))

if __name__ == "__main__":
  run_test()