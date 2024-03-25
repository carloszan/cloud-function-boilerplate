from typing import Any
from injector import inject
from interfaces.api_service import ApiService
from interfaces.storage_service import StorageService
import helpers


class BatchInsertPeopleService:
    @inject
    def __init__(self, storage_service: StorageService, api_service: ApiService) -> None:
        self.storage_service = storage_service
        self.api_service = api_service

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        leads_file_path = self.storage_service.download_file(
            kwds['folder'], kwds['mailing_file'])

        leads = leads_file_path
        return self.api_service.batch_insert_people(leads)
