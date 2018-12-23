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
            getData('/api/v1/' + this.group + '/players', function(data) {
                self.players = data.map((user) => ({name: user}));
            });
        },

        leaveGroup: function(event) {
            console.log("Leaving group!");
            getData('/api/v1/' + this.group + '/leave/' + this.myName, function(data) {
                // Leave empty, 'cause nothing useful is returned.
            })
            this.group = undefined;
            this.frame = 'menuView';
        },

        joinGroup: function(event){
            frame="gameMenu";
            var self = this;
            getData('/api/v1/' + self.group + '/join/' + self.myName, function(data) {
                console.log(data);
                self.players = data.players;
            });

        }
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
        }
    }
});

function changeView(newView) {
    console.log("Changing view to " + newView + '...');
    viewer.frame = newView
}