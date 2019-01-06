import binascii
from string import ascii_lowercase

def single_byte_xor(char):
  char_byte = bytearray(char)[0]

  hex_encoded_str = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
  byte_array = bytearray.fromhex(hex_encoded_str)

  xor_result = bytearray()
  for x in byte_array:
    xor_result.append(x ^ char_byte)
  
  return xor_result.decode("utf-8")

if __name__ == "__main__":
  for ch in ascii_lowercase:
    print("%s --> %s" %(ch, single_byte_xor(ch)))

# answer is x!