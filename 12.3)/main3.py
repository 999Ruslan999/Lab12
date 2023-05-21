from future.moves import tkinter


class Restaurant:
    def __init__(self, name, cuisine_type, rating):
        self.name = name
        self.cuisine_type = cuisine_type
        self.rating = rating

    def describe_restaurant(self):
        print(f"{self.name} - {self.cuisine_type}")
        print(f"Рейтинг: {self.rating}")

    def update_rating(self, new_rating):
        self.rating = new_rating


class IceCreamStand(Restaurant):
    def __init__(self, name, cuisine_type, rating, flavors, location, work_time):
        super().__init__(name, cuisine_type, rating)
        self.flavors = flavors
        self.location = location
        self.work_time = work_time

    def display_flavors(self):
        print("Список сортов мороженого:")
        for flavor in self.flavors:
            print(f"- {flavor}")

    def add_flavor(self, new_flavor):
        self.flavors.append(new_flavor)

    def remove_flavor(self, flavor):
        if flavor in self.flavors:
            self.flavors.remove(flavor)
            print(f"Сорт мороженого '{flavor}' удален из списка.")
        else:
            print(f"Сорта мороженого '{flavor}' нет в списке.")

    def check_flavor(self, flavor):
        if flavor in self.flavors:
            print(f"Сорт мороженого '{flavor}' есть в списке.")
        else:
            print(f"Сорта мороженого '{flavor}' нет в списке.")


class StickIceCream(IceCreamStand):
    def __init__(self, name, cuisine_type, rating, flavors, location, work_time):
        super().__init__(name, cuisine_type, rating, flavors, location, work_time)
        self.type = "Мороженое на палочке"

    def display_type(self):
        print(f"Тип мороженого: {self.type}")


class SoftIceCream(IceCreamStand):
    def __init__(self, name, cuisine_type, rating, flavors, location, work_time):
        super().__init__(name, cuisine_type, rating, flavors, location, work_time)
        self.type = "Мягкое мороженое"

    def display_type(self):
        print(f"Тип мороженого: {self.type}")


restaurant1 = Restaurant("Русский двор", "Русская кухня", 4.5)
restaurant2 = Restaurant("Французская пекарня", "Французская кухня", 4.8)
restaurant3 = Restaurant("Японский сад", "Японская кухня", 4.3)

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()

restaurant1.update_rating(4.7)
restaurant1.describe_restaurant()

ice_cream_stand = IceCreamStand("Мороженое на углу", "Кафе-мороженное", 4.2, ["ванильное", "шоколадное", "клубничное"],
                                "ул. Ленина, 10", "10:00-22:00")
ice_cream_stand.describe_restaurant()
ice_cream_stand.display_flavors()

ice_cream_stand.add_flavor("карамельное")
ice_cream_stand.remove_flavor("шоколадное")
ice_cream_stand.check_flavor("клубничное")
ice_cream_stand.check_flavor("шоколадное")

stick_ice_cream = StickIceCream("Мороженое на палочке", "Кафе-мороженое", 4.5,
                                ["ванильное", "шоколадное", "клубничное", "арбузное"], "ул. Пушкина, 5", "12:00-20:00")
stick_ice_cream.describe_restaurant()
stick_ice_cream.display_type()

soft_ice_cream = SoftIceCream("Мягкое мороженое", "Кафе-мороженое", 4.0,
                              ["ванильное", "шоколадное", "клубничное", "банановое"], "ул. Гагарина, 15", "11:00-21:00")
soft_ice_cream.describe_restaurant()
soft_ice_cream.display_type()


class IceCreamStand:
    def __init__(self, flavors):
        self.flavors = flavors

        self.root = tkinter.Tk()
        self.root.title("Мороженое на углу")

        self.flavors_label = tkinter.Label(self.root, text="Список доступных сортов мороженого:")
        self.flavors_label.pack()

        self.flavors_listbox = tkinter.Listbox(self.root)
        for flavor in self.flavors:
            self.flavors_listbox.insert(tkinter.END, flavor)
        self.flavors_listbox.pack()

        self.root.mainloop()



ice_cream_stand = IceCreamStand(["Ваниль", "Шоколад", "Клубничное"])
