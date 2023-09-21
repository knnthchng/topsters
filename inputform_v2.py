# Topsters CSV Input Form Program

import csv

# Initial variable for "input session"
active = 'y'

# Create function for appending new data to pre-existing CSV file
# def append_to_csv(file, row):

# Create function for getting inputs
def db_input():
    new_entry = []
    # Ask for title and append to db_input
    title = input("What's the title of the album? ")
    new_entry.append(title)

    print("-------------------------------------------------")

    artist = input("Who or what is the artist that recorded this album? ")
    new_entry.append(artist)

    print("-------------------------------------------------")

    year = input("What year was the album released? ")
    new_entry.append(year)

    print("-------------------------------------------------")

    genre = input("What genre does the album fall under? ")
    new_entry.append(genre)

    print("-------------------------------------------------")
    
    subgenre = input("What other genres or subgenres does the album fall under? (Refer to the album's RateYourMusic page and list with commas without spaces after) ")
    new_entry.append(subgenre)

    print("-------------------------------------------------")

    descriptors = input("List the album's descriptors by referring to the album on RateYourMusic or AllMusic (List with commas, without spaces after) ")
    new_entry.append(descriptors)

    print("-------------------------------------------------")

    length = input("How long is the album? (In number of minutes, to two decimal places.) ")
    new_entry.append(length)

    print("-------------------------------------------------")

    label = input("What record label released this album? ")
    new_entry.append(label)

    print("-------------------------------------------------")

    country = input("What country is the artist from? (Use ISO 3166-1 alpha-3) ")
    new_entry.append(country)

    print("-------------------------------------------------")

    compilation = input("Is the album a compilation record (e.g., greatest hits, different artists, etc.)? Y/N ")
    new_entry.append(compilation)

    print("-------------------------------------------------")

    print(new_entry)
    
    correct = input("Is the desired input correct? Y/N ")

    if correct.lower() == 'y':
        with open('Data/topsters_v2.csv', 'a', newline='') as topsters_db:
            writer_object = csv.writer(topsters_db, delimiter=',')
            writer_object.writerow(new_entry)
            topsters_db.close
        print("-------------------------------------------------`")
        repeat = input("Do you wish to enter another album into the database? Y/N ")
        
        if repeat.lower() == 'y':
            print("""-------------------------------------------------
Here we go again!
-------------------------------------------------""")
            new_entry = []
            db_input()
        elif repeat.lower() == 'n':
            print("-------------------------------------------------")
            print("Thank you for using the app!")
            active = 'n'
            raise SystemExit

    elif correct.lower() == 'n':
        print("""-------------------------------------------------
Back from the top. Please double-check your inputs before hitting ENTER.
-------------------------------------------------""")  
        new_entry.clear()
        db_input()

# Display welcome message and instructions
print("""-------------------------------------------------
Topsters Input Form
-------------------------------------------------
Make sure to double-check Wikipedia, Discogs, RateYourMusic, among other sources to authenticate your inputs.
-------------------------------------------------""")
# During the session
while active == 'y':
    db_input()
