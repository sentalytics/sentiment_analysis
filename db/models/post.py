import datetime

def create_post(source, title, body, sentiment=None):
    return {
        'source': source,
        'title': title,
        'body': body,
        'sentiment': sentiment,
        'timestamp': datetime.datetime.now()
    }
