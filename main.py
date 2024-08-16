from color_averaged_uf import ColorAveragedUF as UF
from PIL import Image

def segment_image(image, threshold = 100, min_size = 10):
    #TODO: Implement this method
    pass

def diff(color1, color2):
    """
    Calculate the Euclidean squared difference between two colors.
    Parameters:
    color1 (tuple): A tuple representing the RGB values of the first color.
    color2 (tuple): A tuple representing the RGB values of the second color.
    Returns:
    int: The squared difference between the two colors.
    """
    r1, g1, b1 = color1
    r2, g2, b2 = color2

    return (r1 - r2) ** 2 + (g1 - g2) ** 2 + (b1 - b2) ** 2

def main():
    image_name = "birdhouse.jpg"
    image = Image.open("images/" + image_name)
    segmented_image = segment_image(image)
    segmented_image.save("output/" + image_name + "_segmented.jpg")

if __name__ == "__main__":
    main()