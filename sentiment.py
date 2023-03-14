import textblob

def sent(data):
    """prints out the average review polarity and subjectivity scores"""
    reviews = []
    for review in data:
        reviews.append(review["Review text"])
    
    text = ' '.join(reviews)

    results = textblob.TextBlob(text).sentiment
    print(results)