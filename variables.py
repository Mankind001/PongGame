

class Variables:
    def __init__(self):

        #change the screen setup here
        self.current_width = int(800)
        self.current_height = int(600)


        self.e = self.current_width / 2
        self.f = self.current_height / 2
        self.a = (self.e - ((6.25 * self.e) / 100))
        self.b = self.f - ((6.67 * self.f) / 100)
        self.c = (self.e - (11.25 * self.e) / 100)
        self.d = (self.e - ((15 * self.e) / 100))
        self.g = self.f-((20*self.f)/100)
        self.h= self.e-((57.5 * self.e) / 100)
        self.i=self.f-((33.33*self.f)/100)