import datetime

def create_comment(source, comment):
    return {
        'source': source,
        'comment': comment,
        'timestamp': datetime.datetime.now()
    }
