$(document).ready(function() {

    var leads_fialed_screeing = [];
    var leads_by_ienroll = [];
    var leads_enrolled_successfully = [];
    $.getJSON("/get-chartdata/", function(data) {
        // retreive leads_fialed_screeing
        $.each(data['leads_fialed_screeing'], function(index, value) {
            leads_fialed_screeing.push({
                x: new Date(value['date']),
                y: value['value']
            });
        });
        // retreive leads_fialed_screeing
        $.each(data['leads_by_ienroll'], function(index, value) {
            leads_by_ienroll.push({
                x: new Date(value['date']),
                y: value['value']
            });
        });
        // retreive leads_enrolled_successfully
        $.each(data['leads_enrolled_successfully'], function(index, value) {
            leads_enrolled_successfully.push({
                x: new Date(value['date']),
                y: value['value']
            });
        });
        var chart = new CanvasJS.Chart("chartContainer", {
            title: {
                text: "Chart"
            },
            animationEnabled: true,
            axisX: {
                title: 'date',
                // intervalType: "month",

            },
            axisY: {
                title: "Number of Leads",
            },
            legend: {
                verticalAlign: "bottom",
                horizontalAlign: "center"
            },
            legend: {
                cursor: "pointer",
                itemclick: function(e) {
                    //console.log("legend click: " + e.dataPointIndex);
                    //console.log(e);
                    if (typeof(e.dataSeries.visible) === "undefined" || e.dataSeries.visible) {
                        e.dataSeries.visible = false;
                    } else {
                        e.dataSeries.visible = true;
                    }

                    e.chart.render();
                }
            },
            data: [{
                name: "leads sent by iEnroll;",
                showInLegend: true,
                legendMarkerType: "square",
                type: "line",
                dataPoints: leads_by_ienroll,

            }, {
                name: " of leads failed screening",
                showInLegend: true,
                legendMarkerType: "square",
                type: "line",
                dataPoints: leads_fialed_screeing,

            }, {
                name: " leads successfully enrolled",
                showInLegend: true,
                legendMarkerType: "square",
                type: "line",
                dataPoints: leads_enrolled_successfully,

            }]
        });

        chart.render();



    });

});