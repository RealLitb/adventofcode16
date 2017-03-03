import re
import copy

class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other):
        return abs(self.x - other.x) + abs(self.y - other.y)

    def __str__(self):
        return str((self.x, self.y))

class DirData:
    def __init__(self, transform, delta):
        self.transform = transform
        self.delta = delta

class Walker:
    def __init__(self):
        self._position = Position(0, 0)
        self._direction = "U"
        self._visited = set()
        self._visited_twice = []

    def process_ops(self, list_of_ops):
        for op in list_of_ops:
            self.process_op(op)

    def process_op(self, op):
        turn, count = self._op2turn_and_count(op)
        new_direction = Walker._dir_data[self._direction].transform[turn]
        delta_x, delta_y = Walker._dir_data[new_direction].delta
        self._add_visits(delta_x * count, delta_y * count)
        self._position.x += delta_x * count
        self._position.y += delta_y * count
        self._direction = new_direction

    def current_distance(self):
        return self._position.distance(Position(0, 0))

    def visited_twice(self):
        return self._visited_twice

    def _add_visits(self, count_x, count_y):
        (off_x, off_y) = ((1 if count > 0 else -1) for count in (count_x, count_y))

        iterate_indices = (lambda start, count, off: (i + off for i in range(start, start + count, off)))
        for pos_x in (self._position.x,) if count_x == 0 else iterate_indices(self._position.x, count_x, off_x):
            for pos_y in (self._position.y,) if count_y == 0 else iterate_indices(self._position.y, count_y, off_y):
                pos = (pos_x, pos_y)
                if pos in self._visited:
                    self._visited_twice.append(pos)
                else:
                    self._visited.add(pos)

    def _op2turn_and_count(self, op):
        return op[:1], int(op[1:])

    _dir_data = {
        "L" : DirData(transform={ "R" : "U", "L" : "D" }, delta=(-1, 0)),
        "U" : DirData(transform={ "R" : "R", "L" : "L" }, delta=(0, +1)),
        "R" : DirData(transform={ "R" : "D", "L" : "U" }, delta=(+1, 0)),
        "D" : DirData(transform={ "R" : "L", "L" : "R" }, delta=(0, -1))
    }


input_ops = re.sub("[\\n ]+", "", """
L3, R1, L4, L1, L2, R4, L3, L3, R2,
R3, L5, R1, R3, L4, L1, L2, R2, R1,
L4, L4, R2, L5, R3, R2, R1, L1, L2,
R2, R2, L1, L1, R2, R1, L3, L5, R4,
L3, R3, R3, L5, L190, L4, R4, R51,
L4, R5, R5, R2, L1, L3, R1, R4, L3,
R1, R3, L5, L4, R2, R5, R2, L1, L5,
L1, L1, R78, L3, R2, L3, R5, L2, R2,
R4, L1, L4, R1, R185, R3, L4, L1, L1,
L3, R4, L4, L1, R5, L5, L1, R5, L1, R2,
L5, L2, R4, R3, L2, R3, R1, L3, L5, L4,
R3, L2, L4, L5, L4, R1, L1, R5, L2, R4,
R2, R3, L1, L1, L4, L3, R4, L3, L5, R2,
L5, L1, L1, R2, R3, L5, L3, L2, L1, L4,
R4, R4, L2, R3, R1, L2, R1, L2, L2, R3,
R3, L1, R4, L5, L3, R4, R4, R1, L2, L5,
L3, R1, R4, L2, R5, R4, R2, L5, L3, R4,
R1, L1, R5, L3, R1, R5, L2, R1, L5, L2,
R2, L2, L3, R3, R3, R1
""").split(",")

walker = Walker()
walker.process_ops(input_ops)
print ("Distance to (0, 0)", walker.current_distance(), "blocks")
print ("Blocks visited twice in order", walker.visited_twice())
