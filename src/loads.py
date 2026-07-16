class Load:

    def __init__(self, position: float):

        self.position = position


class PointLoad(Load):

    def __init__(self, force: float, position: float):

        super().__init__(position)

        self.force = force
