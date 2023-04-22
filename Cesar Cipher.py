from art import logo
print(logo)

def cesar(start_text, shift_amount, cipher_diretion):
    end_text = ""
    if cipher_diretion == "decode":
        shift_amount *= -1
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += char
    print(f"Here's the {direction}d result: {end_text}.")

alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

should_contiune = True
while should_contiune:
    direction = input("Type 'encode' to Encrypt, Type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift %= 26

    cesar(start_text=text, shift_amount=shift, cipher_diretion=direction)
    result = input("Type 'yes' if you want to go again, Otherwise type 'no'.\n")
    if result == "no":
        should_contiune = False
        print("Goodbye.")