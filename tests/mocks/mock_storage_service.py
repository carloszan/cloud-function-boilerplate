from interfaces.storage_service import StorageService


class MockStorageService(StorageService):
    def download_file(self, folder: str, file: str) -> str:
        return "downloaded"

    def upload_file(self, folder: str, file: str) -> None:
        return
