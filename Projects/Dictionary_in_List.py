import json

def add_new_country(country, visits, list_of_cities,total_countries):
    new_country = {}
    new_country['country'] = country
    new_country['visits'] = visits
    new_country['list_of_cities'] = list_of_cities
    total_countries.append(new_country)

add_new_city = True
total_countries_count = 0
total_countries = []
while add_new_city:
    country = input("Enter country name: ")
    visits = int(input("How many times you visited?: "))
    cities = input("Enter the list of cities (separated by commas): ")
    total_countries_count += 1
    list_of_cities = [i.strip() for i in cities.split(",")]
    add_new_country(country, visits, list_of_cities, total_countries)

    choice = input("Have you visited other countries? Yes/No: ").lower()
    if choice == 'no':
        add_new_city = False
        print(f"###################### Total countries you have visited: ######################\n{total_countries_count}")
        print("###################### Summarizing your country visits: ######################\n")
        print(json.dumps(total_countries, indent=2))
        print("->->->->-> Keep Travelling! ->->->->->")


