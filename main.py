import requests
import hashlib
import time
import certifi


public_key = "06dc54a132a88b05fa414093b740157e"
private_key = "c7db5d1723656554153ae4779bdc03fc62dcdaee"

print("Hai :3")

def format_marvel_character(data):
    # Extract basic details
    name = data.get("name", "Unknown")
    description = data.get("description", "No description available.")
    modified = data.get("modified", "Unknown date")
    thumbnail_url = f"{data['thumbnail']['path']}.{data['thumbnail']['extension']}" if "thumbnail" in data else "No thumbnail available."
    resource_uri = data.get("resourceURI", "No resource URI available.")
    
    # Extract comics details
    comics_available = data["comics"].get("available", 0) if "comics" in data else 0
    comics_list = data["comics"].get("items", []) if "comics" in data else []
    
    # Format comics list
    comics_str = ""
    if comics_list:
        comics_str = "\n".join([f"  - {comic.get('name', 'Unnamed Comic')}" for comic in comics_list])
    else:
        comics_str = "No comics available."
    
    # Create the formatted string
    result = f"""
Marvel Character Details
-------------------------
Name: {name}
Description: {description}
Last Modified: {modified}
Thumbnail: {thumbnail_url}
Resource URI: {resource_uri}

Comics ({comics_available} available):
{comics_str}
    """
    return result.strip()


#Track Character Apperances

def track_character_apperances():
    pass

#Map Relationships

def track_character_relationships():
    print("What is the name of the character? (Be specific friend)")
    name = input()
    ts = str(time.time())

    to_hash = ts + private_key + public_key
    hash = hashlib.md5(to_hash.encode()).hexdigest()
    url = f"http://gateway.marvel.com/v1/public/characters?apikey={public_key}&ts={ts}&hash={hash}&nameStartsWith={name}"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload, verify=False)


    character = None
        # Check for valid response
    if response.status_code == 200:
        data = response.json()
        if "data" in data and "results" in data["data"] and len(data["data"]["results"]) > 0:
            # Access the first character result
            character = data["data"]["results"][0]
            print(format_marvel_character(character))
        else:
            print("No characters found.")
            return
    else:
        print(f"Error: {response.status_code} - {response.reason}")
        return

    if character == None:
        print("Some error idc")
        return
    




#Identify Major Event Intersections


def track_major_events():
    pass

#Create Timeline

def create_timeline():
    pass

#Main


print("Choose which operation you want to do?")
print("")
print("1) Track Character Apperances")
print("")
print("2) Track Character Relationships")
print("")
print("3) Track Major Events")
print("")
print("4) Track Comic Release Timeline")

ans = input()

if ans == "1":
    track_character_apperances()

elif ans == "2":
    track_character_relationships()

elif ans == "3":
    track_major_events()

elif ans == "4":
    create_timeline()

else:
    print("Invalid Input. Try again loser")

print("Bai :333")
