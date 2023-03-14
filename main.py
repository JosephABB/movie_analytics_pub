'''A movie analytics tool that allows the user to search for a movie of
their choosing and obtain further information about it using online data and text analytics'''

import requests, textblob as tb, nltk, xmltodict, json
import background, reception, poster, wrdcld, sentiment, contloop, creds

print("Welcome to the movie analytics tool!")
movie = input("\nWhat movie would you like to analyze? ")
analysis = input("What would you like to see (background/reception/poster/wordcloud/sentiment)? ")

# corrects and converts movie and analysis inputs to lowercase
analysis = tb.TextBlob(analysis).correct().lower()
movie = tb.TextBlob(movie).correct().lower()

#check if user want to continue
cont = True

while cont:

    # completes urls for APIs
    omdb_url = "https://www.omdbapi.com/?r=xml&apikey=" + creds.api_key +"&t=" + str(movie)
    imdb_url = "https://dgoldberg.sdsu.edu/515/imdb/" + str(movie) + ".json"

    # connects to APIs
    response_omdb = requests.get(omdb_url)
    response_imdb = requests.get(imdb_url)

    #checks if connected to APIs
    if response_omdb:
        omdb_data = xmltodict.parse(response_omdb.text)

        if analysis == "background":
            background.bg(omdb_data)
            cont, movie, analysis = contloop.contLoop()

        elif analysis == "reception":
            reception.rec(omdb_data)
            cont, movie, analysis = contloop.contLoop()

        elif analysis == "poster":
            poster.pos(omdb_data)
            cont, movie, analysis = contloop.contLoop()

        elif analysis == "wordcloud":
            if response_imdb:
                imdb_data = json.loads(response_imdb.text)
                wrdcld.wc(imdb_data)
                cont, movie, analysis = contloop.contLoop()
            else:
                print("\nSorry, the tool could not successfully load any IMDb reviews for this movie. Please try another analysis or movie.")
                cont, movie, analysis = contloop.contLoop()

        elif analysis == "sentiment":
            if response_imdb:
                imdb_data = json.loads(response_imdb.text)
                sentiment.sent(imdb_data)
                cont, movie, analysis = contloop.contLoop()
            else:
                print("\nSorry, the tool could not successfully load any IMDb reviews for this movie. Please try another analysis or movie.")
                cont, movie, analysis = contloop.contLoop()
        else:
            print("\nSorry, that analysis is not supported. Please try again.")
            cont, movie, analysis = contloop.contLoop()

    else:
        print("could not connect to omdb")

print("Session terminated")
