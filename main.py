# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from collections import OrderedDict

from setuptools._vendor.ordered_set import OrderedSet

from Enums.Intervals import Interval


# This will create a set of pitch classes ascending consistently by a specified interval
def generateIntervalSet(interval, pitch_class=0):
    pitch_set = []
    while len(pitch_set) < 12:
        pitch_set.append(pitch_class)
        pitch_class = (pitch_class + interval) % 12
    return pitch_set


# Finds the 12x12 matrix associated with the row
def generateMatrix(pitch_set):
    original = pitch_set
    matrix = []
    for j in range(0, 12):
        transposition = list(map(lambda x: (x + (12 - original[j]) % 12) % 12, original))
        matrix.append(transposition)
    return matrix


# inverts the row provided
def invertRow(pitch_set):
    inverted_row = []
    for pitch_class in pitch_set:
        inverted_row.append((12 - pitch_class) % 12)

    return inverted_row


# Cyclical Sets - sets whose alternate elements unfold complementary cycles of a single interval
def generateCyclicalSet(cycle_set):
    inversion = invertRow(cycle_set)
    cyclical_set = OrderedSet([])

    # Since each row contains all 12 pitch classes, we only need to iterate over the first half of each row
    for i in range(0, (len(cycle_set) // 2) + 1):
        cyclical_set.append(cycle_set[i])
        cyclical_set.append(inversion[i])
    return cyclical_set.items


def transpose(pitch_set, interval):
    return list(map(lambda note: (note + interval) % 12, pitch_set))


def generateAllCognateSets(interval=Interval.per5):
    cycle_7 = generateIntervalSet(interval)
    cyclical_7_set = generateCyclicalSet(cycle_7)

    sets = []
    for i in range(0, len(cycle_7)):
        sets.append(generateDyadsOfParticularSum(cyclical_7_set, cycle_7[i]))
    return sets


def isCognate(pitch_set, dyad_sum, transposition):
    for i in range(0, len(pitch_set)):
        if (pitch_set[i] + transposition[i]) % 12 != dyad_sum:
            return False
        return True


def generateDyadsOfParticularSum(pitch_set, dyad_sum):
    inversion = invertRow(pitch_set)
    cognate = []
    transposition = transpose(inversion, 0)
    for i in range(0, len(inversion) + 1):
        if isCognate(pitch_set, dyad_sum, transposition):
            cognate = transposition
        transposition = transpose(inversion, i)
    return cognate


def swapEveryTwoElements(pitch_set):
    swapped_elements = pitch_set.copy()
    for i in range(0, len(pitch_set), 2):
        swapped_elements[i], swapped_elements[i + 1] = swapped_elements[i + 1], swapped_elements[i]
    return swapped_elements


def findAxisNoteDyads(pitch_set):
    axis_dyads = OrderedDict()
    for i in range(0, len(pitch_set)):
        axis_dyads[pitch_set[i]] = [pitch_set[(i - 1) % 12], pitch_set[(i + 1) % 12]]
    return axis_dyads


if __name__ == '__main__':
    print(generateIntervalSet(Interval.per5), "\n")
    allCognateSets = generateAllCognateSets()

    for cognate_set in allCognateSets:
        print(cognate_set, "\n")

    # for pitch in cyclicalSet:
    #     print(pitch, cycle7AxisDyads[pitch])

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
