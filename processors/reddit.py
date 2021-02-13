from db.models import post as postModel
import requests

from helpers.exceptions import handle_error

baseURL = "https://www.reddit.com/r/"
headers = {'User-Agent': 'Mozilla/5.0'}


def get_posts(sub, symbol, classifier, sort="new"):
    url = f'{baseURL}{sub}/search.json'
    params = {'q': symbol, 'sort': sort}
    try:
        resp = requests.get(url=url, params=params, headers=headers)
        if resp.status_code == 200:
            return __process_posts(resp.json(), classifier)
        else:
            handle_error("Failed to get reddit posts.", str(resp.status_code))
            return []
    except Exception as e:
        handle_error("Failed to get reddit posts.", e)


def __process_posts(rawPosts, classifier):
    posts = rawPosts['data'].get('children', [])
    formatted_posts = []
    for post in posts:
        # Only doing sentiment on post title right now
        sentiment = classifier.classify(post['data'].get('title'))
        formatted_posts.append(
            postModel.create_post("reddit", post['data'].get(
                'title', ''), post['data'].get('selftext', ''), sentiment)
        )

    return formatted_posts
