
with open("Input/Letters/starting_letter.txt", 'r') as file:
    contents = file.read()

with open("Input/Names/invited_names.txt", 'r') as names:
    name = names.readlines()
    for i in name:
        if "[name]" in contents:
            nm = i.strip()
            con = contents.replace("[name]", nm)
            letter = open(f"Output/ReadyToSend/{nm}.txt", "w")
            letter.write(con)
