import textblob as tb

def contLoop():
    """checks if user wants to continue the program"""
    loop = True

    while loop == True:
        iterate = input("\nWould you like to run another analysis (yes/no)? ")
        iterate = tb.TextBlob(iterate).correct().lower()
        if iterate == "yes":
            movie = input("What movie would you like to analyze? ")
            analysis = input("What would you like to see (background/reception/poster/wordcloud/sentiment)? ")
            movie = tb.TextBlob(movie).correct().lower()
            analysis = tb.TextBlob(analysis).correct().lower()

            loop = False
            cont = True
            return (cont, movie, analysis)
        elif iterate == "no":
            loop = False
            cont = False
            movie = "placeholder"
            analysis = "placeholder"

            return (cont, movie, analysis)
        else:
            print("input not valid")
            loop = True
