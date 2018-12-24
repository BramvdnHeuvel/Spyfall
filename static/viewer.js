var viewer = new Vue({
    el: "#frames",
    data: {
        frame: 'menuView',
        group: '',
        myName: 'Mr. Spy',
        role: 'Unknown',
        error: '',
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
    computed: {
        validJoinSyntax: function() {
            return (this.myName != '' && this.group.length === 6)
        },
        validCreateSyntax: function() {
            return (this.myName != '')
        }
    },
    methods: {
        updateUsers: function() {
            var self = this;
            if (self.group !== '') {
                getData('/api/v1/' + self.group + '/players', function(data) {
                    self.players = data.players;
                });
            }
        },

        leaveGroup: function(event) {
            var self = this;
            getData('/api/v1/' + self.group + '/leave/' + self.myName, function(data) {
                // Leave empty, 'cause nothing useful is returned.
            })
            this.group = '';
            this.frame = 'menuView';
            this.stream.close();
        },

        joinGroup: function(event){ 
            var self = this;

            if (self.group === '') {
                self.error = "Please fill in a group code.";
            } else if (self.myName === '') {
                self.error = "Please choose a name.";
            } else {
                getData('/api/v1/' + self.group + '/join/' + self.myName, function(data) {
                    self.players = data.players;
                    self.error = data.error;
    
                    if (data.successful) {
                        self.stream = listentoStream(self.group);
                        self.frame = "gameMenu";
                    }
                });
            }
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