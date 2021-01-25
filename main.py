#TODO: Create a letter using starting_letter.docx 
#for each name in invited_names.txt
PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt", "r") as names_file:
    names = names_file.readlines()
#Replace the [name] placeholder with the actual name.
with open("./Input/Letters/starting_letter.docx") as letter_file:
    letter = letter_file.read()

for name in names:
    name_without_line_break = name.strip()
    new_letter = letter.replace(PLACEHOLDER, name_without_line_break)
    with open(f"./Output/ReadyToSend/{name_without_line_break}.docx", "w") as output_letter:
        output_letter.write(new_letter)
#Save the letters in the folder "ReadyToSend".
