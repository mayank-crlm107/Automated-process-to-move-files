# Create Folder_to_track and folder_destination in appropriate directory before running the code.
# Files are successfully moved only when moving them to the Folder_to_track, not when copying and pasting.

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

import os
import time
import json

class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        for filename in os.listdir(folder_to_track):
            src = folder_to_track + "/" + filename
            new_destination = folder_destination + "/" + filename
            os.rename(src, new_destination)

folder_to_track = "#"
folder_destination = "#"
event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=True)
observer.start()

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()