function getData(link, callback) {
    fetch(link).then((response) => (response.json()))
        .then((data) => callback(data))
}