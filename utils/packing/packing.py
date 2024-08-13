import json
import pickle
from dataclasses import dataclass


@dataclass
class Car:
    brand: str
    model: str
    year: int
    color: tuple
    __condition = {'tires': 100,
                   'engine': 100,
                   'fuel': 100,
                   'glass': 100,
                   'body': 100}
    
    def __dict__(self):
        return {"brand": self.brand, "model": self.model,
                "year": self.year, "color": self.color, "condition": self.__condition}
    
    def save_with_json(self, path):
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(self.__dict__(), f, ensure_ascii=False,
                      separators=(',', ':'), indent=2)
    
    def load_with_json(self, path):
        with open(path, 'r') as f:
            data = json.load(f)
            self.brand = data['brand']
            self.model = data['model']
            self.year = data['year']
            self.color = tuple(data['color'])
            self.__condition = data['condition']
    
    def save_with_pickle(self, path):
        with open(path, 'wb') as f:
            pickle.dump(self.__dict__(), f)

    def load_with_pickle(self, path):
        with open(path, 'rb') as f:
            data = pickle.load(f)
            self.brand = data['brand']
            self.model = data['model']
            self.year = data['year']
            self.color = tuple(data['color'])
            self.__condition = data['condition']


if __name__ == '__main__':
    car1 = Car("Ford", "Mustang", 1967, (0, 0, 255))
    car2 = Car("Chevrolet", "Corvette", 1971, (255, 0, 0))
    # car1.save_with_json('data.json')
    # car2.load_with_json('data.json')
    car1.save_with_pickle('data.pickle')
    car2.load_with_pickle('data.pickle')
    print(car2)

