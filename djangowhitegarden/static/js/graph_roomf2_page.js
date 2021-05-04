$(document).ready(function () {
    var endpoint = "/api/floor2";
    var kwh = [];
    var amp = [];

    $.ajax({
    method: "GET",
    url: endpoint,
    success: function (data) {
        labels = data.labels;
        kwh = data.kwhfloor2; //from apifloor2.py
        amp = data.ampfloor2; //from apifloor2.py


        am4core.ready(function() {

            // Themes begin
            am4core.useTheme(am4themes_animated);
            // Themes end
            
            // Create chart instance
            var chart = am4core.create("chartroomf2", am4charts.XYChart3D);
            
            // Add data
            chart.data = [{
              "roomf2": "Walkway",
              "valroomf2": kwh[1]
            }, {
              "roomf2": "201",
              "valroomf2": kwh[2]
            }, {
              "roomf2": "202",
              "valroomf2": kwh[3]
            }, {
              "roomf2": "203",
              "valroomf2": kwh[4]
            }, {
              "roomf2": "204",
              "valroomf2": kwh[5]
            }, {
              "roomf2": "205",
              "valroomf2": kwh[6]
            }, {
              "roomf2": "206",
              "valroomf2": kwh[7]
            }, {
              "roomf2": "207",
              "valroomf2": kwh[8]
            }, {
              "roomf2": "208",
              "valroomf2": kwh[9]
            }, {
              "roomf2": "209",
              "valroomf2": kwh[10]
            }, {
              "roomf2": "210",
              "valroomf2": kwh[11]
            }, {
              "roomf2": "211",
              "valroomf2": kwh[12]
            },{
              "roomf2": "212",
              "valroomf2": kwh[13]  
            },{
                "roomf2": "213",
                "valroomf2": kwh[14]  
            },{
                "roomf2": "214",
                "valroomf2": kwh[15]  
            },{
                "roomf2": "215",
                "valroomf2": kwh[16]  
            },{
                "roomf2": "216",
                "valroomf2": kwh[17]  
            },{
                "roomf2": "217",
                "valroomf2": kwh[18]  
            }];
            
            // Create axes
            let categoryAxis = chart.xAxes.push(new am4charts.CategoryAxis());
            categoryAxis.dataFields.category = "roomf2";
            categoryAxis.renderer.labels.template.rotation = 270;
            categoryAxis.renderer.labels.template.hideOversized = false;
            categoryAxis.renderer.minGridDistance = 20;
            categoryAxis.renderer.labels.template.horizontalCenter = "right";
            categoryAxis.renderer.labels.template.verticalCenter = "middle";
            categoryAxis.tooltip.label.rotation = 270;
            categoryAxis.tooltip.label.horizontalCenter = "right";
            categoryAxis.tooltip.label.verticalCenter = "middle";
            
            let valueAxis = chart.yAxes.push(new am4charts.ValueAxis());
            valueAxis.title.text = "พลังงาน (หน่วย)";
            valueAxis.title.fontWeight = "bold";
            
            // Create series
            var series = chart.series.push(new am4charts.ColumnSeries3D());
            series.dataFields.valueY = "valroomf2";
            series.dataFields.categoryX = "roomf2";
            series.name = "valroomf2";
            series.tooltipText = "{categoryX}: [bold]{valueY}[/]";
            series.columns.template.fillOpacity = .8;
            
            var columnTemplate = series.columns.template;
            columnTemplate.strokeWidth = 2;
            columnTemplate.strokeOpacity = 1;
            columnTemplate.stroke = am4core.color("#FFFFFF");
            
            columnTemplate.adapter.add("fill", function(fill, target) {
              return chart.colors.getIndex(target.dataItem.index);
            })
            
            columnTemplate.adapter.add("stroke", function(stroke, target) {
              return chart.colors.getIndex(target.dataItem.index);
            })
            
            chart.cursor = new am4charts.XYCursor();
            chart.cursor.lineX.strokeOpacity = 0;
            chart.cursor.lineY.strokeOpacity = 0;
            
            }); // end am4core.ready()
        
    },
    error: function (error_data) {
        console.log("error");
        console.log(error_data);
    },
    });

  });
  