# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


from setuptools._vendor.ordered_set import OrderedSet
from Enums.Intervals import Interval


def generateIntervalSet(interval, pitch_class=0):
    """

    :param pitch_class:
    :type interval: int
    """
    pitch_set = []
    while len(pitch_set) < 12:
        pitch_set.append(pitch_class)
        pitch_class = (pitch_class + interval) % 12
    return OrderedSet(pitch_set)


def invertRow(pitch_set):
    inverted_row = OrderedSet([])
    for pitch_class in pitch_set:
        inverted_row.add((12 - pitch_class) % 12)

    return inverted_row


# Cyclical Sets - sets whose alternate elements unfold complementary cycles of a single interval
def generateCyclicalSet(cycle_set):
    inversion = invertRow(cycle_set)
    cyclical_set = OrderedSet([])

    # Since each row contains all 12 pitch classes, we only need to iterate over the first half of each row
    for i in range(0, (len(cycle_set) // 2) + 1):
        cyclical_set.append(cycle_set[i])
        cyclical_set.append(inversion[i])
    return cyclical_set


# Inversionally related set forms that share a single series of dyads are termed "cognate" sets
def generateCognateSet(pitch_set, pitch_sum=Interval.oct):
    cognate_set = OrderedSet([])
    for i in range(0, len(pitch_set)):
        cognate_set.append((pitch_sum - pitch_set[i]) % 12)
    return cognate_set


if __name__ == '__main__':
    cycle_7 = generateIntervalSet(Interval.per5)
    cycle_5 = generateIntervalSet(Interval.per4)
    cyclical7set = generateCyclicalSet(cycle_7)
    cyclical5set = generateCyclicalSet(cycle_5)

    # Example 12 in Twelve Tone Tonality - George Perle
    print(generateCognateSet(cyclical7set, Interval.per5))
    print(cyclical7set)
    print(invertRow(cyclical7set))
    print(generateCognateSet(cyclical5set, Interval.per4))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
