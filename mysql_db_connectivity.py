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
        sql_query = "create database glassdata"
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
                                                database='glassdata')
        log_obj.log_info(log_file, 'Connection status:' + str(mysql_connection.is_connected()))
        sql_query = "create table if not exists glassdata(col1 int(10),col2 float(10,5) ,col3 float(10,5),col4 float(" \
                    "10,5),col5 float(10,5),col6 float(10,5),col7 float(10,5),col8 float(10,5),col9 float(10,5)," \
                    "col10 float(10,5),col11 int(10)) "
        mysql_cursor = mysql_connection.cursor()
        mysql_cursor.execute(sql_query)
        mysql_cursor.execute('show tables')
        result = mysql_cursor.fetchall()
        for element in result:
            log_obj.log_info(log_file, 'Tables from glassdata DB:' + str(element[0]))

    except Exception as e:
        log_obj.log_error(log_file, 'Exception occurred in create table API:' + str(e))
    finally:
        log_obj.log_info(log_file, 'closing database connection')
        mysql_connection.close()


def batch_insert_sample():
    log_obj.log_info(log_file, 'Running Batch Insert Sample API')
    try:
        mysql_connection = dbconnection.connect(host='localhost', port='3306', user='root', passwd='Joshinirav@21',
                                                database='glassdata')
        log_obj.log_info(log_file, 'Connection status:' + str(mysql_connection.is_connected()))
        mysql_cursor = mysql_connection.cursor()
        with open('glass.data', 'r') as element:
            readData = csv.reader(element, delimiter='\n')
            for record in readData:
                mysql_cursor.execute("INSERT INTO glassdata(col1,col2,col3,col4,col5,col6,col7,col8,col9,col10,"
                                     "col11) VALUES ({data})".format(data=(record[0])))
                mysql_connection.commit()
    except Exception as e:
        log_obj.log_error(log_file, 'Exception occurred in Batch Insert  API:' + str(e))
    finally:
        log_obj.log_info(log_file, 'closing database connection')
        mysql_connection.close()


def main():
    # mysql_database_connectivity_sample()
    # create_database_sample()
    # create_table_sample()
    batch_insert_sample()


main()
