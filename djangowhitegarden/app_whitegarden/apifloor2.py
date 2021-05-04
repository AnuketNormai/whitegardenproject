from influxdb import InfluxDBClient

from rest_framework.views import APIView
from rest_framework.response import Response

### Set Database InfluxDB ###
client = InfluxDBClient(host='52.74.59.121', port=8086, username='dtlab', password='dtlab2019')
client.get_list_database()
#print(client.get_list_database())
client.switch_database('whitegarden')
client.get_list_measurements()

class api_floor2_Data(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        labels = [
         'walkway','201','202','203', '204','205',
         '206','207','208','209','210','211','212',
         '213','214','215','216','217',
        ]

        time = []
        points_kwhfloor2 =[]
        List_kwhfloor2 =[]
        points_ampfloor2 =[]
        List_ampfloor2 =[]



        #!kwh floor 2 kwh query
        # todo floor 2 kwh
        qkwhmainf2=client.query('SELECT last("kwhtotal_sbwg99mainf2daym1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qkwhWalkwayf2=client.query('SELECT last("kwhtotal_sbwg99r0200daym1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qkwhRoom_201=client.query('SELECT last("kwhtotal_sbwg99r0201daym1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qkwhRoom_202=client.query('SELECT last("kwhtotal_sbwg99r0202daym1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qkwhRoom_203=client.query('SELECT last("kwhtotal_sbwg99r0203daym1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qkwhRoom_204=client.query('SELECT last("kwhtotal_sbwg99r0204daym1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qkwhRoom_205=client.query('SELECT last("kwhtotal_sbwg99r0205daym1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qkwhRoom_206=client.query('SELECT last("kwhtotal_sbwg99r0206daym1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qkwhRoom_207=client.query('SELECT last("kwhtotal_sbwg99r0207daym1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qkwhRoom_208=client.query('SELECT last("kwhtotal_sbwg99r0208daym1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qkwhRoom_209=client.query('SELECT last("kwhtotal_sbwg99r0209daym1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qkwhRoom_210=client.query('SELECT last("kwhtotal_sbwg99r0210daym1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qkwhRoom_211=client.query('SELECT last("kwhtotal_sbwg99r0211daym1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qkwhRoom_212=client.query('SELECT last("kwhtotal_sbwg99r0212daym1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qkwhRoom_213=client.query('SELECT last("kwhtotal_sbwg99r0213daym1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qkwhRoom_214=client.query('SELECT last("kwhtotal_sbwg99r0214daym1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qkwhRoom_215=client.query('SELECT last("kwhtotal_sbwg99r0215daym1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qkwhRoom_216=client.query('SELECT last("kwhtotal_sbwg99r0216daym1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qkwhRoom_217=client.query('SELECT last("kwhtotal_sbwg99r0217daym1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')

        # todo point list water level
        points_kwhfloor2.append(qkwhmainf2.get_points(tags={'whitegarden_1': ''})) #index0
        points_kwhfloor2.append(qkwhWalkwayf2.get_points(tags={'whitegarden_1': ''})) #index0
        points_kwhfloor2.append(qkwhRoom_201.get_points(tags={'whitegarden_1': ''})) #index1
        points_kwhfloor2.append(qkwhRoom_202.get_points(tags={'whitegarden_1': ''})) #index2
        points_kwhfloor2.append(qkwhRoom_203.get_points(tags={'whitegarden_1': ''})) #index3
        points_kwhfloor2.append(qkwhRoom_204.get_points(tags={'whitegarden_1': ''})) #index4
        points_kwhfloor2.append(qkwhRoom_205.get_points(tags={'whitegarden_1': ''})) #index5
        points_kwhfloor2.append(qkwhRoom_206.get_points(tags={'whitegarden_1': ''})) #index6
        points_kwhfloor2.append(qkwhRoom_207.get_points(tags={'whitegarden_1': ''})) #index7
        points_kwhfloor2.append(qkwhRoom_208.get_points(tags={'whitegarden_1': ''})) #index8
        points_kwhfloor2.append(qkwhRoom_209.get_points(tags={'whitegarden_1': ''})) #index9
        points_kwhfloor2.append(qkwhRoom_210.get_points(tags={'whitegarden_1': ''})) #index10
        points_kwhfloor2.append(qkwhRoom_211.get_points(tags={'whitegarden_1': ''})) #index11
        points_kwhfloor2.append(qkwhRoom_212.get_points(tags={'whitegarden_1': ''})) #index12
        points_kwhfloor2.append(qkwhRoom_213.get_points(tags={'whitegarden_1': ''})) #index13
        points_kwhfloor2.append(qkwhRoom_214.get_points(tags={'whitegarden_1': ''})) #index14
        points_kwhfloor2.append(qkwhRoom_215.get_points(tags={'whitegarden_1': ''})) #index15
        points_kwhfloor2.append(qkwhRoom_216.get_points(tags={'whitegarden_1': ''})) #index16
        points_kwhfloor2.append(qkwhRoom_217.get_points(tags={'whitegarden_1': ''})) #index17

        #!kwh floor 2 Amp query
        # todo floor 2 Amp
        qampWalkwayf3=client.query('SELECT last("amps_sbwg99r200m1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
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
        points_ampfloor2.append(qampWalkwayf3.get_points(tags={'whitegarden_1': ''})) #index0
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

        
        
        for kwhroom in points_kwhfloor2:
            for i in kwhroom: 
                time.append(i['time'])
                List_kwhfloor2.append(i['last'])

        for amproom in points_ampfloor2:
            for i in amproom: 
                List_ampfloor2.append(i['last'])

        upd_time = time[0].split('T')
        upd_time = upd_time[1].strip("Z")

        data ={
                "labels":labels,
                "time": upd_time,
                "kwhfloor2": List_kwhfloor2,
                "ampfloor2": List_ampfloor2,
            }
        return Response(data)