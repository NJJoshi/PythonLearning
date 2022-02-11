from log.AppLogging import ApplicationLogging
import mysql.connector as dbconnection
import csv

log_obj = ApplicationLogging()
log_file = open('db_connection_sample.log', 'w')


def mysql_database_connectivity_sample():
    log_obj.log_info(log_file, 'Opening database connection')
    try:
        mysql_connection = dbconnection.connect(host='localhost', port='3306', user='root', passwd='Joshinirav@21')
        log_obj.log_info(log_file, 'Connection status:' + str(mysql_connection.is_connected()))
        mysql_cursor = mysql_connection.cursor()
        mysql_cursor.execute('show databases')
        result = mysql_cursor.fetchall()
        for element in result:
            log_obj.log_info(log_file, 'databases from mysql:' + str(element[0]))
    except Exception as e:
        log_obj.log_error(log_file, 'Exception occurred while connecting to database:' + str(e))
    finally:
        log_obj.log_info(log_file, 'closing database connection')
        mysql_connection.close()


def create_database_sample():
    log_obj.log_info(log_file, 'Running Create database sample API')
    try:
        mysql_connection = dbconnection.connect(host="localhost", port="3306", user="root", passwd="Joshinirav@21")
        log_obj.log_info(log_file, 'Connection status:' + str(mysql_connection.is_connected()))
        sql_query = "create database cardata"
        mysql_cursor = mysql_connection.cursor()
        mysql_cursor.execute(sql_query)
        mysql_cursor.execute('show databases')
        result = mysql_cursor.fetchall()
        for element in result:
            log_obj.log_info(log_file, 'Databases from mysql:' + str(element[0]))
    except Exception as e:
        log_obj.log_error(log_file, 'Exception occurred while connecting to database:' + str(e))
    finally:
        log_obj.log_info(log_file, 'closing database connection')
        mysql_connection.close()


def create_table_sample():
    log_obj.log_info(log_file, 'Running Create table sample API')

    try:
        mysql_connection = dbconnection.connect(host='localhost', port='3306', user='root', passwd='Joshinirav@21',
                                                database='cardata')
        log_obj.log_info(log_file, 'Connection status:' + str(mysql_connection.is_connected()))
        sql_query = "create table if not exists car_evolution_data(buying varchar(100),maint varchar(100) ,doors varchar(100),persons varchar(100),lug_boot varchar(100),safety varchar(100),class_values varchar(100) )"
        mysql_cursor = mysql_connection.cursor()
        mysql_cursor.execute(sql_query)
        mysql_cursor.execute('show tables')
        result = mysql_cursor.fetchall()
        for element in result:
            log_obj.log_info(log_file, 'Tables from cardata DB:' + str(element[0]))

    except Exception as e:
        log_obj.log_error(log_file, 'Exception occurred in create table API:' + str(e))
    finally:
        log_obj.log_info(log_file, 'closing database connection')
        mysql_connection.close()


def batch_insert_sample():
    log_obj.log_info(log_file, 'Running Batch Insert Sample API')
    try:
        mysql_connection = dbconnection.connect(host='localhost', port='3306', user='root', passwd='Joshinirav@21',
                                                database='cardata')
        log_obj.log_info(log_file, 'Connection status:' + str(mysql_connection.is_connected()))
        mysql_cursor = mysql_connection.cursor()
        with open('car.data', 'r') as element:
            readData = csv.reader(element, delimiter='\n')
            for record in readData:
                str_arr = record[0].split(",")
                values_str = ''
                for i in str_arr:
                    values_str += '"' + i + '",'
                mysql_cursor.execute("INSERT INTO car_evolution_data(buying,maint,doors,persons,lug_boot,safety,class_values) VALUES ({data})".format(data=(values_str[0:len(values_str)-1:1])))
                mysql_connection.commit()
    except Exception as e:
        log_obj.log_error(log_file, 'Exception occurred in Batch Insert  API:' + str(e))
    finally:
        log_obj.log_info(log_file, 'closing database connection')
        mysql_connection.close()


def validate_records_count():
    log_obj.log_info(log_file, 'Validating Batch Insert Records Count')
    recordCounter = 0
    try:
        mysql_connection = dbconnection.connect(host='localhost', port='3306', user='root', passwd='Joshinirav@21', database='cardata')
        log_obj.log_info(log_file, 'Connection status:' + str(mysql_connection.is_connected()))
        mysql_cursor = mysql_connection.cursor()
        sql_query = "select count(*) from car_evolution_data"
        with open('car.data', 'r') as element:
            readData = csv.reader(element, delimiter='\n')
            for record in readData:
                recordCounter += 1
        mysql_cursor.execute(sql_query)
        result = mysql_cursor.fetchall()
        if int(result[0][0]) == int(recordCounter):
            log_obj.log_info(log_file, 'All car data inserted into data table')
        else:
            log_obj.log_info(log_file, 'Not all car data inserted into data table')
    except Exception as e:
        log_obj.log_error(log_file, 'Exception occurred in Validating Batch Insert count:' + str(e))
    finally:
        log_obj.log_info(log_file, 'closing database connection')
        mysql_connection.close()


