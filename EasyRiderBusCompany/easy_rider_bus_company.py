import json
import re
import itertools
import datetime
from numbers import Number

##TEST1
##json_data = """[{"bus_id" : 128, "stop_id" : 1, "stop_name" : "Prospekt Avenue", "next_stop" : 3, "stop_type" : "S", "a_time" : "08:12"}, {"bus_id" : 128, "stop_id" : 3, "stop_name" : "Elm Street", "next_stop" : 5, "stop_type" : "", "a_time" : "08:19"}, {"bus_id" : 128, "stop_id" : 5, "stop_name" : "Fifth Avenue", "next_stop" : 7, "stop_type" : "O", "a_time" : "08:25"}, {"bus_id" : 128, "stop_id" : 7, "stop_name" : "Sesame Street", "next_stop" : 0, "stop_type" : "F", "a_time" : "08:37"}, {"bus_id" : 512, "stop_id" : 4, "stop_name" : "Bourbon Street", "next_stop" : 6, "stop_type" : "", "a_time" : "08:13"}, {"bus_id" : 512, "stop_id" : 6, "stop_name" : "Sunset Boulevard", "next_stop" : 0, "stop_type" : "F", "a_time" : "08:16"}]"""

##TEST2
##json_data = """[{"bus_id" : 128, "stop_id" : 1, "stop_name" : "Prospekt Avenue", "next_stop" : 3, "stop_type" : "S", "a_time" : "08:12"},
##{"bus_id" : 128, "stop_id" : 3, "stop_name" : "Elm Street", "next_stop" : 5, "stop_type" : "", "a_time" : "08:19"},
##{"bus_id" : 128, "stop_id" : 5, "stop_name" : "Fifth Avenue", "next_stop" : 7, "stop_type" : "O", "a_time" : "08:25"},
##{"bus_id" : 128, "stop_id" : 7, "stop_name" : "Sesame Street", "next_stop" : 0, "stop_type" : "F", "a_time" : "08:37"},
##{"bus_id" : 256, "stop_id" : 2, "stop_name" : "Pilotow Street", "next_stop" : 3, "stop_type" : "S", "a_time" : "09:20"},
##{"bus_id" : 256, "stop_id" : 3, "stop_name" : "Elm Street", "next_stop" : 6, "stop_type" : "", "a_time" : "09:45"},
##{"bus_id" : 256, "stop_id" : 6, "stop_name" : "Sunset Boulevard", "next_stop" : 7, "stop_type" : "", "a_time" : "09:59"},
##{"bus_id" : 256, "stop_id" : 7, "stop_name" : "Sesame Street", "next_stop" : 0, "stop_type" : "F", "a_time" : "10:12"},
##{"bus_id" : 512, "stop_id" : 4, "stop_name" : "Bourbon Street", "next_stop" : 6, "stop_type" : "S", "a_time" : "08:13"},
##{"bus_id" : 512, "stop_id" : 6, "stop_name" : "Sunset Boulevard", "next_stop" : 0, "stop_type" : "F", "a_time" : "08:16"}]"""

