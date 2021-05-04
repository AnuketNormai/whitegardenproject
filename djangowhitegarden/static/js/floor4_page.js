$(document).ready(function () {
    var endpoint = "/api/floor4";
    var kwh = [];
    var amp = [];
    var labels = [];
  
    const $kwhmainf4 = $("#kwhmainf4");
    const $kwhwalkwayf4 = $("#kwhwalkwayf4");
    const $kwhroom401 = $("#kwhroom401");
    const $kwhroom402 = $("#kwhroom402");
    const $kwhroom403 = $("#kwhroom403");
    const $kwhroom404 = $("#kwhroom404");
    const $kwhroom405 = $("#kwhroom405");
    const $kwhroom406 = $("#kwhroom406");
    const $kwhroom407 = $("#kwhroom407");
    const $kwhroom408 = $("#kwhroom408");
    const $kwhroom409 = $("#kwhroom409");
    const $kwhroom410 = $("#kwhroom410");
    const $kwhroom411 = $("#kwhroom411");
    const $kwhroom412 = $("#kwhroom412");
    const $kwhroom413 = $("#kwhroom413");
    const $kwhroom414 = $("#kwhroom414");
    const $kwhroom415 = $("#kwhroom415");
    const $kwhroom416 = $("#kwhroom416");
    const $kwhroom417 = $("#kwhroom417");

    var setpointAmpwalkwayf4 = 0.3;
    var setpointAmproom401 = 0.3;
    var setpointAmproom402 = 0.3;
    var setpointAmproom403 = 0.3;
    var setpointAmproom404 = 0.3;
    var setpointAmproom405 = 0.3;
    var setpointAmproom406 = 0.3;
    var setpointAmproom407 = 0.3;
    var setpointAmproom408 = 0.3;
    var setpointAmproom409 = 0.3;
    var setpointAmproom410 = 0.3;
    var setpointAmproom411 = 0.3;
    var setpointAmproom412 = 0.3;
    var setpointAmproom413 = 0.3;
    var setpointAmproom414 = 0.3;
    var setpointAmproom415 = 0.3;
    var setpointAmproom416 = 0.3;
    var setpointAmproom417 = 0.3;

    var powerOn_color = "#00FF00"; //set color for device has normal #10B410
    var powerOff_color = "#A9A9A9"; //set color for device has normal #10B410


    setInterval(function () {
      $.ajax({
        method: "GET",
        url: endpoint,
        success: function (data) {
          labels = data.labels;
          kwh = data.kwhfloor4; //from apifloor3.py
          amp = data.ampfloor4; //from apifloor3.py

          $kwhmainf4.text(kwh[0].toFixed(2) + " หน่วย");
          $kwhwalkwayf4.text(kwh[1].toFixed(2) + " หน่วย");
          $kwhroom401.text(kwh[2].toFixed(2) + " หน่วย");
          $kwhroom402.text(kwh[3].toFixed(2) + " หน่วย");
          $kwhroom403.text(kwh[4].toFixed(2) + " หน่วย");
          $kwhroom404.text(kwh[5].toFixed(2) + " หน่วย");
          $kwhroom405.text(kwh[6].toFixed(2) + " หน่วย");
          $kwhroom406.text(kwh[7].toFixed(2) + " หน่วย");
          $kwhroom407.text(kwh[8].toFixed(2) + " หน่วย");
          $kwhroom408.text(kwh[9].toFixed(2) + " หน่วย");
          $kwhroom409.text(kwh[10].toFixed(2) + " หน่วย");
          $kwhroom410.text(kwh[11].toFixed(2) + " หน่วย");
          $kwhroom411.text(kwh[12].toFixed(2) + " หน่วย");
          $kwhroom412.text(kwh[13].toFixed(2) + " หน่วย");
          $kwhroom413.text(kwh[14].toFixed(2) + " หน่วย");
          $kwhroom414.text(kwh[15].toFixed(2) + " หน่วย");
          $kwhroom415.text(kwh[16].toFixed(2) + " หน่วย");
          $kwhroom416.text(kwh[17].toFixed(2) + " หน่วย");
          $kwhroom417.text(kwh[18].toFixed(2) + " หน่วย");

          // on-off walkway 
          if (amp[0] <= setpointAmpwalkwayf4) {
            $("#bgwalkwayf4").addClass("bg-light");
          }
          if (amp[0] > setpointAmpwalkwayf4) {
            $("#bgwalkwayf4").removeClass("bg-light");
            $("#bgwalkwayf4").addClass("bg-warning");  
          }
          // on-off room401
          if (amp[1] <= setpointAmproom401) {
            $("#bgroom401").addClass("bg-light");
          }
          if (amp[1] > setpointAmproom401) {
            $("#bgroom401").removeClass("bg-light");
            $("#bgroom401").addClass("bg-warning");  
          }
          // on-off room402
          if (amp[2] <= setpointAmproom402) {
            $("#bgroom402").addClass("bg-light");
          }
          if (amp[2] > setpointAmproom402) {
            $("#bgroom402").removeClass("bg-light");
            $("#bgroom402").addClass("bg-warning");  
          }
          // on-off room403
          if (amp[3] <= setpointAmproom403) {
            $("#bgroom403").addClass("bg-light");
          }
          if (amp[3] > setpointAmproom403) {
            $("#bgroom403").removeClass("bg-light");
            $("#bgroom403").addClass("bg-warning");  
          }
          // on-off room404
          if (amp[4] <= setpointAmproom404) {
            $("#bgroom404").addClass("bg-light");
          }
          if (amp[4] > setpointAmproom404) {
            $("#bgroom404").removeClass("bg-light");
            $("#bgroom404").addClass("bg-warning");  
          }
          // on-off room405
          if (amp[5] <= setpointAmproom405) {
            $("#bgroom405").addClass("bg-light");
          }
          if (amp[5] > setpointAmproom405) {
            $("#bgroom405").removeClass("bg-light");
            $("#bgroom405").addClass("bg-warning");  
          }
          // on-off room406
          if (amp[6] <= setpointAmproom406) {
            $("#bgroom406").addClass("bg-light");
          }
          if (amp[6] > setpointAmproom406) {
            $("#bgroom406").removeClass("bg-light");
            $("#bgroom406").addClass("bg-warning");  
          }
          // on-off room407
          if (amp[7] <= setpointAmproom407) {
            $("#bgroom407").addClass("bg-light");
          }
          if (amp[7] > setpointAmproom407) {
            $("#bgroom407").removeClass("bg-light");
            $("#bgroom407").addClass("bg-warning");  
          }
          // on-off room408
          if (amp[8] <= setpointAmproom408) {
            $("#bgroom408").addClass("bg-light");
          }
          if (amp[8] > setpointAmproom408) {
            $("#bgroom408").removeClass("bg-light");
            $("#bgroom408").addClass("bg-warning");  
          }
          // on-off room409
          if (amp[9] <= setpointAmproom409) {
            $("#bgroom409").addClass("bg-light");
          }
          if (amp[9] > setpointAmproom409) {
            $("#bgroom409").removeClass("bg-light");
            $("#bgroom409").addClass("bg-warning");  
          }
          // on-off room410
          if (amp[10] <= setpointAmproom410) {
            $("#bgroom410").addClass("bg-light");
          }
          if (amp[10] > setpointAmproom410) {
            $("#bgroom410").removeClass("bg-light");
            $("#bgroom410").addClass("bg-warning");  
          }
          // on-off room411
          if (amp[11] <= setpointAmproom411) {
            $("#bgroom411").addClass("bg-light");
          }
          if (amp[11] > setpointAmproom411) {
            $("#bgroom411").removeClass("bg-light");
            $("#bgroom411").addClass("bg-warning");  
          }
          // on-off room412
          if (amp[12] <= setpointAmproom412) {
            $("#bgroom412").addClass("bg-light");
          }
          if (amp[12] > setpointAmproom412) {
            $("#bgroom412").removeClass("bg-light");
            $("#bgroom412").addClass("bg-warning");  
          }
          // on-off room413
          if (amp[13] <= setpointAmproom413) {
            $("#bgroom413").addClass("bg-light");
          }
          if (amp[13] > setpointAmproom413) {
            $("#bgroom413").removeClass("bg-light");
            $("#bgroom413").addClass("bg-warning");  
          }
          // on-off room414
          if (amp[14] <= setpointAmproom414) {
            $("#bgroom414").addClass("bg-light");
          }
          if (amp[14] > setpointAmproom414) {
            $("#bgroom414").removeClass("bg-light");
            $("#bgroom414").addClass("bg-warning");  
          }
          // on-off room415
          if (amp[15] <= setpointAmproom415) {
            $("#bgroom415").addClass("bg-light");
          }
          if (amp[15] > setpointAmproom415) {
            $("#bgroom415").removeClass("bg-light");
            $("#bgroom415").addClass("bg-warning");  
          }
          // on-off room416
          if (amp[16] <= setpointAmproom416) {
            $("#bgroom416").addClass("bg-light");
          }
          if (amp[16] > setpointAmproom416) {
            $("#bgroom416").removeClass("bg-light");
            $("#bgroom416").addClass("bg-warning");  
          }
          // on-off room417
          if (amp[17] <= setpointAmproom417) {
            $("#bgroom417").addClass("bg-light");
          }
          if (amp[17] > setpointAmproom417) {
            $("#bgroom417").removeClass("bg-light");
            $("#bgroom417").addClass("bg-warning");  
          }
        },
        error: function (error_data) {
          console.log("error");
          console.log(error_data);
        },
      });
    }, 5000);
  });
  