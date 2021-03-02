from text_analysis.classifier import TextClassifier

import os
import pickle
import threading


def get_classifier():
    return TextClassifier()

    """
    # Pickling currently results in a SIGKILL. 
    filename = "classifier.pickle"
    if(os.path.exists(filename)):
        classifier = __load_classifier(filename)
    else:
        classifier = TextClassifier()
        __save_classifier(filename, classifier)

    return classifier
    """

def __load_classifier(filename):
    with open(filename, 'rb') as input:
        classifier = pickle.load(input)
    return classifier


def __save_classifier(filename, classifier):
    with open(filename, 'wb') as output:
        pickle.dump(classifier, output, pickle.HIGHEST_PROTOCOL)
