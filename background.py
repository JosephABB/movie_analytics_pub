import json, csv, xmltodict

def bg(data):
    """prints out the movie’s year of release, rating, runtime, genre, actors, and plot summary"""
    year = data["root"]["movie"]["@year"]
    rating = data["root"]["movie"]["@rated"]
    runtime = data["root"]["movie"]["@runtime"]
    genre = data["root"]["movie"]["@genre"]
    actors = data["root"]["movie"]["@actors"]
    plot = data["root"]["movie"]["@plot"]

    print("\nYear: " + year)
    print("Rating: " + rating)
    print("Runtime: " + runtime)
    print("Genre: " + genre)
    print("Actors: " + actors)
    print("Plot: " + plot)