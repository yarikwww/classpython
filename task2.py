'''
2. Реалізуйте попередній спосіб за допомогою чарівного методу
bosnia = Country('Bosnia', 10_000_000)
herzegovina = Country('Herzegovina', 5_000_000)

bosnia_herzegovina = bosnia + herzegovina
bosnia_herzegovina.population -> 15_000_000
bosnia_herzegovina.name -> 'Bosnia Herzegovina'
'''
class Country:
    def __init__(self, name, population):
        self.name = name
        self.population = population

    def __add__(self, other_country):
        combined_name = f"{self.name} {other_country.name}"
        combined_population = self.population + other_country.population
        return Country(combined_name, combined_population)


bosnia = Country('Bosnia', 10_000_000)
herzegovina = Country('Herzegovina', 5_000_000)


bosnia_herzegovina = bosnia + herzegovina


print(f"Population of {bosnia_herzegovina.name}: {bosnia_herzegovina.population}")

