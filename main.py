import random
import string

alphabet = string.ascii_lowercase

state = input('Do you want to encrypt or decrypt? [E/D]: ')
userString = input('Input String: ')
shift = int(input('Input Shift: '))
start = int(input('How many random letters on the start: '))
end = int(input('How many random letters on the end: '))

def encrypt(userString, shift):
  result = ''
  tempResult = ''
  randEnd = ''
  randStart = ''
  for char in userString:
    if char.isalpha():
      shiftedIndex = (alphabet.index(char.lower()) + shift) % 26
      shiftedChar = alphabet[shiftedIndex]
      randStart = ''.join(random.choice(alphabet) for _ in range(start))
      randEnd = ''.join(random.choice(alphabet) for _ in range(end))
      tempResult += shiftedChar
    else:
      tempResult += char

  result = randStart + tempResult + randEnd
  print(f'Encrypted String: {result}')

def decrypt(userString, shift, start, end):
  result = ''
  tempResult = ''
  for char in userString:
    if char.isalpha():
      shiftedIndex = (alphabet.index(char.lower()) - shift) % 26
      shiftedChar = alphabet[shiftedIndex]
      tempResult += shiftedChar
    else:
      tempResult += char
  result = tempResult[start:-end]
  print(f'Decrypted String: {result}')

if state == 'E':
  encrypt(userString, shift,)
elif state == 'D':
  decrypt(userString, shift, start, end)
else:
  print('Invalid input. Try again.')