##TEST3
##json_data = """[{"bus_id" : 128, "stop_id" : 1, "stop_name" : "Fifth Avenue", "next_stop" : 4, "stop_type" : "S", "a_time" : "08:12"},
##{"bus_id" : 128, "stop_id" : 4, "stop_name" : "Abbey Road", "next_stop" : 5, "stop_type" : "", "a_time" : "08:19"},
##{"bus_id" : 128, "stop_id" : 5, "stop_name" : "Santa Monica Boulevard", "next_stop" : 8, "stop_type" : "O", "a_time" : "08:25"},
##{"bus_id" : 128, "stop_id" : 8, "stop_name" : "Elm Street", "next_stop" : 11, "stop_type" : "", "a_time" : "08:37"},
##{"bus_id" : 128, "stop_id" : 11, "stop_name" : "Beale Street", "next_stop" : 12, "stop_type" : "", "a_time" : "09:20"},
##{"bus_id" : 128, "stop_id" : 12, "stop_name" : "Sesame Street", "next_stop" : 14, "stop_type" : "", "a_time" : "09:45"},
##{"bus_id" : 128, "stop_id" : 14, "stop_name" : "Bourbon Street", "next_stop" : 19, "stop_type" : "O", "a_time" : "09:59"},
##{"bus_id" : 128, "stop_id" : 19, "stop_name" : "Prospekt Avenue", "next_stop" : 0, "stop_type" : "F", "a_time" : "10:12"},
##{"bus_id" : 256, "stop_id" : 2, "stop_name" : "Pilotow Street", "next_stop" : 3, "stop_type" : "S", "a_time" : "08:13"},
##{"bus_id" : 256, "stop_id" : 3, "stop_name" : "Startowa Street", "next_stop" : 8, "stop_type" : "", "a_time" : "08:16"},
##{"bus_id" : 256, "stop_id" : 8, "stop_name" : "Elm Street", "next_stop" : 10, "stop_type" : "", "a_time" : "08:29"},
##{"bus_id" : 256, "stop_id" : 10, "stop_name" : "Lombard Street", "next_stop" : 12, "stop_type" : "", "a_time" : "08:44"},
##{"bus_id" : 256, "stop_id" : 12, "stop_name" : "Sesame Street", "next_stop" : 13, "stop_type" : "O", "a_time" : "08:46"},
##{"bus_id" : 256, "stop_id" : 13, "stop_name" : "Orchard Road", "next_stop" : 16, "stop_type" : "", "a_time" : "09:13"},
##{"bus_id" : 256, "stop_id" : 16, "stop_name" : "Sunset Boulevard", "next_stop" : 17, "stop_type" : "", "a_time" : "09:26"},
##{"bus_id" : 256, "stop_id" : 17, "stop_name" : "Khao San Road", "next_stop" : 20, "stop_type" : "O", "a_time" : "10:25"},
##{"bus_id" : 256, "stop_id" : 20, "stop_name" : "Michigan Avenue", "next_stop" : 0, "stop_type" : "F", "a_time" : "11:26"},
##{"bus_id" : 512, "stop_id" : 6, "stop_name" : "Arlington Road", "next_stop" : 7, "stop_type" : "S", "a_time" : "11:06"},
##{"bus_id" : 512, "stop_id" : 7, "stop_name" : "Parizska Street", "next_stop" : 8, "stop_type" : "", "a_time" : "11:15"},
##{"bus_id" : 512, "stop_id" : 8, "stop_name" : "Elm Street", "next_stop" : 9, "stop_type" : "", "a_time" : "11:56"},
##{"bus_id" : 512, "stop_id" : 9, "stop_name" : "Niebajka Avenue", "next_stop" : 15, "stop_type" : "", "a_time" : "12:20"},
##{"bus_id" : 512, "stop_id" : 15, "stop_name" : "Jakis Street", "next_stop" : 16, "stop_type" : "", "a_time" : "12:44"},
##{"bus_id" : 512, "stop_id" : 16, "stop_name" : "Sunset Boulevard", "next_stop" : 18, "stop_type" : "", "a_time" : "13:01"},
##{"bus_id" : 512, "stop_id" : 18, "stop_name" : "Jakas Avenue", "next_stop" : 19, "stop_type" : "", "a_time" : "14:00"},
##{"bus_id" : 1024, "stop_id" : 21, "stop_name" : "Karlikowska Avenue", "next_stop" : 12, "stop_type" : "S", "a_time" : "13:01"},
##{"bus_id" : 1024, "stop_id" : 12, "stop_name" : "Sesame Street", "next_stop" : 0, "stop_type" : "F", "a_time" : "14:00"},
##{"bus_id" : 512, "stop_id" : 19, "stop_name" : "Prospekt Avenue", "next_stop" : 0, "stop_type" : "F", "a_time" : "14:11"}]"""

json_data = """[
    {
        "bus_id": 512,
        "stop_id": 4,
        "stop_name": "Bourbon Street",
        "next_stop": 6,
        "stop_type": "S",
        "a_time": "08:13"
    },
    {
        "bus_id": 512,
        "stop_id": 6,
        "stop_name": "Sunset Boulevard",
        "next_stop": 0,
        "stop_type": "F",
        "a_time": "08:16"
    }
]"""

data = json.loads(json_data)

def int_validation(value):
    if not isinstance(value, int):
        return False
    return True

def stop_name_validation(value):
    template = r"[A-Z].*(Street|Road|Avenue|Boulevard)$"
    if not isinstance(value, str):
        return False
    else:
        return bool(re.match(template, value))

def stop_type_validation(value):
    template = r"^([SOF]){1}$"
    if value == "":
        return True
    elif not isinstance(value, str):
        return False
    else:
        return bool(re.match(template, value))

def a_time_validation(value):
    template = r"^(2[0-3]|[01][0-9]):([0-5]?[0-9])$"
    if not isinstance(value, str):
        return False
    else:
        return bool(re.match(template, value))
    
def validation(data):
    errors = {
        "bus_id": 0,
        "stop_id": 0,
        "stop_name": 0,
        "next_stop": 0,
        "stop_type": 0,
        "a_time": 0
        }
    
    data_val_funcs = [int_validation, int_validation, stop_name_validation,\
                      int_validation, stop_type_validation, a_time_validation]
    data_headers = ["bus_id", "stop_id", "stop_name", "next_stop", "stop_type", "a_time"]
    
    for row in data:
        for func, header in zip(data_val_funcs, data_headers):
            if not func(row[header]):
                errors[header] += 1
                continue
    return errors

def bus_stops(data):
    stops_info = {}
    for row in data:
        header = str(row['bus_id'])
        if header not in stops_info:
            stops_info[header] = 0
        stops_info[header] += 1
    return stops_info

