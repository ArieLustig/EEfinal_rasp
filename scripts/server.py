#!/usr/bin/env python3
import socket
from time import sleep
import random
from datetime import datetime

"""
TODOs 
1. change to the actual data from the sensors
"""


def get_sensor_data():
    """
    Getting the data from the sensors
    Currently the data that is generated is random
    :return: The data from the sensors in a string containing the format of commas
    """
    area_temperature = random.randint(0, 100)
    area_humidity = random.randint(0, 100)
    dog_weight = random.randint(0, 100)
    food_weight = random.randint(0, 100)
    water_weight = random.randint(0, 100)
    water_temperature = random.randint(0, 100)
    time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    print("Time - {}  area_temperature: {:.1f} C    area_humidity: {}%  dog_weight: {}KG    food_weight: {}gr\
       water_weight: {}ml    water_temperature: {}C".format(time, area_temperature, area_humidity, dog_weight,
                                                            food_weight, water_weight, water_temperature))
    data = f'{time},{area_temperature},{area_humidity},{dog_weight},{food_weight},{water_weight},{water_temperature}'
    return data


def socket_server(HOST, PORT=65432, x=5):
    """
    Setting the server socket and waiting for a client to connect
    After connecting, sends the data every x seconds
    :param HOST:
    :param PORT:
    :param x: The time interval between sending data
    :return:
    """
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        print(f"Server Started waiting for client to connect in IP: {HOST} ")
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()

        with conn:
            print('Connected by', addr)
            while True:
                print("Sending data ")
                my_data = get_sensor_data()
                x_encoded_data = my_data.encode('utf-8')
                conn.sendall(x_encoded_data)
                sleep(x)


if __name__ == '__main__':
    HOST = socket.gethostbyname(socket.gethostname())
    try:
        socket_server(HOST)
    except ConnectionAbortedError:
        print("The connection was aborted by the client")
    except Exception as e:
        raise e
