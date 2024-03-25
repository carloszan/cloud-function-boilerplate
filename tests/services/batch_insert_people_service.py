from injector import Injector
from interfaces.api_service import ApiService
from interfaces.storage_service import StorageService
from services.batch_insert_people_service import BatchInsertPeopleService
from tests.mocks.mock_api_service import MockApiService
from tests.mocks.mock_storage_service import MockStorageService


def configure(binder):
    binder.bind(StorageService, MockStorageService)
    binder.bind(ApiService, MockApiService)


def test_batch_insert_people():
    injector = Injector(configure)

    service = injector.get(BatchInsertPeopleService)

    service(folder='test', mailing_file='file')
