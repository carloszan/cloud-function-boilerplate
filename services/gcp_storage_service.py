from interfaces.storage_service import StorageService


class GCPStorageService(StorageService):
    def download_file(self, folder: str, file: str) -> str:
        source_blob_name = f'{folder}/{file}'
        destinations_file_name = f'/tmp/{file}'
        # blob = self.bucket.blob(source_blob_name)
        # blob.download_to_filename(destinations_file_name)

        return destinations_file_name

    def upload_file(self, folder: str, file: str) -> None:
        source_blob_name = f'{folder}/{file}'
        destinations_file_name = f'/tmp/{file}'
        # blob = self.bucket.blob(source_blob_name)
        # blob.upload_from_filename(destinations_file_name)
        return
