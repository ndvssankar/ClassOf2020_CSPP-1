'''
    Document Distance - A detailed description is given in the PDF
'''
import re
import math


def tokenize(string):
    '''
        returns a word list based on input string.
    '''
    regex = re.compile('[^a-z]')
    return [regex.sub('', word.strip()) for word in string.lower().split(' ')]

def vectorize(words, index, dictionary):
    '''
        prepares a dictionary and returns the dictionary.
    '''
    stopwords = load_stopwords("stopwords.txt")
    for word in words:
        if word not in stopwords and len(word) != 0:
            if word not in dictionary:
                dictionary[word] = [0, 0]
            dictionary[word][index] += 1
    return dictionary

def compute_distance(dictionary):
    '''
        calculates the document similarity.
    '''
    numerator = sum(k[0] * k[1] for k in dictionary.values())
    den_1 = math.sqrt(sum(k[0] ** 2 for k in dictionary.values()))
    den_2 = math.sqrt(sum(k[1] ** 2 for k in dictionary.values()))
    return numerator/(den_1*den_2)

def similarity(doc1, doc2):
    '''
        Compute the document distance as given in the PDF
    '''
    dictionary = dict()
    dictionary = vectorize(tokenize(doc1), 0, dictionary)
    dictionary = vectorize(tokenize(doc2), 1, dictionary)
    return compute_distance(dictionary)

def load_stopwords(filename):
    '''
        loads stop words from a file and returns a dictionary
    '''
    stopwords = {}
    with open(filename, 'r') as file_name:
        for line in file_name:
            stopwords[line.strip()] = 0
    return stopwords

def main():
    '''
        take two inputs and call the similarity function
    '''
    input1 = input()
    input2 = input()

    print(similarity(input1, input2))

if __name__ == '__main__':
    main()
