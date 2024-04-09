import string

alphabet = string.ascii_lowercase

userString = input('Input String:')
shift = int(input('Input Shift:'))
result = ''

for char in userString:
  if char.isalpha():
    shiftedIndex = (alphabet.index(char.lower()) + shift) % 26
    shiftedChar = alphabet[shiftedIndex]
    result += shiftedChar
  else:
    result += char

print(f'Encrypted String: {result}')