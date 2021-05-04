$(document).ready(function () {
  var endpoint = "/api/room";
  var f1 = [];
  var f2 = [];
  var f3 = [];
  var f4 = [];
  var f5 = [];
  var labels = [];

  var setpointroomf1 = 0.5;
  var setpointroomf2 = 0.5;
  var setpointroomf3 = 0.5;
  var setpointroomf4 = 0.5;
  var setpointroomf5 = 0.5;

  var powerOn_color = "#00FF00"; //set color for device has normal #10B510
  var powerOff_color = "#A9A9A9"; //set color for device has normal #10B510

  setInterval(function () {
    $.ajax({
      method: "GET",
      url: endpoint,
      success: function (data) {
        labels = data.labels;
        f1 = data.floor1; //from apiroom.py
        f2 = data.floor2; //from apiroom.py
        f3 = data.floor3; //from apiroom.py
        f4 = data.floor4; //from apiroom.py
        f5 = data.floor5; //from apiroom.py

        // floor 1
        //   A1
        if (f1[0] <= setpointroomf1) {
          $("#bgarooma1").addClass("bg-light");
        }
        if (f1[0] > setpointroomf1) {
          $("#bgarooma1").removeClass("bg-light");
          $("#bgarooma1").addClass("bg-warning");
        }
        //   A2
        if (f1[1] <= setpointroomf1) {
          $("#bgarooma2").addClass("bg-light");
        }
        if (f1[1] > setpointroomf1) {
          $("#bgarooma2").removeClass("bg-light");
          $("#bgarooma2").addClass("bg-warning");
        }
        //   A3
        if (f1[2] <= setpointroomf1) {
          $("#bgarooma3").addClass("bg-light");
        }
        if (f1[2] > setpointroomf1) {
          $("#bgarooma3").removeClass("bg-light");
          $("#bgarooma3").addClass("bg-warning");
        }
        //   A4
        if (f1[3] <= setpointroomf1) {
          $("#bgarooma4").addClass("bg-light");
        }
        if (f1[3] > setpointroomf1) {
          $("#bgarooma4").removeClass("bg-light");
          $("#bgarooma4").addClass("bg-warning");
        }
        //   A5
        if (f1[4] <= setpointroomf1) {
          $("#bgarooma5").addClass("bg-light");
        }
        if (f1[4] > setpointroomf1) {
          $("#bgarooma5").removeClass("bg-light");
          $("#bgarooma5").addClass("bg-warning");
        }
        //   A6
        if (f1[5] <= setpointroomf1) {
          $("#bgarooma6").addClass("bg-light");
        }
        if (f1[5] > setpointroomf1) {
          $("#bgarooma6").removeClass("bg-light");
          $("#bgarooma6").addClass("bg-warning");
        }
        //   A7
        if (f1[6] <= setpointroomf1) {
          $("#bgarooma7").addClass("bg-light");
        }
        if (f1[6] > setpointroomf1) {
          $("#bgarooma7").removeClass("bg-light");
          $("#bgarooma7").addClass("bg-warning");
        }
        //   A8
        if (f1[7] <= setpointroomf1) {
          $("#bgarooma8").addClass("bg-light");
        }
        if (f1[7] > setpointroomf1) {
          $("#bgarooma8").removeClass("bg-light");
          $("#bgarooma8").addClass("bg-warning");
        }
        //   A9
        if (f1[8] <= setpointroomf1) {
          $("#bgarooma9").addClass("bg-light");
        }
        if (f1[8] > setpointroomf1) {
          $("#bgarooma9").removeClass("bg-light");
          $("#bgarooma9").addClass("bg-warning");
        }
        //   A10
        if (f1[9] <= setpointroomf1) {
          $("#bgarooma10").addClass("bg-light");
        }
        if (f1[9] > setpointroomf1) {
          $("#bgarooma10").removeClass("bg-light");
          $("#bgarooma10").addClass("bg-warning");
        }
        //   A11
        if (f1[10] <= setpointroomf1) {
          $("#bgarooma11").addClass("bg-light");
        }
        if (f1[10] > setpointroomf1) {
          $("#bgarooma11").removeClass("bg-light");
          $("#bgarooma11").addClass("bg-warning");
        }
        //   A12
        if (f1[11] <= setpointroomf1) {
          $("#bgarooma12").addClass("bg-light");
        }
        if (f1[11] > setpointroomf1) {
          $("#bgarooma12").removeClass("bg-light");
          $("#bgarooma12").addClass("bg-warning");
        }
        //   floor2
        //    Walkway
        if (f2[0] <= setpointroomf2) {
          $("#bgaroomwalkwayf2").addClass("bg-light");
        }
        if (f2[0] > setpointroomf2) {
          $("#bgaroomwalkwayf2").removeClass("bg-light");
          $("#bgaroomwalkwayf2").addClass("bg-warning");
        }
        //    room201
        if (f2[1] <= setpointroomf2) {
          $("#bgaroom201").addClass("bg-light");
        }
        if (f2[1] > setpointroomf2) {
          $("#bgaroom201").removeClass("bg-light");
          $("#bgaroom201").addClass("bg-warning");
        }
        //    room202
        if (f2[2] <= setpointroomf2) {
          $("#bgaroom202").addClass("bg-light");
        }
        if (f2[2] > setpointroomf2) {
          $("#bgaroom202").removeClass("bg-light");
          $("#bgaroom202").addClass("bg-warning");
        }
        //    room203
        if (f2[3] <= setpointroomf2) {
          $("#bgaroom203").addClass("bg-light");
        }
        if (f2[3] > setpointroomf2) {
          $("#bgaroom203").removeClass("bg-light");
          $("#bgaroom203").addClass("bg-warning");
        }
        //    room204
        if (f2[4] <= setpointroomf2) {
          $("#bgaroom204").addClass("bg-light");
        }
        if (f2[4] > setpointroomf2) {
          $("#bgaroom204").removeClass("bg-light");
          $("#bgaroom204").addClass("bg-warning");
        }
        //    room205
        if (f2[5] <= setpointroomf2) {
          $("#bgaroom205").addClass("bg-light");
        }
        if (f2[5] > setpointroomf2) {
          $("#bgaroom205").removeClass("bg-light");
          $("#bgaroom205").addClass("bg-warning");
        }
        //    room206
        if (f2[6] <= setpointroomf2) {
          $("#bgaroom206").addClass("bg-light");
        }
        if (f2[6] > setpointroomf2) {
          $("#bgaroom206").removeClass("bg-light");
          $("#bgaroom206").addClass("bg-warning");
        }
        //    room207
        if (f2[7] <= setpointroomf2) {
          $("#bgaroom207").addClass("bg-light");
        }
        if (f2[7] > setpointroomf2) {
          $("#bgaroom207").removeClass("bg-light");
          $("#bgaroom207").addClass("bg-warning");
        }
        //    room208
        if (f2[8] <= setpointroomf2) {
          $("#bgaroom208").addClass("bg-light");
        }
        if (f2[8] > setpointroomf2) {
          $("#bgaroom208").removeClass("bg-light");
          $("#bgaroom208").addClass("bg-warning");
        }
        //    room209
        if (f2[9] <= setpointroomf2) {
          $("#bgaroom209").addClass("bg-light");
        }
        if (f2[9] > setpointroomf2) {
          $("#bgaroom209").removeClass("bg-light");
          $("#bgaroom209").addClass("bg-warning");
        }
        //    room210
        if (f2[10] <= setpointroomf2) {
          $("#bgaroom210").addClass("bg-light");
        }
        if (f2[10] > setpointroomf2) {
          $("#bgaroom210").removeClass("bg-light");
          $("#bgaroom210").addClass("bg-warning");
        }
        //    room211
        if (f2[11] <= setpointroomf2) {
          $("#bgaroom211").addClass("bg-light");
        }
        if (f2[11] > setpointroomf2) {
          $("#bgaroom211").removeClass("bg-light");
          $("#bgaroom211").addClass("bg-warning");
        }
        //    room212
        if (f2[12] <= setpointroomf2) {
          $("#bgaroom212").addClass("bg-light");
        }
        if (f2[12] > setpointroomf2) {
          $("#bgaroom212").removeClass("bg-light");
          $("#bgaroom212").addClass("bg-warning");
        }
        //    room213
        if (f2[13] <= setpointroomf2) {
          $("#bgaroom213").addClass("bg-light");
        }
        if (f2[13] > setpointroomf2) {
          $("#bgaroom213").removeClass("bg-light");
          $("#bgaroom213").addClass("bg-warning");
        }
        //    room214
        if (f2[14] <= setpointroomf2) {
          $("#bgaroom214").addClass("bg-light");
        }
        if (f2[14] > setpointroomf2) {
          $("#bgaroom214").removeClass("bg-light");
          $("#bgaroom214").addClass("bg-warning");
        }
        //    room215
        if (f2[15] <= setpointroomf2) {
          $("#bgaroom215").addClass("bg-light");
        }
        if (f2[15] > setpointroomf2) {
          $("#bgaroom215").removeClass("bg-light");
          $("#bgaroom215").addClass("bg-warning");
        }
        //    room216
        if (f2[16] <= setpointroomf2) {
          $("#bgaroom216").addClass("bg-light");
        }
        if (f2[16] > setpointroomf2) {
          $("#bgaroom216").removeClass("bg-light");
          $("#bgaroom216").addClass("bg-warning");
        }
        //    room217
        if (f2[17] <= setpointroomf2) {
          $("#bgaroom217").addClass("bg-light");
        }
        if (f2[17] > setpointroomf2) {
          $("#bgaroom217").removeClass("bg-light");
          $("#bgaroom217").addClass("bg-warning");
        }
        //   floor3
        //    Walkway
        if (f3[0] <= setpointroomf3) {
          $("#bgaroomwalkwayf3").addClass("bg-light");
        }
        if (f3[0] > setpointroomf3) {
          $("#bgaroomwalkwayf3").removeClass("bg-light");
          $("#bgaroomwalkwayf3").addClass("bg-warning");
        }
        //    room301
        if (f3[1] <= setpointroomf3) {
          $("#bgaroom301").addClass("bg-light");
        }
        if (f3[1] > setpointroomf3) {
          $("#bgaroom301").removeClass("bg-light");
          $("#bgaroom301").addClass("bg-warning");
        }
        //    room302
        if (f3[2] <= setpointroomf3) {
          $("#bgaroom302").addClass("bg-light");
        }
        if (f3[2] > setpointroomf3) {
          $("#bgaroom302").removeClass("bg-light");
          $("#bgaroom302").addClass("bg-warning");
        }
        //    room303
        if (f3[3] <= setpointroomf3) {
          $("#bgaroom303").addClass("bg-light");
        }
        if (f3[3] > setpointroomf3) {
          $("#bgaroom303").removeClass("bg-light");
          $("#bgaroom303").addClass("bg-warning");
        }
        //    room304
        if (f3[4] <= setpointroomf3) {
          $("#bgaroom304").addClass("bg-light");
        }
        if (f3[4] > setpointroomf3) {
          $("#bgaroom304").removeClass("bg-light");
          $("#bgaroom304").addClass("bg-warning");
        }
        //    room305
        if (f3[5] <= setpointroomf3) {
          $("#bgaroom305").addClass("bg-light");
        }
        if (f3[5] > setpointroomf3) {
          $("#bgaroom305").removeClass("bg-light");
          $("#bgaroom305").addClass("bg-warning");
        }
        //    room306
        if (f3[6] <= setpointroomf3) {
          $("#bgaroom306").addClass("bg-light");
        }
        if (f3[6] > setpointroomf3) {
          $("#bgaroom306").removeClass("bg-light");
          $("#bgaroom306").addClass("bg-warning");
        }
        //    room307
        if (f3[7] <= setpointroomf3) {
          $("#bgaroom307").addClass("bg-light");
        }
        if (f3[7] > setpointroomf3) {
          $("#bgaroom307").removeClass("bg-light");
          $("#bgaroom307").addClass("bg-warning");
        }
        //    room308
        if (f3[8] <= setpointroomf3) {
          $("#bgaroom308").addClass("bg-light");
        }
        if (f3[8] > setpointroomf3) {
          $("#bgaroom308").removeClass("bg-light");
          $("#bgaroom308").addClass("bg-warning");
        }
        //    room309
        if (f3[9] <= setpointroomf3) {
          $("#bgaroom309").addClass("bg-light");
        }
        if (f3[9] > setpointroomf3) {
          $("#bgaroom309").removeClass("bg-light");
          $("#bgaroom309").addClass("bg-warning");
        }
        //    room310
        if (f3[10] <= setpointroomf3) {
          $("#bgaroom310").addClass("bg-light");
        }
        if (f3[10] > setpointroomf3) {
          $("#bgaroom310").removeClass("bg-light");
          $("#bgaroom310").addClass("bg-warning");
        }
        //    room311
        if (f3[11] <= setpointroomf3) {
          $("#bgaroom311").addClass("bg-light");
        }
        if (f3[11] > setpointroomf3) {
          $("#bgaroom311").removeClass("bg-light");
          $("#bgaroom311").addClass("bg-warning");
        }
        //    room312
        if (f3[12] <= setpointroomf3) {
          $("#bgaroom312").addClass("bg-light");
        }
        if (f3[12] > setpointroomf3) {
          $("#bgaroom312").removeClass("bg-light");
          $("#bgaroom312").addClass("bg-warning");
        }
        //    room313
        if (f3[13] <= setpointroomf3) {
          $("#bgaroom313").addClass("bg-light");
        }
        if (f3[13] > setpointroomf3) {
          $("#bgaroom313").removeClass("bg-light");
          $("#bgaroom313").addClass("bg-warning");
        }
        //    room314
        if (f3[14] <= setpointroomf3) {
          $("#bgaroom314").addClass("bg-light");
        }
        if (f3[14] > setpointroomf3) {
          $("#bgaroom314").removeClass("bg-light");
          $("#bgaroom314").addClass("bg-warning");
        }
        //    room315
        if (f3[15] <= setpointroomf3) {
          $("#bgaroom315").addClass("bg-light");
        }
        if (f3[15] > setpointroomf3) {
          $("#bgaroom315").removeClass("bg-light");
          $("#bgaroom315").addClass("bg-warning");
        }
        //    room316
        if (f3[16] <= setpointroomf3) {
          $("#bgaroom316").addClass("bg-light");
        }
        if (f3[16] > setpointroomf3) {
          $("#bgaroom316").removeClass("bg-light");
          $("#bgaroom316").addClass("bg-warning");
        }
        //    room317
        if (f3[17] <= setpointroomf3) {
          $("#bgaroom317").addClass("bg-light");
        }
        if (f3[17] > setpointroomf3) {
          $("#bgaroom317").removeClass("bg-light");
          $("#bgaroom317").addClass("bg-warning");
        }
        //   floor4
        //    Walkway
        if (f4[0] <= setpointroomf4) {
          $("#bgaroomwalkwayf4").addClass("bg-light");
        }
        if (f4[0] > setpointroomf4) {
          $("#bgaroomwalkwayf4").removeClass("bg-light");
          $("#bgaroomwalkwayf4").addClass("bg-warning");
        }
        //    room401
        if (f4[1] <= setpointroomf4) {
          $("#bgaroom401").addClass("bg-light");
        }
        if (f4[1] > setpointroomf4) {
          $("#bgaroom401").removeClass("bg-light");
          $("#bgaroom401").addClass("bg-warning");
        }
        //    room402
        if (f4[2] <= setpointroomf4) {
          $("#bgaroom402").addClass("bg-light");
        }
        if (f4[2] > setpointroomf4) {
          $("#bgaroom402").removeClass("bg-light");
          $("#bgaroom402").addClass("bg-warning");
        }
        //    room403
        if (f4[3] <= setpointroomf4) {
          $("#bgaroom403").addClass("bg-light");
        }
        if (f4[3] > setpointroomf4) {
          $("#bgaroom403").removeClass("bg-light");
          $("#bgaroom403").addClass("bg-warning");
        }
        //    room404
        if (f4[4] <= setpointroomf4) {
          $("#bgaroom404").addClass("bg-light");
        }
        if (f4[4] > setpointroomf4) {
          $("#bgaroom404").removeClass("bg-light");
          $("#bgaroom404").addClass("bg-warning");
        }
        //    room405
        if (f4[5] <= setpointroomf4) {
          $("#bgaroom405").addClass("bg-light");
        }
        if (f4[5] > setpointroomf4) {
          $("#bgaroom405").removeClass("bg-light");
          $("#bgaroom405").addClass("bg-warning");
        }
        //    room406
        if (f4[6] <= setpointroomf4) {
          $("#bgaroom406").addClass("bg-light");
        }
        if (f4[6] > setpointroomf4) {
          $("#bgaroom406").removeClass("bg-light");
          $("#bgaroom406").addClass("bg-warning");
        }
        //    room407
        if (f4[7] <= setpointroomf4) {
          $("#bgaroom407").addClass("bg-light");
        }
        if (f4[7] > setpointroomf4) {
          $("#bgaroom407").removeClass("bg-light");
          $("#bgaroom407").addClass("bg-warning");
        }
        //    room408
        if (f4[8] <= setpointroomf4) {
          $("#bgaroom408").addClass("bg-light");
        }
        if (f4[8] > setpointroomf4) {
          $("#bgaroom408").removeClass("bg-light");
          $("#bgaroom408").addClass("bg-warning");
        }
        //    room409
        if (f4[9] <= setpointroomf4) {
          $("#bgaroom409").addClass("bg-light");
        }
        if (f4[9] > setpointroomf4) {
          $("#bgaroom409").removeClass("bg-light");
          $("#bgaroom409").addClass("bg-warning");
        }
        //    room410
        if (f4[10] <= setpointroomf4) {
          $("#bgaroom410").addClass("bg-light");
        }
        if (f4[10] > setpointroomf4) {
          $("#bgaroom410").removeClass("bg-light");
          $("#bgaroom410").addClass("bg-warning");
        }
        //    room411
        if (f4[11] <= setpointroomf4) {
          $("#bgaroom411").addClass("bg-light");
        }
        if (f4[11] > setpointroomf4) {
          $("#bgaroom411").removeClass("bg-light");
          $("#bgaroom411").addClass("bg-warning");
        }
        //    room412
        if (f4[12] <= setpointroomf4) {
          $("#bgaroom412").addClass("bg-light");
        }
        if (f4[12] > setpointroomf4) {
          $("#bgaroom412").removeClass("bg-light");
          $("#bgaroom412").addClass("bg-warning");
        }
        //    room413
        if (f4[13] <= setpointroomf4) {
          $("#bgaroom413").addClass("bg-light");
        }
        if (f4[13] > setpointroomf4) {
          $("#bgaroom413").removeClass("bg-light");
          $("#bgaroom413").addClass("bg-warning");
        }
        //    room414
        if (f4[14] <= setpointroomf4) {
          $("#bgaroom414").addClass("bg-light");
        }
        if (f4[14] > setpointroomf4) {
          $("#bgaroom414").removeClass("bg-light");
          $("#bgaroom414").addClass("bg-warning");
        }
        //    room415
        if (f4[15] <= setpointroomf4) {
          $("#bgaroom415").addClass("bg-light");
        }
        if (f4[15] > setpointroomf4) {
          $("#bgaroom415").removeClass("bg-light");
          $("#bgaroom415").addClass("bg-warning");
        }
        //    room416
        if (f4[16] <= setpointroomf4) {
          $("#bgaroom416").addClass("bg-light");
        }
        if (f4[16] > setpointroomf4) {
          $("#bgaroom416").removeClass("bg-light");
          $("#bgaroom416").addClass("bg-warning");
        }
        //    room417
        if (f4[17] <= setpointroomf4) {
          $("#bgaroom417").addClass("bg-light");
        }
        if (f4[17] > setpointroomf4) {
          $("#bgaroom417").removeClass("bg-light");
          $("#bgaroom417").addClass("bg-warning");
        }
        //   floor5
        //    Walkway
        if (f5[0] <= setpointroomf5) {
            $("#bgaroomwalkwayf5").addClass("bg-light");
          }
          if (f5[0] > setpointroomf5) {
            $("#bgaroomwalkwayf5").removeClass("bg-light");
            $("#bgaroomwalkwayf5").addClass("bg-warning");
          }
          //    room501
          if (f5[1] <= setpointroomf5) {
            $("#bgaroom501").addClass("bg-light");
          }
          if (f5[1] > setpointroomf5) {
            $("#bgaroom501").removeClass("bg-light");
            $("#bgaroom501").addClass("bg-warning");
          }
          //    room502
          if (f5[2] <= setpointroomf5) {
            $("#bgaroom502").addClass("bg-light");
          }
          if (f5[2] > setpointroomf5) {
            $("#bgaroom502").removeClass("bg-light");
            $("#bgaroom502").addClass("bg-warning");
          }
          //    room503
          if (f5[3] <= setpointroomf5) {
            $("#bgaroom503").addClass("bg-light");
          }
          if (f5[3] > setpointroomf5) {
            $("#bgaroom503").removeClass("bg-light");
            $("#bgaroom503").addClass("bg-warning");
          }
          //    room504
          if (f5[4] <= setpointroomf5) {
            $("#bgaroom504").addClass("bg-light");
          }
          if (f5[4] > setpointroomf5) {
            $("#bgaroom504").removeClass("bg-light");
            $("#bgaroom504").addClass("bg-warning");
          }
          //    room505
          if (f5[5] <= setpointroomf5) {
            $("#bgaroom505").addClass("bg-light");
          }
          if (f5[5] > setpointroomf5) {
            $("#bgaroom505").removeClass("bg-light");
            $("#bgaroom505").addClass("bg-warning");
          }
          //    room506
          if (f5[6] <= setpointroomf5) {
            $("#bgaroom506").addClass("bg-light");
          }
          if (f5[6] > setpointroomf5) {
            $("#bgaroom506").removeClass("bg-light");
            $("#bgaroom506").addClass("bg-warning");
          }
          //    room507
          if (f5[7] <= setpointroomf5) {
            $("#bgaroom507").addClass("bg-light");
          }
          if (f5[7] > setpointroomf5) {
            $("#bgaroom507").removeClass("bg-light");
            $("#bgaroom507").addClass("bg-warning");
          }
          //    room508
          if (f5[8] <= setpointroomf5) {
            $("#bgaroom508").addClass("bg-light");
          }
          if (f5[8] > setpointroomf5) {
            $("#bgaroom508").removeClass("bg-light");
            $("#bgaroom508").addClass("bg-warning");
          }
          //    room509
          if (f5[9] <= setpointroomf5) {
            $("#bgaroom509").addClass("bg-light");
          }
          if (f5[9] > setpointroomf5) {
            $("#bgaroom509").removeClass("bg-light");
            $("#bgaroom509").addClass("bg-warning");
          }
          //    room510
          if (f5[10] <= setpointroomf5) {
            $("#bgaroom510").addClass("bg-light");
          }
          if (f5[10] > setpointroomf5) {
            $("#bgaroom510").removeClass("bg-light");
            $("#bgaroom510").addClass("bg-warning");
          }
          //    room511
          if (f5[11] <= setpointroomf5) {
            $("#bgaroom511").addClass("bg-light");
          }
          if (f5[11] > setpointroomf5) {
            $("#bgaroom511").removeClass("bg-light");
            $("#bgaroom511").addClass("bg-warning");
          }
          //    room512
          if (f5[12] <= setpointroomf5) {
            $("#bgaroom512").addClass("bg-light");
          }
          if (f5[12] > setpointroomf5) {
            $("#bgaroom512").removeClass("bg-light");
            $("#bgaroom512").addClass("bg-warning");
          }
          //    room513
          if (f5[13] <= setpointroomf5) {
            $("#bgaroom513").addClass("bg-light");
          }
          if (f5[13] > setpointroomf5) {
            $("#bgaroom513").removeClass("bg-light");
            $("#bgaroom513").addClass("bg-warning");
          }
          //    room514
          if (f5[14] <= setpointroomf5) {
            $("#bgaroom514").addClass("bg-light");
          }
          if (f5[14] > setpointroomf5) {
            $("#bgaroom514").removeClass("bg-light");
            $("#bgaroom514").addClass("bg-warning");
          }
          //    room515
          if (f5[15] <= setpointroomf5) {
            $("#bgaroom515").addClass("bg-light");
          }
          if (f5[15] > setpointroomf5) {
            $("#bgaroom515").removeClass("bg-light");
            $("#bgaroom515").addClass("bg-warning");
          }
          //    room516
          if (f5[16] <= setpointroomf5) {
            $("#bgaroom516").addClass("bg-light");
          }
          if (f5[16] > setpointroomf5) {
            $("#bgaroom516").removeClass("bg-light");
            $("#bgaroom516").addClass("bg-warning");
          }
          //    room517
          if (f5[17] <= setpointroomf5) {
            $("#bgaroom517").addClass("bg-light");
          }
          if (f5[17] > setpointroomf5) {
            $("#bgaroom517").removeClass("bg-light");
            $("#bgaroom517").addClass("bg-warning");
          }
      },
      error: function (error_data) {
        console.log("error");
        console.log(error_data);
      },  
    });
  }, 5000);
});
