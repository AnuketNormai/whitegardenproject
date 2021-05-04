$(document).ready(function () {
    var endpoint = "/api/floor4";
    var kwh = [];
    var amp = [];

    $.ajax({
    method: "GET",
    url: endpoint,
    success: function (data) {
        labels = data.labels;
        kwh = data.kwhfloor4; //from apifloor2.py
        amp = data.ampfloor4; //from apifloor2.py


        am4core.ready(function() {

            // Themes begin
            am4core.useTheme(am4themes_animated);
            // Themes end
            
            // Create chart instance
            var chart = am4core.create("chartroomf4", am4charts.XYChart3D);
            
            // Add data
            chart.data = [{
              "roomf4": "Walkway",
              "valroomf4": kwh[1]
            }, {
              "roomf4": "401",
              "valroomf4": kwh[2]
            }, {
              "roomf4": "402",
              "valroomf4": kwh[3]
            }, {
              "roomf4": "403",
              "valroomf4": kwh[4]
            }, {
              "roomf4": "404",
              "valroomf4": kwh[5]
            }, {
              "roomf4": "405",
              "valroomf4": kwh[6]
            }, {
              "roomf4": "406",
              "valroomf4": kwh[7]
            }, {
              "roomf4": "407",
              "valroomf4": kwh[8]
            }, {
              "roomf4": "408",
              "valroomf4": kwh[9]
            }, {
              "roomf4": "409",
              "valroomf4": kwh[10]
            }, {
              "roomf4": "410",
              "valroomf4": kwh[11]
            }, {
              "roomf4": "411",
              "valroomf4": kwh[12]
            },{
              "roomf4": "412",
              "valroomf4": kwh[13]  
            },{
                "roomf4": "413",
                "valroomf4": kwh[14]  
            },{
                "roomf4": "414",
                "valroomf4": kwh[15]  
            },{
                "roomf4": "415",
                "valroomf4": kwh[16]  
            },{
                "roomf4": "416",
                "valroomf4": kwh[17]  
            },{
                "roomf4": "417",
                "valroomf4": kwh[18]  
            }];
            
            // Create axes
            let categoryAxis = chart.xAxes.push(new am4charts.CategoryAxis());
            categoryAxis.dataFields.category = "roomf4";
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
            series.dataFields.valueY = "valroomf4";
            series.dataFields.categoryX = "roomf4";
            series.name = "valroomf4";
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
  