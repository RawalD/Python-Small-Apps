PLACEHOLDER = "[name]"

with open("./input/names/names.txt") as names_file:
    names = names_file.readlines()
    # print(names)

with open("./input/letters/starting_letter.docx") as letter_file:
    letter = letter_file.read()

    for name in names:
        stripped_name = name.strip()
        new_letter = letter.replace(PLACEHOLDER, stripped_name)
        # print(new_letter)

        with open(f"./output/readytosend/letter_for_{stripped_name}.docx", mode="w+") as completed:
            completed.write(new_letter)
