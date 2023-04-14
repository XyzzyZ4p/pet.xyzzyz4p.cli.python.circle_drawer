from .utils import check_pairs


class Surroundings:
    def __init__(self, position, area, width):
        self.position = position
        self.area = area
        self.width = width
        self.field = [{'position': None, 'symbol': None} for x in range(9)]
        self.add(0, self.position - self.width - 1)
        self.add(1, self.position - self.width)
        self.add(2, self.position - self.width + 1)
        self.add(3, self.position - 1)
        self.add(4, self.position)
        self.add(5, self.position + 1)
        self.add(6, self.position + self.width - 1)
        self.add(7, self.position + self.width)
        self.add(8, self.position + self.width + 1)

    def fill(self, fill_symbol, blank_symbol):
        center = self.field[4]
        left = self.field[3]
        right = self.field[5]
        upper = self.field[1]
        upper_left = self.field[0]
        upper_right = self.field[2]
        bottom = self.field[7]
        bottom_left = self.field[6]
        bottom_right = self.field[8]

        if center['symbol'] == fill_symbol:
            if center['position'] <= len(self.area) // 2:
                # Check right
                if check_pairs(
                        (right['symbol'], blank_symbol),
                        (upper['symbol'], blank_symbol),
                        (upper_right['symbol'], fill_symbol)
                ):
                    right['symbol'] = fill_symbol
                    self.area[right['position']] = right['symbol']
                    return None

                # Check left
                if check_pairs(
                        (left['symbol'], blank_symbol),
                        (upper['symbol'], blank_symbol),
                        (upper_left['symbol'], fill_symbol)
                ):
                    left['symbol'] = fill_symbol
                    self.area[left['position']] = left['symbol']
                    return None
            else:
                # Check right
                if check_pairs(
                        (right['symbol'], blank_symbol),
                        (upper['symbol'], blank_symbol),
                        (upper_right['symbol'], fill_symbol)
                ):
                    upper['symbol'] = fill_symbol
                    self.area[upper['position']] = upper['symbol']
                    return None

                # Check left
                if check_pairs(
                        (left['symbol'], blank_symbol),
                        (upper['symbol'], blank_symbol),
                        (upper_left['symbol'], fill_symbol)
                ):
                    upper['symbol'] = fill_symbol
                    self.area[upper['position']] = upper['symbol']
                    return None

    def unfill(self, fill_symbol, blank_symbol):
        center = self.field[4]
        left = self.field[3]
        right = self.field[5]
        upper = self.field[1]
        upper_left = self.field[0]
        upper_right = self.field[2]
        bottom = self.field[7]
        bottom_left = self.field[6]
        bottom_right = self.field[8]

        if center['symbol'] == fill_symbol:
            if center['position'] <= len(self.area) // 2:
                # Check right
                if check_pairs(
                        (left['symbol'], fill_symbol),
                        (upper['symbol'], fill_symbol),
                ):
                    center['symbol'] = blank_symbol
                    self.area[center['position']] = center['symbol']
                    return None

                # Check left
                if check_pairs(
                        (right['symbol'], fill_symbol),
                        (upper['symbol'], fill_symbol),
                ):
                    center['symbol'] = blank_symbol
                    self.area[center['position']] = center['symbol']
                    return None
            else:
                # Check right
                if check_pairs(
                        (left['symbol'], fill_symbol),
                        (bottom['symbol'], fill_symbol),
                ):
                    center['symbol'] = blank_symbol
                    self.area[center['position']] = center['symbol']
                    return None

                # Check left
                if check_pairs(
                        (right['symbol'], fill_symbol),
                        (bottom['symbol'], fill_symbol),
                ):
                    center['symbol'] = blank_symbol
                    self.area[center['position']] = center['symbol']
                    return None

    def add(self, idx, position):
        element = self.field[idx]
        if position in range(len(self.area)):
            symbol = self.area[position]
            element['position'] = position
            element['symbol'] = symbol


__all__ = ('Surroundings',)
