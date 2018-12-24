function getData(link, callback) {
    fetch(link).then((response) => (response.json()))
        .then((data) => {callback(data)});
}

function listentoStream(group) {
    var source = new EventSource('/stream/' + group);
    source.onmessage = function(event) {
        console.log("Detected stream msg: " + event.data);
        var message = event.data;

        if (message === "USER UPDATE") {
            viewer.updateUsers();
        } else if (message === "GAME START") {
            viewer.startGame();
        }
    }

    console.log("EventSource initiated for group " + group + ".");
    return source;
}