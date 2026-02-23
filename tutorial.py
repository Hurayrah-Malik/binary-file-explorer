# with open("random_file.txt", "rb") as f:
#     data = f.read()
# #read first 20 bytes
# ordinal_list = list(data[:20])

# # Every byte is a number from 0-255. It can be represented 4 ways: hex (base 16), binary (base 2), decimal (base 10), and ASCII (the character it maps to)
# # and every character is 1 byte. you can represent these letters from any number between 0 to 255
# for letter in ordinal_list:
#     print(hex(letter), bin(letter), letter, chr(letter))

# Before list(): data is a bytes object → displayed as b'\x89PNG\r\n\x1a\n...' (\x notation for non-printable bytes)
# After list():  data is a list of ints  → displayed as [137, 80, 78, 71, 13, 10, 26, 10, ...] (plain decimal numbers)
# Same data underneath — just two different ways Python displays it on screen.


# PNG	[137, 80, 78, 71]
# JPEG	[255, 216, 255]
# PDF	[37, 80, 68, 70] (that's %PDF)
# ZIP	[80, 75, 3, 4] (that's PK)
# #given any file, read the first few bytes to find out what type of file it is.
def detect_file_type(data: bytes):
    file_bytes = list(data)

    # the magic bytes (beginning identifier bytes of each type of file)
    png_bytes = [137, 80, 78, 71]
    jpeg_bytes = [255, 216, 255]
    pdf_bytes = [37, 80, 68, 70]
    zip_bytes = [80, 75, 3, 4]

    if file_bytes[:4] == png_bytes:
        print("png")

    if file_bytes[:3] == jpeg_bytes:
        print("jpeg")

    if file_bytes[:4] == pdf_bytes:
        print("pdf")

    if file_bytes[:4] == zip_bytes:
        print("zip")


with open("HurayrahMalik.pdf", "rb") as f:
    data = f.read()

detect_file_type(data)
