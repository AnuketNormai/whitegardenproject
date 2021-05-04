$(document).ready(function () {
    var endpoint = "/api/floor3";
    var kwh = [];
    var amp = [];

    $.ajax({
    method: "GET",
    url: endpoint,
    success: function (data) {
        labels = data.labels;
        kwh = data.kwhfloor3; //from apifloor2.py
        amp = data.ampfloor3; //from apifloor2.py


        am4core.ready(function() {

            // Themes begin
            am4core.useTheme(am4themes_animated);
            // Themes end
            
            // Create chart instance
            var chart = am4core.create("chartroomf3", am4charts.XYChart3D);
            
            // Add data
            chart.data = [{
              "roomf3": "Walkway",
              "valroomf3": kwh[1]
            }, {
              "roomf3": "301",
              "valroomf3": kwh[2]
            }, {
              "roomf3": "302",
              "valroomf3": kwh[3]
            }, {
              "roomf3": "303",
              "valroomf3": kwh[4]
            }, {
              "roomf3": "304",
              "valroomf3": kwh[5]
            }, {
              "roomf3": "305",
              "valroomf3": kwh[6]
            }, {
              "roomf3": "306",
              "valroomf3": kwh[7]
            }, {
              "roomf3": "307",
              "valroomf3": kwh[8]
            }, {
              "roomf3": "308",
              "valroomf3": kwh[9]
            }, {
              "roomf3": "309",
              "valroomf3": kwh[10]
            }, {
              "roomf3": "310",
              "valroomf3": kwh[11]
            }, {
              "roomf3": "311",
              "valroomf3": kwh[12]
            },{
              "roomf3": "312",
              "valroomf3": kwh[13]  
            },{
                "roomf3": "313",
                "valroomf3": kwh[14]  
            },{
                "roomf3": "314",
                "valroomf3": kwh[15]  
            },{
                "roomf3": "315",
                "valroomf3": kwh[16]  
            },{
                "roomf3": "316",
                "valroomf3": kwh[17]  
            },{
                "roomf3": "317",
                "valroomf3": kwh[18]  
            }];
            
            // Create axes
            let categoryAxis = chart.xAxes.push(new am4charts.CategoryAxis());
            categoryAxis.dataFields.category = "roomf3";
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
            series.dataFields.valueY = "valroomf3";
            series.dataFields.categoryX = "roomf3";
            series.name = "valroomf3";
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
  