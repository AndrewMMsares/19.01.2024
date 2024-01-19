class City:
    def __init__(self, city_name, region_name, country_name, population, postal_code, phone_code):
        self.__city_name = city_name
        self.__region_name = region_name
        self.__country_name = country_name
        self.__population = population
        self.__postal_code = postal_code
        self.__phone_code = phone_code

    def get_city_name(self):
        return self.__city_name

    def get_region_name(self):
        return self.__region_name

    def get_country_name(self):
        return self.__country_name

    def get_population(self):
        return self.__population

    def get_postal_code(self):
        return self.__postal_code

    def get_phone_code(self):
        return self.__phone_code


class Country:
    def __init__(self, country_name, continent_name, population, phone_code, capital_name, cities):
        self.__country_name = country_name
        self.__continent_name = continent_name
        self.__population = population
        self.__phone_code = phone_code
        self.__capital_name = capital_name
        self.__cities = cities

    def get_country_name(self):
        return self.__country_name

    def get_continent_name(self):
        return self.__continent_name

    def get_population(self):
        return self.__population

    def get_phone_code(self):
        return self.__phone_code

    def get_capital_name(self):
        return self.__capital_name

    def get_cities(self):
        return self.__cities

city1 = City("Kyiv", "Kyiv Oblast", "Ukraine", 2800000, "02000", "+380")
city2 = City("Lviv", "Lviv Oblast", "Ukraine", 720000, "79000", "+380")

cities_of_ukraine = [city1, city2]

country = Country("Ukraine", "Europe", 42000000, "+380", "Kyiv", cities_of_ukraine)

print("Country:", country.get_country_name())
print("Continent:", country.get_continent_name())
print("Population:", country.get_population())
print("Phone Code:", country.get_phone_code())
print("Capital:", country.get_capital_name())

print("\nCities:")
for city in country.get_cities():
    print("- " + city.get_city_name())