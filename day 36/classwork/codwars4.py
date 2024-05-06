def remove_url_anchor(url):
    if '#' in url:
        return url.split('#')[0]
    else:
        return url