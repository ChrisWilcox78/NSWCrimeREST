from watchdog_gevent import Observer
from watchdog.events import FileSystemEventHandler, FileSystemEvent
from os import environ
from .csv_processor import process_csv

DEFAULT_DATA_DIR = "../data/"


class CsvProcessingHandler(FileSystemEventHandler):
    def on_created(self, event: FileSystemEvent) -> None:
        self.handle_event(event)

    def on_modified(self, event: FileSystemEvent) -> None:
        self.handle_event(event)

    def handle_event(self, event: FileSystemEvent) -> None:
        if not event.is_directory:
            process_csv(event.src_path)


def startFileSystemObservation():
    observer = Observer()
    observer.schedule(CsvProcessingHandler(), environ.get(
        "CRIMES_DATA_DIR", DEFAULT_DATA_DIR), recursive=False)
    observer.start()


startFileSystemObservation()
