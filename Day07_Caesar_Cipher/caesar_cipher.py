# Caesar Cipher Code with Separate Encode and Decode Functions
print("""
 ▄████████    ▄████████    ▄████████    ▄████████    ▄████████    ▄████████       ▄████████  ▄█     ▄███████▄    ▄█    █▄       ▄████████    ▄████████ 
███    ███   ███    ███   ███    ███   ███    ███   ███    ███   ███    ███      ███    ███ ███    ███    ███   ███    ███     ███    ███   ███    ███ 
███    █▀    ███    ███   ███    █▀    ███    █▀    ███    ███   ███    ███      ███    █▀  ███▌   ███    ███   ███    ███     ███    █▀    ███    ███ 
███          ███    ███  ▄███▄▄▄       ███          ███    ███  ▄███▄▄▄▄██▀      ███        ███▌   ███    ███  ▄███▄▄▄▄███▄▄  ▄███▄▄▄      ▄███▄▄▄▄██▀ 
███        ▀███████████ ▀▀███▀▀▀     ▀███████████ ▀███████████ ▀▀███▀▀▀▀▀        ███        ███▌ ▀█████████▀  ▀▀███▀▀▀▀███▀  ▀▀███▀▀▀     ▀▀███▀▀▀▀▀   
███    █▄    ███    ███   ███    █▄           ███   ███    ███ ▀███████████      ███    █▄  ███    ███          ███    ███     ███    █▄  ▀███████████ 
███    ███   ███    ███   ███    ███    ▄█    ███   ███    ███   ███    ███      ███    ███ ███    ███          ███    ███     ███    ███   ███    ███ 
████████▀    ███    █▀    ██████████  ▄████████▀    ███    █▀    ███    ███      ████████▀  █▀    ▄████▀        ███    █▀      ██████████   ███    ███ 
                                                                 ███    ███                                                                 ███    ███ 
""")
print("Welcome to the Caesar Cipher!")
print("This program can ENCODE (encrypt) or DECODE (decrypt) your messages.")
print("Note: It works only for alphabet letters. Symbols, spaces, and numbers will stay the same.\n")
# List of alphabets
alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(text, shift, direction):
    output_text = ""

    # Reverse the shift if decoding
    if direction == "decode":
        shift *= -1

    for char in text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = (position + shift) % len(alphabet)
            output_text += alphabet[new_position]
        else:
            output_text += char  # Keep non-alphabet characters as it is

    print(f"\nHere's the {direction}d result: {output_text}\n")


# Main program loop
should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    # Handle shifts greater than 26
    shift = shift % 26
    if direction == "encode" or "decode":
        caesar(text, shift, direction)
    else:
        print("Invalid input. Please type 'encode' or 'decode'.")

    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if restart.lower() != "yes":
        should_continue = False
        print("\nOk_bye! Thanks for using the Caesar Cipher!")

