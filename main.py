from text_analysis import classifier_factory
from db.collections import posts
from processors import reddit

if __name__ == "__main__":
    nb_classifier = classifier_factory.get_classifier()
    sub = input("Enter subreddit to scan: ")
    symbol = input("Enter symbol to search: ")
    classified_posts = reddit.get_posts(sub, symbol, nb_classifier)
    posts.batch_insert(classified_posts)


