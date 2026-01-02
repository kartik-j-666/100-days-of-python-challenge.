
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(original_text,shift_amount,encode_or_decode):
    ciper_text = ''
    if encode_or_decode == 'decode':
        shift_amount *= -1

    for i in original_text:

        if i not in alphabet:
            ciper_text += i
        else:
            shifted_position = alphabet.index(i) + shift_amount #shifted_position = alphabet.2 + 3 \\\ in alphabet 'c' in 2position +3
            shifted_position %= len(alphabet) # range_between = 0 - 25
            ciper_text += alphabet[shifted_position] # new_variable = alphabet[5]  \\\ alphabet [5] = 'f'
     print(f"Here is the {encode_or_decode}d result: {ciper_text}")

once_more = True
while once_more:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(original_text=text,shift_amount=shift,encode_or_decode=direction)
    again = input("Type 'yes' if you want to ga again. otherwise type 'no':\n").lower()
    if again == 'no':
        once_more = False
        print("see you next time!")
