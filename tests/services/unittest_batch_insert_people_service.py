import unittest
from injector import Injector, Module
from interfaces.api_service import ApiService
from interfaces.storage_service import StorageService
from services.batch_insert_people_service import BatchInsertPeopleService
from tests.mocks.mock_api_service import MockApiService
from tests.mocks.mock_storage_service import MockStorageService


class BatchInsertPeopleModule(Module):
    def configure(self, binder):
        binder.bind(StorageService, MockStorageService)
        binder.bind(ApiService, MockApiService)


class TestBatchInsertPeople(unittest.TestCase):
    def setUp(self):
        self.__injector = Injector(BatchInsertPeopleModule())
        self.__service = self.__injector.get(BatchInsertPeopleService)

    def test_batch_insert_people(self):
        response = self.__service(folder='test', mailing_file='file')

        self.assertEqual(response, "hello world")


if __name__ == '__main__':
    unittest.main()
