function listentoStream(group) {
    var source = new EventSource('stream/' + group);
    source.onmessage = function(event) {
        /* Assign all the stuff that needs to be done in case new data is received. */
        console.log("Detected new stream income! " + event.data);
        console.log(event);
        console.log(event.data);
        changeView('gameMenu');
    }

    console.log("EventSource initiated for group " + group + ".");
    return source;
}