from influxdb import InfluxDBClient

from rest_framework.views import APIView
from rest_framework.response import Response

### Set Database InfluxDB ###
client = InfluxDBClient(host='52.74.59.121', port=8086, username='dtlab', password='dtlab2019')
client.get_list_database()
#print(client.get_list_database())
client.switch_database('whitegarden')
client.get_list_measurements()

class api_floor3_Data(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):

        labels = [
         'walkwayf3','301','302','303', '304','305',
         '306','307','308','309','310','311','312',
         '313','314','315','316','317',
        ]

        time = []
        points_kwhfloor3 =[]
        List_kwhfloor3 =[]
        points_ampfloor3 =[]
        List_ampfloor3 =[]



        #!kwh floor 2 kwh query
        # todo floor 2 kwh
        qkwhmainf3=client.query('SELECT last("kwhtotal_sbwg99mainf3daym1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qkwhWalkwayf3=client.query('SELECT last("kwhtotal_sbwg99r0300daym1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qkwhRoom_301=client.query('SELECT last("kwhtotal_sbwg99r0301daym1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qkwhRoom_302=client.query('SELECT last("kwhtotal_sbwg99r0302daym1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qkwhRoom_303=client.query('SELECT last("kwhtotal_sbwg99r0303daym1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qkwhRoom_304=client.query('SELECT last("kwhtotal_sbwg99r0304daym1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qkwhRoom_305=client.query('SELECT last("kwhtotal_sbwg99r0305daym1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qkwhRoom_306=client.query('SELECT last("kwhtotal_sbwg99r0306daym1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qkwhRoom_307=client.query('SELECT last("kwhtotal_sbwg99r0307daym1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qkwhRoom_308=client.query('SELECT last("kwhtotal_sbwg99r0308daym1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qkwhRoom_309=client.query('SELECT last("kwhtotal_sbwg99r0209daym1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qkwhRoom_310=client.query('SELECT last("kwhtotal_sbwg99r0310daym1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qkwhRoom_311=client.query('SELECT last("kwhtotal_sbwg99r0311daym1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qkwhRoom_312=client.query('SELECT last("kwhtotal_sbwg99r0312daym1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qkwhRoom_313=client.query('SELECT last("kwhtotal_sbwg99r0313daym1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qkwhRoom_314=client.query('SELECT last("kwhtotal_sbwg99r0314daym1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qkwhRoom_315=client.query('SELECT last("kwhtotal_sbwg99r0315daym1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qkwhRoom_316=client.query('SELECT last("kwhtotal_sbwg99r0316daym1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qkwhRoom_317=client.query('SELECT last("kwhtotal_sbwg99r0317daym1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')

        # todo point list water level
        points_kwhfloor3.append(qkwhmainf3.get_points(tags={'whitegarden_1': ''})) #index0
        points_kwhfloor3.append(qkwhWalkwayf3.get_points(tags={'whitegarden_1': ''})) #index0
        points_kwhfloor3.append(qkwhRoom_301.get_points(tags={'whitegarden_1': ''})) #index1
        points_kwhfloor3.append(qkwhRoom_302.get_points(tags={'whitegarden_1': ''})) #index2
        points_kwhfloor3.append(qkwhRoom_303.get_points(tags={'whitegarden_1': ''})) #index3
        points_kwhfloor3.append(qkwhRoom_304.get_points(tags={'whitegarden_1': ''})) #index4
        points_kwhfloor3.append(qkwhRoom_305.get_points(tags={'whitegarden_1': ''})) #index5
        points_kwhfloor3.append(qkwhRoom_306.get_points(tags={'whitegarden_1': ''})) #index6
        points_kwhfloor3.append(qkwhRoom_307.get_points(tags={'whitegarden_1': ''})) #index7
        points_kwhfloor3.append(qkwhRoom_308.get_points(tags={'whitegarden_1': ''})) #index8
        points_kwhfloor3.append(qkwhRoom_309.get_points(tags={'whitegarden_1': ''})) #index9
        points_kwhfloor3.append(qkwhRoom_310.get_points(tags={'whitegarden_1': ''})) #index10
        points_kwhfloor3.append(qkwhRoom_311.get_points(tags={'whitegarden_1': ''})) #index11
        points_kwhfloor3.append(qkwhRoom_312.get_points(tags={'whitegarden_1': ''})) #index12
        points_kwhfloor3.append(qkwhRoom_313.get_points(tags={'whitegarden_1': ''})) #index13
        points_kwhfloor3.append(qkwhRoom_314.get_points(tags={'whitegarden_1': ''})) #index14
        points_kwhfloor3.append(qkwhRoom_315.get_points(tags={'whitegarden_1': ''})) #index15
        points_kwhfloor3.append(qkwhRoom_316.get_points(tags={'whitegarden_1': ''})) #index16
        points_kwhfloor3.append(qkwhRoom_317.get_points(tags={'whitegarden_1': ''})) #index17

        #!kwh floor 2 Amp query
        # todo floor 2 Amp
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

        
        
        for kwhroom in points_kwhfloor3:
            for i in kwhroom: 
                time.append(i['time'])
                List_kwhfloor3.append(i['last'])

        for amproom in points_ampfloor3:
            for i in amproom: 
                List_ampfloor3.append(i['last'])

        upd_time = time[0].split('T')
        upd_time = upd_time[1].strip("Z")

        data ={
                "labels":labels,
                "time": upd_time,
                "kwhfloor3": List_kwhfloor3,
                "ampfloor3": List_ampfloor3,
            }
        return Response(data)