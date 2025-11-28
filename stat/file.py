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
        if not self.__validate_isfile():
            raise FileNotFoundError(f"{file} not found!")

    def Validate(
        self,
    ) -> bool:
        if self.__validate_isfile() and self.__validate_suffix():
            return True
        return False

    def GetSuffix(self) -> FileExtension | None:
        return self.__get_suffix()

    def GetPath(self) -> str:
        return self.__get_path()

    def __validate_suffix(self) -> bool:
        file_extension = Path(self.file).suffix
        extensions = set(ext.value for ext in FileExtension)
        return file_extension in extensions

    def __validate_isfile(self) -> bool:
        import os

        return os.path.isfile(self.file)

    def __get_suffix(self) -> FileExtension | None:
        file_extension = Path(self.file).suffix

        for _, ext in enumerate(FileExtension):
            if ext.value == file_extension:
                return ext

        return None

    def __get_path(self) -> str:
        return self.file
