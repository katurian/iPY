import ipinfo
import re
import os
import json

access_token = '71c8a7a4a3d410'
handler = ipinfo.getHandler(access_token)

def getLogIPs(logname):
        with open(logname, 'r') as file:
            log_file = file.read().replace('\n', '')
        datalist = []
        for ip in re.findall(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b', log_file):
            details = handler.getDetails(ip)
            try:
                postal = details.postal
            except(AttributeError):
                postal = 'NA'
            datadict = {
                'ip': details.ip,
                'latitude': details.latitude,
                'longitude': details.longitude,
                'country': details.country,
                'region': details.region,
                'city': details.city,
                'postal': postal
            }
            datalist.append(datadict) 
        return datalist


def createJSON(listobj):
    with open('ip.json', 'w') as outfile:
        json.dump(listobj, outfile)


createJSON(getLogIPs('access.log'))

    
    

                       
          

          
