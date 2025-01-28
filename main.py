import requests
import hashlib
import time
import certifi


public_key = "06dc54a132a88b05fa414093b740157e"
private_key = "c7db5d1723656554153ae4779bdc03fc62dcdaee"

print("Hai :3")

#Track Character Apperances

def track_character_apperances():
    pass

#Map Relationships

def track_character_relationships():
    ts = str(time.time())

    to_hash = ts + private_key + public_key
    hash = hashlib.md5(to_hash.encode()).hexdigest()
    url = f"http://gateway.marvel.com/v1/public/characters?apikey={public_key}&ts={ts}&hash={hash}&nameStartsWith=S"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload, verify=False)

    print(response.text)

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
