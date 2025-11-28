---
sidebar_position: 1
---

# API Genel Bakış

Crow üç basit sınıftan oluşur.

## Sınıflar

### File
Dosya doğrulama ve format kontrolü.

**Methodlar:**
- `Validate()` - Dosya geçerliliğini kontrol et
- `GetPath()` - Dosya yolunu al
- `GetSuffix()` - Dosya uzantısını al

[Detaylar →](./file.mdx)

---

### Data
Dosyadan veri yükleme.

**Methodlar:**
- `Load(file)` - Dosyayı yükle
- `GetData()` - pandas DataFrame al

[Detaylar →](./data.mdx)

---

### Statistics
Temel istatistikler.

**Methodlar:**
- `Load(data)` - Veriyi yükle
- `Mean(col)` - Ortalama
- `Variance(col)` - Varyans
- `Median(col)` - Medyan

[Detaylar →](./statistics.mdx)

---

## Kullanım

```python
from crow.file import File
from crow.data import Data
from crow.statistics import Statistics

file = File("data.csv")
data = Data()
data.Load(file)

stats = Statistics()
stats.Load(data)
ortalama = stats.Mean('sutun')
```
