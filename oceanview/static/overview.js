function putText(texts){
    console.log('got texts: '+texts)
    var container = document.getElementById('texts');
    for(text in texts){
        console.log("Adding "+texts[text]);
        //Create a DOM element
        var div = document.createElement('div');
        div.innerHTML = texts[text];
        //Give it the classes needed
        div.classList.add("text");
        div.classList.add("altitude1");
        //insert it
        container.insertBefore(div, container.firstChild.nextElementSibling.nextElementSibling); // Do not ask why.
    }
}

function putShot(shots){

}

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

window.onload = function() {
    // Get data where the loading things are.
    request("text", 10243, addr, function(json){
        var element = document.getElementById("LoadingText");
        element.parentNode.removeChild(element);
        putText(json)
    })
}
