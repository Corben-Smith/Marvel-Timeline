## OKCOMPUTER TEAM
---


### MARVEL Timeline
#### Requirements
- Track character appearances
- Map relationships between characters
- Identify major event intersections
- Generate visual timelines

#### Brainstorming
- Python Console Application
- Determined the use of API
- Develop a program that meets requirements

#### Notes: 
- Track Character Apperances: 
  - Use the stories attricute in API
- Map Relationships:
  - Using the stories/events to find characters that they have shared with someone 
  - collect the 10 most commonly appeared with 
- Identify Major Event Intersection:
  - Use the event attribute 
-Generate Visual Timeline:
  - Real-world timeline 
  - Release of comic data timeline
  - use some graphing module to create a timeline
  - use the comic/series date from API

#### API Information
- API is located at https://developer.marvel.com/docs 
- Query Params (some of the basics)
  - name: Returns only characters matching the specific value
  - comics: Return only characters which appear in the specified comics
  - series: Return only characters which appear in the specified series
  - events: Returns only characters which appear in the specified series 
  - stories: Returns only characters which appear in specified series

#### Problem Solving
###### This section explains how we went about understanding each aspect of the requirements. 
  - Track character appearances
    - We debated on if this meant appearances within each comic or just which comic
    - We decided on which comics a character appears 
  - Map relationships between characters
    - We pretty much assumed this meant how characters interact with one abother (ex. who is in what comic together)
  - Identify major event intersections
    - We pretty much assumed this meant to determine which events had crossovers between comics or characters
  - Generate visual timelines
    - We debated on if this should be a list type visual or a traditional timeline
    - We debated on if it should be in real world time by release date or in the timeline of the comics themselves 

#### Challenges & Issues
- Events functionality
  - having issues with SSL certification
  - Not being able to request anything to the API endpoint due to the SSL error.
  - Creating a clean csv file about major Marvel events.

