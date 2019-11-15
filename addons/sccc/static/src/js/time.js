odoo.define('sccc.time', function(require) {
    "use strict";

    var basic_fields = require('web.basic_fields');
    var field_registry = require('web.field_registry');
    var datepicker = require('web.datepicker');
    
    function tConvert (time) {
        // Check correct time format and split into components
        time = time.toString().match (/^([01]\d|2[0-3])(:)([0-5]\d)(:[0-5]\d)?$/) || [time];
    
        if (time.length > 1) { // If time format correct
            time = time.slice (1);  // Remove full string match value
            time[5] = +time[0] < 12 ? 'AM' : 'PM'; // Set AM/PM
            time[0] = +time[0] % 12 || 12; // Adjust hours
        }
        return time.join (''); // return adjusted time or original string
    }

    var FieldTime = basic_fields.InputField.extend({
        className: 'o_field_time',
        tagName: 'span',
        supportedFieldTypes: ['time'],

        _renderEdit: function () {
            this._super.apply(this, arguments);
            if(this.recordData[this.name] === false){
                this.$el.prop({value:"00:00"});
            }
            this.$el.prop({type:"time"});
        },

        _setValue: function (value, options) {
            if (this.field.trim) {
                value = tConvert(value.trim());
            }
            return this._super(value, options);
        },
    });
    field_registry.add('time', FieldTime);

});