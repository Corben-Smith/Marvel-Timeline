import requests
import hashlib
import time
from ConsoleEvents import main
import numpy as np
import matplotlib.pyplot as plt

public_key = "06dc54a132a88b05fa414093b740157e"
private_key = "c7db5d1723656554153ae4779bdc03fc62dcdaee"

print("Hai :3")

def format_character_counts(data):
    result = "Character Appearances\n" + "-" * 25
    for name, count in sorted(data.items(), key=lambda x: -x[1]):  # Sort by count descending
        result += f"\n{name}: {count}"
    return result


def format_marvel_character(data):
    # Extract basic details
    name = data.get("name", "Unknown")
    description = data.get("description", "No description available.")
    modified = data.get("modified", "Unknown date")
    thumbnail_url = f"{data['thumbnail']['path']}.{data['thumbnail']['extension']}" if "thumbnail" in data else "No thumbnail available."
    resource_uri = data.get("resourceURI", "No resource URI available.")
    
    # Extract comics details
    comics_available = data.get("comics", {}).get("available", 0)
    comics_list = data.get("comics", {}).get("items", [])

    # Extract events details
    events_available = data.get("events", {}).get("available", 0)
    events_list = data.get("events", {}).get("items", [])

    # Extract stories details
    stories_available = data.get("stories", {}).get("available", 0)
    stories_list = data.get("stories", {}).get("items", [])

    # Format lists
    def format_items(item_list):
        return "\n".join([f"  - {item.get('name', 'Unnamed')}" for item in item_list]) if item_list else "No items available."

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
{format_items(comics_list)}

Events ({events_available} available):
{format_items(events_list)}

Stories ({stories_available} available):
{format_items(stories_list)}
    """
    return result.strip()

#Track Character Apperances

def track_character_apperances():
    pass

#Map Relationships

def fetch_all_stories(character_id, private_key, public_key):
    ts = str(time.time())
    to_hash = ts + private_key + public_key
    hash = hashlib.md5(to_hash.encode()).hexdigest()

    base_url = "http://gateway.marvel.com/v1/public/stories"
    stories = []
    limit = 100
    offset = 0

    while offset < 50:
        print(".")
        url = f"{base_url}?apikey={public_key}&ts={ts}&hash={hash}&characters={character_id}&limit={limit}&offset={offset}"
        response = requests.get(url, verify=False)
        data = response.json()

        new_stories = data["data"]["results"]
        if not new_stories:
            break

        stories.extend(new_stories)
        offset += limit

    return stories

def track_character_relationships():
    print("What is the name of the character? (Be specific, friend)")
    name = input()
    ts = str(time.time())

    to_hash = ts + private_key + public_key
    hash = hashlib.md5(to_hash.encode()).hexdigest()
    url = f"http://gateway.marvel.com/v1/public/characters?apikey={public_key}&ts={ts}&hash={hash}&nameStartsWith={name}"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload, verify=False)


    character = None
    if response.status_code == 200:
        data = response.json()
        if "data" in data and "results" in data["data"] and len(data["data"]["results"]) > 0:

            character = data["data"]["results"][0]
            id = character["id"]

            stories = fetch_all_stories(id, private_key, public_key)

            counts = {}
            for story in stories:
                for character in story["characters"]["items"]:
                    if character["name"] in counts:
                        counts[character["name"]] = counts[character["name"]] + 1
                    else:
                        counts[character["name"]] = 1

            print(format_character_counts(counts))
                    
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
    main()

def dodge_points(points, offset=0.3):
    """
    Adjusts y-values to prevent overlap.
    """
    year_counts = {}
    for i, (x, y, title) in enumerate(points):
        if x not in year_counts:
            year_counts[x] = 0
        else:
            year_counts[x] += 1
        points[i][1] = year_counts[x] * offset
    return points

def create_timeline():
    ts = str(time.time())
    to_hash = ts + private_key + public_key
    hash = hashlib.md5(to_hash.encode()).hexdigest()
    url = "http://gateway.marvel.com/v1/public/series"

    params = {
        "apikey": public_key,
        "ts": ts,
        "hash": hash,
        "orderBy": "startYear",
        "limit": 100
    }

    response = requests.get(url, params=params)
    if response.status_code != 200:
        print(f"Error: {response.status_code} - {response.text}")
        return

    data = response.json()
    results = data.get("data", {}).get("results", [])

    series = []
    for serie in results:
        title = serie.get("title", "Unknown Title")
        start_year = serie.get("startYear", None)
        if start_year and 1938 <= start_year <= 1950:
            series.append([start_year, 0, title])  # (year, y-position, title)

    if not series:
        print("No series found for the specified date range.")
        return

    series_array = np.array(series, dtype=object)

    # Apply dodge points to shift y-positions
    dodged_points = dodge_points(series_array.tolist())

    plt.figure(figsize=(12, 6))

    # Plot series with dodged y-positions
    for (x, y, title) in dodged_points:
        plt.scatter(x, y, color='red', marker='o', s=50)  # Markers for visibility
        plt.text(x, y + 0.1, title, ha="center", fontsize=8, rotation=45)

    plt.title("Marvel Series Timeline (1938-1968)", fontsize=14)
    plt.xlabel("Year", fontsize=12)
    plt.yticks([])  
    plt.grid(False)

    plt.xticks(range(1938, 1950, 2))

    plt.tight_layout()
    plt.show()

# Run the function

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
