---
sidebar_position: 1
---

# Crow

Pandas tabanlı basit bir istatistik wrapper'ı.

## Nedir?

Crow, farklı dosya formatlarından (CSV, Excel, JSON, TXT) veri yükleyip temel istatistiksel hesaplamalar yapmanızı sağlayan minimal bir Python kütüphanesidir.

## Kurulum

```bash
git clone https://github.com/riqoto/stat.git
cd stat
pip install -e .
```

## Hızlı Kullanım

```python
from crow.file import File
from crow.data import Data
from crow.statistics import Statistics

# Dosya yükle
file = File("data.csv")
data = Data()
data.Load(file)

# İstatistik hesapla
stats = Statistics()
stats.Load(data)

print(f"Ortalama: {stats.Mean('sutun_adi')}")
print(f"Varyans: {stats.Variance('sutun_adi')}")
print(f"Medyan: {stats.Median('sutun_adi')}")
```

## Özellikler

- CSV, Excel (.xlsx, .xls), JSON, TXT desteği
- Ortalama, varyans, medyan hesaplama
- Pandas DataFrame'e doğrudan erişim

## Sonraki Adımlar

- [API Referansı](./api/overview.md) - Sınıflar ve methodlar
