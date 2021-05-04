from influxdb import InfluxDBClient

from rest_framework.views import APIView
from rest_framework.response import Response

### Set Database InfluxDB ###
client = InfluxDBClient(host='52.74.59.121', port=8086, username='dtlab', password='dtlab2019')
client.get_list_database()
#print(client.get_list_database())
client.switch_database('whitegarden')
client.get_list_measurements()

class api_mdb_Data(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        labels = [
         'lift',
         'lobby',
         'seminar',
         'storage',  
         'toilet' 
        ]

        time = []
        points_mainfloor =[]
        List_mainfloor =[]
        points_pump = []
        List_pump = []
        points_other = []
        List_other = []
        


        #!อัตราการใช้พลังงาน/วัน แต่ละชั้น query
        qmain_floor1=client.query('SELECT last("kwhtotal_sbwg99mainf1daym1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qmain_floor2=client.query('SELECT last("kwhtotal_sbwg99mainf2daym1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qmain_floor3=client.query('SELECT last("kwhtotal_sbwg99mainf3daym1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qmain_floor4=client.query('SELECT last("kwhtotal_sbwg99mainf4daym1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qmain_floor5=client.query('SELECT last("kwhtotal_sbwg99mainf5daym1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')

        # todo point อัตราการใช้พลังงาน/วัน แต่ละชั้น
        points_mainfloor.append(qmain_floor1.get_points(tags={'whitegarden_1': ''})) #index0
        points_mainfloor.append(qmain_floor2.get_points(tags={'whitegarden_1': ''})) #index1
        points_mainfloor.append(qmain_floor3.get_points(tags={'whitegarden_1': ''})) #index2
        points_mainfloor.append(qmain_floor4.get_points(tags={'whitegarden_1': ''})) #index3
        points_mainfloor.append(qmain_floor5.get_points(tags={'whitegarden_1': ''})) #index4

        #!kwhปัมน้ำ
        # todo water ปั้มน้ำ
        qkwh_pumpmain=client.query('SELECT last("kwhtotal_sbwg99mp1m1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qkwh_pump1=client.query('SELECT last("kwhtotal_sbwg99p1daym1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qkwh_pump2=client.query('SELECT last("kwhtotal_sbwg99p2daym1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qkwh_pump3=client.query('SELECT last("kwhtotal_sbwg99p3daym1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qkwh_pump4=client.query('SELECT last("kwhtotal_sbwg99p4daym1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qkwh_pump5=client.query('SELECT last("kwhtotal_sbwg99p5daym1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qkwh_pump6=client.query('SELECT last("kwhtotal_sbwg99p6daym1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qkwh_pump7=client.query('SELECT last("kwhtotal_sbwg99p7daym1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')

        # todo point list water usage
        points_pump.append(qkwh_pumpmain.get_points(tags={'whitegarden_1': ''})) #index0
        points_pump.append(qkwh_pump1.get_points(tags={'whitegarden_1': ''})) #index1
        points_pump.append(qkwh_pump2.get_points(tags={'whitegarden_1': ''})) #index1
        points_pump.append(qkwh_pump3.get_points(tags={'whitegarden_1': ''})) #index1
        points_pump.append(qkwh_pump4.get_points(tags={'whitegarden_1': ''})) #index1
        points_pump.append(qkwh_pump5.get_points(tags={'whitegarden_1': ''})) #index1
        points_pump.append(qkwh_pump6.get_points(tags={'whitegarden_1': ''})) #index1
        points_pump.append(qkwh_pump7.get_points(tags={'whitegarden_1': ''})) #index1

        #!% kwh  อื้นๆ
        # todo water usage
        qmain_Fair=client.query('SELECT last("kwhtotal_sbwg99mainf7daym1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qmain_building=client.query('SELECT last("kwhtotal_sbwg99mainb2daym1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qmain_EDB=client.query('SELECT last("kwhtotal_sbwg99mainedb1daym1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qminer1=client.query('SELECT last("kwhtotal_sbwg99miner1daym1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qminer2=client.query('SELECT last("kwhtotal_sbwg99miner2daym1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qminer3=client.query('SELECT last("kwhtotal_sbwg99miner3daym1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        

        # todo point list % pump working 
        points_other.append(qmain_Fair.get_points(tags={'whitegarden_1': ''})) #index0
        points_other.append(qmain_building.get_points(tags={'whitegarden_1': ''})) #index1
        points_other.append(qmain_EDB.get_points(tags={'whitegarden_1': ''})) #index2
        points_other.append(qminer1.get_points(tags={'whitegarden_1': ''})) #index3
        points_other.append(qminer2.get_points(tags={'whitegarden_1': ''})) #index4
        points_other.append(qminer3.get_points(tags={'whitegarden_1': ''})) #index5
    
        
        for mainfloor in points_mainfloor:
            for i in mainfloor: 
                time.append(i['time'])
                List_mainfloor.append(i['last'])

        for pump in points_pump:
            for i in pump: 
                List_pump.append(i['last'])

        for other in points_other:
            for i in other: 
                List_other.append(i['last'])
     

        upd_time = time[0].split('T')
        upd_time = upd_time[1].strip("Z")

        data ={
                "labels":labels,
                "time": upd_time,
                "floor": List_mainfloor,
                "pump": List_pump,
                "other": List_other,
            }
        return Response(data)