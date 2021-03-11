import sqlite3
import datetime

def execute_query(query:str, connection: sqlite3.connect):
    cursor = connection.cursor()
    query = query
    try:
        cursor.execute(query)
    except Exception as e:
        print(e)
        return e

    connection.commit()


def create_Warehouse(connection: sqlite3.connect):
    query = """CREATE TABLE IF NOT EXISTS Warehouse_room  (
          Room_ID integer PRIMARY KEY AUTOINCREMENT,
          Measure_interval integer);"""

    return execute_query(query, connection)

def create_Pressure_sensor(connect: sqlite3.connect):
    query = """CREATE TABLE IF NOT EXISTS Pressure_sensor (
          Sensor_ID integer PRIMARY KEY AUTOINCREMENT,
          Room_ID integer,
          Value_now integer NOT NULL,
          FOREIGN KEY(Room_ID) REFERENCES Warehouse_room(Room_ID));"""
    return execute_query(query, connect)

def create_Wet_sensor(connection: sqlite3.connect):
    query = """CREATE TABLE IF NOT EXISTS Wet_sensor (
          Sensor_ID integer PRIMARY KEY AUTOINCREMENT,
          Room_ID integer,
          Value_now integer NOT NULL,
          FOREIGN KEY(Room_ID) REFERENCES Warehouse_room(Room_ID));"""
    return execute_query(query, connection)

def create_Temp_sensor(connection: sqlite3.connect):
    query = """CREATE TABLE IF NOT EXISTS Temp_sensor (
          Sensor_ID integer PRIMARY KEY AUTOINCREMENT,
          Room_ID integer,
          Value_now integer NOT NULL,
          FOREIGN KEY(Room_ID) REFERENCES Warehouse_room(Room_ID));"""
    return execute_query(query, connection)


def create_Sensors_snapshots(connection: sqlite3.connect):
    query = """CREATE TABLE IF NOT EXISTS Sensors_snapshots (
      Date_snapshot INEGER NOT NULL,
      Room_ID integer NOT NULL,
      Temperature integer,
      Pressure integer,
      Wet integer,
	PRIMARY KEY (Date_snapshot,room_id),
    FOREIGN KEY(Room_ID) REFERENCES Warehouse_room(Room_ID) );"""
    return execute_query(query, connection)


def create_Tables(connection: sqlite3.connect):
    try:
        create_Warehouse(connection)
        create_Pressure_sensor(connection)
        create_Temp_sensor(connection)
        create_Wet_sensor(connection)
        create_Sensors_snapshots(connection)
        print('Таблицы созданы успешно.')
    except Exception as e:
        print(e)


def get_SS_query(date: datetime.date, room_id, Temp, Pres, Wet):
    query = f"""INSERT INTO Sensors_snapshots
        (Date_snapshot, Room_ID, Temperature, Pressure, Wet)
        VALUES({get_timestamp(date)}, {room_id}, {Temp}, {Pres}, {Wet}); """
    return query

def add_SS(SS_coloumn_tuple:tuple):
    query=get_SS_query(SS_coloumn_tuple[0],SS_coloumn_tuple[1],SS_coloumn_tuple[2],SS_coloumn_tuple[3],SS_coloumn_tuple[4],)
    execute_query(query)

def get_timestamp(year,month,day,hour,min,s):
    return datetime.datetime.timestamp(datetime.datetime(year,month,day,hour,min,s))

def get_date(tmstmp):
    return datetime.datetime.fromtimestamp(tmstmp).date()








