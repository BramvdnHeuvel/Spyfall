Vue.component('checkbutton', {
    props: ['title'],
    data: function() {
        return {
            crossed: false
        }
    },
    template: `
        <button id='node_button'
            v-on:click='crossed=!(crossed)'
            v-if="crossed" style="background-color:rgba(255, 0, 0, 0.3);">
                <del>{{ title }}</del>
        </button>
        <button id='node_button'
            v-on:click='crossed=!(crossed)'
            v-else style="background-color:green;">
                {{ title }}
        </button>`
});
Vue.component('potentialplace', {
    props: ['place'],
    data: function() {
        return {
            visible: true
        }
    },
    methods: {
        deleteLocation: function(event) {
            console.log(this.place);
            this.visible = false;

            getData('/api/v1/' + viewer.group + '/del_loc/' + this.place, function(data) {
                // leave empty if only useless data is sent
            });
        }
    },
    template: `
        <div class="selection-box" v-if="visible">
            <div class="location-box">{{ place }}</div>
            <button
                style="float:right;border-radius:13px;width:93px;margin-right:5px;"
                class="button button-white"
                v-on:click="deleteLocation"
            >X</button>
        </div>`
});