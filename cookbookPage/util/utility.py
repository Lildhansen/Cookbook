noImageStockPhoto = "https://st4.depositphotos.com/14953852/24787/v/600/depositphotos_247872612-stock-illustration-no-image-available-icon-vector.jpg"

def findTagByTagName(tagName, tags):
    for tag in tags:
        if tag.name == tagName:
            return tag
    return None

def findRecipeByRecipeName(recipeName, recipes):
    for recipe in recipes:
        if recipe.name == recipeName:
            return recipe
    return None
