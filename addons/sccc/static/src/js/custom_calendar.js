odoo.define('sccc.sccc_calendar_view', function (require) {
  "use strict";
  
  // var CalendarView = require('web.CalendarView');
  // CalendarView.include({
  //   init: function (viewInfo, params) {
  //     this._super.apply(this, arguments);
  //     if (this.controllerParams.modelName == 'sccc.calendar') {
           
  //     }
  //   }
  // });
  // return CalendarView;
  
  var CalendarModel = require('web.CalendarModel');

  CalendarModel.include({
    _getFullCalendarOptions: function () {
      var res = this._super.apply(this, arguments);
      return _.extend(res, {
        minTime: '08:00:00',
        maxTime: '21:00:00'
      });
    },
  });

  var CalendarView = require('web.CalendarView');

  CalendarView.include({
    jsLibs : ['/sccc/static/src/js/fullcalendar.js'],
  });
});