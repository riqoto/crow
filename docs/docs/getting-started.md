---
sidebar_position: 2
---

# Başlarken

## Kurulum

```bash
git clone https://github.com/riqoto/stat.git
cd stat
pip install -e .
```

**Bağımlılıklar:**
- Python 3.10+
- pandas
- openpyxl (Excel desteği için)

## Temel Kullanım

### 1. Modülleri İçe Aktar

```python
from crow.file import File
from crow.data import Data
from crow.statistics import Statistics
```

### 2. Dosya Yükle

```python
file = File("ogrenciler.csv")  # veya .xlsx, .json, .txt
data = Data()
data.Load(file)
```

### 3. İstatistik Hesapla

```python
stats = Statistics()
stats.Load(data)

ortalama = stats.Mean('matematik_notu')
varyans = stats.Variance('matematik_notu')
medyan = stats.Median('matematik_notu')
```

## Tam Örnek

```python
from crow.file import File
from crow.data import Data
from crow.statistics import Statistics

# Dosya yükle ve doğrula
file = File("data.csv")
if not file.Validate():
    print("Geçersiz format!")
    exit()

# Veriyi yükle
data = Data()
data.Load(file)

# İstatistikleri hesapla
stats = Statistics()
stats.Load(data)

# Sonuçları yazdır
print(f"Ortalama: {stats.Mean('puan')}")
print(f"Varyans: {stats.Variance('puan')}")
print(f"Medyan: {stats.Median('puan')}")
```

## Desteklenen Formatlar

| Format | Uzantı |
|--------|---------|
| CSV | `.csv` |
| Excel | `.xlsx`, `.xls` |
| JSON | `.json` |
| Text | `.txt` |

---

**İleri Kullanım:** DataFrame'e doğrudan erişmek için:
```python
df = data.GetData()  # pandas DataFrame döner
```
