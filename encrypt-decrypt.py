plainText = input("Enter text: ")
distance = int(input("Enter a distance: "))
code = ""
for ch in plainText:
    ordvalue = ord(ch)
    cipherValue = ordvalue + distance
    if cipherValue > ord('z'):
         cipherValue = ord('a') + distance - \
            (ord('z') - ordvalue +1)
    code += chr(cipherValue)
print(code)
