import requests

from interfaces.api_service import ApiService
import helpers


class InfobipApiService(ApiService):

    def __init__(self, api_key, url):
        self.url = url
        self.api_key = api_key

    def batch_insert_people(self, people):
        response = self._post(people)
        return response

    def batch_update_people(self, people):
        response = self._patch(people)
        return response

    @helpers.retry(Exception, tries=3)
    def _post(self, payload):
        return self._fetch_person_batch(requests.post, payload)

    @helpers.retry(Exception, tries=3)
    def _patch(self, payload):
        return self._fetch_person_batch(requests.patch, payload)

    def _fetch_person_batch(self, func, payload):
        url = f'{self.url}/news/'

        headers = {
            "accept": "application/json",
            "Content-Type": "application/json",
            'Authorization': f'App {self.api_key}'
        }
        response = func(url, headers=headers, json=payload)

        response.raise_for_status()

        return response
