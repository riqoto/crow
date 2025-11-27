from enum import Enum
from pathlib import Path


class FileExtension(Enum):
    CSV = ".csv"
    EXCEL = ".xlsx"
    EXCEL_OLD = ".xls"
    JSON = ".json"
    TXT = ".txt"


class File:
    def __init__(self, file: str):
        self.file = file
        if not self._validate_isfile():
            raise FileNotFoundError(f"{file} not found!")

    def Validate(
        self,
    ) -> bool:
        if self._validate_isfile() and self._validate_suffix():
            return True
        return False

    def _validate_suffix(self):
        file_extension = Path(self.file).suffix
        extensions = set(item.value for item in FileExtension)
        return file_extension in extensions

    def _validate_isfile(self) -> bool:
        import os

        return os.path.isfile(self.file)
