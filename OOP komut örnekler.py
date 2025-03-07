

# animal.py (Ana Sınıf)
class Animal:
    def __init__(self, isim):
        self.isim = isim

    def konus(self):
        return "Bilinmeyen ses"


# dog.py (Alt Sınıf, Fonksiyon Güncelleme)
class Dog(Animal):
    def konus(self):
        return f"{self.isim} havlıyor!"


# cat.py (Alt Sınıf, Fonksiyon Güncelleme)
class Cat(Animal):
    def konus(self):
        return f"{self.isim} miyavlıyor!"


# main.py (Programı Çalıştırma)
if __name__ == "__main__":
    kopek = Dog("Buddy")
    kedi = Cat("Whiskers")

    hayvanlar = [kopek, kedi]

    print("Hayvanat bahçesindeki hayvanlar:")
    for hayvan in hayvanlar:
        print(hayvan.konus())

