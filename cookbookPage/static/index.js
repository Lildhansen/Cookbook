function updateSearch(searchBarValue)
{
    allTagElements = document.getElementsByClassName("tagElement")
    allTagElementsCopy = [...allTagElements]
    for (const tag of allTagElementsCopy)
    {
        tag.style.display = "block"
        tagName = tag.querySelector('button[name="tagInTagsMenu"]').value
        console.log(typeof tagName)
        if (!tagName.includes(searchBarValue))
            tag.style.display = "none"
    }
}

function removeTag(removeSymbolForTagToRemove)
{
    tagElement = removeSymbolDivForTagToRemove.parentElement
    tagValue = tagElement.querySelector('button[name="tagInTagsMenu"]').value
    if (window.confirm(`Are you sure you want to delete the, ${tagValue}, tag`))
    tagElement
    //jeg tror ikke det skal gøres i JS, da den bare skal slette elementet i databasen.
    // skal dog finde en måde at lave window.confirm gennem django - måske bare at den først tjekker på JS og derefter sender en post til django
}

function verifyTagIsUnique(newTagNameForm)
{
    allTagElements = document.getElementsByClassName("tagElement")
    allTagElementsCopy = [...allTagElements]
    newTagName = newTagNameForm.querySelector('input[name="addTagInput"]').value
    for (const tag of allTagElementsCopy)
    {
        tagName = tag.querySelector('button[name="tagInTagsMenu"]').value
        if (newTagName == tagName)
        {
            alert(`A tag with the name, ${tagName} already exists.`)
            return false
        }
    }
    return true
}