from influxdb import InfluxDBClient

from rest_framework.views import APIView
from rest_framework.response import Response

### Set Database InfluxDB ###
client = InfluxDBClient(host='52.74.59.121', port=8086, username='dtlab', password='dtlab2019')
client.get_list_database()
#print(client.get_list_database())
client.switch_database('whitegarden')
client.get_list_measurements()

class api_floor4_Data(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):

        labels = [
         'walkwayf4','401','402','403', '404','405',
         '406','407','408','409','410','411','412',
         '413','414','415','416','417',
        ]

        time = []
        points_kwhfloor4 =[]
        List_kwhfloor4 =[]
        points_ampfloor4 =[]
        List_ampfloor4 =[]



        #!kwh floor 2 kwh query
        # todo floor 2 kwh
        qkwhmainf4=client.query('SELECT last("kwhtotal_sbwg99mainf4daym1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qkwhWalkwayf4=client.query('SELECT last("kwhtotal_sbwg99r0400daym1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qkwhRoom_401=client.query('SELECT last("kwhtotal_sbwg99r0401daym1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qkwhRoom_402=client.query('SELECT last("kwhtotal_sbwg99r0402daym1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qkwhRoom_403=client.query('SELECT last("kwhtotal_sbwg99r0403daym1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qkwhRoom_404=client.query('SELECT last("kwhtotal_sbwg99r0404daym1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qkwhRoom_405=client.query('SELECT last("kwhtotal_sbwg99r0405daym1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qkwhRoom_406=client.query('SELECT last("kwhtotal_sbwg99r0406daym1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qkwhRoom_407=client.query('SELECT last("kwhtotal_sbwg99r0407daym1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qkwhRoom_408=client.query('SELECT last("kwhtotal_sbwg99r0408daym1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qkwhRoom_409=client.query('SELECT last("kwhtotal_sbwg99r0209daym1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qkwhRoom_410=client.query('SELECT last("kwhtotal_sbwg99r0410daym1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qkwhRoom_411=client.query('SELECT last("kwhtotal_sbwg99r0411daym1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qkwhRoom_412=client.query('SELECT last("kwhtotal_sbwg99r0412daym1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qkwhRoom_413=client.query('SELECT last("kwhtotal_sbwg99r0413daym1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qkwhRoom_414=client.query('SELECT last("kwhtotal_sbwg99r0414daym1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qkwhRoom_415=client.query('SELECT last("kwhtotal_sbwg99r0415daym1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qkwhRoom_416=client.query('SELECT last("kwhtotal_sbwg99r0416daym1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qkwhRoom_417=client.query('SELECT last("kwhtotal_sbwg99r0417daym1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')

        # todo point list water level
        points_kwhfloor4.append(qkwhmainf4.get_points(tags={'whitegarden_1': ''})) #index0
        points_kwhfloor4.append(qkwhWalkwayf4.get_points(tags={'whitegarden_1': ''})) #index0
        points_kwhfloor4.append(qkwhRoom_401.get_points(tags={'whitegarden_1': ''})) #index1
        points_kwhfloor4.append(qkwhRoom_402.get_points(tags={'whitegarden_1': ''})) #index2
        points_kwhfloor4.append(qkwhRoom_403.get_points(tags={'whitegarden_1': ''})) #index3
        points_kwhfloor4.append(qkwhRoom_404.get_points(tags={'whitegarden_1': ''})) #index4
        points_kwhfloor4.append(qkwhRoom_405.get_points(tags={'whitegarden_1': ''})) #index5
        points_kwhfloor4.append(qkwhRoom_406.get_points(tags={'whitegarden_1': ''})) #index6
        points_kwhfloor4.append(qkwhRoom_407.get_points(tags={'whitegarden_1': ''})) #index7
        points_kwhfloor4.append(qkwhRoom_408.get_points(tags={'whitegarden_1': ''})) #index8
        points_kwhfloor4.append(qkwhRoom_409.get_points(tags={'whitegarden_1': ''})) #index9
        points_kwhfloor4.append(qkwhRoom_410.get_points(tags={'whitegarden_1': ''})) #index10
        points_kwhfloor4.append(qkwhRoom_411.get_points(tags={'whitegarden_1': ''})) #index11
        points_kwhfloor4.append(qkwhRoom_412.get_points(tags={'whitegarden_1': ''})) #index12
        points_kwhfloor4.append(qkwhRoom_413.get_points(tags={'whitegarden_1': ''})) #index13
        points_kwhfloor4.append(qkwhRoom_414.get_points(tags={'whitegarden_1': ''})) #index14
        points_kwhfloor4.append(qkwhRoom_415.get_points(tags={'whitegarden_1': ''})) #index15
        points_kwhfloor4.append(qkwhRoom_416.get_points(tags={'whitegarden_1': ''})) #index16
        points_kwhfloor4.append(qkwhRoom_417.get_points(tags={'whitegarden_1': ''})) #index17

        #!kwh floor 2 Amp query
        # todo floor 2 Amp
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

        
        
        for kwhroom in points_kwhfloor4:
            for i in kwhroom: 
                time.append(i['time'])
                List_kwhfloor4.append(i['last'])

        for amproom in points_ampfloor4:
            for i in amproom: 
                List_ampfloor4.append(i['last'])

        upd_time = time[0].split('T')
        upd_time = upd_time[1].strip("Z")

        data ={
                "labels":labels,
                "time": upd_time,
                "kwhfloor4": List_kwhfloor4,
                "ampfloor4": List_ampfloor4,
            }
        return Response(data)