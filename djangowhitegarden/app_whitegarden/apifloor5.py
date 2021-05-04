from influxdb import InfluxDBClient

from rest_framework.views import APIView
from rest_framework.response import Response

### Set Database InfluxDB ###
client = InfluxDBClient(host='52.74.59.121', port=8086, username='dtlab', password='dtlab2019')
client.get_list_database()
#print(client.get_list_database())
client.switch_database('whitegarden')
client.get_list_measurements()

class api_floor5_Data(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):

        labels = [
         'walkwayf5','501','502','503', '504','505',
         '506','507','508','509','510','511','512',
         '513','514','515','516','517',
        ]

        time = []
        points_kwhfloor5 =[]
        List_kwhfloor5 =[]
        points_ampfloor5 =[]
        List_ampfloor5 =[]



        #!kwh floor 2 kwh query
        # todo floor 2 kwh
        qkwhmainf5=client.query('SELECT last("kwhtotal_sbwg99mainf5daym1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qkwhWalkwayf5=client.query('SELECT last("kwhtotal_sbwg99r0500daym1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qkwhRoom_501=client.query('SELECT last("kwhtotal_sbwg99r0501daym1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qkwhRoom_502=client.query('SELECT last("kwhtotal_sbwg99r0502daym1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qkwhRoom_503=client.query('SELECT last("kwhtotal_sbwg99r0503daym1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qkwhRoom_504=client.query('SELECT last("kwhtotal_sbwg99r0504daym1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qkwhRoom_505=client.query('SELECT last("kwhtotal_sbwg99r0505daym1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qkwhRoom_506=client.query('SELECT last("kwhtotal_sbwg99r0506daym1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qkwhRoom_507=client.query('SELECT last("kwhtotal_sbwg99r0507daym1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qkwhRoom_508=client.query('SELECT last("kwhtotal_sbwg99r0508daym1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qkwhRoom_509=client.query('SELECT last("kwhtotal_sbwg99r0209daym1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qkwhRoom_510=client.query('SELECT last("kwhtotal_sbwg99r0510daym1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qkwhRoom_511=client.query('SELECT last("kwhtotal_sbwg99r0511daym1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qkwhRoom_512=client.query('SELECT last("kwhtotal_sbwg99r0512daym1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qkwhRoom_513=client.query('SELECT last("kwhtotal_sbwg99r0513daym1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qkwhRoom_514=client.query('SELECT last("kwhtotal_sbwg99r0514daym1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qkwhRoom_515=client.query('SELECT last("kwhtotal_sbwg99r0515daym1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qkwhRoom_516=client.query('SELECT last("kwhtotal_sbwg99r0516daym1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qkwhRoom_517=client.query('SELECT last("kwhtotal_sbwg99r0517daym1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')

        # todo point list water level
        points_kwhfloor5.append(qkwhmainf5.get_points(tags={'whitegarden_1': ''})) #index0
        points_kwhfloor5.append(qkwhWalkwayf5.get_points(tags={'whitegarden_1': ''})) #index0
        points_kwhfloor5.append(qkwhRoom_501.get_points(tags={'whitegarden_1': ''})) #index1
        points_kwhfloor5.append(qkwhRoom_502.get_points(tags={'whitegarden_1': ''})) #index2
        points_kwhfloor5.append(qkwhRoom_503.get_points(tags={'whitegarden_1': ''})) #index3
        points_kwhfloor5.append(qkwhRoom_504.get_points(tags={'whitegarden_1': ''})) #index4
        points_kwhfloor5.append(qkwhRoom_505.get_points(tags={'whitegarden_1': ''})) #index5
        points_kwhfloor5.append(qkwhRoom_506.get_points(tags={'whitegarden_1': ''})) #index6
        points_kwhfloor5.append(qkwhRoom_507.get_points(tags={'whitegarden_1': ''})) #index7
        points_kwhfloor5.append(qkwhRoom_508.get_points(tags={'whitegarden_1': ''})) #index8
        points_kwhfloor5.append(qkwhRoom_509.get_points(tags={'whitegarden_1': ''})) #index9
        points_kwhfloor5.append(qkwhRoom_510.get_points(tags={'whitegarden_1': ''})) #index10
        points_kwhfloor5.append(qkwhRoom_511.get_points(tags={'whitegarden_1': ''})) #index11
        points_kwhfloor5.append(qkwhRoom_512.get_points(tags={'whitegarden_1': ''})) #index12
        points_kwhfloor5.append(qkwhRoom_513.get_points(tags={'whitegarden_1': ''})) #index13
        points_kwhfloor5.append(qkwhRoom_514.get_points(tags={'whitegarden_1': ''})) #index14
        points_kwhfloor5.append(qkwhRoom_515.get_points(tags={'whitegarden_1': ''})) #index15
        points_kwhfloor5.append(qkwhRoom_516.get_points(tags={'whitegarden_1': ''})) #index16
        points_kwhfloor5.append(qkwhRoom_517.get_points(tags={'whitegarden_1': ''})) #index17

        #!kwh floor 2 Amp query
        # todo floor 2 Amp
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

        
        
        for kwhroom in points_kwhfloor5:
            for i in kwhroom: 
                time.append(i['time'])
                List_kwhfloor5.append(i['last'])

        for amproom in points_ampfloor5:
            for i in amproom: 
                List_ampfloor5.append(i['last'])

        upd_time = time[0].split('T')
        upd_time = upd_time[1].strip("Z")

        data ={
                "labels":labels,
                "time": upd_time,
                "kwhfloor5": List_kwhfloor5,
                "ampfloor5": List_ampfloor5,
            }
        return Response(data)