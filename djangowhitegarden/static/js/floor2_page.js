$(document).ready(function () {
    var endpoint = "/api/floor2";
    var kwh = [];
    var amp = [];
    var labels = [];
  
    const $kwhmainf2 = $("#kwhmainf2");
    const $kwhwalkwayf2 = $("#kwhwalkwayf2");
    const $kwhroom201 = $("#kwhroom201");
    const $kwhroom202 = $("#kwhroom202");
    const $kwhroom203 = $("#kwhroom203");
    const $kwhroom204 = $("#kwhroom204");
    const $kwhroom205 = $("#kwhroom205");
    const $kwhroom206 = $("#kwhroom206");
    const $kwhroom207 = $("#kwhroom207");
    const $kwhroom208 = $("#kwhroom208");
    const $kwhroom209 = $("#kwhroom209");
    const $kwhroom210 = $("#kwhroom210");
    const $kwhroom211 = $("#kwhroom211");
    const $kwhroom212 = $("#kwhroom212");
    const $kwhroom213 = $("#kwhroom213");
    const $kwhroom214 = $("#kwhroom214");
    const $kwhroom215 = $("#kwhroom215");
    const $kwhroom216 = $("#kwhroom216");
    const $kwhroom217 = $("#kwhroom217");

    var setpointAmpwalkwayf2 = 0.3;
    var setpointAmproom201 = 0.3;
    var setpointAmproom202 = 0.3;
    var setpointAmproom203 = 0.3;
    var setpointAmproom204 = 0.3;
    var setpointAmproom205 = 0.3;
    var setpointAmproom206 = 0.3;
    var setpointAmproom207 = 0.3;
    var setpointAmproom208 = 0.3;
    var setpointAmproom209 = 0.3;
    var setpointAmproom210 = 0.3;
    var setpointAmproom211 = 0.3;
    var setpointAmproom212 = 0.3;
    var setpointAmproom213 = 0.3;
    var setpointAmproom214 = 0.3;
    var setpointAmproom215 = 0.3;
    var setpointAmproom216 = 0.3;
    var setpointAmproom217 = 0.3;

    var powerOn_color = "#00FF00"; //set color for device has normal #10B310
    var powerOff_color = "#A9A9A9"; //set color for device has normal #10B310


    setInterval(function () {
      $.ajax({
        method: "GET",
        url: endpoint,
        success: function (data) {
          labels = data.labels;
          kwh = data.kwhfloor2; //from apifloor2.py
          amp = data.ampfloor2; //from apifloor2.py

          $kwhmainf2.text(kwh[0].toFixed(2) + " หน่วย");
          $kwhwalkwayf2.text(kwh[1].toFixed(2) + " หน่วย");
          $kwhroom201.text(kwh[2].toFixed(2) + " หน่วย");
          $kwhroom202.text(kwh[3].toFixed(2) + " หน่วย");
          $kwhroom203.text(kwh[4].toFixed(2) + " หน่วย");
          $kwhroom204.text(kwh[5].toFixed(2) + " หน่วย");
          $kwhroom205.text(kwh[6].toFixed(2) + " หน่วย");
          $kwhroom206.text(kwh[7].toFixed(2) + " หน่วย");
          $kwhroom207.text(kwh[8].toFixed(2) + " หน่วย");
          $kwhroom208.text(kwh[9].toFixed(2) + " หน่วย");
          $kwhroom209.text(kwh[10].toFixed(2) + " หน่วย");
          $kwhroom210.text(kwh[11].toFixed(2) + " หน่วย");
          $kwhroom211.text(kwh[12].toFixed(2) + " หน่วย");
          $kwhroom212.text(kwh[13].toFixed(2) + " หน่วย");
          $kwhroom213.text(kwh[14].toFixed(2) + " หน่วย");
          $kwhroom214.text(kwh[15].toFixed(2) + " หน่วย");
          $kwhroom215.text(kwh[16].toFixed(2) + " หน่วย");
          $kwhroom216.text(kwh[17].toFixed(2) + " หน่วย");
          $kwhroom217.text(kwh[18].toFixed(2) + " หน่วย");

          // on-off walkway 
          if (amp[0] <= setpointAmpwalkwayf2) {
            $("#bgwalkwayf2").addClass("bg-light");
          }
          if (amp[0] > setpointAmpwalkwayf2) {
            $("#bgwalkwayf2").removeClass("bg-light");
            $("#bgwalkwayfx").addClass("bg-warning");  
          }
          // on-off room201
          if (amp[1] <= setpointAmproom201) {
            $("#bgroom201").addClass("bg-light");
          }
          if (amp[1] > setpointAmproom201) {
            $("#bgroom201").removeClass("bg-light");
            $("#bgroom201").addClass("bg-warning");  
          }
          // on-off room202
          if (amp[2] <= setpointAmproom202) {
            $("#bgroom202").addClass("bg-light");
          }
          if (amp[2] > setpointAmproom202) {
            $("#bgroom202").removeClass("bg-light");
            $("#bgroom202").addClass("bg-warning");  
          }
          // on-off room203
          if (amp[3] <= setpointAmproom203) {
            $("#bgroom203").addClass("bg-light");
          }
          if (amp[3] > setpointAmproom203) {
            $("#bgroom203").removeClass("bg-light");
            $("#bgroom203").addClass("bg-warning");  
          }
          // on-off room204
          if (amp[4] <= setpointAmproom204) {
            $("#bgroom204").addClass("bg-light");
          }
          if (amp[4] > setpointAmproom204) {
            $("#bgroom204").removeClass("bg-light");
            $("#bgroom204").addClass("bg-warning");  
          }
          // on-off room205
          if (amp[5] <= setpointAmproom205) {
            $("#bgroom205").addClass("bg-light");
          }
          if (amp[5] > setpointAmproom205) {
            $("#bgroom205").removeClass("bg-light");
            $("#bgroom205").addClass("bg-warning");  
          }
          // on-off room206
          if (amp[6] <= setpointAmproom206) {
            $("#bgroom206").addClass("bg-light");
          }
          if (amp[6] > setpointAmproom206) {
            $("#bgroom206").removeClass("bg-light");
            $("#bgroom206").addClass("bg-warning");  
          }
          // on-off room207
          if (amp[7] <= setpointAmproom207) {
            $("#bgroom207").addClass("bg-light");
          }
          if (amp[7] > setpointAmproom207) {
            $("#bgroom207").removeClass("bg-light");
            $("#bgroom207").addClass("bg-warning");  
          }
          // on-off room208
          if (amp[8] <= setpointAmproom208) {
            $("#bgroom208").addClass("bg-light");
          }
          if (amp[8] > setpointAmproom208) {
            $("#bgroom208").removeClass("bg-light");
            $("#bgroom208").addClass("bg-warning");  
          }
          // on-off room209
          if (amp[9] <= setpointAmproom209) {
            $("#bgroom209").addClass("bg-light");
          }
          if (amp[9] > setpointAmproom209) {
            $("#bgroom209").removeClass("bg-light");
            $("#bgroom209").addClass("bg-warning");  
          }
          // on-off room210
          if (amp[10] <= setpointAmproom210) {
            $("#bgroom210").addClass("bg-light");
          }
          if (amp[10] > setpointAmproom210) {
            $("#bgroom210").removeClass("bg-light");
            $("#bgroom210").addClass("bg-warning");  
          }
          // on-off room211
          if (amp[11] <= setpointAmproom211) {
            $("#bgroom211").addClass("bg-light");
          }
          if (amp[11] > setpointAmproom211) {
            $("#bgroom211").removeClass("bg-light");
            $("#bgroom211").addClass("bg-warning");  
          }
          // on-off room212
          if (amp[12] <= setpointAmproom212) {
            $("#bgroom212").addClass("bg-light");
          }
          if (amp[12] > setpointAmproom212) {
            $("#bgroom212").removeClass("bg-light");
            $("#bgroom212").addClass("bg-warning");  
          }
          // on-off room213
          if (amp[13] <= setpointAmproom213) {
            $("#bgroom213").addClass("bg-light");
          }
          if (amp[13] > setpointAmproom213) {
            $("#bgroom213").removeClass("bg-light");
            $("#bgroom213").addClass("bg-warning");  
          }
          // on-off room214
          if (amp[14] <= setpointAmproom214) {
            $("#bgroom214").addClass("bg-light");
          }
          if (amp[14] > setpointAmproom214) {
            $("#bgroom214").removeClass("bg-light");
            $("#bgroom214").addClass("bg-warning");  
          }
          // on-off room215
          if (amp[15] <= setpointAmproom215) {
            $("#bgroom215").addClass("bg-light");
          }
          if (amp[15] > setpointAmproom215) {
            $("#bgroom215").removeClass("bg-light");
            $("#bgroom215").addClass("bg-warning");  
          }
          // on-off room216
          if (amp[16] <= setpointAmproom216) {
            $("#bgroom216").addClass("bg-light");
          }
          if (amp[16] > setpointAmproom216) {
            $("#bgroom216").removeClass("bg-light");
            $("#bgroom216").addClass("bg-warning");  
          }
          // on-off room217
          if (amp[17] <= setpointAmproom217) {
            $("#bgroom217").addClass("bg-light");
          }
          if (amp[17] > setpointAmproom217) {
            $("#bgroom217").removeClass("bg-light");
            $("#bgroom217").addClass("bg-warning");  
          }
        },
        error: function (error_data) {
          console.log("error");
          console.log(error_data);
        },
      });
    }, 5000);
  });
  