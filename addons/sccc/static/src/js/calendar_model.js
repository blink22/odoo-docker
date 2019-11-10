odoo.define('sccc.CalendarModel', function (require) {
    "use strict";

    var CalendarModel = require('web.CalendarModel');
    var session = require('web.session');
    var core = require('web.core');
    var fieldUtils = require('web.field_utils');
    var _t = core._t;
    CalendarModel.include({
        load: function (params) {
            this.fieldColumn = params.fieldColumn;
            this.forceColumns = params.forceColumns;
            return this._super.apply(this, arguments);
        },
        _loadCalendar: function () {
            var self = this;
            return this._super.apply(this, arguments).then(function () {
                self._compute_columns(self.data, self.data.data);
            });
        },
        _compute_columns: function (element, events) {
            if (this.fieldColumn && this.forceColumns) {
                this.data.columns = this.forceColumns;
            }
            else if (this.fieldColumn) {
                var fieldName = this.fieldColumn;
                var columns = {}
                var elements = events;
                _.each(events, function (event) {
                    var value = event.record[fieldName];
                    var key = _.isArray(value) ? value[0] : value;
                    columns[key] = _.isArray(value) ? value[1] : value;
                });
                this.data.columns = columns;
            }
        },
        _loadFilter: function (filter) {
            if (!filter.write_model) {
                if(filter.fieldName === 'location') {
                    return this._rpc({
                        model: 'sccc.location',
                        method: 'search_read',
                        domain: [],
                        fields: ['name'],
                    }).then(function (res) {
                        var records = _.map(res, function (record) {
                            var value = record.id;
                            var f = _.find(filter.filters, function (f) {return f.value === value;});
                            return {
                                display: true,
                                value: record.id,
                                label: record.name,
                                active: !f || f.active,
                                avatar_model: 'sccc.location',
                                color_index: record.id
                            };
                        });
                        records.sort(function (f1,f2) {
                            return _.string.naturalCmp(f2.label, f1.label);
                        });
                        filter.filters = records;
                    });
                } else {
                    return Promise.resolve();
                }
            }
    
            var field = this.fields[filter.fieldName];
            return this._rpc({
                    model: filter.write_model,
                    method: 'search_read',
                    domain: [["user_id", "=", session.uid]],
                    fields: [filter.write_field],
                })
                .then(function (res) {
                    var records = _.map(res, function (record) {
                        var _value = record[filter.write_field];
                        var value = _.isArray(_value) ? _value[0] : _value;
                        var f = _.find(filter.filters, function (f) {return f.value === value;});
                        var formater = fieldUtils.format[_.contains(['many2many', 'one2many'], field.type) ? 'many2one' : field.type];
                        return {
                            'id': record.id,
                            'value': value,
                            'label': formater(_value, field),
                            'active': !f || f.active,
                        };
                    });
                    records.sort(function (f1,f2) {
                        return _.string.naturalCmp(f2.label, f1.label);
                    });
    
                    // add my profile
                    if (field.relation === 'res.partner' || field.relation === 'res.users') {
                        var value = field.relation === 'res.partner' ? session.partner_id : session.uid;
                        var me = _.find(records, function (record) {
                            return record.value === value;
                        });
                        if (me) {
                            records.splice(records.indexOf(me), 1);
                        } else {
                            var f = _.find(filter.filters, function (f) {return f.value === value;});
                            me = {
                                'value': value,
                                'label': session.name + _t(" [Me]"),
                                'active': !f || f.active,
                            };
                        }
                        records.unshift(me);
                    }
                    // add all selection
                    records.push({
                        'value': 'all',
                        'label': field.relation === 'res.partner' || field.relation === 'res.users' ? _t("Everybody's calendars") : _t("Everything"),
                        'active': filter.all,
                    });
    
                    filter.filters = records;
                });
        },
        _recordToCalendarEvent: function (evt) {
            var result = this._super.apply(this, arguments);
            var value = evt[this.fieldColumn];
            result.resourceId = _.isArray(value) ? value[0] : value;
            return result;
        },
        _getFullCalendarOptions: function () {
            var result = this._super.apply(this, arguments);
            if (this.fieldColumn)
                result.resources = [];
            
            return _.extend(result, {
                minTime: '08:00:00',
                maxTime: '21:00:00'
            });
		    // return result;
		},
		calendarEventToRecord: function (event) {
		    var result = this._super.apply(this, arguments);
		    if (event.resourceId)
		        result[this.fieldColumn] = event.resourceId;
		    return result;
		},
    });
});
