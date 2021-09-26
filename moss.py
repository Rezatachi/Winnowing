

# main function that executes winnowing algorithm functionality


def main():
    k = 5
    t = 9
    test = "print(Hello World!)"
    test2 = "print(Hello World!))"

    print("\n----------TEST-----------")
    print("Test String: " + test + "\n")

    fingerprints = fingerprint(k, t, test)
    fingerprints2 = fingerprint(k, t, test2)
    print("Fingerprints:")
    print("Document 1: ")
    print(fingerprints)
    print('Document 2:')
    print(fingerprints2)


# returns the string in all lower case without irrelevant features (spaces, punctuation)
def refine(inputString):
    # defines list of irrelevant characters
    irrelevant = [" ", ".", ",", ":", "'", '"', "!", "?", "-", ";", ]
    # initializes outputString
    outputString = ""

    # adds lowercase of every char of inputString that is not irrelevant to outputString
    for i in range(len(inputString)):
        if not(inputString[i] in irrelevant):
            outputString += inputString[i].lower()

    # returns final outputString
    return outputString


# splits input into k-grams and returns a list of pairs [k-gram, index]
def kSplit(k, inputString):
    # initialize pairs list
    pairs = []

    # runs i from 0 to n - k + 1 where n = length of input
    for i in range(len(inputString) - k + 1):
        # sets gram equal to the k-gram substring
        gram = inputString[i: i + k]
        # adds the k-gram and index as a pair to pairs
        pairs.append([gram, i])

    # returns final pairs list
    return pairs


# hashes the inputString and returns the hash value
def hash_31(inputString):
    # sets asciiValues to a list of ASCII values of inputString
    asciiValues = []
    for i in range(len(inputString)):
        asciiValues.append(ord(inputString[i]))

    # Uses horner's method to compute summation[31^i * x(i)] as the hash value
    hashValue = 0
    for i in range(len(asciiValues) - 1, -1, -1):
        hashValue = 31 * hashValue + asciiValues[i]

    # returns final hashValue
    return hashValue


# returns hashed pairs [hash, index] from original pairs [k-gram, index]
def hashGrams(info):
    # initializes hashedPairs list
    hashedPairs = []

    # gets hash for every k-gram and adds [hash, index] pair to hashedPairs
    for i in range(len(info)):
        hashedGram = hash_31(info[i][0])
        hashedPairs.append([hashedGram, info[i][1]])

    # returns final hashedPairs list
    return hashedPairs


# returns list of fingerprints by selecting from defined windows
def windowSelect(k, t, pairs):
    # sets the value for the size of each window
    w = t - k + 1
    # initializes the list that will hold all selections for fingerprints
    selections = []

    # sets variable that will keep track of previously added fingerprint's index to -1
    previousIndex = -1
    # runs through every pair from 0 to n - w
    for i in range(len(pairs) - w + 1):
        # sets min to current i pair
        min = pairs[i][0]
        # sets minIndex to matching index for min
        minIndex = pairs[i][1]
        # imitates window from i to i + w, checking for min value of window
        for j in range(i + 1, i + w):
            # sets new min and minIndex if hash value for current j pair is <= min
            if pairs[j][0] <= min:
                min = pairs[j][0]
                minIndex = pairs[j][1]
        # checks if min is already in selections by comparing indexes
        if minIndex != previousIndex:
            # if new pair, adds [min, minIndex] pair to selections and sets previousIndex to minIndex
            previousIndex = minIndex
            selections.append([min, minIndex])

    # returns final selections list of fingerprints
    return selections


# selects fingerprints from inputString by applying all other functions
def fingerprint(k, t, inputString):
    # sets preproccessed to inputString with all irrelevant features removed
    preprocessed = refine(inputString)
    print("Preproccessed: " + preprocessed)
    # sets pairs to list of [k-gram, index]
    pairs = kSplit(k, preprocessed)
    print("k-gram Pairs: " + str(pairs))
    # sets hashedPairs to list of [hash, index]
    hashedPairs = hashGrams(pairs)
    print("Hashed Pairs: " + str(hashedPairs))
    # sets fingerprints to list of [fingerprint, index]
    fingerprints = windowSelect(k, t, hashedPairs)
    # returns list of [fingerprint, index] pairs
    return fingerprints


# calls main to run program
main()
