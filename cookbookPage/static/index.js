function updateSearch(searchBarValue)
{
    allTagElements = document.getElementsByClassName("tagElement")
    allTagElementsCopy = [...allTagElements]
    for (const tag of allTagElementsCopy)
    {
        tag.style.display = "inline-block"
        tagName = tag.querySelector('button[name="tagInTagsMenu"]').value
        if (!tagName.includes(searchBarValue))
            tag.style.display = "none"
    }
}

function test(tagValue)
{
    var csrftoken = getCookie('csrftoken')
    fetch('deleteTag', {
    method: 'POST',
    action: 'deleteTag',
    headers: {
        "X-Requested-With": "XMLHttpRequest",
        "X-CSRFToken": csrftoken,
    },
    body: tagValue
})
}

function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
  }



//return window.confirm('Are you sure you want to delete this tag? ')
function removeTag(removeSymbolDivForTagToRemove)
{
    tagElement = removeSymbolDivForTagToRemove.parentElement
    tagValue = tagElement.querySelector('button[name="tagInTagsMenu"]').value
    console.log(tagValue)
    if (window.confirm(`Are you sure you want to delete the, ${tagValue}, tag`))
    {
        return test(tagValue)      
    }
}

function verifyTagIsUnique(newTagNameForm)
{
    invalidChars = ['/', '%', '&', '<', '>', '[', ']', '{', '}', ']', '\\','\'','"']
    allTagElements = document.getElementsByClassName("tagElement")
    allTagElementsCopy = [...allTagElements]
    newTagName = newTagNameForm.querySelector('input[name="addTagInput"]').value
    newTagName = newTagName.trim()
    if (newTagName == "")
    {
        alert("tag cannot be empty")
        return false
    }
    else if (stringContainsInvalidCharacters(newTagName,invalidChars))
    {
        alert(`The characters, ${invalidChars.join(", ")}, are not allowed in a tag`)
        return false
    }
    for (const tag of allTagElementsCopy) //checks uniqueness
    {
        tagName = tag.querySelector('button[name="tagInTagsMenu"]').value
        if (newTagName.toLowerCase() == tagName.toLowerCase())
        {
            alert(`A tag with the name, ${tagName} already exists.`)
            return false
        }
    }
    return true
}

function stringContainsInvalidCharacters(myString,invalidChars)
{
    match = false
    invalidChars.forEach(char => {
        console.log(char)
        console.log(myString.includes(char))
        console.log(`is ${char} in ${myString}`)
        if (myString.includes(char))
        {
            match = true
            return
        }
    });
    return match
}