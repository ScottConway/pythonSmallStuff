import re

def isAnagramInitial(word1, word2):
    for c in word1:
        if word2.find(c) == -1:
            return False

    return True

def isAnagramV2(word1, word2):
    if word1.lower().__eq__(word2.lower()):
        return False

    return sorted(word1.strip().lower()) == sorted(word2.strip().lower())

def isAnagram(word1, word2):
    if word1.lower().__eq__(word2.lower()):
        return False

    return sorted(re.findall("\w", word1.strip().lower())) == sorted(re.findall("\w", word2.strip().lower()))

def anagramTest():
    testData = [("dab", "sad", False),
                ("dab", "bad", True),
                ("dad", "dab", False),
                ("dab", "dad", False),
                ("Dab", "Bad", True),
                ("Bad", "dAb", True),
                ("bad", "bad", False),
                ("bad", "BAD", False),
                ("Clint Eastwood", "old west action", True),
                ("Clint Eastwood", "Clint Eastwood", False),
                ("old west action", "Clint Eastwood", True),
                ("Clint Eastwood", "Old west action!", True),
                ("Old west action!", "Clint Eastwood", True),
                ("I said okay.", "Is aid okay?", True)
                ]

    for test in testData:
        if isAnagram(test[0], test[1]) == test[2]:
            print(f'Test passed for \"{test[0]}\" and \"{test[1]}\"')
        else:
            print(f'Test failed for \"{test[0]}\" and \"{test[1]}\"')

if __name__ == '__main__':
    anagramTest()