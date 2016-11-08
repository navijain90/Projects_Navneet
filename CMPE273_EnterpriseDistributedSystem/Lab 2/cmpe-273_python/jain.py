import urllib, json, operator
#import re
url = "https://api.spotcrime.com/crimes.json?lat=37.334164&lon=-121.884301&radius=0.02&key=."
response = urllib.urlopen(url)
json_obj = json.loads(response.read())
json_obj1=json_obj['crimes']
dict_crimeType={}
dict_address={}
dict_time={"12:01am-3am":0,"3:01am-6am":0,"6:01am-9am":0,"9:01am-12noon":0,"12:01pm-3pm":0,"3:01pm-6pm":0,"6:01pm-9pm":0,"9:01pm-12midnight":0}
# def addStreetToDict(street):
#     if dict_address.has_key(street):
#         #print "match found"
#         dict_address[street]+=1
#     else:
#         #print "no match found"
#         dict_address2={street:1}
#         dict_address.update(dict_address2)
# def addCrimeTypeToDict(crimeType):
#     if dict_crimeType.has_key(crimeType):
#         #print "Inside if"
#         dict_crimeType[crimeType]+=1
#     else:
#         #print "Inside else"
#         dict_crimeType2={crimeType:1}
#         dict_crimeType.update(dict_crimeType2)
# def addCrimeTimeToDict(crimeTime):
#     time=crimeTime.split(" ",1)[0]
#     time2=crimeTime.split(" ",1)[1]
#     hours=int(time.split(":",1)[0])
#     mins=int(time.split(":",1)[1])
#     if (hours>=12 and mins>0) or (hours<3 and mins>0) or (hours==3 and mins==0):
#         if time2 == 'AM':
#             dict_time['12:01am-3am']+=1
#         else:
#             dict_time['12:01pm-3pm']+=1
#     elif (hours>=3 and mins>0) or (hours<6 and mins>0) or (hours==6 and mins==0):
#         if time2=='AM':
#             dict_time['3:01am-6am'] += 1
#         else:
#             dict_time['3:01pm-6pm'] += 1
#     elif (hours>=6 and mins>0) or (hours<9 and min>0) or (hours==9 and mins==0):
#         if time2=='AM':
#             dict_time['6:01am-9am']+=1
#         else:
#             dict_time['6:01pm-9pm']+=1
#     elif (hours>=9 and mins>0) or (hours<12 and min>0):
#         if time2=='AM':
#             dict_time['9:01am-12noon']+=1
#         else:
#             dict_time['9:01pm-12midnight']+=1
#     else:
#         if time2=='AM':
#             dict_time['9:01pm-12midnight'] += 1
#         else:
#             dict_time['9:01am-12noon'] += 1

for json_obj2  in json_obj1:
    #print '*****************************8'
    crimeType=json_obj2['type']
    if dict_crimeType.has_key(crimeType):
        #print "Inside if"
        dict_crimeType[crimeType]+=1
    else:
        #print "Inside else"
        dict_crimeType2={crimeType:1}
        dict_crimeType.update(dict_crimeType2)
    crimeAddress=str(json_obj2['address'])
    if crimeAddress.find("OF") >= 0:
        street = crimeAddress.split(" OF ", 1)[1]
        if dict_address.has_key(street):
            dict_address[street] += 1
        else:
            dict_address2 = {street: 1}
            dict_address.update(dict_address2)
    elif crimeAddress.find("&")>=0:
        street = crimeAddress.split(" & ", 1)[0]
        if dict_address.has_key(street):
            dict_address[street] += 1
        else:
            dict_address2 = {street: 1}
            dict_address.update(dict_address2)
        #print crimeAddress
        street = crimeAddress.split(" & ", 1)[1]
        if dict_address.has_key(street):
            dict_address[street] += 1
        else:
            dict_address2 = {street: 1}
            dict_address.update(dict_address2)
    elif crimeAddress.find("BLOCK")>=0:
        street = crimeAddress.split(" BLOCK ", 1)[1]
        print street
        print street.find("BLOCK")
        if street.find("BLOCK")>=0:
            print "Inside if"
            street1=street.split("BLOCK ",1)[1]
            print street1
        else:
            street1=street
            print "inside else"+street1
        if dict_address.has_key(street1):
            dict_address[street1] += 1
        else:
            dict_address2 = {street1: 1}
            dict_address.update(dict_address2)
    else:
        if dict_address.has_key(crimeAddress):
            dict_address[crimeAddress] += 1
        else:
            dict_address2 = {crimeAddress: 1}
            dict_address.update(dict_address2)
    crimeDate=str(json_obj2['date'])
    crimeTime=crimeDate.split(" ",1)[1]
    time = crimeTime.split(" ", 1)[0]
    time2 = crimeTime.split(" ", 1)[1]
    hours = int(time.split(":", 1)[0])
    mins = int(time.split(":", 1)[1])
    if (hours >= 12 and mins > 0) or (hours < 3 and mins > 0) or (hours == 3 and mins == 0):
        if time2 == 'AM':
            dict_time['12:01am-3am'] += 1
        else:
            dict_time['12:01pm-3pm'] += 1
    elif (hours >= 3 and mins > 0) or (hours < 6 and mins > 0) or (hours == 6 and mins == 0):
        if time2 == 'AM':
            dict_time['3:01am-6am'] += 1
        else:
            dict_time['3:01pm-6pm'] += 1
    elif (hours >= 6 and mins > 0) or (hours < 9 and min > 0) or (hours == 9 and mins == 0):
        if time2 == 'AM':
            dict_time['6:01am-9am'] += 1
        else:
            dict_time['6:01pm-9pm'] += 1
    elif (hours >= 9 and mins > 0) or (hours < 12 and min > 0):
        if time2 == 'AM':
            dict_time['9:01am-12noon'] += 1
        else:
            dict_time['9:01pm-12midnight'] += 1
    else:
        if time2 == 'AM':
            dict_time['9:01pm-12midnight'] += 1
        else:
            dict_time['9:01am-12noon'] += 1

totalCrimes=sum(dict_crimeType.values())
sorted_dict_address = sorted(dict_address.items(), key=operator.itemgetter(1),reverse=True)
top_three_dangerous_streets=[]

for k, v in sorted_dict_address[:3]:
     top_three_dangerous_streets.append(k)

print "Top three dangerorus Streets = "+str(top_three_dangerous_streets)

print "Total number of crimes = "+str(totalCrimes)

print dict_time
print dict_crimeType
print sorted_dict_address