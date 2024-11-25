import os
import json
from PIL import Image 


def process_image(filename, currentDirectory, principalDirectory):
   
    try:
        # Construct full path for the image
        image_path = os.path.join(currentDirectory, filename)
        
        # Check if the file exists
        if not os.path.isfile(image_path):
            raise FileNotFoundError(f"File '{filename}' not found in '{currentDirectory}'")

        # Open the image
        with Image.open(image_path) as img:
            # Extract metadata
            image_data = {
                "filename": filename,
                "format": img.format,
                "size": img.size,  # (width, height)
                "mode": img.mode   # e.g., RGB, CMYK
            }

        # Ensure the principal directory exists
        os.makedirs(principalDirectory, exist_ok=True)

        # Define the JSON file path
        json_file_path = os.path.join(principalDirectory, "image_metadata.json")

        # Save metadata to JSON
        with open(json_file_path, "w") as json_file:
            json.dump(image_data, json_file, indent=4)
        
        print(f"Metadata for '{filename}' saved to '{json_file_path}'")
    
    except Exception as e:
        print(f"An error occurred: {e}")


#current_dir = os.getcwd()
#print(f"Current Directory: {current_dir}")


os.chdir("/home/xraval/dico")
current_dir = os.getcwd()
print(f"Current Directory: {current_dir}")

# List all items in the current directory
all_items = os.listdir(current_dir)


# Filter to include only directories
directories = [item for item in all_items if os.path.isdir(os.path.join(current_dir, item))]

# Print the directories
print("Directories inside the current directory:")


for directory in directories:
    print(directory)

user_input = input("Enter Directory you want to work on")


os.chdir("/home/xraval/dico/"+user_input)
sub_dir = os.getcwd()
all_items_on_sb_dir = os.listdir(sub_dir)

my_list = []

for directory in all_items_on_sb_dir:
    #print(directory)
    my_list.append(directory)

    process_image(
    filename=directory,
    currentDirectory=sub_dir,
    principalDirectory=current_dir
)
data = {
     'DIRECTORY': user_input,
     "file" : my_list
}


json_file_path = os.path.join(current_dir, "image_metadata.json")
with open(json_file_path, "r") as json_file:
    dataLoaded = json.load(json_file)
    dataLoaded.update(data)

with open(json_file_path, "w") as json_file:
    json.dump(dataLoaded, json_file, indent=4)


with open("/home/xraval/dico/dico-data.json", "r") as file:
    data = json.load(file)


#print(data["name"])  # Output: Raval