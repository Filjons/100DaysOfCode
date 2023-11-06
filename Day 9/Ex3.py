#Nesting a dict in a dict

travel_log = {
    "France": {"cities_visited":["Paris", "Lille", "Dijon"], "total_visits": 12}, 
    "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 2}
}

#Nesting dicts in a list

travel_log = [
    {
        "country": "France",
        "cities": ["Paris", "Lille", "Dijon"],
        "visits": 12
    },
    {
        "country": "Germany",
        "cities": ["Berlin", "Hamburg", "Stuttgart"],
        "visits": 5
    }
]

def add_new_country(country, visits, list_of_cities):
    travel_log.append(
        {
            "country": country,
            "cities": list_of_cities,
            "visits": visits
        }
        )

new_country = input("What country?\n")
new_visits = int(input("How many visits?\n"))
new_list_of_cities = eval(input("Please list the cities:\n"))

add_new_country(country=new_country, visits=new_visits, list_of_cities=new_list_of_cities)

print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times!")
print(f"My favourite city was {travel_log[2]['cities'][0]}.")
