import csv
import datetime
import os
import time
from logging import getLogger

from sqlalchemy import DateTime, Integer, MetaData, Table, Text, create_engine
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
        if exampleCase == 1:
            cmd = 'COPY examplecase1(data1, data2, data3) FROM STDIN WITH (FORMAT CSV, HEADER FALSE)'
        if exampleCase == 2:
            cmd = 'COPY examplecase2(date, data) FROM STDIN WITH (FORMAT CSV, HEADER FALSE)'
        if exampleCase == 3:
            cmd = 'COPY examplecase3(name, phone) FROM STDIN WITH (FORMAT CSV, HEADER FALSE)'

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

def pauseUpload(exampleCase, filename):
    """ 
    The plan here is to split the file up into chunks and add the chunks to database. 
    When the pause method is called, the last chunk will be commited and then the partially completed chunk will be 
    rolled back so that no further change happens to the DB. So if there are 100 chunks of data and the user sends a pause
    request when the 74th chunk is being processed - the first 73 chunks will be commited and the 74th and onwards chunks will not be uploaded. 
    We can improve the upload speeds by multithreading the upload process so that many chunks can be uploaded at once
    """
    pass

def resumeUpload(exampleCase, filename, chunkNo):
    """
    To resume the upload process, we  need to know the chunk no of the paused upload. Once we have that, we can start commiting chunks from chunkNo to 
    the end. To verify that the integrity of the data is maintaianed, we can introduce a hash check. We could hash all the chunks and then 
    during resuming the upload process, verify the hashes with the original ones. If the hashes of the chunks are different, we need to alert the user
    that the data has changed and decide whether to continue the upload process or abort it. 
    """     
    pass
