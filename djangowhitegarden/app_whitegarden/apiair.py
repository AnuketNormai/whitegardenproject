from influxdb import InfluxDBClient

from rest_framework.views import APIView
from rest_framework.response import Response

### Set Database InfluxDB ###
client = InfluxDBClient(host='52.74.59.121', port=8086, username='dtlab', password='dtlab2019')
client.get_list_database()
#print(client.get_list_database())
client.switch_database('whitegarden')
client.get_list_measurements()

class api_airfloor1_Data(APIView):
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
        points_kwhair =[]
        List_kwhair =[]
        points_ampair =[]
        List_ampair =[]

        
        #!kwhAir Floor1 query
        qkwhAir1=client.query('SELECT last("kwhtotal_sbwg99a1daym1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qkwhAir2=client.query('SELECT last("kwhtotal_sbwg99a2daym1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qkwhAir3=client.query('SELECT last("kwhtotal_sbwg99a3daym1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qkwhAir4=client.query('SELECT last("kwhtotal_sbwg99a4daym1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qkwhAir5=client.query('SELECT last("kwhtotal_sbwg99a5daym1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qkwhAir6=client.query('SELECT last("kwhtotal_sbwg99a6daym1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qkwhAir7=client.query('SELECT last("kwhtotal_sbwg99a7daym1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qkwhAir8=client.query('SELECT last("kwhtotal_sbwg99a8daym1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qkwhAir9=client.query('SELECT last("kwhtotal_sbwg99a9daym1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qkwhAir10=client.query('SELECT last("kwhtotal_sbwg99a10daym1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qkwhAir11=client.query('SELECT last("kwhtotal_sbwg99a11daym1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')
        qkwhAir12=client.query('SELECT last("kwhtotal_sbwg99a12daym1") FROM "whitegarden_1" GROUP BY "whitegarden_1"')

        # todo point kwhAir Floor1
        points_kwhair.append(qkwhAir1.get_points(tags={'whitegarden_1': ''})) #index0
        points_kwhair.append(qkwhAir2.get_points(tags={'whitegarden_1': ''})) #index1
        points_kwhair.append(qkwhAir3.get_points(tags={'whitegarden_1': ''})) #index2
        points_kwhair.append(qkwhAir4.get_points(tags={'whitegarden_1': ''})) #index3
        points_kwhair.append(qkwhAir5.get_points(tags={'whitegarden_1': ''})) #index4
        points_kwhair.append(qkwhAir6.get_points(tags={'whitegarden_1': ''})) #index4
        points_kwhair.append(qkwhAir7.get_points(tags={'whitegarden_1': ''})) #index4
        points_kwhair.append(qkwhAir8.get_points(tags={'whitegarden_1': ''})) #index4
        points_kwhair.append(qkwhAir9.get_points(tags={'whitegarden_1': ''})) #index4
        points_kwhair.append(qkwhAir10.get_points(tags={'whitegarden_1': ''})) #index4
        points_kwhair.append(qkwhAir11.get_points(tags={'whitegarden_1': ''})) #index4
        points_kwhair.append(qkwhAir12.get_points(tags={'whitegarden_1': ''})) #index4


        #!kwhAir Floor1 query
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

        # todo point kwhAir Floor1
        points_ampair.append(qampAir1.get_points(tags={'whitegarden_1': ''})) #index0
        points_ampair.append(qampAir2.get_points(tags={'whitegarden_1': ''})) #index1
        points_ampair.append(qampAir3.get_points(tags={'whitegarden_1': ''})) #index2
        points_ampair.append(qampAir4.get_points(tags={'whitegarden_1': ''})) #index3
        points_ampair.append(qampAir5.get_points(tags={'whitegarden_1': ''})) #index4
        points_ampair.append(qampAir6.get_points(tags={'whitegarden_1': ''})) #index4
        points_ampair.append(qampAir7.get_points(tags={'whitegarden_1': ''})) #index4
        points_ampair.append(qampAir8.get_points(tags={'whitegarden_1': ''})) #index4
        points_ampair.append(qampAir9.get_points(tags={'whitegarden_1': ''})) #index4
        points_ampair.append(qampAir10.get_points(tags={'whitegarden_1': ''})) #index4
        points_ampair.append(qampAir11.get_points(tags={'whitegarden_1': ''})) #index4
        points_ampair.append(qampAir12.get_points(tags={'whitegarden_1': ''})) #index4

        for kwhair in points_kwhair:
            for i in kwhair: 
                time.append(i['time'])
                List_kwhair.append(i['last'])

        for ampair in points_ampair:
            for i in ampair: 
                List_ampair.append(i['last'])


        time = time[0].split('T')
        upd_time = time[1].strip("Z")


        data ={
                "labels":labels,
                "date" : time[0],
                "time": upd_time,
                "kwhair": List_kwhair,
                "ampair": List_ampair,
            }
        return Response(data)