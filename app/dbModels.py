import datetime
import time
import os
import csv

from logging import getLogger
from sqlalchemy import Integer, DateTime, Text, create_engine, MetaData, Table
from sqlalchemy.orm import sessionmaker

LOG = getLogger(__name__)

commitDB = True
TEST_DATA_DIR = "app/test-data/"
engine = create_engine("postgresql+psycopg2://mukul:mukul@localhost/collect")
connection = engine.raw_connection()

def CSVtoDB(exampleCase, filename):
    global commitDB    
    LOG.info("Converting {} to SQLALchemy Object".format(filename))
    
    LOG.info("PWD: " + os.getcwd())

    fileName = TEST_DATA_DIR + filename
    tableName = "examplecase{}".format(str(exampleCase))

    with open(fileName, 'r') as f:    
        cursor = connection.cursor()
        cmd = 'COPY examplecase1(data1, data2, data3) FROM STDIN WITH (FORMAT CSV, HEADER FALSE)'
        cursor.copy_expert(cmd, f)
    
    LOG.info("Commit Status: " + str(commitDB))
    if commitDB:
        commit()

def commit():
    try:
        LOG.info("Done converting to SQLALchemy Object")
        connection.commit()
        LOG.info("Commited Changes to Database")
    except Exception as e:
        print(e)
        LOG.debug(e)

def stop():
    global commitDB
    commitDB = False
    connection = engine.raw_connection()
    LOG.info("Stopped Adding files to Database")
    connection.rollback()
    connection.close()
    LOG.info("Rolled Back changes made to database")