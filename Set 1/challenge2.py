import binascii

def fixed_xor(buffer1, buffer2):
  xor = bytearray()
  for x,y in zip(bytearray.fromhex(buffer1), bytearray.fromhex(buffer2)):
    xor.append(x ^ y)

  return binascii.hexlify(xor)

def run_test():
  hex1 = "1c0111001f010100061a024b53535009181c"
  hex2 = "686974207468652062756c6c277320657965"

  expected = "746865206b696420646f6e277420706c6179"
  actual = fixed_xor(hex1, hex2)

  print("Test passes: %s" % (expected == actual))

if __name__ == "__main__":
  run_test()