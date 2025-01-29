import pandas as pd
import matplotlib.pyplot as plt

# Setting up the data frame
df = pd.read_csv('./MarvelEvents_Clean.csv')
filtered_df = df[['Event','Date','Developments','Startyear']]


# Search event by name
# Parameters:
# name (str): The name of the event to search for.
# Returns:
# none
def Get_Event(name):
    event = filtered_df[filtered_df['Event'].str.contains(name, case=False)]
    
    if not event.empty:
        print(f"\nName: {event['Event'].values[0]}")
        print(f"Period: {event['Date'].values[0]}")
        print(f"Description: {event['Developments'].values[0]}")
        print(f"First Appearance: {int(event['Startyear'].values[0])}\n")
    else:
        print("\nEvent not found.\n")

# Order the events by start year in desc order
orderedEvents = filtered_df.sort_values(by='Startyear', ascending=True)

# Display the events on the console log
# Parameters:
# none
# Returns:
# none
def Display_Events():
    for _, event in orderedEvents.iterrows():
        startyear = event['Startyear']
        if pd.isna(startyear):
            print(f"------------ Unknown Year ------------")
        else:
            print(f"------------ {int(startyear)} ------------")
        print(f"Event: {event['Event']}")
        print(f"Period: {event['Date']}\n")

# Display the timeline graph using matplotlib
# Parameters:
# none
# Returns:
# none
def Display_Timeline():
    event_names = orderedEvents['Event']
    start_years = orderedEvents['Startyear']
    start_years = start_years.astype(int)

    plt.figure(figsize=(12, 6))
    plt.scatter(start_years, [1] * len(start_years), color='blue', marker='o', s=100)

    for i, event in orderedEvents.iterrows():
        year = event['Startyear']
        name = event['Event']
        plt.text(year, 1.02, name, ha='center', va='bottom', fontsize=9, rotation=90)

    plt.title('Marvel Major Event Timeline', fontsize=14)
    plt.xlabel('Year', fontsize=12)
    plt.yticks([])
    plt.grid(False)

    plt.xticks(range(int(start_years.min()), int(start_years.max()) + 1, 2))

    plt.tight_layout()  
    plt.show()

# This is just for testing
if __name__ == "__main__":
    print("-----------------------------------------------------------")
    print(filtered_df.head())
    Display_Timeline()