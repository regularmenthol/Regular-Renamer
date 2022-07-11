#the Renamer class

import time
from pathlib import Path

from PyQt6.QtCore import QObject, pyqtSignal

class Renamer(QObject):
    #Define custom signals
    progressed = pyqtSignal(int)
    renamedFile = pyqtSignal(Path)
    finished = pyqtSignal()

    def __init__(self, files, prefix):
        super().__init__()
        self._files = files
        self._prefix = prefix

    def renameFiles(self):
        for fileNumber, file in enumerate(self._files, 1):
            newFile = file.parent.joinpath(
                f"{self._prefix}{str(fileNumber)}{file.suffix}"
            )
            file.rename(newFile)
            time.sleep(0.1) #arbitrary sleep timer
            self.progressed.emit(fileNumber)
            self.renamedFile.emit(newFile)
        self.progressed.emit(0)
        self.finished.emit()