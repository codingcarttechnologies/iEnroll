window.onload = function () {
    var chart_data = [];
    $.getJSON("/get-chartdata/", function(data) {
        $.each(data['chartData'], function(index, value) {
            chart_data.push({
                label: value['category'],
                y: value['count']
            });
        });
  
    var chart = new CanvasJS.Chart("chartContainer",
    {
      title:{
        text: " Category vs Leads"    
      },
      animationEnabled: true,
      axisY: {
        title: "Number of leads"
      },
      axisX: {
        title: "Category"
      },
      theme: "theme2",
      dataPointMaxWidth: 30,
      data: [

          {        
            type: "column",  
            dataPoints : chart_data
           }   
        ]
    });

    chart.render();

     });
  }    
     