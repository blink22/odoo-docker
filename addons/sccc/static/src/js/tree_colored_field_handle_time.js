odoo.define('sccc', function (require) {
    'use strict';

    var ListRenderer = require('web.ListRenderer');
    var pyUtils = require("web.py_utils");
    
    function tConvert(time) {
        // Check correct time format and split into components
        time = time.toString().match (/^([01]\d|2[0-3])(:)([0-5]\d)(:[0-5]\d)?$/) || [time];
      
        if (time.length > 1) { // If time format correct
            time = time.slice (1);  // Remove full string match value
            time[5] = +time[0] < 12 ? ' AM' : ' PM'; // Set AM/PM
            time[0] = +time[0] % 12 || 12; // Adjust hours
        }
        return time.join (''); // return adjusted time or original string
    }

    ListRenderer.include({
        /**
         * Look up for a `color_field` parameter in tree `colors` attribute
         *
         * @override
         */
        _renderBody: function () {
            if (this.arch.attrs.colors) {
                var colorAttr = this.arch.attrs.colors.split(';');
                if (colorAttr.length > 0) {
                    var colorField = colorAttr[0].split(':')[1].trim();
                    // validate the presence of that field in tree view
                    if (this.state.data.length && colorField in this.state.data[0].data) {
                        this.colorField = colorField;
                    } else {
                        // console.warn(
                        //     "No field named '" + colorField + "' present in view."
                        // );
                    }
                }
            }
            return this._super();
        },
        /**
         * Colorize a cell during it's render
         *
         * @override
         */
        _renderBodyCell: function (record, node, colIndex, options) {
            var $td = this._super.apply(this, arguments);
            var ctx = this.getEvalContext(record);
            this.applyColorize($td, record, node, ctx);
            if(node.attrs.name === 'to_time' || node.attrs.name === 'from_time') {
                this.handleTime($td, record, node, ctx)
            }
            return $td;
        },
        handleTime: function ($td, record, node, ctx) {
          if($td[0].innerHTML.includes("PM") || $td[0].innerHTML.includes("pm") ||
             $td[0].innerHTML.includes("AM") || $td[0].innerHTML.includes("am")) {
              // do nothing
          } else {
              $td[0].innerHTML = tConvert($td[0].innerHTML)
          }
        },
        /**
         * Colorize the current cell depending on expressions provided.
         *
         * @param {Query Node} $td a <td> tag inside a table representing a list view
         * @param {Object} node an XML node (must be a <field>)
         */
        applyColorize: function ($td, record, node, ctx) {
            // safely resolve value of `color_field` given in <tree>
            var treeColor = record.data[this.colorField];
            if (treeColor) {
                $td.css('color', treeColor);
            }
            // apply <field>'s own `options`
            if (!node.attrs.options) { return; }
            if (node.tag !== 'field') { return; }
            var nodeOptions = node.attrs.options;
            if (!_.isObject(nodeOptions)) {
                nodeOptions = pyUtils.py_eval(nodeOptions);
            }
            this.applyColorizeHelper($td, nodeOptions, node, 'fg_color', 'color', ctx);
            this.applyColorizeHelper($td, nodeOptions, node, 'bg_color', 'background-color', ctx);
        },
        /**
         * @param {Object} nodeOptions a mapping of nodeOptions parameters to the color itself
         * @param {Object} node an XML node (must be a <field>)
         * @param {string} nodeAttribute an attribute of a node to apply a style onto
         * @param {string} cssAttribute a real CSS-compatible attribute
         */
        applyColorizeHelper: function ($td, nodeOptions, node, nodeAttribute, cssAttribute, ctx) {
            if (nodeOptions[nodeAttribute]) {
                var colors = _(nodeOptions[nodeAttribute].split(';'))
                    .chain()
                    .map(this.pairColors)
                    .value()
                    .filter(function CheckUndefined(value, index, ar) {
                        return value !== undefined;
                    });
                for (var i=0, len=colors.length; i<len; ++i) {
                    var pair = colors[i],
                        color = pair[0],
                        expression = pair[1];
                    if (py.evaluate(expression, ctx).toJSON()) {
                        $td.css(cssAttribute, color);
                    }
                }
            }
        },

        /**
         * Parse `<color>: <field> <operator> <value>` forms to
         * evaluable expressions
         *
         * @param {string} pairColor `color: expression` pair
         */
        pairColors: function (pairColor) {
            if (pairColor !== "") {
                var pairList = pairColor.split(':'),
                    color = pairList[0],
                    // if one passes a bare color instead of an expression,
                    // then we consider that color is to be shown in any case
                    expression = pairList[1]? pairList[1] : 'True';
                return [color, py.parse(py.tokenize(expression)), expression];
            }
            return undefined;
        },
        /**
         * Construct domain evaluation context, mostly by passing
         * record's fields's values to local scope.
         *
         * @param {Object} record a record to build a context from
         */
        getEvalContext: function (record) {
            var ctx = _.extend(
                {},
                record.data,
                pyUtils.context()
            );
            for (var key in ctx) {
                var value = ctx[key];
                if (ctx[key] instanceof moment) {
                    // date/datetime fields are represented w/ Moment objects
                    // docs: https://momentjs.com/
                    ctx[key] = value.format('YYYY-MM-DD hh:mm:ss');
                }
            }
            return ctx;
        }
    });
});
