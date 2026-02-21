# with open("random_file.txt", "rb") as f:
#     data = f.read()
# #read first 20 bytes
# ordinal_list = list(data[:20])

# # Every byte is a number from 0-255. It can be represented 4 ways: hex (base 16), binary (base 2), decimal (base 10), and ASCII (the character it maps to)
# # and every character is 1 byte. you can represent these letters from any number between 0 to 255
# for letter in ordinal_list:
#     print(hex(letter), bin(letter), letter, chr(letter))


with open("random.png", "rb") as f:
    data = f.read()
png_bytes = list(data[:8])

print(png_bytes)
for byte in png_bytes:
    print(byte, chr(byte))
