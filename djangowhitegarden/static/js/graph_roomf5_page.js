$(document).ready(function () {
    var endpoint = "/api/floor5";
    var kwh = [];
    var amp = [];

    $.ajax({
    method: "GET",
    url: endpoint,
    success: function (data) {
        labels = data.labels;
        kwh = data.kwhfloor5; //from apifloor2.py
        amp = data.ampfloor5; //from apifloor2.py


        am4core.ready(function() {

            // Themes begin
            am4core.useTheme(am4themes_animated);
            // Themes end
            
            // Create chart instance
            var chart = am4core.create("chartroomf5", am4charts.XYChart3D);
            
            // Add data
            chart.data = [{
              "roomf5": "Walkway",
              "valroomf5": kwh[1]
            }, {
              "roomf5": "501",
              "valroomf5": kwh[2]
            }, {
              "roomf5": "502",
              "valroomf5": kwh[3]
            }, {
              "roomf5": "503",
              "valroomf5": kwh[4]
            }, {
              "roomf5": "504",
              "valroomf5": kwh[5]
            }, {
              "roomf5": "505",
              "valroomf5": kwh[6]
            }, {
              "roomf5": "506",
              "valroomf5": kwh[7]
            }, {
              "roomf5": "507",
              "valroomf5": kwh[8]
            }, {
              "roomf5": "508",
              "valroomf5": kwh[9]
            }, {
              "roomf5": "509",
              "valroomf5": kwh[10]
            }, {
              "roomf5": "510",
              "valroomf5": kwh[11]
            }, {
              "roomf5": "511",
              "valroomf5": kwh[12]
            },{
              "roomf5": "512",
              "valroomf5": kwh[13]  
            },{
                "roomf5": "513",
                "valroomf5": kwh[14]  
            },{
                "roomf5": "514",
                "valroomf5": kwh[15]  
            },{
                "roomf5": "515",
                "valroomf5": kwh[16]  
            },{
                "roomf5": "516",
                "valroomf5": kwh[17]  
            },{
                "roomf5": "517",
                "valroomf5": kwh[18]  
            }];
            
            // Create axes
            let categoryAxis = chart.xAxes.push(new am4charts.CategoryAxis());
            categoryAxis.dataFields.category = "roomf5";
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
            series.dataFields.valueY = "valroomf5";
            series.dataFields.categoryX = "roomf5";
            series.name = "valroomf5";
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
  