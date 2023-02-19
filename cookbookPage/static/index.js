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
    $.ajax({
        url: "/deleteTag",
        type: "POST",
        data: tagValue,
        headers: {
            "X-Requested-With": "XMLHttpRequest",
            "X-CSRFToken": getCookie("csrftoken"),
          },
        success: function (data) {
            console.log(data);
        },
        error: (error) => {
            console.log(error);
          }
       })
}

//return window.confirm('Are you sure you want to delete this tag? ')
function removeTag(removeSymbolDivForTagToRemove)
{
    tagElement = removeSymbolDivForTagToRemove.parentElement
    tagValue = tagElement.querySelector('button[name="tagInTagsMenu"]').value
    console.log(tagValue)
    if (window.confirm(`Are you sure you want to delete the, ${tagValue}, tag`))
    {
        test(tagValue)      
        }
       //window.location.href = "/deleteTag"
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