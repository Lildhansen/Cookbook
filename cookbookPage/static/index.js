//tag stuff

function updateTagSearch(searchBarValue)
{
    searchBarValue = searchBarValue.toLowerCase() //search should be case insensitive
    allTagElements = document.getElementsByClassName("tagElement")
    allTagElementsCopy = [...allTagElements]
    for (const tag of allTagElementsCopy)
    {
        tag.style.display = "block"
        tagName = tag.querySelector('button[name="tagInTagsMenu"]').value.toLowerCase()
        if (!tagName.includes(searchBarValue))
            tag.style.display = "none"
    }
}

function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
  }

function sendDeleteTagHTTP(tagValue)
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


function sendDeleteRecipeHTTP(idOfRecipeToDelete)
{
    var csrftoken = getCookie('csrftoken')
    fetch('deleteRecipe', {
    method: 'POST',
    action: 'deleteRecipe',
    headers: {
        "X-Requested-With": "XMLHttpRequest",
        "X-CSRFToken": csrftoken,
    },
    body: idOfRecipeToDelete
})
}


function removeTag(removeSymbolDivForTagToRemove)
{
    tagElement = removeSymbolDivForTagToRemove.parentElement
    tagValue = tagElement.querySelector('button[name="tagInTagsMenu"]').value
    console.log(tagValue)
    if (window.confirm(`Are you sure you want to delete the, ${tagValue}, tag`))
    {
        return sendDeleteTagHTTP(tagValue)      
    }
}

function removeRecipe(recipeId, recipeElement)
{
    console.log(recipeId)
    recipeTitleAndTags = recipeElement.querySelector('.titleAndTagsForRecipeDiv')
    recipeTitleElement = recipeTitleAndTags.querySelector('.titleForRecipe')
    recipeTitle = recipeTitleElement.innerHTML
    console.log(recipeTitle)
    if (window.confirm(`Are you sure you want to delete the recipe, ${recipeTitle}`))
    {
        return sendDeleteRecipeHTTP(recipeId)      
    }
}

// should probably be named santize tag input or smth
function verifyTag(newTagNameForm)
{
    invalidChars = ['/', '%', '&', '<', '>', '[', ']', '{', '}', ']', '\\','\'','"']
    allTagElements = document.getElementsByClassName("tagElement")
    allTagElementsCopy = [...allTagElements]
    newTagName = newTagNameForm.querySelector('input[name="addTagInput"]').value
    newTagName = newTagName.trim()
    if (newTagName == "")
    {
        alert("tag cannot be empty")
        newTagNameForm.querySelector('input[name="addTagInput"]').value = ""
        return false
    }

    else if (newTagName.length > 25)
    {
        alert("tag cannot be longer than 25 characters")
        newTagNameForm.querySelector('input[name="addTagInput"]').value = ""
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


//recipe stuff

function updateSearch(searchBar)
{
    searchBarValue = searchBar.value.toLowerCase() //search should be case insensitive
    typeOfSearch = document.getElementById("typeOfSearchSelection")
    allRecipeElements = document.getElementsByClassName("recipeDiv")
    if (typeOfSearch.value == "recipes")
    {
        for (const recipeElement of allRecipeElements)
        {
            recipeElement.style.display = "grid"
            //if recipe is being edited they should always be shown
            if (recipeIsBeingEdited(recipeElement))
            {
                recipeElement.style.display = "grid"
            }

            else 
            {
                console.log("recipe: ",recipeElement.getElementsByClassName("titleForRecipe")[0])
                recipeName = recipeElement.getElementsByClassName("titleForRecipe")[0].innerHTML.toLowerCase()
                if (!recipeName.includes(searchBarValue))
                    recipeElement.style.display = "none"

            }
        }

    }

    else if (typeOfSearch.value == "tags")
    {
        for (const recipeElement of allRecipeElements)
        {
            recipeElement.style.display = "grid"
            //if recipe is being edited they should always be shown
            if (recipeIsBeingEdited(recipeElement))
            {
                recipeElement.style.display = "grid"
                continue
            }
            tagNames = recipeElement.getElementsByClassName("tagsForRecipeText")[0].innerHTML.toLowerCase()
            if (!tagNames.includes(searchBarValue))
                recipeElement.style.display = "none"
        }
    }

    // allTagElementsCopy = [...allTagElements]
    // for (const tag of allTagElementsCopy)
    // {
    //     tag.style.display = "inline-block"
    //     tagName = tag.querySelector('button[name="tagInTagsMenu"]').value
    //     if (!tagName.includes(searchBarValue))
    //         tag.style.display = "none"
    // }
}

//handles updating the suggested search results
function changeTypeOfSearchSelection(typeOfSearchSelection)
{
    searchBar = document.getElementById("searchBarForRecipeOrTag")
    if (typeOfSearchSelection.value == "tags")
    {
        searchBar.placeholder = "tags..."
        allTagElements = document.getElementsByClassName("tagElement")
        for (tagElement of allTagElements)
        {
            tagValue = tagElement.getElementsByClassName("tagInTagsMenu")[0].value.toLowerCase()
            option = document.createElement('option');
            option.value = tagValue;
            
            searchBarSuggestions = document.getElementById("searchBarSuggestions")
            searchBarSuggestions.appendChild(option)   
        }
    }

    else if (typeOfSearchSelection.value == "recipes")
    {
        searchBar.placeholder = "recipe..."
        searchBarSuggestions = document.getElementById("searchBarSuggestions")
        while (searchBarSuggestions.firstChild) 
        {
            searchBarSuggestions.removeChild(searchBarSuggestions.lastChild);
        }   
    }
    
}


function recipeIsBeingEdited(recipeDiv)
{
    return recipeDiv.getElementsByClassName("titleAndTagsForRecipeDiv").length == 0
}

function editRecipe(recipe)
{
    console.log(recipe.value)
}