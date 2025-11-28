import pandas as PD
from data import Data


class Statistics:
    """
    İstatistiksel hesaplamaları yapan sınıf.

    Yüklenen veri seti üzerinde ortalama, varyans ve medyan gibi
    temel istatistiksel analizleri gerçekleştirir.

    Attributes:
        data (PD.DataFrame | None): Analiz edilecek veri seti.
    """
    def Load(self, data: Data | None):
        """
        Analiz edilecek veriyi yükler.

        Args:
            data (Data | None): Veri nesnesi.
        """
        self.data = self.__load(data)

    def Mean(self, col: str) -> PD.Series | float | int | None:
        """
        Belirtilen sütunun aritmetik ortalamasını hesaplar.

        Args:
            col (str): İşlem yapılacak sütun adı.

        Returns:
            PD.Series | float | int | None: Ortalama değeri veya hata durumunda None.
        """
        return self.__mean(col)

    def Variance(self, col: str) -> PD.Series | float | int | None:
        """
        Belirtilen sütunun varyansını hesaplar.

        Args:
            col (str): İşlem yapılacak sütun adı.

        Returns:
            PD.Series | float | int | None: Varyans değeri veya hata durumunda None.
        """
        return self.__variance(col)

    def Median(self, col: str) -> PD.Series | float | int | None:
        """
        Belirtilen sütunun medyanını hesaplar.

        Args:
            col (str): İşlem yapılacak sütun adı.

        Returns:
            PD.Series | float | int | None: Medyan değeri veya hata durumunda None.
        """
        return self.__median(col)

    def __load(self, data: Data | None) -> PD.DataFrame | None:
        if not data:
            return None
        return data.GetData()

    def __mean(self, col: str):
        self.__validate(col)
        if self.data is None:
            return None

        return self.data[col].mean()

    def __variance(self, col: str) -> PD.Series | float | int | None:
        self.__validate(col)
        if self.data is None:
            return None

        return self.data[col].var()

    def __median(self, col: str) -> PD.Series | float | int | None:
        self.__validate(col)

        if self.data is None:
            return None

        return self.data[col].median()

    def __validate(self, col: str):
        if not col:
            return None
        if self.data is None or col not in self.data.columns:
            return None
