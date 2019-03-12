import random


class Grid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self._content = {}

    def get(self, x, y):
        try:
            return self._content[(x, y)]
        except KeyError:
            return ' '
    
    def set(self, x, y, value):
        if x < self.width and y < self.height:
            self._content[(x, y)] = value

    def __str__(self):
        lines = []
        for y in range(self.height):
            line = []
            for x in range(self.width):
                line.append(self.get(x, y))
            lines.append(''.join(line))
        return '\n'.join(reversed(lines))


def _set_root(grid):
    grid.set(grid.width//2, 0, random.choice('\\/'))


def make_tree(width, height):
    grid = Grid(width, height)
    _set_root(grid)
    reverse_branch = {'\\': '/', '/': '\\'}
    for y in range(1, height):
        vert_prob = y / (height-1)
        for x in range(width):
            below = grid.get(x, y-1)
            if below == ' ':
                if random.random() < vert_prob and random.random() < .25:
                    grid.set(x, y, ' ')
                elif grid.get(x-1, y-1) == '/':
                    grid.set(x, y, '/')
                elif grid.get(x+1, y-1) == '\\':
                    grid.set(x, y, '\\')
            else:
                if random.random() < vert_prob:
                    grid.set(x, y, reverse_branch[below])
                else:
                    grid.set(x, y, ' ')
    return str(grid)