def stops_list(data):
    bus_ids = {}
    stops_info = {'Start stops': set(), 'Transfer stops': set(), 'Finish stops': set()}
    transfers = {}

    for row in data:
        header = str(row['bus_id'])
        temp = header
        if header not in bus_ids:
            bus_ids[header] = []
            transfers[header] = set()
        if row['stop_type'] == 'S':
            bus_ids[header].append('S')
            transfers[header].add(row["stop_name"])
            stops_info['Start stops'].add(row["stop_name"])
        elif row['stop_type'] == 'F':
            bus_ids[header].append('F')
            transfers[header].add(row["stop_name"])
            stops_info['Finish stops'].add(row["stop_name"])
        else:
            transfers[header].add(row["stop_name"])
        if not bus_ids[header] or bus_ids[header][0] != 'S':
            print(f"There is no start or end stop for the line: {header}.")
            stops_info = []
            break
        
    if stops_info:
        for busid in bus_ids:
            if bus_ids[busid][-1] != 'F':
                print(f"There is no start or end stop for the line: {busid}.")
                stops_info = []
                break
    if transfers and stops_info:
        values = [set_line for set_line in transfers.values()]
        trans_comb = itertools.combinations(values,2)
        filt_comb = [i[0].intersection(i[1]) for i in trans_comb]
        flat_comb = [j for i in filt_comb for j in i]
        stops_info['Transfer stops'].update(flat_comb)

    return stops_info

def datetime_check(val1, val2, time_format=None):
    if time_format is None:
        time_format = "%H:%M"
    return datetime.datetime.strptime(val1, time_format) <= datetime.datetime.strptime(val2, time_format)
    
def time_check(data):
    bus_ids = {}
    stops = {}
    times = {}
    wrong_stops = {}

    for row in data:
        header = str(row['bus_id'])
        if header not in bus_ids:
            bus_ids[header] = []
        if header not in stops:
            stops[header] = []
        bus_ids[header].append(row["a_time"])
        stops[header].append(row["stop_name"])

    for line in bus_ids:
        if len(bus_ids[line]) > 1:
            for num in range(len(bus_ids[line])):
                if num == 0:
                    continue
                if line in times:
                    if len(times[line]) >= 1:
                        break
                if not datetime_check(bus_ids[line][num-1], bus_ids[line][num]):
                    if line not in times:
                        times[line] = []
                    if line not in wrong_stops:
                        wrong_stops[line] = []
##                    times[line].append(bus_ids[line][num])
                    times[line].append(stops[line][num])
    return times

def on_demand_list(data):
    bus_ids = {}
    on_demand = []

    for row in data:
        header = str(row['bus_id'])
        temp = header
        if header not in bus_ids:
            bus_ids[header] = []
        if row['stop_type'] == 'O':
            on_demand.append(row["stop_name"])
    return on_demand

def on_demand_check():
    stops = stops_list(data)
    on_demand_stops = on_demand_list(data)
    wrong_stops = []
    
    
    if stops:
        all_stops_notcomp = []
        for stop in stops:
            all_stops_notcomp.append(stops[stop])
        all_stops = [stop for stops in all_stops_notcomp for stop in stops]
        
    if on_demand_stops:
        for stop in on_demand_stops:
            if stop in all_stops:
                wrong_stops.append(stop)

    return wrong_stops

wrong_stops = on_demand_check()
print("On demand stops test:")
if wrong_stops:
    print(f"Wrong stop type: {wrong_stops}")
else:
    print("OK")
    




##times = time_check(data)
##print("Arrival time test:")
##if times:
##    for time in times:
##        print(f"bus_id line {time}: wrong time on station {times[time][0]}")
##else:
##    print("OK")


        
##stops = stops_list(data)
##
##if stops:
##    for stop in stops:
##        print(f"{stop}: {len(stops[stop])} {sorted(list(stops[stop]))}")
        
    

##bus_stops = bus_stops(data)
##print("Line names and number of stops:")
##for name, value in bus_stops.items():
##    print(f"bus_id: {name}, stops: {value}")

##errors = validation(data)
####errors_sum = sum(i for i in errors.values())
##f_erros = [errors['stop_name'], errors['stop_type'], errors['a_time']]
##
##
##print(f"Format validation: {sum(f_erros)} errors")
####for i,j in errors.items():
####    if j > 0:
####        print(i +":", j)
##print(f"stop_name: {errors['stop_name']}")
##print(f"stop_type: {errors['stop_type']}")
##print(f"a_time: {errors['a_time']}")

##errors = validation(data)
####errors_sum = sum(i for i in errors.values())
##f_erros = [errors['stop_name'], errors['stop_type'], errors['a_time']]
##
##
##print(f"Format validation: {sum(f_erros)} errors")
####for i,j in errors.items():
####    if j > 0:
####        print(i +":", j)
##print(f"stop_name: {errors['stop_name']}")
##print(f"stop_type: {errors['stop_type']}")
##print(f"a_time: {errors['a_time']}")
        
        

