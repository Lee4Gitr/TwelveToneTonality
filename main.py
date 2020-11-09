# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


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
    cyclical_set = []

    # Since each row contains all 12 pitch classes, we only need to iterate over the first half of each row
    for i in range(0, (len(cycle_set) // 2) + 1):
        cyclical_set.append(cycle_set[i])
        cyclical_set.append(inversion[i])
    return cyclical_set


def findCognateSets(pitch_set):
    pitch_set_items = pitch_set
    inverted_set_items = invertRow(pitch_set)

    cognates = []
    dyad_sum = ((pitch_set_items[0] - inverted_set_items[0]) % 12)
    cognate_candidate = inverted_set_items
    matrix = generateMatrix(pitch_set_items)

    for tone_row in matrix:
        findCognate(cognate_candidate, dyad_sum, inverted_set_items, tone_row, cognates)

    return cognates


def findCognate(cognate_candidate, dyad_sum, inverted_set_items, pitch_set_items, cognates):
    for j in range(0, len(inverted_set_items)):
        if (pitch_set_items[j] + cognate_candidate[j] % 12) != dyad_sum:
            first = cognate_candidate.pop(0)
            cognate_candidate.append(first)
            continue
    cognates.append({f'Dyad of sum {cognate_candidate[0] - pitch_set_items[0] % 12}': cognate_candidate})


# Inversionally related set forms that share a single series of dyads are termed "cognate" sets
# def generateCognateSet(pitch_set, pitch_sum=Interval.oct):
#     cognate_set = OrderedSet([])
#     for i in range(0, len(pitch_set)):
#         cognate_set.append((pitch_sum - pitch_set[i]) % 12)
#     return cognate_set


if __name__ == '__main__':
    cycle7 = generateIntervalSet(Interval.per5)
    print(generateMatrix(cycle7))
    print(findCognateSets(cycle7))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
