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
        updateUsers: function() {
            var self = this;
            getData('/api/v1/' + self.group + '/players', function(data) {
                self.players = data.map((user) => ({name: user}));
            });
        },

        leaveGroup: function(event) {
            console.log("Leaving group!");
            var self = this;
            getData('/api/v1/' + self.group + '/leave/' + self.myName, function(data) {
                // Leave empty, 'cause nothing useful is returned.
            })
            this.group = undefined;
            this.frame = 'menuView';
        },

        joinGroup: function(event){
            this.frame="gameMenu";
            var self = this;
            getData('/api/v1/' + self.group + '/join/' + self.myName, function(data) {
                console.log(data);
                self.players = data.players;
            });
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