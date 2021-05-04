$(document).ready(function () {
    var endpoint = "/api/floor3";
    var kwh = [];
    var amp = [];
    var labels = [];
  
    const $kwhmainf3 = $("#kwhmainf3");
    const $kwhwalkwayf3 = $("#kwhwalkwayf3");
    const $kwhroom301 = $("#kwhroom301");
    const $kwhroom302 = $("#kwhroom302");
    const $kwhroom303 = $("#kwhroom303");
    const $kwhroom304 = $("#kwhroom304");
    const $kwhroom305 = $("#kwhroom305");
    const $kwhroom306 = $("#kwhroom306");
    const $kwhroom307 = $("#kwhroom307");
    const $kwhroom308 = $("#kwhroom308");
    const $kwhroom309 = $("#kwhroom309");
    const $kwhroom310 = $("#kwhroom310");
    const $kwhroom311 = $("#kwhroom311");
    const $kwhroom312 = $("#kwhroom312");
    const $kwhroom313 = $("#kwhroom313");
    const $kwhroom314 = $("#kwhroom314");
    const $kwhroom315 = $("#kwhroom315");
    const $kwhroom316 = $("#kwhroom316");
    const $kwhroom317 = $("#kwhroom317");

    var setpointAmpwalkwayf3 = 0.3;
    var setpointAmproom301 = 0.3;
    var setpointAmproom302 = 0.3;
    var setpointAmproom303 = 0.3;
    var setpointAmproom304 = 0.3;
    var setpointAmproom305 = 0.3;
    var setpointAmproom306 = 0.3;
    var setpointAmproom307 = 0.3;
    var setpointAmproom308 = 0.3;
    var setpointAmproom309 = 0.3;
    var setpointAmproom310 = 0.3;
    var setpointAmproom311 = 0.3;
    var setpointAmproom312 = 0.3;
    var setpointAmproom313 = 0.3;
    var setpointAmproom314 = 0.3;
    var setpointAmproom315 = 0.3;
    var setpointAmproom316 = 0.3;
    var setpointAmproom317 = 0.3;

    var powerOn_color = "#00FF00"; //set color for device has normal #10B310
    var powerOff_color = "#A9A9A9"; //set color for device has normal #10B310


    setInterval(function () {
      $.ajax({
        method: "GET",
        url: endpoint,
        success: function (data) {
          labels = data.labels;
          kwh = data.kwhfloor3; //from apifloor3.py
          amp = data.ampfloor3; //from apifloor3.py

          $kwhmainf3.text(kwh[0].toFixed(2) + " หน่วย");
          $kwhwalkwayf3.text(kwh[1].toFixed(2) + " หน่วย");
          $kwhroom301.text(kwh[2].toFixed(2) + " หน่วย");
          $kwhroom302.text(kwh[3].toFixed(2) + " หน่วย");
          $kwhroom303.text(kwh[4].toFixed(2) + " หน่วย");
          $kwhroom304.text(kwh[5].toFixed(2) + " หน่วย");
          $kwhroom305.text(kwh[6].toFixed(2) + " หน่วย");
          $kwhroom306.text(kwh[7].toFixed(2) + " หน่วย");
          $kwhroom307.text(kwh[8].toFixed(2) + " หน่วย");
          $kwhroom308.text(kwh[9].toFixed(2) + " หน่วย");
          $kwhroom309.text(kwh[10].toFixed(2) + " หน่วย");
          $kwhroom310.text(kwh[11].toFixed(2) + " หน่วย");
          $kwhroom311.text(kwh[12].toFixed(2) + " หน่วย");
          $kwhroom312.text(kwh[13].toFixed(2) + " หน่วย");
          $kwhroom313.text(kwh[14].toFixed(2) + " หน่วย");
          $kwhroom314.text(kwh[15].toFixed(2) + " หน่วย");
          $kwhroom315.text(kwh[16].toFixed(2) + " หน่วย");
          $kwhroom316.text(kwh[17].toFixed(2) + " หน่วย");
          $kwhroom317.text(kwh[18].toFixed(2) + " หน่วย");

          // on-off walkway 
          if (amp[0] <= setpointAmpwalkwayf3) {
            $("#bgwalkwayf3").addClass("bg-light");
          }
          if (amp[0] > setpointAmpwalkwayf3) {
            $("#bgwalkwayf3").removeClass("bg-light");
            $("#bgwalkwayf3").addClass("bg-warning");  
          }
          // on-off room301
          if (amp[1] <= setpointAmproom301) {
            $("#bgroom301").addClass("bg-light");
          }
          if (amp[1] > setpointAmproom301) {
            $("#bgroom301").removeClass("bg-light");
            $("#bgroom301").addClass("bg-warning");  
          }
          // on-off room302
          if (amp[2] <= setpointAmproom302) {
            $("#bgroom302").addClass("bg-light");
          }
          if (amp[2] > setpointAmproom302) {
            $("#bgroom302").removeClass("bg-light");
            $("#bgroom302").addClass("bg-warning");  
          }
          // on-off room303
          if (amp[3] <= setpointAmproom303) {
            $("#bgroom303").addClass("bg-light");
          }
          if (amp[3] > setpointAmproom303) {
            $("#bgroom303").removeClass("bg-light");
            $("#bgroom303").addClass("bg-warning");  
          }
          // on-off room304
          if (amp[4] <= setpointAmproom304) {
            $("#bgroom304").addClass("bg-light");
          }
          if (amp[4] > setpointAmproom304) {
            $("#bgroom304").removeClass("bg-light");
            $("#bgroom304").addClass("bg-warning");  
          }
          // on-off room305
          if (amp[5] <= setpointAmproom305) {
            $("#bgroom305").addClass("bg-light");
          }
          if (amp[5] > setpointAmproom305) {
            $("#bgroom305").removeClass("bg-light");
            $("#bgroom305").addClass("bg-warning");  
          }
          // on-off room306
          if (amp[6] <= setpointAmproom306) {
            $("#bgroom306").addClass("bg-light");
          }
          if (amp[6] > setpointAmproom306) {
            $("#bgroom306").removeClass("bg-light");
            $("#bgroom306").addClass("bg-warning");  
          }
          // on-off room307
          if (amp[7] <= setpointAmproom307) {
            $("#bgroom307").addClass("bg-light");
          }
          if (amp[7] > setpointAmproom307) {
            $("#bgroom307").removeClass("bg-light");
            $("#bgroom307").addClass("bg-warning");  
          }
          // on-off room308
          if (amp[8] <= setpointAmproom308) {
            $("#bgroom308").addClass("bg-light");
          }
          if (amp[8] > setpointAmproom308) {
            $("#bgroom308").removeClass("bg-light");
            $("#bgroom308").addClass("bg-warning");  
          }
          // on-off room309
          if (amp[9] <= setpointAmproom309) {
            $("#bgroom309").addClass("bg-light");
          }
          if (amp[9] > setpointAmproom309) {
            $("#bgroom309").removeClass("bg-light");
            $("#bgroom309").addClass("bg-warning");  
          }
          // on-off room310
          if (amp[10] <= setpointAmproom310) {
            $("#bgroom310").addClass("bg-light");
          }
          if (amp[10] > setpointAmproom310) {
            $("#bgroom310").removeClass("bg-light");
            $("#bgroom310").addClass("bg-warning");  
          }
          // on-off room311
          if (amp[11] <= setpointAmproom311) {
            $("#bgroom311").addClass("bg-light");
          }
          if (amp[11] > setpointAmproom311) {
            $("#bgroom311").removeClass("bg-light");
            $("#bgroom311").addClass("bg-warning");  
          }
          // on-off room312
          if (amp[12] <= setpointAmproom312) {
            $("#bgroom312").addClass("bg-light");
          }
          if (amp[12] > setpointAmproom312) {
            $("#bgroom312").removeClass("bg-light");
            $("#bgroom312").addClass("bg-warning");  
          }
          // on-off room313
          if (amp[13] <= setpointAmproom313) {
            $("#bgroom313").addClass("bg-light");
          }
          if (amp[13] > setpointAmproom313) {
            $("#bgroom313").removeClass("bg-light");
            $("#bgroom313").addClass("bg-warning");  
          }
          // on-off room314
          if (amp[14] <= setpointAmproom314) {
            $("#bgroom314").addClass("bg-light");
          }
          if (amp[14] > setpointAmproom314) {
            $("#bgroom314").removeClass("bg-light");
            $("#bgroom314").addClass("bg-warning");  
          }
          // on-off room315
          if (amp[15] <= setpointAmproom315) {
            $("#bgroom315").addClass("bg-light");
          }
          if (amp[15] > setpointAmproom315) {
            $("#bgroom315").removeClass("bg-light");
            $("#bgroom315").addClass("bg-warning");  
          }
          // on-off room316
          if (amp[16] <= setpointAmproom316) {
            $("#bgroom316").addClass("bg-light");
          }
          if (amp[16] > setpointAmproom316) {
            $("#bgroom316").removeClass("bg-light");
            $("#bgroom316").addClass("bg-warning");  
          }
          // on-off room317
          if (amp[17] <= setpointAmproom317) {
            $("#bgroom317").addClass("bg-light");
          }
          if (amp[17] > setpointAmproom317) {
            $("#bgroom317").removeClass("bg-light");
            $("#bgroom317").addClass("bg-warning");  
          }
        },
        error: function (error_data) {
          console.log("error");
          console.log(error_data);
        },
      });
    }, 5000);
  });
  