odoo.define('sccc.field_utils', function (require) {
    "use strict";

    var fu = require('web.field_utils');
    var core = require('web.core');
    var dom = require('web.dom');
    var session = require('web.session');
    var time = require('web.time');
    var utils = require('web.utils');

    var _t = core._t;

    function formatTime(value, field, options) {
        if (value === false) {
            return "";
        }
        var timePattern = time.getLangTimeFormat();
        return moment('1970-01-01 ' + value).format(timePattern);
        // return value;
    }

    function tConvert (time) {
        // Check correct time format and split into components
        time = time.toString().match (/^([01]\d|2[0-3])(:)([0-5]\d)(:[0-5]\d)?$/) || [time];
    
        if (time.length > 1) { // If time format correct
            time = time.slice (1);  // Remove full string match value
            time[5] = +time[0] < 12 ? ' AM' : ' PM'; // Set AM/PM
            time[0] = +time[0] % 12 || 12; // Adjust hours
        }
        return time.join (''); // return adjusted time or original string
    }

    function parseTime(value, field, options) {
        if (!value) {
            return false;
        }
        // var timePattern = time.getLangTimeFormat();
        // return moment('1970-01-01 ' + value).format(timePattern);
        return tConvert(value);
    }

    fu.format.__defineGetter__('time', function() {
        return formatTime;
    });

    fu.parse.__defineGetter__('time', function() {
        return parseTime;
    });

});