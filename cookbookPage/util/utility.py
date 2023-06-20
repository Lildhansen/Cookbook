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
