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
    source.onerror = function(event) {
        console.log("Seems like I got an error! Oh no!");
        this.close();
        console.log("Opening new stream...");
        source = listentoStream(group);
    }

    console.log("EventSource initiated for group " + group + ".");
    return source;
}