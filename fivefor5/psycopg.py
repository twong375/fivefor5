import psycopg2
import sys
import pprint
from flask import jsonify

def main():

    host = 'ec2-54-197-230-161.compute-1.amazonaws.com'
    dbname = 'd6l8miq2r8htqp'
    user = 'fexwmpttektrdn'
    password = 'NfW0iifDUW4n_kevHD_MfTJFTb'
    port = 5432
    song_id = 7
    conn_string = "host='%s' dbname='%s' user='%s' password='%s' port='%i'"\
                    % (host, dbname, user, password, port)
     
    # print the connection string we will use to connect
    print "Connecting to database\n ->%s" % (conn_string)
     
    try:
        # get a connection, if a connect cannot be made an exception will be raised here
        conn = psycopg2.connect(conn_string)
        # conn.cursor will return a cursor object, you can use this cursor to perform queries
        cursor = conn.cursor()
        print "Connected!\n"
    except:
        # Get the most recent exception
        exceptionType, exceptionValue, exceptionTraceback = sys.exc_info()
        # Exit the script and print an error telling what happened.
        sys.exit("Database connection failed!\n ->%s" % (exceptionValue))


    cursor.execute("SELECT  array_to_json(array_agg(view_song_list_cached)) FROM view_song_list_cached")
     
    # retrieve the records from the database
    records = cursor.fetchall()
    print (type(records)) 

    #for r in records:
     #   print records[r]

    # print out the records using pretty print
    # note that the NAMES of the columns are not shown, instead just indexes.
    # for most people this isn't very useful so we'll show you how to return
    # columns as a dictionary (hash) in the next example.
    #print map(str, records)
    jsonify (records)
    #pprint.pprint (records)

if __name__ == "__main__":
    main()