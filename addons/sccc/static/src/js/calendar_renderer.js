odoo.define('sccc.CalendarRenderer', function (require) {
    "use strict";

    var CalendarRenderer = require('web.CalendarRenderer');
    var core = require('web.core');
    var qweb = core.qweb;
    var _t = core._t;
    var rpc = require('web.rpc');
    var count = 1;
    CalendarRenderer.include({
        getColor: function (key) {
            if(key === 'Hold') return '#EDB183';
            if(key === 'Match') return '#A4D0D8';
            if(key === 'Confirmed') return '#B5D99C';
            if(key === 'Cancelled') return '';

            if (!key) {
                return;
            }
            if (this.color_map[key]) {
                return this.color_map[key];
            }
            // check if the key is a css color
            if (typeof key === 'string' && key.match(/^((#[A-F0-9]{3})|(#[A-F0-9]{6})|((hsl|rgb)a?\(\s*(?:(\s*\d{1,3}%?\s*),?){3}(\s*,[0-9.]{1,4})?\))|)$/i)) {
                return this.color_map[key] = key;
            }
            var index = (((_.keys(this.color_map).length + 1) * 5) % 24) + 1;
            this.color_map[key] = index;
            return index;
        },
        _initCalendar: function () {
            var self = this;

            this.$calendar = this.$(".o_calendar_widget");

            // This seems like a workaround but apparently passing the locale
            // in the options is not enough. We should initialize it beforehand
            var locale = moment.locale();
            $.fullCalendar.locale(locale);

            //Documentation here : http://arshaw.com/fullcalendar/docs/
            var fc_options = $.extend({}, this.state.fc_options, {
                eventDrop: function (event) {
                    self.trigger_up('dropRecord', event);
                },
                eventResize: function (event) {
                    self.trigger_up('updateRecord', event);
                },
                eventClick: function (event) {
                    self.trigger_up('openEvent', event);
                    self.$calendar.fullCalendar('unselect');
                },
                select: function (target_date, end_date, event, _js_event, resource) {
                    var data = {'start': target_date, 'end': end_date, 'resource': resource};
                    
                    if (self.state.context.default_name) {
                        data.title = self.state.context.default_name;
                    }

                    data.date = target_date.format('YYYY-MM-DD');
                    data.start_time = target_date.format('hh:mm');
                    data.end_time = end_date.format('hh:mm');
                    self.trigger_up('openCreate', data);
                    self.$calendar.fullCalendar('unselect');
                },
                eventRender: function (event, element) {
                    var $render = $(self._eventRender(event));
                    event.title = $render.find('.o_field_type_char:first').text();
                    element.find('.fc-content').html($render.html());
                    element.addClass($render.attr('class'));
                    var display_hour = '';
                    if (!event.allDay) {
                        var start = event.r_start || event.start;
                        var end = event.r_end || event.end;
                        var timeFormat = _t.database.parameters.time_format.search("%H") != -1 ? 'HH:mm': 'h:mma';
                        display_hour = start.format(timeFormat) + ' - ' + end.format(timeFormat);
                        if (display_hour === '00:00 - 00:00') {
                            display_hour = _t('All day');
                        }
                    }
                    element.find('.fc-content .fc-time').text(display_hour);
                    element.find('.fc-content').css({'text-align': 'justify', '-webkit-text-emphasis': 'filled'})
                    if(event.record && event.record.status) {
                        element.find('.fc-bg').css({background: self.getColor(event.record.status[1])});
                    }
                },
                // Dirty hack to ensure a correct first render
                eventAfterAllRender: function () {                    
                    $(window).trigger('resize');
                    if(count === 1) {
                        var htmlColleaction = document.getElementsByClassName('o_calendar_button_today btn btn-primary');
                        if(htmlColleaction.length > 0) {
                            htmlColleaction[0].click();
                        }
                        count = 0;
                    }
                    self.state.filters.location.filters.forEach(filter => {
                        filter.display = true;
                    });
                    self.state.filters.status.filters.forEach(filter => {
                        if(filter.label !== 'Cancelled') { 
                            filter.display = true;
                        }
                    });
                },
                viewRender: function (view) {
                    // compute mode from view.name which is either 'month', 'agendaWeek' or 'agendaDay'
                    var mode = view.name === 'month' ? 'month' : (view.name === 'agendaWeek' ? 'week' : 'day');
                    // compute title: in week mode, display the week number
                    var title = mode === 'week' ? view.intervalStart.week() : view.title;
                },
                //eventResourceEditable: true, // except for between resources
                height: 'parent',
                unselectAuto: false,
                locale: locale, // reset locale when fullcalendar has already been instanciated before now
            });
            this.$calendar.fullCalendar(fc_options);
        },
        _renderEvents: function () {
            var self = this;
            this.$calendar.fullCalendar('removeEvents');
            if (this.state.columns) {
                rpc.query({
                    model: 'sccc.room',
                    method: 'get_rooms'
                }).then(function(result) {
                    self.$calendar.fullCalendar('getResources').forEach(element => {
                        self.$calendar.fullCalendar('removeResource', element);
                    });
                    _.each(Object.entries(result[0]), function (column) {
                        var location_id = result[1][column[0]];
                        var location = self.state.filters.location.filters.find((item) => item.value === location_id);
                        if(location && location.active) {
                            self.$calendar.fullCalendar('addResource', {
                                id: column[0],
                                title: column[1]
                            });
                        }
                    });
                });
            }
            this.$calendar.fullCalendar('addEventSource', this.state.data);
        },
    });
});
