import time
from bs4 import BeautifulSoup

# Get the name of the new recipe
new_recipe_file_name = input("New Recipe Name in small: ")
new_recipe_name = new_recipe_file_name.capitalize()

# Read the HTML template
print("Opening Template:")
with open('example.html', 'r') as template:
    old_html = template.read()

# Parse the HTML with BeautifulSoup
soup = BeautifulSoup(old_html, 'html.parser')

# Replace the title of the webpage
print(f"Replacing webpage title with {new_recipe_name}")
soup.title.string.replace_with(f"Xian's {new_recipe_name}")
print("Done")

# Replace the recipe name
print(f"Adding {new_recipe_name} to {new_recipe_file_name}.html")
recipe_name_element = soup.find('h1', {'class': 'rec_name'})
recipe_name_element.string.replace_with(new_recipe_name)
print("Done")

# Replace the recipe quote
new_recipe_quote = input("Please enter the quote: ")
print(f"Adding new quote '{new_recipe_quote}' to {new_recipe_file_name}.html")
recipe_quote_element = soup.find('h2', {'class': 'rec_quote'})
recipe_quote_element.string.replace_with(new_recipe_quote)
print("Done")

# Replace the ingredients list
new_recipe_ingredients_str = input("Enter the new ingredients separated by commas: ")
new_recipe_ingredients = [ingredient.strip() for ingredient in new_recipe_ingredients_str.split(',')]
print("Creating li elements")
new_ingredients_list = []
for ingredient in new_recipe_ingredients:
    # Create a new <li> tag for each ingredient
    li_tag = soup.new_tag("li")
    li_tag.string = ingredient
    new_ingredients_list.append(li_tag)
    print(f"Adding {ingredient} to ingredients list")

# Replace the old ingredients list with the new one
ingredients_list_element = soup.find('ul', {'class': 'rec_ingred'})
ingredients_list_element.clear()
ingredients_list_element.extend(new_ingredients_list)
print("Done with ingredients list")

# Replace the recipe steps
new_recipe_steps_str = input("Enter the new steps separated by commas: ")
new_recipe_steps = [step.strip() for step in new_recipe_steps_str.split(',')]
print("Replacing steps")
steps_blockquote = soup.find('div', {'class': 'letsmake'}).blockquote
steps_blockquote.clear()
for i, step in enumerate(new_recipe_steps):
    # Create a new <strong> tag for each step
    strong_tag = soup.new_tag('strong')
    strong_tag.string = f"Step {i+1}: "
    steps_blockquote.append(strong_tag)
    steps_blockquote.append(step)
    # Add a <br> tag after each step except the last one
    if i < len(new_recipe_steps) - 1:
        steps_blockquote.append(soup.new_tag('br'))
    print(f"Adding step {i+1}: {step}")
print("Done with steps")

# Replace the end quote
new_recipe_end_quote = input("Please enter end quote: ")
print(f"Adding end quote '{new_recipe_end_quote}' to {new_recipe_file_name}.html")
end_quote_element = soup.find('h2', {'class': 'rec_ending'})
end_quote_element.string.replace_with(new_recipe_end_quote)
print("Done with end quote")

# Write the new HTML to a file
print(f"Saving changes and writing to {new_recipe_file_name}.html")
with open(f"{new_recipe_file_name}.html", "w") as f:
    f.write(str(soup))
print("Saved successfully.")
