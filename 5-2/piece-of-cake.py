# program receives a dictionary of ingredients and their quantities, a list of optional ingredients which will not be
# considered and a dictionary of prices for each ingredient program returns the price of the recipe



def get_recipe_price(dictionary, optionals=[], **prices):
    price = 0
    for ingredient in dictionary:
        if ingredient in optionals:
            continue
        price += dictionary[ingredient] * prices[ingredient] / 100
    return price


print(get_recipe_price({'chocolate': 18, 'milk': 8}, chocolate=200, milk=100))
print(get_recipe_price({'chocolate': 18, 'milk': 8}, optionals=['milk'], chocolate=300))
