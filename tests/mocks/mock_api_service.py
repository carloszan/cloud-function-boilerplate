
from interfaces.api_service import ApiService


class MockApiService(ApiService):
    def batch_insert_people(self, people):
        return "hello world"

    def batch_update_people(self, people):
        return
