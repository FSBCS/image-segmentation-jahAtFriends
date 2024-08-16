from . import color_averaged_uf as uf
from PIL import Image

def segment_image(image, threshold = 100, min_size = 10):
    #TODO: Implement this method
    pass

def main():
    image_name = "birdhouse.jpg"
    image = Image.open("images/" + image_name)
    segmented_image = uf.segment_image(image)
    segmented_image.save("output/" + image_name + "_segmented.jpg")

if __name__ == "__main__":
    main()