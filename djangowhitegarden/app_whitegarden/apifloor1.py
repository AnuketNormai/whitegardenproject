from influxdb import InfluxDBClient

from rest_framework.views import APIView
from rest_framework.response import Response

### Set Database InfluxDB ###
client = InfluxDBClient(host='52.74.59.121', port=8086, username='dtlab', password='dtlab2019')
client.get_list_database()
#print(client.get_list_database())
client.switch_database('whitegarden')
client.get_list_measurements()

class api_floor1_Data(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        labels = [
         'waterlevel',
         'Light Load',
         'No Load',
         'Offline',   
        ]

        time = []
        points_waterlevel =[]
        List_waterlevel =[]
        points_waterusage =[]
        List_waterusage = []
        points_percentpump =[]
        List_percentpump = []
        points_unitpump =[]
        List_unitpump = []
        points_statuspump =[]
        List_statuspump=[]


        #!water level query
        # todo water level
        qWaterlevel_ground=client.query('SELECT last("WaterLevel_bot1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qWaterlevel_roof=client.query('SELECT last("WaterLevel_top") FROM "whitegarden_1" GROUP BY "whitegarden_1"')

        # todo point list water level
        points_waterlevel.append(qWaterlevel_ground.get_points(tags={'whitegarden_1': ''})) #index0
        points_waterlevel.append(qWaterlevel_roof.get_points(tags={'whitegarden_1': ''})) #index1

        #!water usage query
        # todo water usage
        qWaterusage_ground=client.query('SELECT last("water_sbwg99bot1days1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qWaterusage_roof=client.query('SELECT last("water_sbwg99topdays1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')

        # todo point list water usage
        points_waterusage.append(qWaterusage_ground.get_points(tags={'whitegarden_1': ''})) #index0
        points_waterusage.append(qWaterusage_roof.get_points(tags={'whitegarden_1': ''})) #index1

        #!% pump working query
        # todo water usage
        qPercentpump_1=client.query('SELECT last("daily1_sbwg99workp1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qPercentpump_2=client.query('SELECT last("daily1_sbwg99workp2") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qPercentpump_3=client.query('SELECT last("daily1_sbwg99workp3") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qPercentpump_4=client.query('SELECT last("daily1_sbwg99workp4") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qPercentpump_5=client.query('SELECT last("daily1_sbwg99workp5") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qPercentpump_6=client.query('SELECT last("daily1_sbwg99workp6") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qPercentpump_7=client.query('SELECT last("daily1_sbwg99workp7") FROM "whitegarden_1" GROUP BY "whitegarden_1"')

        # todo point list % pump working 
        points_percentpump.append(qPercentpump_1.get_points(tags={'whitegarden_1': ''})) #index0
        points_percentpump.append(qPercentpump_2.get_points(tags={'whitegarden_1': ''})) #index1
        points_percentpump.append(qPercentpump_3.get_points(tags={'whitegarden_1': ''})) #index2
        points_percentpump.append(qPercentpump_4.get_points(tags={'whitegarden_1': ''})) #index3
        points_percentpump.append(qPercentpump_5.get_points(tags={'whitegarden_1': ''})) #index4
        points_percentpump.append(qPercentpump_6.get_points(tags={'whitegarden_1': ''})) #index5
        points_percentpump.append(qPercentpump_7.get_points(tags={'whitegarden_1': ''})) #index6

        #!Unit pump query
        # todo Unit pump
        qUnitpump_1=client.query('SELECT last("kwhtotal_sbwg99p1daym1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qUnitpump_2=client.query('SELECT last("kwhtotal_sbwg99p2daym1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qUnitpump_3=client.query('SELECT last("kwhtotal_sbwg99p3daym1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qUnitpump_4=client.query('SELECT last("kwhtotal_sbwg99p4daym1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qUnitpump_5=client.query('SELECT last("kwhtotal_sbwg99p5daym1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qUnitpump_6=client.query('SELECT last("kwhtotal_sbwg99p6daym1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qUnitpump_7=client.query('SELECT last("kwhtotal_sbwg99p7daym1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')

        # todo point list Unit pump 
        points_unitpump.append(qUnitpump_1.get_points(tags={'whitegarden_1': ''})) #index0
        points_unitpump.append(qUnitpump_2.get_points(tags={'whitegarden_1': ''})) #index1
        points_unitpump.append(qUnitpump_3.get_points(tags={'whitegarden_1': ''})) #index2
        points_unitpump.append(qUnitpump_4.get_points(tags={'whitegarden_1': ''})) #index3
        points_unitpump.append(qUnitpump_5.get_points(tags={'whitegarden_1': ''})) #index4
        points_unitpump.append(qUnitpump_6.get_points(tags={'whitegarden_1': ''})) #index5
        points_unitpump.append(qUnitpump_7.get_points(tags={'whitegarden_1': ''})) #index6

        #!status(amp) pump query
        # todo status(amp) pump
        qStatuspump_1=client.query('SELECT last("amps_sbwg99p1m1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qStatuspump_2=client.query('SELECT last("amps_sbwg99p2m1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qStatuspump_3=client.query('SELECT last("amps_sbwg99p3m1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qStatuspump_4=client.query('SELECT last("amps_sbwg99p4m1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qStatuspump_5=client.query('SELECT last("amps_sbwg99p5m1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qStatuspump_6=client.query('SELECT last("amps_sbwg99p6m1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qStatuspump_7=client.query('SELECT last("amps_sbwg99p7m1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')

        # todo point list status(amp) pump 
        points_statuspump.append(qStatuspump_1.get_points(tags={'whitegarden_1': ''})) #index0
        points_statuspump.append(qStatuspump_2.get_points(tags={'whitegarden_1': ''})) #index1
        points_statuspump.append(qStatuspump_3.get_points(tags={'whitegarden_1': ''})) #index2
        points_statuspump.append(qStatuspump_4.get_points(tags={'whitegarden_1': ''})) #index3
        points_statuspump.append(qStatuspump_5.get_points(tags={'whitegarden_1': ''})) #index4
        points_statuspump.append(qStatuspump_6.get_points(tags={'whitegarden_1': ''})) #index5
        points_statuspump.append(qStatuspump_7.get_points(tags={'whitegarden_1': ''})) #index6

        
        for waterlevel in points_waterlevel:
            for i in waterlevel: 
                time.append(i['time'])
                List_waterlevel.append(i['last'])

        for waterusage in points_waterusage:
            for i in waterusage: 
                List_waterusage.append(i['last'])

        for percentpump in points_percentpump:
            for i in percentpump: 
                List_percentpump.append(i['last'])

        for unitpump in points_unitpump:
            for i in unitpump: 
                List_unitpump.append(i['last'])

        for statuspump in points_statuspump:
            for i in statuspump: 
                List_statuspump.append(i['last'])
        

        upd_time = time[0].split('T')
        upd_time = upd_time[1].strip("Z")

        data ={
                "labels":labels,
                "time": upd_time,
                "waterlevel": List_waterlevel,
                "waterusage": List_waterusage,
                "percentpump": List_percentpump,
                "unitpump" : List_unitpump,
                "statuspump" : List_statuspump,
            }
        return Response(data)