from friendsbalt.acs import average_color as ac
from friendsbalt.acs.uf import WeightedQuickUnion

class ColorAveragedUF(WeightedQuickUnion):
    '''
    A class that represents a union-find data structure applied to an image
    that keeps track of the average color of each component as pixels are
    added to the component.
    '''
    def __init__(self, image):
        super().__init__(self, image.width * image.height)
        self.colors = [image.get_pixel(x, y) for x in range(image.width) for y in range(image.height)]
    
    def union(self, p, q):
        '''
        Union the components containing pixels p and q and
        update the color of the new component
        '''
        #TODO: Override the union method to (weighted) average the colors
        #  of the two components
        root_p = self.root(p)
        root_q = self.root(q)
        p_color = self.colors[p]
        q_color = self.colors[q]
        sz_p = self.size(root_p)
        sz_q = self.size(root_q)
        
        color_mix = ac.proportional_average_rgb(p_color, sz_p, q_color, sz_q)
        
        super().union(root_p, root_q)
        
        if sz_p < sz_q:
            self.colors[q] = color_mix
        else:
            self.colors[p] = color_mix
                       


    def get_average_color(self, p):
        '''
        Get the average color of the component containing pixel p
        '''
        #TODO: Implement this method
        pass
