import matplotlib.pyplot as plt, skimage.io

def pos(data):
    """shows an image of the movie’s poster"""
    image = data["root"]["movie"]["@poster"]
    image = skimage.io.imread(image)
    plt.imshow(image, interpolation = "bilinear")
    plt.axis("off")
    plt.show()