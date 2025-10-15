spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    return [food["name"] for food in spicy_foods]

def get_spiciest_foods(spicy_foods):
     return [food for food in spicy_foods if food["heat_level"] > 5]

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {'🌶' * food['heat_level']}")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food

def print_spiciest_foods(spicy_foods):
    spiciest = get_spiciest_foods(spicy_foods)
    print_spicy_foods(spiciest)

def get_average_heat_level(spicy_foods):
    total_heat = sum(food["heat_level"] for food in spicy_foods)
    return total_heat

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(new_food)
    return spicy_foods


spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]


def get_names(spicy_foods):
    """Return a list of food names."""
    return [food["name"] for food in spicy_foods]


def get_spiciest_foods(spicy_foods):
    """Return foods with heat level greater than 5."""
    return [food for food in spicy_foods if food["heat_level"] > 5]


def print_spicy_foods(spicy_foods):
    """Print each food in the format: Name (Cuisine) | Heat Level: 🌶 repeated."""
    for food in spicy_foods:
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {'🌶' * food['heat_level']}")


def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    """Return the food that matches the given cuisine."""
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food


def print_spiciest_foods(spicy_foods):
    """Print only the foods with heat level > 5."""
    spiciest = get_spiciest_foods(spicy_foods)
    print_spicy_foods(spiciest)


def get_average_heat_level(spicy_foods):
    """Return the average heat level as an integer."""
    total_heat = sum(food["heat_level"] for food in spicy_foods)
    return total_heat // len(spicy_foods)


def create_spicy_food(spicy_foods, new_food):
    """Add a new spicy food to the list and return the updated list."""
    spicy_foods.append(new_food)
    return spicy_foods


# Example test outputs
if __name__ == "__main__":
    print("get_names:", get_names(spicy_foods))
    print("get_spiciest_foods:", get_spiciest_foods(spicy_foods))
    print("print_spicy_foods:")
    print_spicy_foods(spicy_foods)
    print("get_spicy_food_by_cuisine (Thai):", get_spicy_food_by_cuisine(spicy_foods, "Thai"))
    print("print_spiciest_foods:")
    print_spiciest_foods(spicy_foods)
    print("average_heat_level:", average_heat_level(spicy_foods))
    print("create_spicy_food:", create_spicy_food(spicy_foods, {
        'name': 'Griot',
        'cuisine': 'Haitian',
        'heat_level': 10
    }))

