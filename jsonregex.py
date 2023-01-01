import re

# Open the input file for reading
with open('Untitled.json', 'r', encoding="utf-8") as infile:
    # Read the contents of the file into a string
    string = infile.read()

# Compile the regular expression
pattern = re.compile(
    r'"email"\s*:\s*"([^"]*)",\s*"passwordHash"\s*:\s*"([^"]*)"')


# Open the output file for writing
with open('output.txt', 'w+') as outfile:
    # Iterate over the matches in the string
    for match in pattern.finditer(string):
        # Extract the email and password hash from the match
        email = match.group(1)
        password_hash = match.group(2)

        # Write the email and password hash to the file
        # outfile.write(f'Email: {email}\n')
        # outfile.write(f'Password hash: {password_hash}\n')
        outfile.write(f'{email}:{password_hash}\n')
