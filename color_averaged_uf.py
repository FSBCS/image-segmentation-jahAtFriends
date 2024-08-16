from friendsbalt.acs import average_color as ac
from friendsbalt.acs.uf import WeightedQuickUnion

class ColorAveragedUF(WeightedQuickUnion):
    '''
    A class that represents a union-find data structure applied to an image
    that keeps track of the average color of each component as pixels are
    added to the component.
    '''
    def __init__(self, image):
        super().__init__(image.width * image.height)
        self.colors = [image.getpixel((x, y)) for y in range(image.height) for x in range(image.width)]
    
    def union(self, p, q):
        '''
        Union the components containing pixels p and q and
        update the color of the new component
        '''
        #TODO: Override the union method to (weighted) average the colors
        #  of the two components
        pass

    def get_average_color(self, p):
        '''
        Get the average color of the component containing pixel p
        '''
        #TODO: Implement this method
        pass
