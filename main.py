# TODO: Create a letter using starting_letter.txt
PLACEHOLDER = "[name]"
with open("./Input/Names/invited_names.txt") as data:
    invitees = data.readlines()

# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".
# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

for each_name in invitees:
    with open("./Input/Letters/starting_letter.txt") as data:
        letter = data.read()
    stripped_name = each_name.strip()
    letter = letter.replace(PLACEHOLDER, stripped_name)
    with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as data:
        data.write(letter)
