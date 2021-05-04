from influxdb import InfluxDBClient

from rest_framework.views import APIView
from rest_framework.response import Response

### Set Database InfluxDB ###
client = InfluxDBClient(host='52.74.59.121', port=8086, username='dtlab', password='dtlab2019')
client.get_list_database()
#print(client.get_list_database())
client.switch_database('whitegarden')
client.get_list_measurements()

class api_ampkwhtoday_Data(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):

        labels = [
         'A1','A2','A3','A4', 'A5','A6',
         'A7','A8','A9','A10','A11','A12',
         'walkwayf2','201','202','203', '204','205',
         '206','207','208','209','210','211','212',
         '213','214','215','216','217',
         'walkwayf3','301','302','303', '304','305',
         '306','307','308','309','310','311','313',
         '313','314','315','316','317',
         'walkwayf4','401','402','403', '404','405',
         '406','407','408','409','410','411','414',
         '414','414','415','416','417',
         'walkwayf5','501','502','503', '504','505',
         '506','507','508','509','510','511','515',
         '515','515','515','516','517',
        ]

        time = []
        points_ampfloor1 =[]
        List_ampfloor1 =[]
        points_todaykwhfloor1 =[]
        List_todaykwhfloor1 =[]

        points_ampfloor2 =[]
        List_ampfloor2 =[]
        points_todaykwhfloor2 =[]
        List_todaykwhfloor2 =[]

        points_ampfloor3 =[]
        List_ampfloor3 =[]
        points_todaykwhfloor3 =[]
        List_todaykwhfloor3 =[]

        points_ampfloor4 =[]
        List_ampfloor4 =[]
        points_todaykwhfloor4 =[]
        List_todaykwhfloor4 =[]

        points_ampfloor5 =[]
        List_ampfloor5 =[]
        points_todaykwhfloor5 =[]
        List_todaykwhfloor5 =[]


        # Start Floor 1
        #!AmpAir Floor1 query
        qampAir1=client.query('SELECT last("amps1_sbwg99a1m1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qampAir2=client.query('SELECT last("amps1_sbwg99a2m1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qampAir3=client.query('SELECT last("amps1_sbwg99a3m1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qampAir4=client.query('SELECT last("amps1_sbwg99a4m1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qampAir5=client.query('SELECT last("amps_sbwg99a5m1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qampAir6=client.query('SELECT last("amps_sbwg99a6m1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qampAir7=client.query('SELECT last("amps_sbwg99a7m1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qampAir8=client.query('SELECT last("amps_sbwg99a8m1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qampAir9=client.query('SELECT last("amps_sbwg99a9m1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qampAir10=client.query('SELECT last("amps_sbwg99a10m1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qampAir11=client.query('SELECT last("amps_sbwg99a11m1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qampAir12=client.query('SELECT last("amps_sbwg99a12m1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')

        # todo point AmpAir Floor1
        points_ampfloor1.append(qampAir1.get_points(tags={'whitegarden_1': ''})) #index0
        points_ampfloor1.append(qampAir2.get_points(tags={'whitegarden_1': ''})) #index1
        points_ampfloor1.append(qampAir3.get_points(tags={'whitegarden_1': ''})) #index2
        points_ampfloor1.append(qampAir4.get_points(tags={'whitegarden_1': ''})) #index3
        points_ampfloor1.append(qampAir5.get_points(tags={'whitegarden_1': ''})) #index4
        points_ampfloor1.append(qampAir6.get_points(tags={'whitegarden_1': ''})) #index4
        points_ampfloor1.append(qampAir7.get_points(tags={'whitegarden_1': ''})) #index4
        points_ampfloor1.append(qampAir8.get_points(tags={'whitegarden_1': ''})) #index4
        points_ampfloor1.append(qampAir9.get_points(tags={'whitegarden_1': ''})) #index4
        points_ampfloor1.append(qampAir10.get_points(tags={'whitegarden_1': ''})) #index4
        points_ampfloor1.append(qampAir11.get_points(tags={'whitegarden_1': ''})) #index4
        points_ampfloor1.append(qampAir12.get_points(tags={'whitegarden_1': ''})) #index4

        #!todaykwhAir Floor1 query
        qtodaykwhAir1=client.query('SELECT last("kwhtotal_sbwg99a1m1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qtodaykwhAir2=client.query('SELECT last("kwhtotal_sbwg99a2m1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qtodaykwhAir3=client.query('SELECT last("kwhtotal_sbwg99a3m1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qtodaykwhAir4=client.query('SELECT last("kwhtotal_sbwg99a4m1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qtodaykwhAir5=client.query('SELECT last("kwh_sbwg99a5m1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qtodaykwhAir6=client.query('SELECT last("kwh_sbwg99a6m1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qtodaykwhAir7=client.query('SELECT last("kwh_sbwg99a7m1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qtodaykwhAir8=client.query('SELECT last("kwh_sbwg99a8m1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qtodaykwhAir9=client.query('SELECT last("kwh_sbwg99a9m1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qtodaykwhAir10=client.query('SELECT last("kwh_sbwg99a10m1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qtodaykwhAir11=client.query('SELECT last("kwh_sbwg99a11m1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qtodaykwhAir12=client.query('SELECT last("kwh_sbwg99a12m1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')

        # todo point AmpAir Floor1
        points_todaykwhfloor1.append(qtodaykwhAir1.get_points(tags={'whitegarden_1': ''})) #index0
        points_todaykwhfloor1.append(qtodaykwhAir2.get_points(tags={'whitegarden_1': ''})) #index1
        points_todaykwhfloor1.append(qtodaykwhAir3.get_points(tags={'whitegarden_1': ''})) #index2
        points_todaykwhfloor1.append(qtodaykwhAir4.get_points(tags={'whitegarden_1': ''})) #index3
        points_todaykwhfloor1.append(qtodaykwhAir5.get_points(tags={'whitegarden_1': ''})) #index4
        points_todaykwhfloor1.append(qtodaykwhAir6.get_points(tags={'whitegarden_1': ''})) #index4
        points_todaykwhfloor1.append(qtodaykwhAir7.get_points(tags={'whitegarden_1': ''})) #index4
        points_todaykwhfloor1.append(qtodaykwhAir8.get_points(tags={'whitegarden_1': ''})) #index4
        points_todaykwhfloor1.append(qtodaykwhAir9.get_points(tags={'whitegarden_1': ''})) #index4
        points_todaykwhfloor1.append(qtodaykwhAir10.get_points(tags={'whitegarden_1': ''})) #index4
        points_todaykwhfloor1.append(qtodaykwhAir11.get_points(tags={'whitegarden_1': ''})) #index4
        points_todaykwhfloor1.append(qtodaykwhAir12.get_points(tags={'whitegarden_1': ''})) #index4
        # End Floor 1

        # start Floor 2
        # todo floor 2 Amp
        qampWalkwayf2=client.query('SELECT last("amps_sbwg99r200m1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qampRoom_201=client.query('SELECT last("amps_sbwg99r201m1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qampRoom_202=client.query('SELECT last("amps_sbwg99r202m1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qampRoom_203=client.query('SELECT last("amps_sbwg99r203m1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qampRoom_204=client.query('SELECT last("amps_sbwg99r204m1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qampRoom_205=client.query('SELECT last("amps_sbwg99r205m1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qampRoom_206=client.query('SELECT last("amps_sbwg99r206m1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qampRoom_207=client.query('SELECT last("amps_sbwg99r207m1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qampRoom_208=client.query('SELECT last("amps_sbwg99r208m1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qampRoom_209=client.query('SELECT last("amps_sbwg99r209m1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qampRoom_210=client.query('SELECT last("amps_sbwg99r210m1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qampRoom_211=client.query('SELECT last("amps_sbwg99r211m1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qampRoom_212=client.query('SELECT last("amps_sbwg99r212m1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qampRoom_213=client.query('SELECT last("amps_sbwg99r213m1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qampRoom_214=client.query('SELECT last("amps_sbwg99r214m1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qampRoom_215=client.query('SELECT last("amps_sbwg99r215m1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qampRoom_216=client.query('SELECT last("amps_sbwg99r216m1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qampRoom_217=client.query('SELECT last("amps_sbwg99r217m1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')

        # todo point list water level
        points_ampfloor2.append(qampWalkwayf2.get_points(tags={'whitegarden_1': ''})) #index0
        points_ampfloor2.append(qampRoom_201.get_points(tags={'whitegarden_1': ''})) #index1
        points_ampfloor2.append(qampRoom_202.get_points(tags={'whitegarden_1': ''})) #index1
        points_ampfloor2.append(qampRoom_203.get_points(tags={'whitegarden_1': ''})) #index1
        points_ampfloor2.append(qampRoom_204.get_points(tags={'whitegarden_1': ''})) #index1
        points_ampfloor2.append(qampRoom_205.get_points(tags={'whitegarden_1': ''})) #index1
        points_ampfloor2.append(qampRoom_206.get_points(tags={'whitegarden_1': ''})) #index1
        points_ampfloor2.append(qampRoom_207.get_points(tags={'whitegarden_1': ''})) #index1
        points_ampfloor2.append(qampRoom_208.get_points(tags={'whitegarden_1': ''})) #index1
        points_ampfloor2.append(qampRoom_209.get_points(tags={'whitegarden_1': ''})) #index1
        points_ampfloor2.append(qampRoom_210.get_points(tags={'whitegarden_1': ''})) #index1
        points_ampfloor2.append(qampRoom_211.get_points(tags={'whitegarden_1': ''})) #index1
        points_ampfloor2.append(qampRoom_212.get_points(tags={'whitegarden_1': ''})) #index1
        points_ampfloor2.append(qampRoom_213.get_points(tags={'whitegarden_1': ''})) #index1
        points_ampfloor2.append(qampRoom_214.get_points(tags={'whitegarden_1': ''})) #index1
        points_ampfloor2.append(qampRoom_215.get_points(tags={'whitegarden_1': ''})) #index1
        points_ampfloor2.append(qampRoom_216.get_points(tags={'whitegarden_1': ''})) #index1
        points_ampfloor2.append(qampRoom_217.get_points(tags={'whitegarden_1': ''})) #index1

        # todo floor 2 kwh
        qtodaykwhWalkwayf2=client.query('SELECT last("kwh_sbwg99r200m1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qtodaykwhRoom_201=client.query('SELECT last("kwh_sbwg99r201m1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qtodaykwhRoom_202=client.query('SELECT last("kwh_sbwg99r202m1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qtodaykwhRoom_203=client.query('SELECT last("kwh_sbwg99r203m1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qtodaykwhRoom_204=client.query('SELECT last("kwh_sbwg99r204m1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qtodaykwhRoom_205=client.query('SELECT last("kwh_sbwg99r205m1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qtodaykwhRoom_206=client.query('SELECT last("kwh_sbwg99r206m1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qtodaykwhRoom_207=client.query('SELECT last("kwh_sbwg99r207m1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qtodaykwhRoom_208=client.query('SELECT last("kwh_sbwg99r208m1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qtodaykwhRoom_209=client.query('SELECT last("kwh_sbwg99r209m1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qtodaykwhRoom_210=client.query('SELECT last("kwh_sbwg99r210m1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qtodaykwhRoom_211=client.query('SELECT last("kwh_sbwg99r211m1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qtodaykwhRoom_212=client.query('SELECT last("kwh_sbwg99r212m1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qtodaykwhRoom_213=client.query('SELECT last("kwh_sbwg99r213m1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qtodaykwhRoom_214=client.query('SELECT last("kwh_sbwg99r214m1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qtodaykwhRoom_215=client.query('SELECT last("kwh_sbwg99r215m1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qtodaykwhRoom_216=client.query('SELECT last("kwh_sbwg99r216m1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qtodaykwhRoom_217=client.query('SELECT last("kwh_sbwg99r217m1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')

        # todo point list water level
        points_todaykwhfloor2.append(qtodaykwhWalkwayf2.get_points(tags={'whitegarden_1': ''})) #index0
        points_todaykwhfloor2.append(qtodaykwhRoom_201.get_points(tags={'whitegarden_1': ''})) #index1
        points_todaykwhfloor2.append(qtodaykwhRoom_202.get_points(tags={'whitegarden_1': ''})) #index1
        points_todaykwhfloor2.append(qtodaykwhRoom_203.get_points(tags={'whitegarden_1': ''})) #index1
        points_todaykwhfloor2.append(qtodaykwhRoom_204.get_points(tags={'whitegarden_1': ''})) #index1
        points_todaykwhfloor2.append(qtodaykwhRoom_205.get_points(tags={'whitegarden_1': ''})) #index1
        points_todaykwhfloor2.append(qtodaykwhRoom_206.get_points(tags={'whitegarden_1': ''})) #index1
        points_todaykwhfloor2.append(qtodaykwhRoom_207.get_points(tags={'whitegarden_1': ''})) #index1
        points_todaykwhfloor2.append(qtodaykwhRoom_208.get_points(tags={'whitegarden_1': ''})) #index1
        points_todaykwhfloor2.append(qtodaykwhRoom_209.get_points(tags={'whitegarden_1': ''})) #index1
        points_todaykwhfloor2.append(qtodaykwhRoom_210.get_points(tags={'whitegarden_1': ''})) #index1
        points_todaykwhfloor2.append(qtodaykwhRoom_211.get_points(tags={'whitegarden_1': ''})) #index1
        points_todaykwhfloor2.append(qtodaykwhRoom_212.get_points(tags={'whitegarden_1': ''})) #index1
        points_todaykwhfloor2.append(qtodaykwhRoom_213.get_points(tags={'whitegarden_1': ''})) #index1
        points_todaykwhfloor2.append(qtodaykwhRoom_214.get_points(tags={'whitegarden_1': ''})) #index1
        points_todaykwhfloor2.append(qtodaykwhRoom_215.get_points(tags={'whitegarden_1': ''})) #index1
        points_todaykwhfloor2.append(qtodaykwhRoom_216.get_points(tags={'whitegarden_1': ''})) #index1
        points_todaykwhfloor2.append(qtodaykwhRoom_217.get_points(tags={'whitegarden_1': ''})) #index1
        # End Floor 2

        # start Floor 3
        # todo floor 3 Amp
        qampWalkwayf3=client.query('SELECT last("amps_sbwg99r300m1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qampRoom_301=client.query('SELECT last("amps_sbwg99r301m1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qampRoom_302=client.query('SELECT last("amps_sbwg99r302m1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qampRoom_303=client.query('SELECT last("amps_sbwg99r303m1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qampRoom_304=client.query('SELECT last("amps_sbwg99r304m1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qampRoom_305=client.query('SELECT last("amps_sbwg99r305m1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qampRoom_306=client.query('SELECT last("amps_sbwg99r306m1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qampRoom_307=client.query('SELECT last("amps_sbwg99r307m1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qampRoom_308=client.query('SELECT last("amps_sbwg99r308m1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qampRoom_309=client.query('SELECT last("amps_sbwg99r309m1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qampRoom_310=client.query('SELECT last("amps_sbwg99r310m1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qampRoom_311=client.query('SELECT last("amps_sbwg99r311m1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qampRoom_312=client.query('SELECT last("amps_sbwg99r312m1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qampRoom_313=client.query('SELECT last("amps_sbwg99r313m1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qampRoom_314=client.query('SELECT last("amps_sbwg99r314m1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qampRoom_315=client.query('SELECT last("amps_sbwg99r315m1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qampRoom_316=client.query('SELECT last("amps_sbwg99r316m1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qampRoom_317=client.query('SELECT last("amps_sbwg99r317m1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')

        # todo point list water level
        points_ampfloor3.append(qampWalkwayf3.get_points(tags={'whitegarden_1': ''})) #index0
        points_ampfloor3.append(qampRoom_301.get_points(tags={'whitegarden_1': ''})) #index1
        points_ampfloor3.append(qampRoom_302.get_points(tags={'whitegarden_1': ''})) #index1
        points_ampfloor3.append(qampRoom_303.get_points(tags={'whitegarden_1': ''})) #index1
        points_ampfloor3.append(qampRoom_304.get_points(tags={'whitegarden_1': ''})) #index1
        points_ampfloor3.append(qampRoom_305.get_points(tags={'whitegarden_1': ''})) #index1
        points_ampfloor3.append(qampRoom_306.get_points(tags={'whitegarden_1': ''})) #index1
        points_ampfloor3.append(qampRoom_307.get_points(tags={'whitegarden_1': ''})) #index1
        points_ampfloor3.append(qampRoom_308.get_points(tags={'whitegarden_1': ''})) #index1
        points_ampfloor3.append(qampRoom_309.get_points(tags={'whitegarden_1': ''})) #index1
        points_ampfloor3.append(qampRoom_310.get_points(tags={'whitegarden_1': ''})) #index1
        points_ampfloor3.append(qampRoom_311.get_points(tags={'whitegarden_1': ''})) #index1
        points_ampfloor3.append(qampRoom_312.get_points(tags={'whitegarden_1': ''})) #index1
        points_ampfloor3.append(qampRoom_313.get_points(tags={'whitegarden_1': ''})) #index1
        points_ampfloor3.append(qampRoom_314.get_points(tags={'whitegarden_1': ''})) #index1
        points_ampfloor3.append(qampRoom_315.get_points(tags={'whitegarden_1': ''})) #index1
        points_ampfloor3.append(qampRoom_316.get_points(tags={'whitegarden_1': ''})) #index1
        points_ampfloor3.append(qampRoom_317.get_points(tags={'whitegarden_1': ''})) #index1

        # todo floor 2 kwh
        qtodaykwhWalkwayf3=client.query('SELECT last("kwh_sbwg99r300m1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qtodaykwhRoom_301=client.query('SELECT last("kwh_sbwg99r301m1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qtodaykwhRoom_302=client.query('SELECT last("kwh_sbwg99r302m1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qtodaykwhRoom_303=client.query('SELECT last("kwh_sbwg99r303m1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qtodaykwhRoom_304=client.query('SELECT last("kwh_sbwg99r304m1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qtodaykwhRoom_305=client.query('SELECT last("kwh_sbwg99r305m1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qtodaykwhRoom_306=client.query('SELECT last("kwh_sbwg99r306m1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qtodaykwhRoom_307=client.query('SELECT last("kwh_sbwg99r307m1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qtodaykwhRoom_308=client.query('SELECT last("kwh_sbwg99r308m1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qtodaykwhRoom_309=client.query('SELECT last("kwh_sbwg99r309m1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qtodaykwhRoom_310=client.query('SELECT last("kwh_sbwg99r310m1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qtodaykwhRoom_311=client.query('SELECT last("kwh_sbwg99r311m1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qtodaykwhRoom_312=client.query('SELECT last("kwh_sbwg99r312m1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qtodaykwhRoom_313=client.query('SELECT last("kwh_sbwg99r313m1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qtodaykwhRoom_314=client.query('SELECT last("kwh_sbwg99r314m1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qtodaykwhRoom_315=client.query('SELECT last("kwh_sbwg99r315m1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qtodaykwhRoom_316=client.query('SELECT last("kwh_sbwg99r316m1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qtodaykwhRoom_317=client.query('SELECT last("kwh_sbwg99r317m1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')

        # todo point list water level
        points_todaykwhfloor3.append(qtodaykwhWalkwayf3.get_points(tags={'whitegarden_1': ''})) #index0
        points_todaykwhfloor3.append(qtodaykwhRoom_301.get_points(tags={'whitegarden_1': ''})) #index1
        points_todaykwhfloor3.append(qtodaykwhRoom_302.get_points(tags={'whitegarden_1': ''})) #index1
        points_todaykwhfloor3.append(qtodaykwhRoom_303.get_points(tags={'whitegarden_1': ''})) #index1
        points_todaykwhfloor3.append(qtodaykwhRoom_304.get_points(tags={'whitegarden_1': ''})) #index1
        points_todaykwhfloor3.append(qtodaykwhRoom_305.get_points(tags={'whitegarden_1': ''})) #index1
        points_todaykwhfloor3.append(qtodaykwhRoom_306.get_points(tags={'whitegarden_1': ''})) #index1
        points_todaykwhfloor3.append(qtodaykwhRoom_307.get_points(tags={'whitegarden_1': ''})) #index1
        points_todaykwhfloor3.append(qtodaykwhRoom_308.get_points(tags={'whitegarden_1': ''})) #index1
        points_todaykwhfloor3.append(qtodaykwhRoom_309.get_points(tags={'whitegarden_1': ''})) #index1
        points_todaykwhfloor3.append(qtodaykwhRoom_310.get_points(tags={'whitegarden_1': ''})) #index1
        points_todaykwhfloor3.append(qtodaykwhRoom_311.get_points(tags={'whitegarden_1': ''})) #index1
        points_todaykwhfloor3.append(qtodaykwhRoom_312.get_points(tags={'whitegarden_1': ''})) #index1
        points_todaykwhfloor3.append(qtodaykwhRoom_313.get_points(tags={'whitegarden_1': ''})) #index1
        points_todaykwhfloor3.append(qtodaykwhRoom_314.get_points(tags={'whitegarden_1': ''})) #index1
        points_todaykwhfloor3.append(qtodaykwhRoom_315.get_points(tags={'whitegarden_1': ''})) #index1
        points_todaykwhfloor3.append(qtodaykwhRoom_316.get_points(tags={'whitegarden_1': ''})) #index1
        points_todaykwhfloor3.append(qtodaykwhRoom_317.get_points(tags={'whitegarden_1': ''})) #index1
        # End Floor 3

        # todo floor 4 Amp
        qampWalkwayf4=client.query('SELECT last("amps_sbwg99r400m1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qampRoom_401=client.query('SELECT last("amps_sbwg99r401m1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qampRoom_402=client.query('SELECT last("amps_sbwg99r402m1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qampRoom_403=client.query('SELECT last("amps_sbwg99r403m1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qampRoom_404=client.query('SELECT last("amps_sbwg99r404m1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qampRoom_405=client.query('SELECT last("amps_sbwg99r405m1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qampRoom_406=client.query('SELECT last("amps_sbwg99r406m1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qampRoom_407=client.query('SELECT last("amps_sbwg99r407m1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qampRoom_408=client.query('SELECT last("amps_sbwg99r408m1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qampRoom_409=client.query('SELECT last("amps_sbwg99r409m1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qampRoom_410=client.query('SELECT last("amps_sbwg99r410m1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qampRoom_411=client.query('SELECT last("amps_sbwg99r411m1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qampRoom_412=client.query('SELECT last("amps_sbwg99r412m1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qampRoom_413=client.query('SELECT last("amps_sbwg99r413m1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qampRoom_414=client.query('SELECT last("amps_sbwg99r414m1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qampRoom_415=client.query('SELECT last("amps_sbwg99r415m1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qampRoom_416=client.query('SELECT last("amps_sbwg99r416m1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qampRoom_417=client.query('SELECT last("amps_sbwg99r417m1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')

        # todo point list water level
        points_ampfloor4.append(qampWalkwayf4.get_points(tags={'whitegarden_1': ''})) #index0
        points_ampfloor4.append(qampRoom_401.get_points(tags={'whitegarden_1': ''})) #index1
        points_ampfloor4.append(qampRoom_402.get_points(tags={'whitegarden_1': ''})) #index1
        points_ampfloor4.append(qampRoom_403.get_points(tags={'whitegarden_1': ''})) #index1
        points_ampfloor4.append(qampRoom_404.get_points(tags={'whitegarden_1': ''})) #index1
        points_ampfloor4.append(qampRoom_405.get_points(tags={'whitegarden_1': ''})) #index1
        points_ampfloor4.append(qampRoom_406.get_points(tags={'whitegarden_1': ''})) #index1
        points_ampfloor4.append(qampRoom_407.get_points(tags={'whitegarden_1': ''})) #index1
        points_ampfloor4.append(qampRoom_408.get_points(tags={'whitegarden_1': ''})) #index1
        points_ampfloor4.append(qampRoom_409.get_points(tags={'whitegarden_1': ''})) #index1
        points_ampfloor4.append(qampRoom_410.get_points(tags={'whitegarden_1': ''})) #index1
        points_ampfloor4.append(qampRoom_411.get_points(tags={'whitegarden_1': ''})) #index1
        points_ampfloor4.append(qampRoom_412.get_points(tags={'whitegarden_1': ''})) #index1
        points_ampfloor4.append(qampRoom_413.get_points(tags={'whitegarden_1': ''})) #index1
        points_ampfloor4.append(qampRoom_414.get_points(tags={'whitegarden_1': ''})) #index1
        points_ampfloor4.append(qampRoom_415.get_points(tags={'whitegarden_1': ''})) #index1
        points_ampfloor4.append(qampRoom_416.get_points(tags={'whitegarden_1': ''})) #index1
        points_ampfloor4.append(qampRoom_417.get_points(tags={'whitegarden_1': ''})) #index1

        # todo floor 4 kwh
        qtodaykwhWalkwayf4=client.query('SELECT last("kwh_sbwg99r400m1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qtodaykwhRoom_401=client.query('SELECT last("kwh_sbwg99r401m1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qtodaykwhRoom_402=client.query('SELECT last("kwh_sbwg99r402m1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qtodaykwhRoom_403=client.query('SELECT last("kwh_sbwg99r403m1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qtodaykwhRoom_404=client.query('SELECT last("kwh_sbwg99r404m1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qtodaykwhRoom_405=client.query('SELECT last("kwh_sbwg99r405m1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qtodaykwhRoom_406=client.query('SELECT last("kwh_sbwg99r406m1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qtodaykwhRoom_407=client.query('SELECT last("kwh_sbwg99r407m1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qtodaykwhRoom_408=client.query('SELECT last("kwh_sbwg99r408m1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qtodaykwhRoom_409=client.query('SELECT last("kwh_sbwg99r409m1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qtodaykwhRoom_410=client.query('SELECT last("kwh_sbwg99r410m1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qtodaykwhRoom_411=client.query('SELECT last("kwh_sbwg99r411m1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qtodaykwhRoom_412=client.query('SELECT last("kwh_sbwg99r412m1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qtodaykwhRoom_413=client.query('SELECT last("kwh_sbwg99r413m1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qtodaykwhRoom_414=client.query('SELECT last("kwh_sbwg99r414m1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qtodaykwhRoom_415=client.query('SELECT last("kwh_sbwg99r415m1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qtodaykwhRoom_416=client.query('SELECT last("kwh_sbwg99r416m1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qtodaykwhRoom_417=client.query('SELECT last("kwh_sbwg99r417m1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')

        # todo point list 
        points_todaykwhfloor4.append(qtodaykwhWalkwayf4.get_points(tags={'whitegarden_1': ''})) #index0
        points_todaykwhfloor4.append(qtodaykwhRoom_401.get_points(tags={'whitegarden_1': ''})) #index1
        points_todaykwhfloor4.append(qtodaykwhRoom_402.get_points(tags={'whitegarden_1': ''})) #index1
        points_todaykwhfloor4.append(qtodaykwhRoom_403.get_points(tags={'whitegarden_1': ''})) #index1
        points_todaykwhfloor4.append(qtodaykwhRoom_404.get_points(tags={'whitegarden_1': ''})) #index1
        points_todaykwhfloor4.append(qtodaykwhRoom_405.get_points(tags={'whitegarden_1': ''})) #index1
        points_todaykwhfloor4.append(qtodaykwhRoom_406.get_points(tags={'whitegarden_1': ''})) #index1
        points_todaykwhfloor4.append(qtodaykwhRoom_407.get_points(tags={'whitegarden_1': ''})) #index1
        points_todaykwhfloor4.append(qtodaykwhRoom_408.get_points(tags={'whitegarden_1': ''})) #index1
        points_todaykwhfloor4.append(qtodaykwhRoom_409.get_points(tags={'whitegarden_1': ''})) #index1
        points_todaykwhfloor4.append(qtodaykwhRoom_410.get_points(tags={'whitegarden_1': ''})) #index1
        points_todaykwhfloor4.append(qtodaykwhRoom_411.get_points(tags={'whitegarden_1': ''})) #index1
        points_todaykwhfloor4.append(qtodaykwhRoom_412.get_points(tags={'whitegarden_1': ''})) #index1
        points_todaykwhfloor4.append(qtodaykwhRoom_413.get_points(tags={'whitegarden_1': ''})) #index1
        points_todaykwhfloor4.append(qtodaykwhRoom_414.get_points(tags={'whitegarden_1': ''})) #index1
        points_todaykwhfloor4.append(qtodaykwhRoom_415.get_points(tags={'whitegarden_1': ''})) #index1
        points_todaykwhfloor4.append(qtodaykwhRoom_416.get_points(tags={'whitegarden_1': ''})) #index1
        points_todaykwhfloor4.append(qtodaykwhRoom_417.get_points(tags={'whitegarden_1': ''})) #index1
        # End Floor 4

        #!kwh floor 5 Amp query
        # todo floor 5 Amp
        qampWalkwayf5=client.query('SELECT last("amps_sbwg99r500m1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qampRoom_501=client.query('SELECT last("amps_sbwg99r501m1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qampRoom_502=client.query('SELECT last("amps_sbwg99r502m1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qampRoom_503=client.query('SELECT last("amps_sbwg99r503m1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qampRoom_504=client.query('SELECT last("amps_sbwg99r504m1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qampRoom_505=client.query('SELECT last("amps_sbwg99r505m1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qampRoom_506=client.query('SELECT last("amps_sbwg99r506m1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qampRoom_507=client.query('SELECT last("amps_sbwg99r507m1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qampRoom_508=client.query('SELECT last("amps_sbwg99r508m1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qampRoom_509=client.query('SELECT last("amps_sbwg99r509m1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qampRoom_510=client.query('SELECT last("amps_sbwg99r510m1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qampRoom_511=client.query('SELECT last("amps_sbwg99r511m1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qampRoom_512=client.query('SELECT last("amps_sbwg99r512m1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qampRoom_513=client.query('SELECT last("amps_sbwg99r513m1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qampRoom_514=client.query('SELECT last("amps_sbwg99r514m1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qampRoom_515=client.query('SELECT last("amps_sbwg99r515m1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qampRoom_516=client.query('SELECT last("amps_sbwg99r516m1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qampRoom_517=client.query('SELECT last("amps_sbwg99r517m1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')

        # todo point list water level
        points_ampfloor5.append(qampWalkwayf5.get_points(tags={'whitegarden_1': ''})) #index0
        points_ampfloor5.append(qampRoom_501.get_points(tags={'whitegarden_1': ''})) #index1
        points_ampfloor5.append(qampRoom_502.get_points(tags={'whitegarden_1': ''})) #index1
        points_ampfloor5.append(qampRoom_503.get_points(tags={'whitegarden_1': ''})) #index1
        points_ampfloor5.append(qampRoom_504.get_points(tags={'whitegarden_1': ''})) #index1
        points_ampfloor5.append(qampRoom_505.get_points(tags={'whitegarden_1': ''})) #index1
        points_ampfloor5.append(qampRoom_506.get_points(tags={'whitegarden_1': ''})) #index1
        points_ampfloor5.append(qampRoom_507.get_points(tags={'whitegarden_1': ''})) #index1
        points_ampfloor5.append(qampRoom_508.get_points(tags={'whitegarden_1': ''})) #index1
        points_ampfloor5.append(qampRoom_509.get_points(tags={'whitegarden_1': ''})) #index1
        points_ampfloor5.append(qampRoom_510.get_points(tags={'whitegarden_1': ''})) #index1
        points_ampfloor5.append(qampRoom_511.get_points(tags={'whitegarden_1': ''})) #index1
        points_ampfloor5.append(qampRoom_512.get_points(tags={'whitegarden_1': ''})) #index1
        points_ampfloor5.append(qampRoom_513.get_points(tags={'whitegarden_1': ''})) #index1
        points_ampfloor5.append(qampRoom_514.get_points(tags={'whitegarden_1': ''})) #index1
        points_ampfloor5.append(qampRoom_515.get_points(tags={'whitegarden_1': ''})) #index1
        points_ampfloor5.append(qampRoom_516.get_points(tags={'whitegarden_1': ''})) #index1
        points_ampfloor5.append(qampRoom_517.get_points(tags={'whitegarden_1': ''})) #index1

        # todo floor 5 kwh
        qtodaykwhWalkwayf5=client.query('SELECT last("kwh_sbwg99r500m1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qtodaykwhRoom_501=client.query('SELECT last("kwh_sbwg99r501m1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qtodaykwhRoom_502=client.query('SELECT last("kwh_sbwg99r502m1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qtodaykwhRoom_503=client.query('SELECT last("kwh_sbwg99r503m1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qtodaykwhRoom_504=client.query('SELECT last("kwh_sbwg99r504m1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qtodaykwhRoom_505=client.query('SELECT last("kwh_sbwg99r505m1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qtodaykwhRoom_506=client.query('SELECT last("kwh_sbwg99r506m1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qtodaykwhRoom_507=client.query('SELECT last("kwh_sbwg99r507m1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qtodaykwhRoom_508=client.query('SELECT last("kwh_sbwg99r508m1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qtodaykwhRoom_509=client.query('SELECT last("kwh_sbwg99r509m1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qtodaykwhRoom_510=client.query('SELECT last("kwh_sbwg99r510m1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qtodaykwhRoom_511=client.query('SELECT last("kwh_sbwg99r511m1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qtodaykwhRoom_512=client.query('SELECT last("kwh_sbwg99r512m1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qtodaykwhRoom_513=client.query('SELECT last("kwh_sbwg99r513m1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qtodaykwhRoom_514=client.query('SELECT last("kwh_sbwg99r514m1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qtodaykwhRoom_515=client.query('SELECT last("kwh_sbwg99r515m1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qtodaykwhRoom_516=client.query('SELECT last("kwh_sbwg99r516m1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qtodaykwhRoom_517=client.query('SELECT last("kwh_sbwg99r517m1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')

        # todo point list water level
        points_todaykwhfloor5.append(qtodaykwhWalkwayf5.get_points(tags={'whitegarden_1': ''})) #index0
        points_todaykwhfloor5.append(qtodaykwhRoom_501.get_points(tags={'whitegarden_1': ''})) #index1
        points_todaykwhfloor5.append(qtodaykwhRoom_502.get_points(tags={'whitegarden_1': ''})) #index1
        points_todaykwhfloor5.append(qtodaykwhRoom_503.get_points(tags={'whitegarden_1': ''})) #index1
        points_todaykwhfloor5.append(qtodaykwhRoom_504.get_points(tags={'whitegarden_1': ''})) #index1
        points_todaykwhfloor5.append(qtodaykwhRoom_505.get_points(tags={'whitegarden_1': ''})) #index1
        points_todaykwhfloor5.append(qtodaykwhRoom_506.get_points(tags={'whitegarden_1': ''})) #index1
        points_todaykwhfloor5.append(qtodaykwhRoom_507.get_points(tags={'whitegarden_1': ''})) #index1
        points_todaykwhfloor5.append(qtodaykwhRoom_508.get_points(tags={'whitegarden_1': ''})) #index1
        points_todaykwhfloor5.append(qtodaykwhRoom_509.get_points(tags={'whitegarden_1': ''})) #index1
        points_todaykwhfloor5.append(qtodaykwhRoom_510.get_points(tags={'whitegarden_1': ''})) #index1
        points_todaykwhfloor5.append(qtodaykwhRoom_511.get_points(tags={'whitegarden_1': ''})) #index1
        points_todaykwhfloor5.append(qtodaykwhRoom_512.get_points(tags={'whitegarden_1': ''})) #index1
        points_todaykwhfloor5.append(qtodaykwhRoom_513.get_points(tags={'whitegarden_1': ''})) #index1
        points_todaykwhfloor5.append(qtodaykwhRoom_514.get_points(tags={'whitegarden_1': ''})) #index1
        points_todaykwhfloor5.append(qtodaykwhRoom_515.get_points(tags={'whitegarden_1': ''})) #index1
        points_todaykwhfloor5.append(qtodaykwhRoom_516.get_points(tags={'whitegarden_1': ''})) #index1
        points_todaykwhfloor5.append(qtodaykwhRoom_517.get_points(tags={'whitegarden_1': ''})) #index1
        # End Floor 5
   
        for f1 in points_ampfloor1:
            for i in f1: 
                time.append(i['time'])
                List_ampfloor1.append(i['last'])
        
        for kwh1 in points_todaykwhfloor1:
            for i in kwh1: 
                time.append(i['time'])
                List_todaykwhfloor1.append(i['last'])

        for f2 in points_ampfloor2:
            for i in f2: 
                List_ampfloor2.append(i['last'])

        for kwh2 in points_todaykwhfloor2:
            for i in kwh2: 
                time.append(i['time'])
                List_todaykwhfloor2.append(i['last'])

        for f3 in points_ampfloor3:
            for i in f3: 
                List_ampfloor3.append(i['last'])

        for kwh3 in points_todaykwhfloor3:
            for i in kwh3: 
                time.append(i['time'])
                List_todaykwhfloor3.append(i['last'])

        for f4 in points_ampfloor4:
            for i in f4: 
                List_ampfloor4.append(i['last'])

        for kwh4 in points_todaykwhfloor4:
            for i in kwh4: 
                time.append(i['time'])
                List_todaykwhfloor4.append(i['last'])

        for f5 in points_ampfloor5:
            for i in f5: 
                List_ampfloor5.append(i['last'])

        for kwh5 in points_todaykwhfloor5:
            for i in kwh5: 
                time.append(i['time'])
                List_todaykwhfloor5.append(i['last'])

        upd_time = time[0].split('T')
        upd_time = upd_time[1].strip("Z")

        data ={
                "labels":labels,
                "time": upd_time,
                "floor1": List_ampfloor1,
                "todaykwh1":List_todaykwhfloor1,
                "floor2": List_ampfloor2,
                "todaykwh2":List_todaykwhfloor2,
                "floor3": List_ampfloor3,
                "todaykwh3":List_todaykwhfloor3,
                "floor4": List_ampfloor4,
                "todaykwh4":List_todaykwhfloor4,
                "floor5": List_ampfloor5,
                "todaykwh5":List_todaykwhfloor5,
            }
        return Response(data)