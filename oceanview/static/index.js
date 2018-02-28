/*
    OCEANVIEW index.js
    To load IPS and Tags.
    To Add/Remove Tags.
    author: Ethan Witherington etw9578@rit.edu
*/

window.onload = function() {
    // Get the IPs and Tags, and built the rest of the page.
    request("ip", 0, "broadcast", function(json){
        for(host of json){
            document.getElementById("targetbox").appendChild(buildhost(host));
        }
    })
}

// Make a request, call the supplied callback with the response.
function request(type, since, addr, callback){
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            callback(JSON.parse(this.responseText));
        }
    };
    xhttp.open("POST", "/data", true);
    xhttp.setRequestHeader("Content-Type", "application/json");
    xhttp.send(JSON.stringify({type: type, since: since, addr: addr}));
}

// Given an IP and that IP's tags, build an element for the page.
var buildhost = function(host){
    /*
    What we get:

    {
        "ip": 127.127.127.127
        "tags": [
            "testing",
            "test"
        ]
    }

    What we need to build:

    <div class="target altitude1">
        <!-- IP / A -->
        <a href="overview/127.127.127.127">127.127.127.127</a>
        <!-- Container for the Tags -->
        <div class="tags">
        </div>
        <!-- Input to add more tags -->
        <input type="text" onKeyDown="if(event.keyCode==13) addTagFromInput(this);">
    </div>

    */

    // Build Outer Div
    var outerdiv = document.createElement('div');
    outerdiv.classList.add("target");
    outerdiv.classList.add("altitude1");

    // Build host link
    var hostlink = document.createElement('a');
    hostlink.href = "overview/"+host.ip;
    hostlink.appendChild(document.createTextNode(host.ip));
    outerdiv.appendChild(hostlink);

    // Build tagbox
    var tagbox = document.createElement('div');
    tagbox.classList.add("tags");
    outerdiv.appendChild(tagbox);

    // Put new tags into the tagbox
    for(tag of host.tags){
        addTag(tag, tagbox);
    }

    // Build input bar for adding more tags
    var inbar = document.createElement('input');
    inbar.type = 'text';
    inbar.onkeydown = function(e){
        if(event.keyCode==13) addTagFromInput(this);
    }
    outerdiv.appendChild(inbar);

    return outerdiv;
}

// inputs call this when the user adds a tag.
var addTagFromInput = function(input){
    // First of all, make sure it's legit.
    if(input.value==""){
        return;
    }
    addTag(input.value, input.previousElementSibling);
    input.value = "";
}

/*
Build a tag, and put it in an element.
text: The text of the tag to add.
target: The element to put the tag inside of.
*/
var addTag = function(text, target){
    // Build the parent tag element
    var newtag = document.createElement('div');
    newtag.classList.add("tag");
    newtag.style.backgroundColor = hashToColor(hashString(text));

    // Build the span with the tag text
    var tagnamespan = document.createElement('span');
    tagnamespan.appendChild(document.createTextNode(text));
    newtag.appendChild(tagnamespan);

    // We'll need a delete button.
    var tagx = document.createElement('a');
    tagx.classList.add("tagX");
    tagx.href="#"; // so mousover looks clickable
    tagx.appendChild(document.createTextNode("x"));
    tagx.addEventListener("click", function(){
        tagx.parentNode.parentNode.removeChild(tagx.parentNode);
    }, false);
    newtag.appendChild(tagx);

    // Attach our new tag to the target container.
    target.appendChild(newtag);
}

// ~~~~~~~~~~~~~~~~~~~~  Tag Color Generation. ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
// I spent too much time on this, but it's awesome.

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
