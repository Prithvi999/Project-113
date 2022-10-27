import sys
import time
import random

import os
import shutil

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

src_path = "C:/Users/kalya/Downloads/destination91"

class FileEventHandler(FileSystemEventHandler):
    def onCreated(self, event):
        print(f'Hey, {event.src_path} has been created')

    def onDeleted(self, event):
        print(f'Someone has deleted {event.src_path}')

    def onModified(self, event):
        print(f'Hey, {event.src_path} has been modified')

    def onMoved(self, event):
        print(f'Hey, someone moved {event.src_path} to {event.dest_path}')

try:
    while True:
        time.sleep(2)
        print("running . . .")
except KeyboardInterrupt:
    print('Stopped')
    Observer.stop()
