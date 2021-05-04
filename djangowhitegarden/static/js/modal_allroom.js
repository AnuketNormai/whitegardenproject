$(document).ready(function () {
    var endpoint = "/api/ampkwhtoday";
    var f1 = [];
    var todaykwh1 = [];
    var f2 = [];
    var todaykwh2 = [];
    var f3 = [];
    var todaykwh3 = [];
    var f4 = [];
    var todaykwh4 = [];
    var f5 = [];
    var todaykwh5 = [];
    var labels = [];
  
    var setpointroomf1 = 0.3;
    var setpointroomf2 = 0.2;
    var setpointroomf3 = 0.3;
    var setpointroomf4 = 0.2;
    var setpointroomf5 = 0.2;
  
    var powerOn_color = "#00FF00"; //set color for device has normal #10B510
    var powerOff_color = "#A9A9A9"; //set color for device has normal #10B510
  
    setInterval(function () {
      $.ajax({
        method: "GET",
        url: endpoint,
        success: function (data) {
          labels = data.labels;
          f1 = data.floor1; //from apiroom.py
          todaykwh1 = data.todaykwh1 //from apiampkwhtoday.py
          f2 = data.floor2; //from apiroom.py
          todaykwh2 = data.todaykwh2 //from apiampkwhtoday.py
          f3 = data.floor3; //from apiroom.py
          todaykwh3 = data.todaykwh3 //from apiampkwhtoday.py
          f4 = data.floor4; //from apiroom.py
          todaykwh4 = data.todaykwh4 //from apiampkwhtoday.py
          f5 = data.floor5; //from apiroom.py
          todaykwh5 = data.todaykwh5 //from apiampkwhtoday.py

          // Floor 1
          $("#todayampA1").text(f1[0].toFixed(2) + " แอมป์");
          $("#todaykwhA1").text(todaykwh1[0].toFixed(2) + " หน่วย");

          $("#todayampA2").text(f1[1].toFixed(2) + " แอมป์");
          $("#todaykwhA2").text(todaykwh1[1].toFixed(2) + " หน่วย");

          $("#todayampA3").text(f1[2].toFixed(2) + " แอมป์");
          $("#todaykwhA3").text(todaykwh1[2].toFixed(2) + " หน่วย");

          $("#todayampA4").text(f1[3].toFixed(2) + " แอมป์");
          $("#todaykwhA4").text(todaykwh1[3].toFixed(2) + " หน่วย");

          $("#todayampA5").text(f1[4].toFixed(2) + " แอมป์");
          $("#todaykwhA5").text(todaykwh1[4].toFixed(2) + " หน่วย");

          $("#todayampA6").text(f1[5].toFixed(2) + " แอมป์");
          $("#todaykwhA6").text(todaykwh1[5].toFixed(2) + " หน่วย");

          $("#todayampA7").text(f1[6].toFixed(2) + " แอมป์");
          $("#todaykwhA7").text(todaykwh1[6].toFixed(2) + " หน่วย");

          $("#todayampA8").text(f1[7].toFixed(2) + " แอมป์");
          $("#todaykwhA8").text(todaykwh1[7].toFixed(2) + " หน่วย");

          $("#todayampA9").text(f1[8].toFixed(2) + " แอมป์");
          $("#todaykwhA9").text(todaykwh1[8].toFixed(2) + " หน่วย");

          $("#todayampA10").text(f1[9].toFixed(2) + " แอมป์");
          $("#todaykwhA10").text(todaykwh1[9].toFixed(2) + " หน่วย");

          $("#todayampA11").text(f1[10].toFixed(2) + " แอมป์");
          $("#todaykwhA11").text(todaykwh1[10].toFixed(2) + " หน่วย");

          $("#todayampA12").text(f1[11].toFixed(2) + " แอมป์");
          $("#todaykwhA12").text(todaykwh1[11].toFixed(2) + " หน่วย");
   
          // Floor 2
          $("#todayampwalkwayf2").text(f2[0].toFixed(2) + " แอมป์");
          $("#todaykwhwalkwayf2").text(todaykwh2[0].toFixed(2) + " หน่วย");

          $("#todayamp201").text(f2[1].toFixed(2) + " แอมป์");
          $("#todaykwh201").text(todaykwh2[1].toFixed(2) + " หน่วย");

          $("#todayamp202").text(f2[2].toFixed(2) + " แอมป์");
          $("#todaykwh202").text(todaykwh2[2].toFixed(2) + " หน่วย");

          $("#todayamp203").text(f2[3].toFixed(2) + " แอมป์");
          $("#todaykwh203").text(todaykwh2[3].toFixed(2) + " หน่วย");

          $("#todayamp204").text(f2[4].toFixed(2) + " แอมป์");
          $("#todaykwh204").text(todaykwh2[4].toFixed(2) + " หน่วย");

          $("#todayamp205").text(f2[5].toFixed(2) + " แอมป์");
          $("#todaykwh205").text(todaykwh2[5].toFixed(2) + " หน่วย");

          $("#todayamp206").text(f2[6].toFixed(2) + " แอมป์");
          $("#todaykwh206").text(todaykwh2[6].toFixed(2) + " หน่วย");

          $("#todayamp207").text(f2[7].toFixed(2) + " แอมป์");
          $("#todaykwh207").text(todaykwh2[7].toFixed(2) + " หน่วย");

          $("#todayamp208").text(f2[8].toFixed(2) + " แอมป์");
          $("#todaykwh208").text(todaykwh2[8].toFixed(2) + " หน่วย");

          $("#todayamp209").text(f2[9].toFixed(2) + " แอมป์");
          $("#todaykwh209").text(todaykwh2[9].toFixed(2) + " หน่วย");

          $("#todayamp210").text(f2[10].toFixed(2) + " แอมป์");
          $("#todaykwh210").text(todaykwh2[10].toFixed(2) + " หน่วย");

          $("#todayamp211").text(f2[11].toFixed(2) + " แอมป์");
          $("#todaykwh211").text(todaykwh2[11].toFixed(2) + " หน่วย");

          $("#todayamp212").text(f2[12].toFixed(2) + " แอมป์");
          $("#todaykwh212").text(todaykwh2[12].toFixed(2) + " หน่วย");

          $("#todayamp213").text(f2[13].toFixed(2) + " แอมป์");
          $("#todaykwh213").text(todaykwh2[13].toFixed(2) + " หน่วย");

          $("#todayamp214").text(f2[14].toFixed(2) + " แอมป์");
          $("#todaykwh214").text(todaykwh2[14].toFixed(2) + " หน่วย");

          $("#todayamp215").text(f2[15].toFixed(2) + " แอมป์");
          $("#todaykwh215").text(todaykwh2[15].toFixed(2) + " หน่วย");

          $("#todayamp216").text(f2[16].toFixed(2) + " แอมป์");
          $("#todaykwh216").text(todaykwh2[16].toFixed(2) + " หน่วย");

          $("#todayamp217").text(f2[17].toFixed(2) + " แอมป์");
          $("#todaykwh217").text(todaykwh2[17].toFixed(2) + " หน่วย");

          // Floor 3
          $("#todayampwalkwayf3").text(f3[0].toFixed(2) + " แอมป์");
          $("#todaykwhwalkwayf3").text(todaykwh3[0].toFixed(2) + " หน่วย");

          $("#todayamp301").text(f3[1].toFixed(2) + " แอมป์");
          $("#todaykwh301").text(todaykwh3[1].toFixed(2) + " หน่วย");

          $("#todayamp302").text(f3[2].toFixed(2) + " แอมป์");
          $("#todaykwh302").text(todaykwh3[2].toFixed(2) + " หน่วย");

          $("#todayamp303").text(f3[3].toFixed(2) + " แอมป์");
          $("#todaykwh303").text(todaykwh3[3].toFixed(2) + " หน่วย");

          $("#todayamp304").text(f3[4].toFixed(2) + " แอมป์");
          $("#todaykwh304").text(todaykwh3[4].toFixed(2) + " หน่วย");

          $("#todayamp305").text(f3[5].toFixed(2) + " แอมป์");
          $("#todaykwh305").text(todaykwh3[5].toFixed(2) + " หน่วย");

          $("#todayamp306").text(f3[6].toFixed(2) + " แอมป์");
          $("#todaykwh306").text(todaykwh3[6].toFixed(2) + " หน่วย");

          $("#todayamp307").text(f3[7].toFixed(2) + " แอมป์");
          $("#todaykwh307").text(todaykwh3[7].toFixed(2) + " หน่วย");

          $("#todayamp308").text(f3[8].toFixed(2) + " แอมป์");
          $("#todaykwh308").text(todaykwh3[8].toFixed(2) + " หน่วย");

          $("#todayamp309").text(f3[9].toFixed(2) + " แอมป์");
          $("#todaykwh309").text(todaykwh3[9].toFixed(2) + " หน่วย");

          $("#todayamp310").text(f3[10].toFixed(2) + " แอมป์");
          $("#todaykwh310").text(todaykwh3[10].toFixed(2) + " หน่วย");

          $("#todayamp311").text(f3[11].toFixed(2) + " แอมป์");
          $("#todaykwh311").text(todaykwh3[11].toFixed(2) + " หน่วย");

          $("#todayamp312").text(f3[12].toFixed(2) + " แอมป์");
          $("#todaykwh312").text(todaykwh3[12].toFixed(2) + " หน่วย");

          $("#todayamp313").text(f3[13].toFixed(2) + " แอมป์");
          $("#todaykwh313").text(todaykwh3[13].toFixed(2) + " หน่วย");

          $("#todayamp314").text(f3[14].toFixed(2) + " แอมป์");
          $("#todaykwh314").text(todaykwh3[14].toFixed(2) + " หน่วย");

          $("#todayamp315").text(f3[15].toFixed(2) + " แอมป์");
          $("#todaykwh315").text(todaykwh3[15].toFixed(2) + " หน่วย");

          $("#todayamp316").text(f3[16].toFixed(2) + " แอมป์");
          $("#todaykwh316").text(todaykwh3[16].toFixed(2) + " หน่วย");

          $("#todayamp317").text(f3[17].toFixed(2) + " แอมป์");
          $("#todaykwh317").text(todaykwh3[17].toFixed(2) + " หน่วย");

          // Floor 4
          $("#todayampwalkwayf4").text(f4[0].toFixed(2) + " แอมป์");
          $("#todaykwhwalkwayf4").text(todaykwh4[0].toFixed(2) + " หน่วย");

          $("#todayamp401").text(f4[1].toFixed(2) + " แอมป์");
          $("#todaykwh401").text(todaykwh4[1].toFixed(2) + " หน่วย");

          $("#todayamp402").text(f4[2].toFixed(2) + " แอมป์");
          $("#todaykwh402").text(todaykwh4[2].toFixed(2) + " หน่วย");

          $("#todayamp403").text(f4[3].toFixed(2) + " แอมป์");
          $("#todaykwh403").text(todaykwh4[3].toFixed(2) + " หน่วย");

          $("#todayamp404").text(f4[4].toFixed(2) + " แอมป์");
          $("#todaykwh404").text(todaykwh4[4].toFixed(2) + " หน่วย");

          $("#todayamp405").text(f4[5].toFixed(2) + " แอมป์");
          $("#todaykwh405").text(todaykwh4[5].toFixed(2) + " หน่วย");

          $("#todayamp406").text(f4[6].toFixed(2) + " แอมป์");
          $("#todaykwh406").text(todaykwh4[6].toFixed(2) + " หน่วย");

          $("#todayamp407").text(f4[7].toFixed(2) + " แอมป์");
          $("#todaykwh407").text(todaykwh4[7].toFixed(2) + " หน่วย");

          $("#todayamp408").text(f4[8].toFixed(2) + " แอมป์");
          $("#todaykwh408").text(todaykwh4[8].toFixed(2) + " หน่วย");

          $("#todayamp409").text(f4[9].toFixed(2) + " แอมป์");
          $("#todaykwh409").text(todaykwh4[9].toFixed(2) + " หน่วย");

          $("#todayamp410").text(f4[10].toFixed(2) + " แอมป์");
          $("#todaykwh410").text(todaykwh4[10].toFixed(2) + " หน่วย");

          $("#todayamp411").text(f4[11].toFixed(2) + " แอมป์");
          $("#todaykwh411").text(todaykwh4[11].toFixed(2) + " หน่วย");

          $("#todayamp412").text(f4[12].toFixed(2) + " แอมป์");
          $("#todaykwh412").text(todaykwh4[12].toFixed(2) + " หน่วย");

          $("#todayamp413").text(f4[13].toFixed(2) + " แอมป์");
          $("#todaykwh413").text(todaykwh4[13].toFixed(2) + " หน่วย");

          $("#todayamp414").text(f4[14].toFixed(2) + " แอมป์");
          $("#todaykwh414").text(todaykwh4[14].toFixed(2) + " หน่วย");

          $("#todayamp415").text(f4[15].toFixed(2) + " แอมป์");
          $("#todaykwh415").text(todaykwh4[15].toFixed(2) + " หน่วย");

          $("#todayamp416").text(f4[16].toFixed(2) + " แอมป์");
          $("#todaykwh416").text(todaykwh4[16].toFixed(2) + " หน่วย");

          $("#todayamp417").text(f4[17].toFixed(2) + " แอมป์");
          $("#todaykwh417").text(todaykwh4[17].toFixed(2) + " หน่วย");

          // Floor 5
          $("#todayampwalkwayf5").text(f5[0].toFixed(2) + " แอมป์");
          $("#todaykwhwalkwayf5").text(todaykwh5[0].toFixed(2) + " หน่วย");

          $("#todayamp501").text(f5[1].toFixed(2) + " แอมป์");
          $("#todaykwh501").text(todaykwh5[1].toFixed(2) + " หน่วย");

          $("#todayamp502").text(f5[2].toFixed(2) + " แอมป์");
          $("#todaykwh502").text(todaykwh5[2].toFixed(2) + " หน่วย");

          $("#todayamp503").text(f5[3].toFixed(2) + " แอมป์");
          $("#todaykwh503").text(todaykwh5[3].toFixed(2) + " หน่วย");

          $("#todayamp504").text(f5[4].toFixed(2) + " แอมป์");
          $("#todaykwh504").text(todaykwh5[4].toFixed(2) + " หน่วย");

          $("#todayamp505").text(f5[5].toFixed(2) + " แอมป์");
          $("#todaykwh505").text(todaykwh5[5].toFixed(2) + " หน่วย");

          $("#todayamp506").text(f5[6].toFixed(2) + " แอมป์");
          $("#todaykwh506").text(todaykwh5[6].toFixed(2) + " หน่วย");

          $("#todayamp507").text(f5[7].toFixed(2) + " แอมป์");
          $("#todaykwh507").text(todaykwh5[7].toFixed(2) + " หน่วย");

          $("#todayamp508").text(f5[8].toFixed(2) + " แอมป์");
          $("#todaykwh508").text(todaykwh5[8].toFixed(2) + " หน่วย");

          $("#todayamp509").text(f5[9].toFixed(2) + " แอมป์");
          $("#todaykwh509").text(todaykwh5[9].toFixed(2) + " หน่วย");

          $("#todayamp510").text(f5[10].toFixed(2) + " แอมป์");
          $("#todaykwh510").text(todaykwh5[10].toFixed(2) + " หน่วย");

          $("#todayamp511").text(f5[11].toFixed(2) + " แอมป์");
          $("#todaykwh511").text(todaykwh5[11].toFixed(2) + " หน่วย");

          $("#todayamp512").text(f5[12].toFixed(2) + " แอมป์");
          $("#todaykwh512").text(todaykwh5[12].toFixed(2) + " หน่วย");

          $("#todayamp513").text(f5[13].toFixed(2) + " แอมป์");
          $("#todaykwh513").text(todaykwh5[13].toFixed(2) + " หน่วย");

          $("#todayamp514").text(f5[14].toFixed(2) + " แอมป์");
          $("#todaykwh514").text(todaykwh5[14].toFixed(2) + " หน่วย");

          $("#todayamp515").text(f5[15].toFixed(2) + " แอมป์");
          $("#todaykwh515").text(todaykwh5[15].toFixed(2) + " หน่วย");

          $("#todayamp516").text(f5[16].toFixed(2) + " แอมป์");
          $("#todaykwh516").text(todaykwh5[16].toFixed(2) + " หน่วย");

          $("#todayamp517").text(f5[17].toFixed(2) + " แอมป์");
          $("#todaykwh517").text(todaykwh5[17].toFixed(2) + " หน่วย");
        },
        error: function (error_data) {
          console.log("error");
          console.log(error_data);
        },
        
        
      });
    }, 5000);
  });
  