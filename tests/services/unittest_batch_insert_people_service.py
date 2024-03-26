import unittest
from unittest.mock import Mock
from injector import Injector
from interfaces.api_service import ApiService
from interfaces.storage_service import StorageService
from services.batch_insert_people_service import BatchInsertPeopleService


class TestBatchInsertPeople(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestBatchInsertPeople, self).__init__(*args, **kwargs)
        self.api_service_mock = Mock()

    def _configure(self, binder):
        binder.bind(StorageService, Mock())
        binder.bind(ApiService, self.api_service_mock)

    def setUp(self):
        self.__injector = Injector(self._configure)
        self.__service = self.__injector.get(BatchInsertPeopleService)

    def test_batch_insert_people(self):
        # Arrange
        self.api_service_mock.batch_insert_people.return_value = "hello world"

        # Act
        response = self.__service(folder='test', mailing_file='file')

        # Assert
        self.assertEqual(response, "hello world")


if __name__ == '__main__':
    unittest.main()
