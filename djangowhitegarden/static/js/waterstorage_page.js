$(document).ready(function () {
  var endpoint = "/api/water";
  var waterlevel = [];
  var waterusage = [];
  var percentpump = [];
  var labels = [];

  const $waterlevel_ground = $("#waterlevelground");
  const $waterlevel_roof = $("#waterlevelroof");
  const $waterusage_ground = $("#waterusageground");
  const $waterusage_roof = $("#waterusageroof");
  const $percentpump_1 = $("#percentpump1");
  const $percentpump_2 = $("#percentpump2");
  const $percentpump_3 = $("#percentpump3");
  const $percentpump_4 = $("#percentpump4");
  const $percentpump_5 = $("#percentpump5");
  const $percentpump_6 = $("#percentpump6");
  const $percentpump_7 = $("#percentpump7");
  const $unitpump_1 = $("#unitpump1");
  const $unitpump_2 = $("#unitpump2");
  const $unitpump_3 = $("#unitpump3");
  const $unitpump_4 = $("#unitpump4");
  const $unitpump_5 = $("#unitpump5");
  const $unitpump_6 = $("#unitpump6");
  const $unitpump_7 = $("#unitpump7");
  const $statuspump_1 = $("#statuspump1");
  const $statuspump_2 = $("#statuspump2");
  const $statuspump_3 = $("#statuspump3");
  const $statuspump_4 = $("#statuspump4");
  const $statuspump_5 = $("#statuspump5");
  const $statuspump_6 = $("#statuspump6");
  const $statuspump_7 = $("#statuspump7");

  var setpointAmpPump1 = 0.1;
  var setpointAmpPump2 = 0.1;
  var setpointAmpPump3 = 0.1;
  var setpointAmpPump4 = 0.1;
  var setpointAmpPump5 = 0.1;
  var setpointAmpPump6 = 0.1;
  var setpointAmpPump7 = 0.1;

  var powerOn_color = "#00FF00"; //set color for device has normal #10B310
  var powerOff_color = "#A9A9A9"; //set color for device has normal #10B310

  setInterval(function () {
    $.ajax({
      method: "GET",
      url: endpoint,
      success: function (data) {
        labels = data.labels;
        waterlevel = data.waterlevel; //from apiwater.py
        waterusage = data.waterusage; //from apiwater.py
        percentpump = data.percentpump; //from apiwater.py
        unitpump = data.unitpump; //from apiwater.py
        statuspump = data.statuspump; //from apiwater.py

        $waterlevel_ground.text(waterlevel[0].toFixed(1) + " เมตร");
        $waterusage_ground.text(waterusage[0].toFixed(1) + " ลบ.เมตร");

        $waterlevel_roof.text(waterlevel[1].toFixed(1) + " เมตร");
        $waterusage_roof.text(waterusage[1].toFixed(1) + " ลบ.เมตร");

        $percentpump_1.text(percentpump[0].toFixed(2) + " %");
        $percentpump_2.text(percentpump[1].toFixed(2) + " %");
        $percentpump_3.text(percentpump[2].toFixed(2) + " %");
        $percentpump_4.text(percentpump[3].toFixed(2) + " %");
        $percentpump_5.text(percentpump[4].toFixed(2) + " %");
        $percentpump_6.text(percentpump[5].toFixed(2) + " %");
        $percentpump_7.text(percentpump[6].toFixed(2) + " %");

        $unitpump_1.text(unitpump[0].toFixed(2) + " หน่วย");
        $unitpump_2.text(unitpump[1].toFixed(2) + " หน่วย");
        $unitpump_3.text(unitpump[2].toFixed(2) + " หน่วย");
        $unitpump_4.text(unitpump[3].toFixed(2) + " หน่วย");
        $unitpump_5.text(unitpump[4].toFixed(2) + " หน่วย");
        $unitpump_6.text(unitpump[5].toFixed(2) + " หน่วย");
        $unitpump_7.text(unitpump[6].toFixed(2) + " หน่วย");

        // on-off pump 1
        if (statuspump[0] <= setpointAmpPump1) {
          $("#bgwpump1").addClass("bg-light");
          $("#bgupump1").addClass("bg-light");
          $("#statuspump1").css("color", powerOff_color);
          $("#pump1").removeClass("bg-warning");
        }
        if (statuspump[0] > setpointAmpPump1) {
          $("#bgwpump1").removeClass("bg-light");
          $("#bgwpump1").addClass("bg-warning");
          $("#bgupump1").removeClass("bg-light");
          $("#bgupump1").addClass("bg-warning");
          $("#statuspump1").css("color", powerOn_color);
          $("#pump1").addClass("bg-warning");
        }
        // on-off pump 2
        if (statuspump[1] <= setpointAmpPump2) {
          $("#bgwpump2").addClass("bg-light");
          $("#bgupump2").addClass("bg-light");
          $("#statuspump2").css("color", powerOff_color);
          $("#pump2").removeClass("bg-warning");
        }
        if (statuspump[1] > setpointAmpPump2) {
          $("#bgwpump2").removeClass("bg-light");
          $("#bgwpump2").addClass("bg-warning");
          $("#bgupump2").removeClass("bg-light");
          $("#bgupump2").addClass("bg-warning");
          $("#statuspump2").css("color", powerOn_color);
          $("#pump2").addClass("bg-warning");
        }
        // on-off pump 3
        if (statuspump[2] <= setpointAmpPump3) {
          $("#bgwpump3").addClass("bg-light");
          $("#bgupump3").addClass("bg-light");
          $("#statuspump3").css("color", powerOff_color);
          $("#pump3").removeClass("bg-warning");
        }
        if (statuspump[2] > setpointAmpPump3) {
          $("#bgwpump3").removeClass("bg-light");
          $("#bgwpump3").addClass("bg-warning");
          $("#bgupump3").removeClass("bg-light");
          $("#bgupump3").addClass("bg-warning");
          $("#statuspump3").css("color", powerOn_color);
          $("#pump3").addClass("bg-warning");
        }
        // on-off pump 4
        if (statuspump[3] <= setpointAmpPump4) {
          $("#bgwpump4").addClass("bg-light");
          $("#bgupump4").addClass("bg-light");
          $("#statuspump4").css("color", powerOff_color);
          $("#pump4").removeClass("bg-warning");
        }
        if (statuspump[3] > setpointAmpPump4) {
          $("#bgwpump4").removeClass("bg-light");
          $("#bgwpump4").addClass("bg-warning");
          $("#bgupump4").removeClass("bg-light");
          $("#bgupump4").addClass("bg-warning");
          $("#statuspump4").css("color", powerOn_color);
          $("#pump4").addClass("bg-warning");
        }
        // on-off pump 5
        if (statuspump[4] <= setpointAmpPump5) {
          $("#bgwpump5").addClass("bg-light");
          $("#bgupump5").addClass("bg-light");
          $("#statuspump5").css("color", powerOff_color);
          $("#pump5").removeClass("bg-warning");
        }
        if (statuspump[4] > setpointAmpPump5) {
          $("#bgwpump5").removeClass("bg-light");
          $("#bgwpump5").addClass("bg-warning");
          $("#bgupump5").removeClass("bg-light");
          $("#bgupump5").addClass("bg-warning");
          $("#statuspump5").css("color", powerOn_color);
          $("#pump5").addClass("bg-warning");
        }
        // on-off pump 6
        if (statuspump[5] <= setpointAmpPump6) {
          $("#bgwpump6").addClass("bg-light");
          $("#bgupump6").addClass("bg-light");
          $("#statuspump6").css("color", powerOff_color);
          $("#pump6").removeClass("bg-warning");
        }
        if (statuspump[5] > setpointAmpPump6) {
          $("#bgwpump6").removeClass("bg-light");
          $("#bgwpump6").addClass("bg-warning");
          $("#bgupump6").removeClass("bg-light");
          $("#bgupump6").addClass("bg-warning");
          $("#statuspump6").css("color", powerOn_color);
          $("#pump6").addClass("bg-warning");
        }
        // on-off pump 7
        if (statuspump[6] <= setpointAmpPump7) {
          $("#bgwpump7").addClass("bg-light");
          $("#bgupump7").addClass("bg-light");
          $("#statuspump7").css("color", powerOff_color);
          $("#pump7").removeClass("bg-warning");
        }
        if (statuspump[6] > setpointAmpPump7) {
          $("#bgwpump7").removeClass("bg-light");
          $("#bgwpump7").addClass("bg-warning");
          $("#bgupump7").removeClass("bg-light");
          $("#bgupump7").addClass("bg-warning");
          $("#statuspump7").css("color", powerOn_color);
          $("#pump7").addClass("bg-warning");
        }
      },
      error: function (error_data) {
        console.log("error");
        console.log(error_data);
      },
    });
  }, 5000);
});
