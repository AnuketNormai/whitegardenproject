$(document).ready(function () {
    var endpoint = "/api/airf1";
    var kwh = [];
    var amp = [];
    var labels = [];
    var dates = [];
    var time = [];
  
    const $kwhair1 = $("#kwhair1");
    const $kwhair2 = $("#kwhair2");
    const $kwhair3 = $("#kwhair3");
    const $kwhair4 = $("#kwhair4");
    const $kwhair5 = $("#kwhair5");
    const $kwhair6 = $("#kwhair6");
    const $kwhair7 = $("#kwhair7");
    const $kwhair8 = $("#kwhair8");
    const $kwhair9 = $("#kwhair9");
    const $kwhair10 = $("#kwhair10");
    const $kwhair11 = $("#kwhair11");
    const $kwhair12 = $("#kwhair12");

    const $ampair1 = $("#ampair1");
    const $ampair2 = $("#ampair2");
    const $ampair3 = $("#ampair3");
    const $ampair4 = $("#ampair4");
    const $ampair5 = $("#ampair5");
    const $ampair6 = $("#ampair6");
    const $ampair7 = $("#ampair7");
    const $ampair8 = $("#ampair8");
    const $ampair9 = $("#ampair9");
    const $ampair10 = $("#ampair10");
    const $ampair11 = $("#ampair11");
    const $ampair12 = $("#ampair12");

    var setpointAmpAir1 = 0.5;
    var setpointAmpAir2 = 0.5;
    var setpointAmpAir3 = 0.5;
    var setpointAmpAir4 = 0.5;
    var setpointAmpAir5 = 0.5;
    var setpointAmpAir6 = 0.5;
    var setpointAmpAir7 = 0.5;
    var setpointAmpAir8 = 0.5;
    var setpointAmpAir9 = 0.5;
    var setpointAmpAir10 = 0.5;
    var setpointAmpAir11 = 0.5;
    var setpointAmpAir12 = 0.5;

    var powerOn_color = "#00FF00"; //set color for device has normal #10B310
    var powerOff_color = "#A9A9A9"; //set color for device has normal #10B310

      $.ajax({
        method: "GET",
        url: endpoint,
        success: function (data) {
          labels = data.labels;
          kwh = data.kwhair; //from apiair.py
          amp = data.ampair; //from apiair.py
          date = data.date; //from apiair.py
          time = data.time; //from apiair.py

          $("#graphdate").text(date);
          $("#graphtime").text(time);

          am4core.ready(function() {

            // Themes begin
            am4core.useTheme(am4themes_animated);
            // Themes end
            
            // Create chart instance
            var chart = am4core.create("chartAir", am4charts.XYChart3D);
            
            // Add data
            chart.data = [{
              "air": "แอร์ตัวที่ 1",
              "valair": kwh[0]
            }, {
              "air": "แอร์ตัวที่ 2",
              "valair": kwh[1]
            }, {
              "air": "แอร์ตัวที่ 3",
              "valair": kwh[2]
            }, {
              "air": "แอร์ตัวที่ 4",
              "valair": kwh[3]
            }, {
              "air": "แอร์ตัวที่ 5",
              "valair": kwh[4]
            }, {
              "air": "แอร์ตัวที่ 6",
              "valair": kwh[5]
            }, {
              "air": "แอร์ตัวที่ 7",
              "valair": kwh[6]
            }, {
              "air": "แอร์ตัวที่ 8",
              "valair": kwh[7]
            }, {
              "air": "แอร์ตัวที่ 9",
              "valair": kwh[8]
            }, {
              "air": "แอร์ตัวที่ 10",
              "valair": kwh[9]
            }, {
              "air": "แอร์ตัวที่ 11",
              "valair": kwh[10]
            }, {
              "air": "แอร์ตัวที่ 12",
              "valair": kwh[11]
            }];
            
            // Create axes
            let categoryAxis = chart.xAxes.push(new am4charts.CategoryAxis());
            categoryAxis.dataFields.category = "air";
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
            series.dataFields.valueY = "valair";
            series.dataFields.categoryX = "air";
            series.name = "valair";
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
  