from color_averaged_uf import ColorAveragedUF as UF
from PIL import Image
import numpy as np

def segment_image(image: Image, threshold = 100, min_size = 0):
    #TODO: Implement this method
    uf = UF(image)
    width = image.width
    height = image.height
    
    for y in range(height):
        for x in range(width):
            p = y * width + x
            if x < width - 1 and diff(image.getpixel((x,y)), image.getpixel((x + 1, y))) < threshold:
                uf.union(p, p + 1)
            if y < height - 1 and diff(image.getpixel((x,y)), image.getpixel((x, y+1))) < threshold:
                uf.union(p, p + width)
                
    segment_sizes = get_segment_sizes(uf)
    
    while has_small_segments(segment_sizes, min_size):
        merge_small_segments(uf, image, segment_sizes, min_size)
        segment_sizes = get_segment_sizes(uf)
        print("merging")
        
    return generate_new_image(height, width, uf)
        

def generate_new_image(height, width, uf):
    new_image = Image.new(mode="RGB", size=(width, height))
    pixels = new_image.load()
    for y in range(height):
        for x in range(width):
            pixels[x, y] = uf.get_average_color(y * width + x)
    
    return new_image
    
def get_segment_sizes(uf: UF):
    segment_sizes = {}
    for i in range(len(uf.id)):
        root = uf.root(i)
        segment_sizes[root] = segment_sizes.get(root, 0) + 1
    
    return segment_sizes

def has_small_segments(segment_sizes, min_size):
    for _, value in segment_sizes.items():
        if value < min_size: return True
    return False

def merge_small_segments(uf, image, segment_sizes, min_size):
    width = image.width
    height = image.height
    for y in range(height):
        for x in range(width):
            p = y * width + x
            if segment_sizes[uf.root(p)] < min_size:
                neighbors = get_neighbors(image, x, y)
                valid_neighbors = [n for n in neighbors if not uf.connected(n[1] * width + n[0], y * width + x)]
                
                if not valid_neighbors: continue
                
                most_similar = min(valid_neighbors, key = lambda n: diff(image.getpixel((x,y)), image.getpixel(n)))
                uf.union(y * width + x, most_similar[1] * width + most_similar[0])

def get_neighbors(image, x, y):
    neighbors = []
    
    if x > 0:
        neighbors.append((x - 1, y))
    if x < image.width - 1:
        neighbors.append((x + 1, y))
    if y > 0: 
        neighbors.append((x, y - 1))
    if y < image.height - 1:
        neighbors.append((x, y + 1))
    
    return neighbors
    
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
    image_name = "plants.jpg"
    image = Image.open("images/" + image_name)
    segmented_image = segment_image(image, threshold = 500, min_size = 400)
    segmented_image.save("output/" + image_name + "_segmented.jpg")

if __name__ == "__main__":
    main()