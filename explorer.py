# WHY PYTHON LOOKS "INCONSISTENT" WITH BYTES:
# The data never changes — it's always the same raw numbers underneath.
# What changes is the TYPE Python is displaying, and each type has its own display rules.
#
# type(raw_bytes) -> bytes object
# print(raw_bytes)        → bytes object  → Python shows \x25\x50PDF... (mix of \x hex and letters)
# print(list(raw_bytes)) → list of ints  → Python shows [37, 80, 68, 70, ...] (always decimal)
# iterating -> for bytes in raw_bytes ->  decimal numbers
# print(hex(byte))        → str           → Python shows '0x25' (hex with 0x prefix)
#
# Same byte (value 37), three different displays — because three different types.
# Python is not being inconsistent with the DATA, it's just applying different display
# rules to different types. The number 37 is always 37 — you're just choosing how to dress it up.


def main():
    # open the file and store the bytes in data
    with open("HurayrahMalik.pdf", "rb") as f:
        raw_bytes = f.read()
        # print(raw_bytes)
        hexdump(raw_bytes)


# take in bytes and output should look like this :
# output : 00000000  48 65 6c 6c 6f 20 57 6f  72 6c 64 21 0a 00 00 00  |Hello World!....|
# 00000010  ...next 16 bytes...
def hexdump(raw_bytes: bytes):
    # list of decimal bytes
    bytes_decimal = list(raw_bytes)
    # convert all these decimals to hex
    bytes_hex = []
    for byte in bytes_decimal:
        bytes_hex.append(hex(byte))

    # print first line
    print(f"{hex(16)}  {bytes_hex[:16]}")
    printable_bytes(bytes_decimal)


# function for building column 3 (each byte shown as ascii character if printable)
# printable: if byte is between 32 and 126, print letter
# not printable: print '.'
# print the bytes one by one first (test)
def printable_bytes(bytes_decimal: list):
    counter = 0
    # loop over every byte (decimal list)
    for byte in bytes_decimal:
        # if printable
        if 32 <= byte <= 126:
            print(chr(byte), end="")
            counter += 1
        # if not printable
        else:
            print(".", end="")
            counter += 1
        if counter > 16:
            break


if __name__ == "__main__":
    main()
