function validateInput() {
    var name, groupName, text;

    /* Get the value of the input field with id="name" */
    name = document.getElementById("name").value;
    groupName = document.getElementById("groupName").value;

    /*  */
    if (name == "" || groupName == "")
        text = "Name or groupname cannot be empty!";
    else
        text = "Hello " + name + "! Your group is: " + groupName;
    document.getElementById("nameView").innerHTML = text;

    // let API know you wanna join game

    viewer.updateUsers();
}

function cross(name) {
    var button = document.getElementById("button_{{name}}");
    
    button.firstChild.data = "Poffertjes";
}