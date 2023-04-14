from .area import Surroundings


class Circle:
    # https://stackoverflow.com/questions/70722545/draw-circle-in-console-using-python

    def __init__(self, diameter, draw_symbol, blank_symbol):
        self.diameter = diameter
        self.draw_symbol = draw_symbol
        self.blank_symbol = blank_symbol
        self._radius = None
        self._area = None
        self._edge = None

    @property
    def radius(self):
        # You must account for the loops being zero-based, but the quotient of the diameter / 2 being
        # one-based. If you use the exact radius, you will be short one column and one row.
        if not self._radius:
            self._radius = (self.diameter / 2) - .5
        return self._radius

    @property
    def area(self):
        if not self._area:
            self._area = (self.radius + .5) ** 2 + 1
        return self._area

    @property
    def edge(self):
        if not self._edge:
            self._edge = self.area - self.diameter
        return self._edge

    def full(self):
        figure = ''
        for i in range(self.diameter):
            x = (i - self.radius) ** 2
            for j in range(self.diameter):
                y = (j - self.radius) ** 2
                if self.area >= x + y:
                    figure += self.draw_symbol
                else:
                    figure += self.blank_symbol
            figure += '\n'
        return figure

    def hollow(self):
        figure = ''
        for i in range(self.diameter):
            x = (i - self.radius) ** 2
            for j in range(self.diameter):
                y = (j - self.radius) ** 2
                if self.area >= x + y >= self.edge:
                    figure += self.draw_symbol
                else:
                    figure += self.blank_symbol
            figure += '\n'
        return figure

    def thick(self):
        figure = []
        for i in range(self.diameter):
            x = (i - self.radius) ** 2
            for j in range(self.diameter):
                y = (j - self.radius) ** 2
                if self.area >= x + y >= self.edge:
                    figure.append(self.draw_symbol)
                else:
                    figure.append(self.blank_symbol)
            figure.append('\n')

        for idx in range(len(figure)):
            neighbours = Surroundings(idx, figure, self.diameter + 1)
            neighbours.fill(self.draw_symbol, self.blank_symbol)

        return ''.join(figure)

    def thin(self):
        figure = []
        for i in range(self.diameter):
            x = (i - self.radius) ** 2
            for j in range(self.diameter):
                y = (j - self.radius) ** 2
                if self.area >= x + y >= self.edge:
                    figure.append(self.draw_symbol)
                else:
                    figure.append(self.blank_symbol)
            figure.append('\n')

        for idx in range(len(figure)):
            neighbours = Surroundings(idx, figure, self.diameter + 1)
            neighbours.unfill(self.draw_symbol, self.blank_symbol)

        return ''.join(figure)


__all__ = ('Circle',)
