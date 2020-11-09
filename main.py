# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


# Cyclical Sets - sets whose alternate elements unfold complementary cycles of a single interval
def generateCyclicalSet(interval, pitch_class=0):
    """

    :param pitch_class:
    :type interval: int
    """
    cyclical_set = []
    while len(cyclical_set) < 12:
        cyclical_set.append(pitch_class)
        pitch_class = (pitch_class + interval) % 12
    return cyclical_set


if __name__ == '__main__':
    print(generateCyclicalSet(5))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
