var viewer = new Vue({
    el: "#frames",
    data: {
        frame: 'menuView',
        group: undefined,
        myName: 'Mr. Spy',
        role: 'Unknown',
        players: [
            'Bram',
            'Mark',
            'Sam'
        ],
        locations: [
            'Airplane',
            'Bank',
            'Bram\'s imaginary girlfriend\'s house'
        ],
        stream: undefined
    },
    methods: {
        updateUsers: function() {
            var self = this;
            getData('/api/v1/' + self.group + '/players', function(data) {
                self.players = data.players;
            });
        },

        leaveGroup: function(event) {
            var self = this;
            getData('/api/v1/' + self.group + '/leave/' + self.myName, function(data) {
                // Leave empty, 'cause nothing useful is returned.
            })
            this.group = undefined;
            this.frame = 'menuView';
            this.stream.close();
        },

        joinGroup: function(event){
            this.frame="gameMenu";
            this.stream = listentoStream(this.group);
            var self = this;
            getData('/api/v1/' + self.group + '/join/' + self.myName, function(data) {
                self.players = data.players;
            });
        },

        startGame: function() {
            var self = this;

            if (self.frame === 'gameMenu') {
                self.frame = 'gameView';

                getData('/api/v1/' + self.group + '/start', function(data) {
                    self.players = data.players;
                    self.locations = data.locations;
                });

                getData('/api/v1/' + self.group + '/myrole/' + self.myName, function(data) {
                    self.role = data.role;
                })
            }
        },

        /* TODO: Refactor */
        createGroup: function(event) {

            getData('/api/v1/creategroup/' + this.myName, function(data) {
                if (data.successful) {            
                    viewer.group = data.groupname
                    viewer.stream = listentoStream(viewer.group);

                    viewer.frame = "gameMenu"
                    viewer.updateUsers();
                } else {
                    console.log("Something went WORK");
                }
            });
        }
    }
});

function changeView(newView) {
    console.log("Changing view to " + newView + '...');
    viewer.frame = newView
}