def get_data_group_by_buying():
    log_obj.log_info(log_file, 'Get Data Group By Buying')
    try:
        mysql_connection = dbconnection.connect(host='localhost', port='3306', user='root', passwd='Joshinirav@21', database='cardata')
        log_obj.log_info(log_file, 'Connection status:' + str(mysql_connection.is_connected()))
        mysql_cursor = mysql_connection.cursor()
        sql_query = "select buying, count(*) from car_evolution_data group by buying"
        mysql_cursor.execute(sql_query)
        result = mysql_cursor.fetchall()
        log_obj.log_info(log_file, ' (buying, no of records for buying option) ' + str(result))
    except Exception as e:
        log_obj.log_error(log_file, 'Exception occurred in Get Data Group By Buying:' + str(e))
    finally:
        log_obj.log_info(log_file, 'closing database connection')
        mysql_connection.close()


def get_data_where_no_of_door_is_four():
    log_obj.log_info(log_file, 'Get Data Where No of Doors will be 4')
    try:
        mysql_connection = dbconnection.connect(host='localhost', port='3306', user='root', passwd='Joshinirav@21', database='cardata')
        log_obj.log_info(log_file, 'Connection status:' + str(mysql_connection.is_connected()))
        mysql_cursor = mysql_connection.cursor()
        sql_query = "select * from car_evolution_data where doors=4"
        mysql_cursor.execute(sql_query)
        result = mysql_cursor.fetchall()
        log_obj.log_info(log_file, ' Get Data Where No of Doors will be 4: ' + str(result))
    except Exception as e:
        log_obj.log_error(log_file, 'Exception occurred in Get Data Where No of Doors will be 4:' + str(e))
    finally:
        log_obj.log_info(log_file, 'closing database connection')
        mysql_connection.close()


def update_data_door():
    log_obj.log_info(log_file, 'Update No of Doors will be 8 where ever it will be 4')
    try:
        mysql_connection = dbconnection.connect(host='localhost', port='3306', user='root', passwd='Joshinirav@21', database='cardata')
        log_obj.log_info(log_file, 'Connection status:' + str(mysql_connection.is_connected()))
        mysql_cursor = mysql_connection.cursor()
        mysql_cursor.execute('SET SQL_SAFE_UPDATES = 0')
        sql_query = "update car_evolution_data set doors='8' where doors='2'"
        mysql_cursor.execute(sql_query)
        log_obj.log_info(log_file, ' Updated Data Where No of Doors will be 2 to 8 ')
    except Exception as e:
        log_obj.log_error(log_file, 'Exception occurred in Update No of Doors will be 8 where ever it will be 4:' + str(e))
    finally:
        log_obj.log_info(log_file, 'closing database connection')
        mysql_connection.close()


def drop_table():
    log_obj.log_info(log_file, 'Drop table')
    try:
        mysql_connection = dbconnection.connect(host='localhost', port='3306', user='root', passwd='Joshinirav@21', database='cardata')
        log_obj.log_info(log_file, 'Connection status:' + str(mysql_connection.is_connected()))
        mysql_cursor = mysql_connection.cursor()
        mysql_cursor.execute('drop table car_evolution_data')
        log_obj.log_info(log_file, ' Table has been dropped')
    except Exception as e:
        log_obj.log_error(log_file, 'Exception occurred in Drop table:' + str(e))
    finally:
        log_obj.log_info(log_file, 'closing database connection')
        mysql_connection.close()


def drop_database():
    log_obj.log_info(log_file, 'Drop Database')
    try:
        mysql_connection = dbconnection.connect(host='localhost', port='3306', user='root', passwd='Joshinirav@21', database='sys')
        log_obj.log_info(log_file, 'Connection status:' + str(mysql_connection.is_connected()))
        mysql_cursor = mysql_connection.cursor()
        mysql_cursor.execute('drop database cardata')
        log_obj.log_info(log_file, ' Database has been dropped')
    except Exception as e:
        log_obj.log_error(log_file, 'Exception occurred in Drop Database:' + str(e))
    finally:
        log_obj.log_info(log_file, 'closing database connection')
        mysql_connection.close()


def main():
    mysql_database_connectivity_sample()
    create_database_sample()
    create_table_sample()
    batch_insert_sample()
    validate_records_count()
    get_data_group_by_buying()
    get_data_where_no_of_door_is_four()
    update_data_door()
    drop_table()
    drop_database()


main()
