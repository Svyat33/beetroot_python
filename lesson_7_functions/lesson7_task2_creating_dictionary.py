# Task 2
# Creating a dictionary.
# Create a function called make_country, which takes in a country’s name and
# capital as parameters. Then create a dictionary from those parameters, with ‘name’
# and ‘capital’ as keys. Make the function print out the values of the dictionary to
# make sure that it works as intended.


def make_country(country_name, country_capital):
    country_name = country_name.strip().lower().capitalize()
    country_capital = country_capital.strip().lower().capitalize()
    if country_name and country_capital:
        countries = {
            'name': country_name,
            'capital': country_capital,
        }
        print(countries)
    else:
        print('You must enter name of Country and name of it\'s capital!')


if __name__ == "__main__":
    name = 'ukRainE'
    capital = 'kyiV'
    make_country(name, capital)
