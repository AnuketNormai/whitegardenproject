$(document).ready(function () {
    var endpoint = "/api/floor5";
    var kwh = [];
    var amp = [];
    var labels = [];
  
    const $kwhmainf5 = $("#kwhmainf5");
    const $kwhwalkwayf5 = $("#kwhwalkwayf5");
    const $kwhroom501 = $("#kwhroom501");
    const $kwhroom502 = $("#kwhroom502");
    const $kwhroom503 = $("#kwhroom503");
    const $kwhroom504 = $("#kwhroom504");
    const $kwhroom505 = $("#kwhroom505");
    const $kwhroom506 = $("#kwhroom506");
    const $kwhroom507 = $("#kwhroom507");
    const $kwhroom508 = $("#kwhroom508");
    const $kwhroom509 = $("#kwhroom509");
    const $kwhroom510 = $("#kwhroom510");
    const $kwhroom511 = $("#kwhroom511");
    const $kwhroom512 = $("#kwhroom512");
    const $kwhroom513 = $("#kwhroom513");
    const $kwhroom514 = $("#kwhroom514");
    const $kwhroom515 = $("#kwhroom515");
    const $kwhroom516 = $("#kwhroom516");
    const $kwhroom517 = $("#kwhroom517");

    var setpointAmpwalkwayf5 = 0.3;
    var setpointAmproom501 = 0.3;
    var setpointAmproom502 = 0.3;
    var setpointAmproom503 = 0.3;
    var setpointAmproom504 = 0.3;
    var setpointAmproom505 = 0.3;
    var setpointAmproom506 = 0.3;
    var setpointAmproom507 = 0.3;
    var setpointAmproom508 = 0.3;
    var setpointAmproom509 = 0.3;
    var setpointAmproom510 = 0.3;
    var setpointAmproom511 = 0.3;
    var setpointAmproom512 = 0.3;
    var setpointAmproom513 = 0.3;
    var setpointAmproom514 = 0.3;
    var setpointAmproom515 = 0.3;
    var setpointAmproom516 = 0.3;
    var setpointAmproom517 = 0.3;

    var powerOn_color = "#00FF00"; //set color for device has normal #10B510
    var powerOff_color = "#A9A9A9"; //set color for device has normal #10B510


    setInterval(function () {
      $.ajax({
        method: "GET",
        url: endpoint,
        success: function (data) {
          labels = data.labels;
          kwh = data.kwhfloor5; //from apifloor3.py
          amp = data.ampfloor5; //from apifloor3.py

          $kwhmainf5.text(kwh[0].toFixed(2) + " หน่วย");
          $kwhwalkwayf5.text(kwh[1].toFixed(2) + " หน่วย");
          $kwhroom501.text(kwh[2].toFixed(2) + " หน่วย");
          $kwhroom502.text(kwh[3].toFixed(2) + " หน่วย");
          $kwhroom503.text(kwh[4].toFixed(2) + " หน่วย");
          $kwhroom504.text(kwh[5].toFixed(2) + " หน่วย");
          $kwhroom505.text(kwh[6].toFixed(2) + " หน่วย");
          $kwhroom506.text(kwh[7].toFixed(2) + " หน่วย");
          $kwhroom507.text(kwh[8].toFixed(2) + " หน่วย");
          $kwhroom508.text(kwh[9].toFixed(2) + " หน่วย");
          $kwhroom509.text(kwh[10].toFixed(2) + " หน่วย");
          $kwhroom510.text(kwh[11].toFixed(2) + " หน่วย");
          $kwhroom511.text(kwh[12].toFixed(2) + " หน่วย");
          $kwhroom512.text(kwh[13].toFixed(2) + " หน่วย");
          $kwhroom513.text(kwh[14].toFixed(2) + " หน่วย");
          $kwhroom514.text(kwh[15].toFixed(2) + " หน่วย");
          $kwhroom515.text(kwh[16].toFixed(2) + " หน่วย");
          $kwhroom516.text(kwh[17].toFixed(2) + " หน่วย");
          $kwhroom517.text(kwh[18].toFixed(2) + " หน่วย");

          // on-off walkway 
          if (amp[0] <= setpointAmpwalkwayf5) {
            $("#bgwalkwayf5").addClass("bg-light");
          }
          if (amp[0] > setpointAmpwalkwayf5) {
            $("#bgwalkwayf5").removeClass("bg-light");
            $("#bgwalkwayf5").addClass("bg-warning");  
          }
          // on-off room501
          if (amp[1] <= setpointAmproom501) {
            $("#bgroom501").addClass("bg-light");
          }
          if (amp[1] > setpointAmproom501) {
            $("#bgroom501").removeClass("bg-light");
            $("#bgroom501").addClass("bg-warning");  
          }
          // on-off room502
          if (amp[2] <= setpointAmproom502) {
            $("#bgroom502").addClass("bg-light");
          }
          if (amp[2] > setpointAmproom502) {
            $("#bgroom502").removeClass("bg-light");
            $("#bgroom502").addClass("bg-warning");  
          }
          // on-off room503
          if (amp[3] <= setpointAmproom503) {
            $("#bgroom503").addClass("bg-light");
          }
          if (amp[3] > setpointAmproom503) {
            $("#bgroom503").removeClass("bg-light");
            $("#bgroom503").addClass("bg-warning");  
          }
          // on-off room504
          if (amp[4] <= setpointAmproom504) {
            $("#bgroom504").addClass("bg-light");
          }
          if (amp[4] > setpointAmproom504) {
            $("#bgroom504").removeClass("bg-light");
            $("#bgroom504").addClass("bg-warning");  
          }
          // on-off room505
          if (amp[5] <= setpointAmproom505) {
            $("#bgroom505").addClass("bg-light");
          }
          if (amp[5] > setpointAmproom505) {
            $("#bgroom505").removeClass("bg-light");
            $("#bgroom505").addClass("bg-warning");  
          }
          // on-off room506
          if (amp[6] <= setpointAmproom506) {
            $("#bgroom506").addClass("bg-light");
          }
          if (amp[6] > setpointAmproom506) {
            $("#bgroom506").removeClass("bg-light");
            $("#bgroom506").addClass("bg-warning");  
          }
          // on-off room507
          if (amp[7] <= setpointAmproom507) {
            $("#bgroom507").addClass("bg-light");
          }
          if (amp[7] > setpointAmproom507) {
            $("#bgroom507").removeClass("bg-light");
            $("#bgroom507").addClass("bg-warning");  
          }
          // on-off room508
          if (amp[8] <= setpointAmproom508) {
            $("#bgroom508").addClass("bg-light");
          }
          if (amp[8] > setpointAmproom508) {
            $("#bgroom508").removeClass("bg-light");
            $("#bgroom508").addClass("bg-warning");  
          }
          // on-off room509
          if (amp[9] <= setpointAmproom509) {
            $("#bgroom509").addClass("bg-light");
          }
          if (amp[9] > setpointAmproom509) {
            $("#bgroom509").removeClass("bg-light");
            $("#bgroom509").addClass("bg-warning");  
          }
          // on-off room510
          if (amp[10] <= setpointAmproom510) {
            $("#bgroom510").addClass("bg-light");
          }
          if (amp[10] > setpointAmproom510) {
            $("#bgroom510").removeClass("bg-light");
            $("#bgroom510").addClass("bg-warning");  
          }
          // on-off room511
          if (amp[11] <= setpointAmproom511) {
            $("#bgroom511").addClass("bg-light");
          }
          if (amp[11] > setpointAmproom511) {
            $("#bgroom511").removeClass("bg-light");
            $("#bgroom511").addClass("bg-warning");  
          }
          // on-off room512
          if (amp[12] <= setpointAmproom512) {
            $("#bgroom512").addClass("bg-light");
          }
          if (amp[12] > setpointAmproom512) {
            $("#bgroom512").removeClass("bg-light");
            $("#bgroom512").addClass("bg-warning");  
          }
          // on-off room513
          if (amp[13] <= setpointAmproom513) {
            $("#bgroom513").addClass("bg-light");
          }
          if (amp[13] > setpointAmproom513) {
            $("#bgroom513").removeClass("bg-light");
            $("#bgroom513").addClass("bg-warning");  
          }
          // on-off room514
          if (amp[14] <= setpointAmproom514) {
            $("#bgroom514").addClass("bg-light");
          }
          if (amp[14] > setpointAmproom514) {
            $("#bgroom514").removeClass("bg-light");
            $("#bgroom514").addClass("bg-warning");  
          }
          // on-off room515
          if (amp[15] <= setpointAmproom515) {
            $("#bgroom515").addClass("bg-light");
          }
          if (amp[15] > setpointAmproom515) {
            $("#bgroom515").removeClass("bg-light");
            $("#bgroom515").addClass("bg-warning");  
          }
          // on-off room516
          if (amp[16] <= setpointAmproom516) {
            $("#bgroom516").addClass("bg-light");
          }
          if (amp[16] > setpointAmproom516) {
            $("#bgroom516").removeClass("bg-light");
            $("#bgroom516").addClass("bg-warning");  
          }
          // on-off room517
          if (amp[17] <= setpointAmproom517) {
            $("#bgroom517").addClass("bg-light");
          }
          if (amp[17] > setpointAmproom517) {
            $("#bgroom517").removeClass("bg-light");
            $("#bgroom517").addClass("bg-warning");  
          }
        },
        error: function (error_data) {
          console.log("error");
          console.log(error_data);
        },
      });
    }, 5000);
  });
  