
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
    newtag.style.backgroundColor = hashToColor(hashString(input.value));
    newtag.appendChild(tagnamespan);
    newtag.appendChild(tagx);

    // Attach our new tag to the tags container.
    input.previousElementSibling.appendChild(newtag);

    // wipe the input box to reset it.
    input.value = "";
}
var hashString = function(str){
    var hash = 0;
    for (var i = 0; i < str.length; i++) {
        hash = str.charCodeAt(i) + ((hash << 5) - hash);
    }
    return hash;
}
var hashToColor = function(seed){
    // Gen random from 0 to 5.999
    var rand_1 = Math.abs((Math.sin(seed++) * 104743)) % 6;
    var rand_2 = Math.abs((Math.sin(seed++) * 104743)) % 6;
    var rand_3 = Math.abs((Math.sin(seed++) * 104743)) % 6;

    // floor to 0->5, multiply to 0->15
    var red   = Math.floor(rand_1)*3;
    var green = Math.floor(rand_2)*3;
    var blue  = Math.floor(rand_3)*3;

    console.log("color: "+red+", "+green+", "+blue);

    // Make sure it's a bright, tasty color.
    var L = calcLuminosity(red*17, green*17, blue*17);
    if(L <= 0.179){ // luminosity too low, invert.
        console.log("invert the above.")
        red = 15-red;
        green = 15-green;
        blue = 15-blue;
    }

    return "#"+red.toString(16)+""+green.toString(16)+""+blue.toString(16);
}
var calcLuminosity = function(red, green, blue){
    // https://stackoverflow.com/questions/3942878/how-to-decide-font-color-in-white-or-black-depending-on-background-color
    console.log("calculating: "+red+", "+green+", "+blue);
    var rgb = [red, green, blue];
    for(var i=0; i<3; i++){
        var c = rgb[i];
        c = c / 255;
        c = c <= 0.03928 ? c/12.92 : Math.pow((c+0.055)/1.055, 2.4);
        rgb[i] = c;
    }
    return 0.2126 * rgb[0] + 0.7152 * rgb[1] + 0.0722 * rgb[2];
}
