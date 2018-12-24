function getData(link, callback) {
    fetch(link).then((response) => (response.json()))
        .then((data) => {callback(data)});
}

function listentoStream(group, callback) {
    var source = new EventSource('/stream/' + group);
    source.onmessage = function(event) {
        console.log("Detected stream msg: " + event.data);
        callback(event.data);
    }

    console.log("EventSource initiated for group " + group + ".");
    return source;
}