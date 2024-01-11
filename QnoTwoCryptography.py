def decrypt(cryptogram, shift):
    decrypted_text = ''

    for char in cryptogram:
        if char.isalpha():
            if char.islower():
                decrypted_text += chr((ord(char) - shift - 97) % 26 + 97)
            else:
                decrypted_text += chr((ord(char) - shift - 65) % 26 + 65)
        else:
            decrypted_text += char

    return decrypted_text

#cryptogram from the newspaper 
cryptogram = "VZ FRYSVFU VZCNGVRAG NAQ N YVGGYR VAFRPHER V ZNXR ZVFGNXRF V NZ BHG BS PBAGEBY NAQNG GVZRF UNEQ GB UNAQYR OHG VS LBH PNAG UNAQYR ZR NG ZL JBEFG GURA LBH FHER NF URYYQBAG QRFREIR ZR NG ZL ORFG ZNEVYLA ZBAEBR"

#checking shift keys for orginal text
for shift in range(14):
    decrypted_text = decrypt(cryptogram, shift)
    print(f"Shift {shift}: {decrypted_text}")

print("Orginal text come in Shift 13")
