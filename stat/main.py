from statistics import Statistics

from data import Data
from file import File


def main():
    print("Hello from stat!")


if __name__ == "__main__":
    main()

    file = File("/home/bhh/Belgeler/python/stat/stat/data.csv")

    data = Data()
    data.Load(file)

    stat = Statistics()
    stat.Load(data)
    print(f"{file.GetPath()} dosyasindaki Matematik notlarina iliskin veriler:")
    print(f"Aritmetik Ortalama: {stat.Mean('math_score')}")
    print(f"Varyans: {stat.Variance('math_score')}")
    print(f"Medyan: {stat.Median('math_score')}")
