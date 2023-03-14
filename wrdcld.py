import matplotlib.pyplot as plt
import wordcloud

def wc(data):
    """generates and show a wordcloud based on all the downloaded IMDb reviews"""
    reviews = []
    for review in data:
        reviews.append(review["Review text"])
    
    text = ' '.join(reviews)

    cloud = wordcloud.WordCloud()
    cloud.generate(text)

    plt.imshow(cloud, interpolation = "bilinear")
    plt.axis("off")
    plt.show()