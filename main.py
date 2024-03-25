from injector import Injector
from interfaces.api_service import ApiService
from interfaces.storage_service import StorageService
from services.batch_insert_people_service import BatchInsertPeopleService
from services.gcp_storage_service import GCPStorageService
from services.infobip_api_service import InfobipApiService


def configure(binder):
    binder.bind(StorageService, to=GCPStorageService)
    binder.bind(ApiService, to=InfobipApiService('api_key', 'url'))


def main(request):
    request_json = request
    event = request_json['event']

    injector = Injector(configure)

    events = {
        'batch_insert_people': injector.get(BatchInsertPeopleService),
    }

    if event not in events.keys():
        headers = {'Content-Type': 'application/json'}
        data = {'message': 'Event doesn`t exist.'}
        return (data, 400, headers)

    events[event](mailing_file='example.csv', folder='example')

    return "200"


main({'event': 'batch_insert_people'})
