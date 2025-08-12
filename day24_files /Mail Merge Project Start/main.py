
"""
#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


"""





# import os

# # Paths
# input_folder = "input"
# output_folder = "output"
# names_file = os.path.join(input_folder, "/Users/kgreen/PycharmProjects/PYLEARNING/day24_files /Mail Merge Project Start/Input/Names/invited_names.txt")
# template_file = os.path.join(input_folder, "/Users/kgreen/PycharmProjects/PYLEARNING/day24_files /Mail Merge Project Start/Input/Letters", "/Users/kgreen/PycharmProjects/PYLEARNING/day24_files /Mail Merge Project Start/Input/Letters/starting_letter.txt")
# output_file = os.path.join(output_folder, "/Users/kgreen/PycharmProjects/PYLEARNING/day24_files /Mail Merge Project Start/Output/ReadyToSend/example.txt")

# # Step 1: Read names from "invited_names.txt"
# with open(names_file, "r") as file:
#     names = [line.strip() for line in file.readlines()]  # Strip whitespace/newlines

# # Step 2: Read the template letter from "starting_letter.txt"
# with open(template_file, "r") as file:
#     template = file.read()

# # Step 3: Generate personalized letters
# personalized_letters = []
# for name in names:
#     personalized_letter = template.replace("[name]", name)  # Replace placeholder
#     personalized_letters.append(personalized_letter)

# # Step 4: Write personalized letters to a single file ("example.txt")
# with open(output_file, "w") as file:
#     for letter in personalized_letters:
#         file.write(letter + "\n\n")  # Separate letters with blank lines

# print(f"Mail merge completed! Letters saved to {output_file}")


import os

# Paths
input_folder = "input"
output_folder = "/Users/kgreen/PycharmProjects/PYLEARNING/day24_files /Mail Merge Project Start/Output/ReadyToSend"
names_file = "/Users/kgreen/PycharmProjects/PYLEARNING/day24_files /Mail Merge Project Start/Input/Names/invited_names.txt"
template_file = "/Users/kgreen/PycharmProjects/PYLEARNING/day24_files /Mail Merge Project Start/Input/Letters/starting_letter.txt"

# Ensure the output folder exists
os.makedirs(output_folder, exist_ok=True)

# Step 1: Read names from "invited_names.txt"
with open(names_file, "r") as file:
    names = [line.strip() for line in file.readlines()]  # Strip whitespace/newlines

# Step 2: Read the template letter from "starting_letter.txt"
with open(template_file, "r") as file:
    template = file.read()

# Step 3: Generate and save individual letters for each invitee
for name in names:
    # Replace the placeholder with the actual name
    personalized_letter = template.replace("[name]", name)
    
    # Define the output file path for each letter
    output_path = os.path.join(output_folder, f"letter_for_{name}.docx")
    
    # Write the personalized letter to the file
    with open(output_path, "w") as output_file:
        output_file.write(personalized_letter)

print(f"Mail merge completed! Individual letters saved to {output_folder}")
