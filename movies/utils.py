import requests
from django.conf import settings


def get_movies_data(page=1):
    url = "https://demo.credy.in/api/v1/maya/movies/?page={page}".format(
        page=page)
    username = settings.CREDY_MOVIES_USERNAME
    password = settings.CREDY_MOVIE_PASSWORD
    response = requests.get(
        url, auth=requests.auth.HTTPBasicAuth(username, password), timeout=None
    )
    if response.ok:
        return response.json()
    else:
        return get_movies_data(page)
