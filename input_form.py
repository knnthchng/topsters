# Topsters CSV Input

from csv import writer

# Initial variable for "input session"
active = 'y'

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

    length = input("How long is the album (in minutes)? ")
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
        with open('Data/topsters.csv', 'a') as topsters_db:

            writer_object = writer(topsters_db, delimiter=',')

            writer_object.writerow(new_entry)

            topsters_db.close
        print("-------------------------------------------------")

        repeat = input("Do you wish to enter another album into the database? Y/N ")
        
        if repeat.lower() == 'y':
            print("-----------------Here we go again----------------")
            new_entry = []
            db_input()
        elif repeat.lower() == 'n':
            print("-------------------------------------------------")
            print("Thank you for using the app!")
            active = 'n'

    elif correct.lower() == 'n':
        print("---------------Back from the top...-----------------")  
        new_entry = []
        db_input()

# Display welcome message and instructions
print("""-------------------------------------------------
Topsters Input Form
Make sure to double-check Wikipedia, Discogs, RateYourMusic, among other sources to authenticate your inputs.
-------------------------------------------------""")
# During the session
while active == 'y':
    db_input()
