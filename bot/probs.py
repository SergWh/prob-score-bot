import random


class Prob:
    title = ''
    message = None
    prob = 0.0,
    units = "%"

    def __init__(self, title, message, probability, units):
        self.title = title
        self.message = message
        self.prob = probability
        self.units = units


special_distribution = [*range(0, 101)] + [146]


def probs():
    return [
        Prob("Вероятность моего призыва", "Вероятность моего призыва {0}{1}", random.choice(special_distribution), "%"),
        Prob("Размер моего члена", "Размер моего члена {0} {1} ", int(random.betavariate(1.5, 11) * 100), "см"),
        Prob("Вероятность", None, random.randint(0, 100), "%")
    ]
