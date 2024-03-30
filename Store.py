#Ваша задача — создать класс Store, который можно будет использовать для создания различных магазинов.
#Шаги:
#1. Создай класс Store:
#-Атрибуты класса:
#name: название магазина.
#address: адрес магазина.
#items: словарь, где ключ - название товара, а значение - его цена. Например, {'apples': 0.5, 'bananas': 0.75}.

#Методы класса:
#__init__ - конструктор, который инициализирует название и адрес, а также пустой словарь дляitems`.
#-  метод для добавления товара в ассортимент.
#метод для удаления товара из ассортимента.
#метод для получения цены товара по его названию. Если товар отсутствует, возвращайте None.
#метод для обновления цены товара.
#2. Создай несколько объектов класса Store:
#Создай не менее трех различных магазинов с разными названиями, адресами и добавь в каждый из них несколько товаров.
#3. Протестировать методы:
#Выбери один из созданных магазинов и протестируй все его методы: добавь товар, обнови цену, убери товар и запрашивай цену.

class Store:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}  # Инициализируем пустой словарь товаров

    def add_item(self, item_name, price):
        self.items[item_name] = price

    def remove_item(self, item_name):
        if item_name in self.items:
            del self.items[item_name]

    def get_price(self, item_name):
        return self.items.get(item_name, None)

    def update_price(self, item_name, new_price):
        if item_name in self.items:
            self.items[item_name] = new_price


store1 = Store("У Aшота", "ул. Вицлипуцли 1")
store2 = Store("Bишенка", "ул. 300-летия граненному стакану 2")
store3 = Store("Яйцо", "ул. Патриса Лумумбы 30")


store1.add_item("Яблоки", 90.0)
store1.add_item("Бананы", 175.0)


store2.add_item("Молоко", 80.0)
store2.add_item("Хлеб", 34.0)

store3.add_item("Яйца", 120.0)
store3.add_item("Сыр", 530.0)

print(f"Товары в магазине {store1.name}: {store1.items}")
print("Добавили лимоны")
store1.add_item("Лимоны", 165.0)

print(f"Товары в магазине {store1.name}: {store1.items}")
print(f"Цена яблок в магазине {store1.name}: {store1.get_price('Яблоки')}руб")
store1.update_price("Яблоки", 155.0)
print(f"Новая цена яблок в магазине {store1.name}: {store1.get_price('Яблоки')}руб")
store1.remove_item("Бананы")
print(f"Цена бананов в магазине  {store1.name} после удаления: {store1.get_price('Бананы')}")

print(f"Товары в магазине {store1.name}: {store1.items}")
