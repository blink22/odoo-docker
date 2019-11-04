odoo.define('web_view_calendar_column.CalendarView', function (require) {
    "use strict";

    var CalendarView = require('web.CalendarView');

    CalendarView.include({
        jsLibs: [
            '/web/static/lib/fullcalendar/js/fullcalendar.js',
            '/web_view_calendar_column/static/lib/scheduler.min.js'
        ],
        cssLibs: [
            '/web/static/lib/fullcalendar/css/fullcalendar.css',
            '/web_view_calendar_column/static/lib/scheduler.min.css'
        ],
        init: function (viewInfo, params) {
            this._super.apply(this, arguments);
            var fieldNames = this.loadParams.fieldNames;
            this.loadParams.fieldColumn = 'room';
            this.loadParams.fieldNames = _.uniq(fieldNames);
            this.loadParams.forceColumns =  params.context.force_columns;
        },
    });
});
