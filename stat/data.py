import pandas as PD
from file import File, FileExtension


class Data:
    def GetData(self) -> PD.DataFrame | None:
        return self.__get_data()

    def Load(self, file: File):
        self.__load(file)

    def __load(self, file: File):
        ext = file.GetSuffix()

        match ext:
            case FileExtension.CSV:
                self.data = PD.read_csv(file.GetPath())
                return
            case FileExtension.EXCEL:
                self.data = PD.read_excel(file.GetPath())
                return
            case FileExtension.EXCEL_OLD:
                self.data = PD.read_excel(file.GetPath())
                return
            case FileExtension.JSON:
                self.data = PD.read_json(file.GetPath())
                return
            case FileExtension.TXT:
                self.data = PD.read_csv(file.GetPath())
                return
            case _:
                return

    def __get_data(self) -> PD.DataFrame | None:
        if not isinstance(self.data, PD.DataFrame):
            return None
        return self.data


# class Frame(PD.)
