$(document).ready(function () {
    var endpoint = "/api/mdb";
    var floor = [];
    var pump = [];
    var other = [];
    var labels = [];
  
    const $kwhdailymain_floor1 = $("#kwhdailymainfloor1");
    const $kwhdailymain_floor2 = $("#kwhdailymainfloor2");
    const $kwhdailymain_floor3 = $("#kwhdailymainfloor3");
    const $kwhdailymain_floor4 = $("#kwhdailymainfloor4");
    const $kwhdailymain_floor5 = $("#kwhdailymainfloor5");
    const $kwhdaily_mainpump = $("#kwhdailymainpump");
    const $kwhdaily_pump1 = $("#kwhdailypump1");
    const $kwhdaily_pump2 = $("#kwhdailypump2");
    const $kwhdaily_pump3 = $("#kwhdailypump3");
    const $kwhdaily_pump4 = $("#kwhdailypump4");
    const $kwhdaily_pump5 = $("#kwhdailypump5");
    const $kwhdaily_pump6 = $("#kwhdailypump6");
    const $kwhdaily_pump7 = $("#kwhdailypump7");
    const $kwhother_airF = $("#kwhairf");
    const $kwhother_building = $("#kwhbuilding");
    const $kwhother_EDB = $("#kwhEDB");
    const $kwhother_miner1 = $("#kwhminer1");
    const $kwhother_miner2 = $("#kwhminer2");
    const $kwhother_miner3 = $("#kwhminer3");

 
  
 
  
    setInterval(function () {
      $.ajax({
        method: "GET",
        url: endpoint,
        success: function (data) {
          labels = data.labels;
          floor = data.floor; //from apimdb.py
          pump = data.pump;
          other = data.other; //from apimdb.py

          $kwhdailymain_floor1.text(floor[0].toFixed(2) + " หน่วย");
          $kwhdailymain_floor2.text(floor[1].toFixed(2) + " หน่วย");
          $kwhdailymain_floor3.text(floor[2].toFixed(2) + " หน่วย");
          $kwhdailymain_floor4.text(floor[3].toFixed(2) + " หน่วย");
          $kwhdailymain_floor5.text(floor[4].toFixed(2) + " หน่วย");
          
          $kwhdaily_mainpump.text(pump[0].toFixed(2) + " หน่วย");
          $kwhdaily_pump1.text(pump[1].toFixed(2) + " หน่วย");
          $kwhdaily_pump2.text(pump[2].toFixed(2) + " หน่วย");
          $kwhdaily_pump3.text(pump[3].toFixed(2) + " หน่วย");
          $kwhdaily_pump4.text(pump[4].toFixed(2) + " หน่วย");
          $kwhdaily_pump5.text(pump[5].toFixed(2) + " หน่วย");
          $kwhdaily_pump6.text(pump[6].toFixed(2) + " หน่วย");
          $kwhdaily_pump7.text(pump[7].toFixed(2) + " หน่วย");

          $kwhother_airF.text(other[0].toFixed(2) + " หน่วย");
          $kwhother_building.text(other[1].toFixed(2) + " หน่วย");
          $kwhother_EDB.text(other[2].toFixed(2) + " หน่วย");
          $kwhother_miner1.text(other[3].toFixed(2) + " หน่วย");
          $kwhother_miner2.text(other[4].toFixed(2) + " หน่วย");
          $kwhother_miner3.text(other[5].toFixed(2) + " หน่วย");
        },
        error: function (error_data) {
          console.log("error");
          console.log(error_data);
        },
      });
    }, 5000);
  });
  