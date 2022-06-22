from conversions import conversions


class Converter():
    def __init__(self) -> None:
        self.n1 = 0
        self.n2 = 0

        self.type1 = ""
        self.type2 = ""

        self.conversions = conversions

        self.ratio = 0

    def convert(self, n1, type1, type2):
        self.n1 = n1
        self.type1 = type1
        self.type2 = type2

        self.ratio = self.conversions[self.type1][self.type2]
        self.n2 = self.n1 * self.ratio

        return self.n2