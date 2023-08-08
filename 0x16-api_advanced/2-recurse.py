import requests


def get_hot_posts(subreddit):
    """Returns a list of titles of all hot posts on a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"
    headers = {"User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"}
    hot_list = []
    after = ""
    count = 0

    while True:
        params = {"after": after, "count": count, "limit": 100}
        response = requests.get(url, headers=headers,
                                params=params, allow_redirects=False)

        if response.status_code == 404:
            return None

        results = response.json().get("data")
        after = results.get("after")
        count += results.get("dist")

        for c in results.get("children"):
            hot_list.append(c.get("data").get("title"))

        if after is None:
            break

    return hot_list


subreddit_name = "python"
hot_posts = get_hot_posts(subreddit_name)
print(hot_posts)
