var viewer = new Vue({
    el: "#frames",
    data: {
        frame: 'menuView',
        group: undefined,
        myName: '{{name}}',
        players: [
            {name: 'Bram'},
            {name: 'Sam'},
            {name: 'Mark'}
        ]
    },
    methods: {
        updateUsers: function(group) {
            fetch('/api/v1/' + group + '/players')
                .then((response) => {return response.json()})
                .then((data) => {
                    this.players = data.map((user) => ({name: user}));
                });
        },

        leaveGroup: function(event) {
            console.log("Leaving group!");
            fetch('/api/v1/' + this.group + '/leave/' + this.myName)
                .then((response) => {return response.json()})
                .then((data) => {
                    // Leave empty if nothing useful is returned.
                })
            this.group = undefined;
            this.frame = 'menuView';
        },

        // Used to toggle style on clicked user lists
        clickUser: function(event) {
            var button = event.target;
            var user = this.players.find(x => x.name === button.innerText);

            while (button.type != 'submit') {
                button = button.parentElement;
            }

            user.crossed = !user.crossed;
            if (user.crossed) {
                button.style.backgroundColor = "rgba(255, 0, 0, 0.3)";
            } else {
                button.style.backgroundColor = "green";
            }
        },

        createGame: function(event) {
            console.log("HELLAOOA");
            var text, name = document.getElementById("nameCreate").value;
            console.log(name);
            if (name === "") {
                text = "Name field is empty!";
            } else {
                fetch('/api/v1/creategroup/' + name)
                    .then((response) => response.json())
                    .then((data) => {
                        if (data.successful) {
                            text = "Your group name is: " + data.groupname;
                        } else {
                            text = "Something went work";
                        }
                    });
            }
        
            document.getElementById("createView").innerText = text;
        }
    }
});

function changeView(newView) {
    console.log("Changing view to " + newView + '...');
    viewer.frame = newView
}