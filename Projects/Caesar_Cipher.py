def caesar(cipher_text, msg, shift_number):
    end_text = ""
    if cipher_text == 'decode':
        shift_number *= -1
    for letter in msg:
        position = alphabets.index(letter)
        new_position = shift_number + position
        end_text += alphabets[new_position]
    print(f"The {cipher_text}d value is: {end_text}")

should_continue = True
while should_continue:
    alphabets = 2 * [chr(i) for i in range(97, 123)]
    cipher_text = input("Type 'encode' for Encryption, 'decode' for decryption the text: ")
    msg = input("Enter the message (without space): ").lower()
    shift_number = int(input("Enter the shift number: "))

    # If user enters the shift_number out of range, so we can simply divide by 26 and add the remainder as shift_number
    shift_number = shift_number % 26
    caesar(cipher_text, msg, shift_number)

    restart = input("Type 'yes' to play again and 'no' to exit: ").lower()
    if restart == "no":
        should_continue = False
        print("Goodbye! ")
