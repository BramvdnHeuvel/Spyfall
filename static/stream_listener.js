function listentoStream(group, callback) {
    var source = new EventSource('/stream/' + group);
    source.onmessage = function(event) {
        /* Assign all the stuff that needs to be done in case new data is received. */
        console.log("Detected new stream income! " + event.data);
        callback(event.data);
    }

    console.log("EventSource initiated for group " + group + ".");
    return source;
}