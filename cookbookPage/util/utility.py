def findTagByTagName(tagName, tags):
    for tag in tags:
        if tag.name == tagName:
            return tag
    return None
