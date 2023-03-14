
def rec(data):
    """prints out the movie’s awards, metascore, and IMDb rating"""
    awards = data["root"]["movie"]["@awards"]
    metascore = data["root"]["movie"]["@metascore"]
    rating = data["root"]["movie"]["@imdbRating"]

    print("\nAwards: " + awards)
    print("Metascore: " + metascore)
    print("IMDb rating: " + rating)