import random, string

defaultLengthOfStrings = 24
defaultNumberOfRandomStrings = 10

def generateRandomString(length, usePunctuation):
    characterList = string.ascii_letters + string.digits
    if usePunctuation:
        characterList += string.punctuation
    randomizedString = ''.join(random.choices(characterList, k=length))
    return randomizedString

while True:
    lengthOfStrings = input(f'\nPlease enter the number for length of each string (default: {defaultLengthOfStrings}): ')
    if lengthOfStrings:
        try:
            lengthOfStrings = int(lengthOfStrings)
            break
        except ValueError:
            print("WARNING: The input must contain an integer {0-9} no other characters {a-z} {!@#$%^&*()}\n")
    else:
        lengthOfStrings = defaultLengthOfStrings
        break

while True:
    numberOfRandomStrings = input(f'Please enter the number for number of strings generated (default: {defaultNumberOfRandomStrings}): ')
    if numberOfRandomStrings:
        try:
            numberOfRandomStrings = int(numberOfRandomStrings)
            break
        except ValueError:
            print("WARNING: The input must contain an integer {0-9} no other characters {a-z} {!@#$%^&*()}\n")
    else:
        numberOfRandomStrings = defaultNumberOfRandomStrings
        break

print(
    '\nListed below are the randomized strings.\n' \
    'Change values inside the integer variables for length and number of strings.\n\n' \
    f'Length Of Each String: {lengthOfStrings}\n' \
    f'Number Of Strings Generated: {numberOfRandomStrings}\n'
)

for i in range(int(numberOfRandomStrings)):
    print(f'Random String #{i+1}: {generateRandomString(lengthOfStrings, True)}')
