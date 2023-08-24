# Topsters CSV Input

from csv import writer

# Initial variable for "input session"
active = 'y'

# Create the array for inputs
db_input = []

# Define our query for asking and appending input:
"""
def db_append():

    # Ask for title and append to db_input
    title = input("What's the title of the album? ")
    db_input.append(title)

    print("-------------------------------------------------")

    artist = input("Who or what is the artist that recorded this album? ")
    db_input.append(artist)

    print("-------------------------------------------------")

    year = input("What year was the album released? ")
    db_input.append(year)

    print("-------------------------------------------------")

    genre = input("What genre does the album fall under? ")
    db_input.append(genre)

    print("-------------------------------------------------")


    length = input("How long is the album (in minutes)? ")
    db_input.append(length)

    print("-------------------------------------------------")

    label = input("What record label released this album? ")
    db_input.append(label)

    print("-------------------------------------------------")

    country = input("What country is the artist from? (Use ISO 3166-1 alpha-3) ")
    db_input.append(country)

    print("-------------------------------------------------")

    compilation = input("Is the album a compilation record (e.g., greatest hits, different artists, etc.)? Y/N ")
    db_input.append(compilation)

    print("-------------------------------------------------")

    print(db_input)
    
    correct = input("Is the desired input correct? Y/N ")
"""

# Display welcome message and instructions
print("Make sure to double-check Wikipedia, Discogs, RateYourMusic, among other sources to authenticate your inputs.")
print("-------------------------------------------------")
# During the session
while active == 'y':
    # Ask for title and append to db_input
    title = input("What's the title of the album? ")
    db_input.append(title)

    print("-------------------------------------------------")

    artist = input("Who or what is the artist that recorded this album? ")
    db_input.append(artist)

    print("-------------------------------------------------")

    year = input("What year was the album released? ")
    db_input.append(year)

    print("-------------------------------------------------")

    genre = input("What genre does the album fall under? ")
    db_input.append(genre)

    print("-------------------------------------------------")


    length = input("How long is the album (in minutes)? ")
    db_input.append(length)

    print("-------------------------------------------------")

    label = input("What record label released this album? ")
    db_input.append(label)

    print("-------------------------------------------------")

    country = input("What country is the artist from? (Use ISO 3166-1 alpha-3) ")
    db_input.append(country)

    print("-------------------------------------------------")

    compilation = input("Is the album a compilation record (e.g., greatest hits, different artists, etc.)? Y/N ")
    db_input.append(compilation)

    print("-------------------------------------------------")

    print(db_input)
    
    correct = input("Is the desired input correct? Y/N ")

    if correct == 'Y':
        with open('Data/topsters.csv', 'a') as topsters_db:

            writer_object = writer(topsters_db, delimiter=',')

            writer_object.writerow(db_input)

            topsters_db.close

        print("Thank you for using the service.")
        active = 'n'

    elif correct == 'N':
        db_input = []