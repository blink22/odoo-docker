odoo.define('sccc.CalendarController', function (require) {
    "use strict";

    var CalendarController = require('web.CalendarController');
    var rpc = require('web.rpc');
    CalendarController.include({
        _onOpenCreate: function (event) {
            // if (event.data.resource && event.data.resource.id) {
            //     var value = event.data.resource.id;
            //     if (this.model.fields[this.model.fieldColumn].type === 'many2one')
            //         value = parseInt(value);
            //     this.context['default_'+ this.model.fieldColumn] = value;
            // }
            // else
            //     this.context['default_'+ this.model.fieldColumn] = false;
            
            if (event.data.resource && event.data.resource.id) {
                var self = this
                rpc.query({
                    model: 'sccc.room',
                    method: 'get_room',
                    args: [{
                        'id': event.data.resource.id,
                    }]
                }).then(function(result) {
                    self.context['default_location'] = result.location_id
                    self.context['default_room'] = result.id
                })
            }

            if(event.data.date) {
                this.context['default_date'] = event.data.date
                this.context['default_start_time'] = event.data.start_time
                this.context['default_end_time'] = event.data.end_time
            }
            return this._super.apply(this, arguments);
        },
    });
});
