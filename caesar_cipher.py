message = input("Enter your message: ")
key = int(input("Enter the shift key: "))

ciphertext = ""

for ch in message:
    ordch = ord(ch)
    
    if 'a' <= ch <= 'z':
        ordch += key

        if ordch > ord('z'):
            ordch = ord('a') + (ordch - ord('z') - 1)
        newch = chr(ordch)
        ciphertext += newch
    
    elif 'A' <= ch <= 'Z':
        ordch += key

        if ordch > ord('Z'):
            ordch = ord('A') + (ordch - ord('Z') - 1)
        newch = chr(ordch)
        ciphertext += newch
    
    else:
        ciphertext += ch

print("Ciphertext:", ciphertext)
