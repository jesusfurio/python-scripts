from datetime import datetime, date, timedelta
import requests
import json

def date_epoch(date):

    d = datetime.strptime(date,'%Y-%m-%d %H:%M:%S')
    convert = d.strftime("%s") 

    return convert

def subtract_dates(date1,date2):

    return (date2 - date1).timedelta(hours)

def get_input_params():

    try:
        st_date = input("Start date of the incident. The correct format is YYYY-MM-DD hh:mm:ss : ")
        st_epoch = date_epoch(st_date)

        end_date = input("End date of the incident. The correct format is YYYY-MM-DD hh:mm:ss : ")
        end_epoch = date_epoch(end_date)

        ip = input("Write affected IP: ")

        return st_epoch, end_epoch, ip
    
    except ValueError:

        exit("Invalid date format.")

def get_sla(start,end,ip):

    url = "URL".format(ip)

    response = requests.get(url , params = {"start":start,"end":end})
    
    if response.status_code == 200:
        payload = response.json()
        availability = payload["availability"]
        print(availability * 100, "% of time available")    

    if response.status_code == 500:
        print("Invalid IP address.")

    #else:
        #print(response.content)

def main():

    start, end, ip = get_input_params()

    get_sla(start,end,ip)


if __name__ == '__main__':
    main()