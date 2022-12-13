'''
    Starts the application.
'''
from Ui.ui import ui
from src.Repository.repo import repository, repository_txt, repository_binary
from src.Services.services import service

repository = repository()
repository_txt = repository_txt('files/text')
repository_binary = repository_binary('files/binary.txt')

service = service(repository_txt)
ui = ui(service)

service.test_add_book()

ui.start()
