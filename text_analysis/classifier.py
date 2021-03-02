import random

from nltk.corpus import twitter_samples
from textblob.classifiers import NaiveBayesClassifier

class TextClassifier:
    def __init__(self):
        pos_tweets = [(x, 'Positive') for x in twitter_samples.strings('positive_tweets.json')]
        neg_tweets = [(x, 'Negative') for x in twitter_samples.strings('negative_tweets.json')]

        full_dataset = pos_tweets + neg_tweets
        random.shuffle(full_dataset)
        dataset_size = len(full_dataset)
        
        # Have to divide the dataset. Larger datasets can result in a SIGKILL 
        # Probably due to limited memory in the docker container(needs further investigation)
        train_size = dataset_size//5
        train_dataset = full_dataset[:train_size]
        
        self.nb_classifier = NaiveBayesClassifier(train_dataset)
        
        
    def classify(self, text):
        return self.nb_classifier.classify(text)

    
if __name__ == "__main__":
    classifier = TextClassifier()

    print(classifier.classify("Wow I'm happy. This should be a great positive tweet"))
    print(classifier.classify("This is bad. I hate this tweet. It should be negative"))
