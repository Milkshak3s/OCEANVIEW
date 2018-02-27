
function addtag(input){
    // First of all, make sure it's legit.
    if(input.value==""){
        return;
    }
    //Building a new tag element, from the ground up.

    // We'll need a delete button.
    var tagx = document.createElement('a');
    tagx.classList.add("tagX");
    tagx.href="#"; // so mousover looks clickable
    tagx.appendChild(document.createTextNode("x"));
    tagx.addEventListener("click", function(){
        tagx.parentNode.parentNode.removeChild(tagx.parentNode);
    }, false);

    // We'll need a name span for the tag
    var tagnamespan = document.createElement('span');
    tagnamespan.appendChild(document.createTextNode(input.value));

    // Create the parent tag element
    var newtag = document.createElement('div');
    newtag.classList.add("tag");
    newtag.style.backgroundColor = stringToColour(input.value);
    newtag.appendChild(tagnamespan);
    newtag.appendChild(tagx);

    // Attach our new tag to the tags container.
    input.previousElementSibling.appendChild(newtag);

    // wipe the input box to reset it.
    input.value = "";
}
var stringToColour = function(str) {
    var hash = 0;
    for (var i = 0; i < str.length; i++) {
        hash = str.charCodeAt(i) + ((hash << 5) - hash);
    }
    var colour = '#';
    for (var i = 0; i < 3; i++) {
        var value = (hash >> (i * 8)) & 0xFF;
        colour += ('00' + value.toString(16)).substr(-2);
    }
    // If the color is too dark, invert it. ? todo.
    return colour;
}
