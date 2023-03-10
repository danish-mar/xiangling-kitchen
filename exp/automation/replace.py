#importing bs4
import time
from bs4 import BeautifulSoup
#declaring variables
new_recipe_ingred = []
new_recipe_name = ''
new_recipe_file_name = input("New Recipe Name in small:")
new_recipe_name = new_recipe_file_name.capitalize()
print("Opening Template:")
with open('example.html','r') as template:
     old_html = template.read()
    
soup = BeautifulSoup(old_html, 'html.parser')
#Part to edit the main h1 tag

print(f"Adding {new_recipe_name} to {new_recipe_file_name}.html")
temp_heading = soup.find('h1',{'class': 'rec_name'})
temp_heading.string.replace_with(new_recipe_name)
print("done")

#workout to replace the rec_quote
new_recipe_quote = input("Please enter the quote:")
print(f"Adding New quote {new_recipe_quote} to {new_recipe_file_name}.html")
temp_quote = soup.find('h2',{'class':'rec_quote'})
temp_quote.string.replace_with(new_recipe_quote)
print("done with recipe quote")

#steps to replace the ingredients list with class rec_ingred
temp_ingred = soup.find('ul',{'class':'rec_ingred'})
new_recipe_ingred = []
new_recipe_ingred = input("Enter the new ingredients separated by commas: ")
print("Creating li element")
new_ingredients_list = []
new_ingredients_list = [f"<li>{ingredient.strip()}</li>" for ingredient in new_recipe_ingred.split(',')]
print("removing old ingred")
temp_ingred.clear()
print("Replacing elements")

for item in new_ingredients_list:
    new_ingredients_list.append(BeautifulSoup(item, 'html.parser'))
    print(f"Replacing {item}")


print("done With ingredients list")

#Steps to replace the steps with class letsmake
print("Replacing steps")
steps_blockquote = soup.find("div", class_="letsmake").blockquote

# Get the existing steps as a list of strings
existing_steps = [step.string for step in steps_blockquote.find_all("strong")]

# Prompt the user to enter the new steps, separated by newlines
new_steps_str = input("Enter the new steps, separated by ,:\n")
new_steps = new_steps_str.split(",")
print("Replacing...")
# Create a new <blockquote> tag containing the new steps
new_steps_blockquote = soup.new_tag("blockquote")
print("New blockquote created!")
for i, step in enumerate(new_steps):
    # Insert a <br> tag after each step except the last one
    if i < len(new_steps) - 1:
        new_steps_blockquote.append(step)
        new_steps_blockquote.append(soup.new_tag("br"))
    else:
        new_steps_blockquote.append(step)

# Replace the existing <blockquote> tag with the new one
steps_blockquote.replace_with(new_steps_blockquote)
print(f'done adding')
print(new_steps_blockquote)
# The endquote file
temp_end_quote = input("Please enter end_quote:")
temp_old_endquote = soup.find('h2',{'class': 'rec_ending'})
temp_old_endquote.string.replace_with(temp_end_quote)
print(f"done adding {temp_end_quote} to end")
time.sleep(1)
print(f"done making {new_recipe_file_name}.html")
print(f"Saving Changes and writing to {new_recipe_file_name}.html")

with open(f'{new_recipe_file_name}.html', 'w') as f:
    f.write(str(soup))

print("saved successfully.")


