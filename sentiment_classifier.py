import random

from data_processing import create_dataset, remove_noise_and_lemmatize
from nltk import NaiveBayesClassifier
from nltk.corpus import twitter_samples
from nltk.tokenize import word_tokenize

class SentimentClassifier:
    def __init__(self):
        positive_dataset = create_dataset(twitter_samples.tokenized('positive_tweets.json'), "Positive")
        negative_dataset = create_dataset(twitter_samples.tokenized('negative_tweets.json'), "Negative")

        full_dataset = positive_dataset + negative_dataset

        # Randomize data order (to avoid bias)
        random.shuffle(full_dataset)
        train_data = full_dataset[:7000]
        test_data = full_dataset[7000:]

        self.classifier = NaiveBayesClassifier.train(train_data)
        return

    def classify(self, statement):
        custom_tokens = remove_noise_and_lemmatize(word_tokenize(statement))
        return self.classifier.classify(dict([token, True] for token in custom_tokens))


if __name__ == '__main__':
    classifier = SentimentClassifier()
    print(classifier.classify("Wow I'm happy. This should be a great positive tweet"))
    print(classifier.classify("This is bad. I hate this tweet. It should be negative"))