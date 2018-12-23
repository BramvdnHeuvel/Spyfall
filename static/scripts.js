function validateInput() {
    var name, groupName, text, delayHref, correct = 0;

    /* Get the value of the input field with id="name" */
    name = document.getElementById("name").value;
    groupName = document.getElementById("groupName").value;

    /*  */
    if (name == "" || groupName == "")
        text = "Name or groupname cannot be empty!";
    else
        hrefCall();
    document.getElementById("nameView").innerHTML = text;

}

function hrefCall() {
    document.getElementById('goSpyfall').click();
}

function cross(name) {
    var button = document.getElementById("button_{{name}}");
    
    button.firstChild.data = "Poffertjes";
}