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


    setInterval(function () {
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


          $kwhair1.text(kwh[0].toFixed(2) + " หน่วย");
          $kwhair2.text(kwh[1].toFixed(2) + " หน่วย");
          $kwhair3.text(kwh[2].toFixed(2) + " หน่วย");
          $kwhair4.text(kwh[3].toFixed(2) + " หน่วย");
          $kwhair5.text(kwh[4].toFixed(2) + " หน่วย");
          $kwhair6.text(kwh[5].toFixed(2) + " หน่วย");
          $kwhair7.text(kwh[6].toFixed(2) + " หน่วย");
          $kwhair8.text(kwh[7].toFixed(2) + " หน่วย");
          $kwhair9.text(kwh[8].toFixed(2) + " หน่วย");
          $kwhair10.text(kwh[9].toFixed(2) + " หน่วย");
          $kwhair11.text(kwh[10].toFixed(2) + " หน่วย");
          $kwhair12.text(kwh[11].toFixed(2) + " หน่วย");
          
          // on-off Air 1
          if (amp[0] <= setpointAmpAir1) {
            $("#bgair1").addClass("bg-light");
          }
          if (amp[0] > setpointAmpAir1) {
            $("#bgair1").removeClass("bg-light");
            $("#bgair1").addClass("bg-warning");  
          }
          // on-off Air 2
          if (amp[1] <= setpointAmpAir2) {
            $("#bgair2").addClass("bg-light");
          }
          if (amp[1] > setpointAmpAir2) {
            $("#bgair2").removeClass("bg-light");
            $("#bgair2").addClass("bg-warning");  
          }
          // on-off Air 3
          if (amp[2] <= setpointAmpAir3) {
            $("#bgair3").addClass("bg-light");
          }
          if (amp[2] > setpointAmpAir3) {
            $("#bgair3").removeClass("bg-light");
            $("#bgair3").addClass("bg-warning");  
          }
          // on-off Air 4
          if (amp[3] <= setpointAmpAir4) {
            $("#bgair4").addClass("bg-light");
          }
          if (amp[3] > setpointAmpAir4) {
            $("#bgair4").removeClass("bg-light");
            $("#bgair4").addClass("bg-warning");  
          }
          // on-off Air 5
          if (amp[4] <= setpointAmpAir5) {
            $("#bgair5").addClass("bg-light");
          }
          if (amp[4] > setpointAmpAir5) {
            $("#bgair5").removeClass("bg-light");
            $("#bgair5").addClass("bg-warning");  
          }
          // on-off Air 6
          if (amp[5] <= setpointAmpAir6) {
            $("#bgair6").addClass("bg-light");
          }
          if (amp[5] > setpointAmpAir6) {
            $("#bgair6").removeClass("bg-light");
            $("#bgair6").addClass("bg-warning");  
          }
          // on-off Air 7
          if (amp[6] <= setpointAmpAir7) {
            $("#bgair7").addClass("bg-light");
          }
          if (amp[6] > setpointAmpAir7) {
            $("#bgair7").removeClass("bg-light");
            $("#bgair7").addClass("bg-warning");  
          }
          // on-off Air 8
          if (amp[7] <= setpointAmpAir8) {
            $("#bgair8").addClass("bg-light");
          }
          if (amp[7] > setpointAmpAir8) {
            $("#bgair8").removeClass("bg-light");
            $("#bgair8").addClass("bg-warning");  
          }
          // on-off Air 9
          if (amp[8] <= setpointAmpAir9) {
            $("#bgair9").addClass("bg-light");
          }
          if (amp[8] > setpointAmpAir9) {
            $("#bgair9").removeClass("bg-light");
            $("#bgair9").addClass("bg-warning");  
          }
          // on-off Air 10
          if (amp[9] <= setpointAmpAir10) {
            $("#bgair10").addClass("bg-light");
          }
          if (amp[9] > setpointAmpAir10) {
            $("#bgair10").removeClass("bg-light");
            $("#bgair10").addClass("bg-warning");  
          }
          // on-off Air 11
          if (amp[10] <= setpointAmpAir11) {
            $("#bgair11").addClass("bg-light");
          }
          if (amp[10] > setpointAmpAir11) {
            $("#bgair11").removeClass("bg-light");
            $("#bgair11").addClass("bg-warning");  
          }
          // on-off Air 12
          if (amp[11] <= setpointAmpAir12) {
            $("#bgair12").addClass("bg-light");
          }
          if (amp[11] > setpointAmpAir12) {
            $("#bgair12").removeClass("bg-light");
            $("#bgair12").addClass("bg-warning");  
          }
        },
        error: function (error_data) {
          console.log("error");
          console.log(error_data);
        },
      });
    }, 5000);
  });
  