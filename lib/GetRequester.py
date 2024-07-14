import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    @property
    def url(self):
        return self._url
    
    @url.setter
    def url(self, url):
        if isinstance(url, str):
            self._url = url
        else:
            raise TypeError("URL must be a string.")

    def get_response_body(self):
        response = requests.get(self.url)
        return response.content

    def load_json(self):
        results = requests.get(self.url)
        return results.json()


