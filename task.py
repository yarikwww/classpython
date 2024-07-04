'''
1. Створіть метод add, щоб додати дві країни. Цей метод повинен створити ще один об'єкт country з назвою двох країн разом і населенням двох країн.
bosnia = Country('Bosnia', 10_000_000)
herzegovina = Country('Herzegovina', 5_000_000)

bosnia_herzegovina = bosnia.add(herzegovina)
bosnia_herzegovina.population -> 15_000_000
bosnia_herzegovina.name -> 'Bosnia Herzegovina'

'''
class Country:
    def __init__(self, name, population):
        self.name = name
        self.population = population

    def add(self, other_country):
        combined_name = f"{self.name} і {other_country.name}"
        combined_population = self.population + other_country.population
        combined_country = Country(combined_name, combined_population)
        return combined_country

bosnia = Country('Боснія', 10000000)
herzegovina = Country('Герцоговина', 5000000)

bosnia_herzegovina = bosnia.add(herzegovina)

print(f'Населення: {bosnia_herzegovina.population}, Назва: {bosnia_herzegovina.name}')




