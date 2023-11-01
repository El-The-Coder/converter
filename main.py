import hashlib

def hex_to_text(hex_string):
    return bytearray.fromhex(hex_string).decode('utf-8')

def text_to_hex(text):
    return ''.join(format(ord(char), '02x') for char in text)

def binary_to_text(binary_string):
    return ''.join(chr(int(binary_string[i:i+8], 2)) for i in range(0, len(binary_string), 8))

def text_to_binary(text):
    return ''.join(format(ord(char), '08b') for char in text)

def md5_hash(text):
    return hashlib.md5(text.encode()).hexdigest()

def md5_to_text(md5_hash):
    return md5_hash

def hex_converter():
    while True:
        print("\nHex Converter Sub-menu:")
        print("1. Hex to Text")
        print("2. Text to Hex")
        print("0. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            hex_input = input("Enter Hexadecimal: ")
            print("Text: ", hex_to_text(hex_input))

        elif choice == "2":
            text_input = input("Enter Text: ")
            print("Hex: ", text_to_hex(text_input))

        elif choice == "0":
            break

        else:
            print("Invalid choice. Please enter a valid menu number.")

def binary_converter():
    while True:
        print("\nBinary Converter Sub-menu:")
        print("1. Binary to Text")
        print("2. Text to Binary")
        print("0. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            binary_input = input("Enter Binary: ")
            print("Text: ", binary_to_text(binary_input))

        elif choice == "2":
            text_input = input("Enter Text: ")
            print("Binary: ", text_to_binary(text_input))

        elif choice == "0":
            break

        else:
            print("Invalid choice. Please enter a valid menu number.")

def md5_hasher():
    while True:
        print("\nMD5 Hasher Sub-menu:")
        print("1. Text to MD5 Hash")
        print("2. MD5 Hash to Text")
        print("0. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            text_input = input("Enter Text for MD5 Hash: ")
            hashed_text = md5_hash(text_input)
            print("MD5 Hash: ", hashed_text)

        elif choice == "2":
            md5_input = input("Enter MD5 Hash: ")
            print("Text: ", md5_to_text(md5_input))

        elif choice == "0":
            break

        else:
            print("Invalid choice. Please enter a valid menu number.")

def main():
    banner="""

  .oooooo.    oooo                               .                    88
 d8P'  `Y8b   `888                             .o8           .dP     .8' Yb
888            888 .oo.    .ooooo.   .oooo.o .o888oo       .dP      .8'   `Yb
888            888P"Y88b  d88' `88b d88(  "8   888        dP       .8'      `Yb
888    ooooo   888   888  888   888 `"Y88b.    888        Yb      .8'       .dP
`88.    .88'   888   888  888   888 o.  )88b   888 .       `Yb   .8'      .dP
 `Y8bood8P'   o888o o888o `Y8bod8P' 8""888P'   "888"         `Yb 88      dP

 """
    print(banner)
    while True:
        print("\nMain Menu:")
        print("1. Hex Converter")
        print("2. Binary Converter")
        print("3. MD5 Hasher")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            hex_converter()

        elif choice == "2":
            binary_converter()

        elif choice == "3":
            md5_hasher()

        elif choice == "0":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please enter a valid menu number.")

if __name__ == "__main__":
    main()
