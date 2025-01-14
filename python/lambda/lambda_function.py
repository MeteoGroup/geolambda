import os
import subprocess
import sys
import logging

# set up logger
logger = logging.getLogger(__file__)
logger.setLevel(logging.DEBUG)
# commented out to avoid duplicate logs in lambda
# logger.addHandler(logging.StreamHandler())

# imports used for the example code below
from osgeo import gdal


#test_filename = 'https://landsat-pds.s3.amazonaws.com/c1/L8/086/240/LC08_L1GT_086240_20180827_20180827_01_RT/LC08_L1GT_086240_20180827_20180827_01_RT_B1.TIF'
test_filename = '/drone/src/tests/data/wavewatch_blacksea_6min_st2_gfs_fields_20190808_1200.nc'


def lambda_handler(event, context=None):
    """ Lambda handler """
    logger.debug(event)

    # this try block is for testing and info only,
    # it prints out info on the the libgdal binary and paths to linked libraries
    #try:
    #    output = subprocess.check_output('readelf -d /opt/lib/libgdal.so'.split(' '))
    #    logger.info(output.decode())
    #    output = subprocess.check_output('ldd /opt/lib/libgdal.so'.split(' '))
    #    logger.info(output.decode())
    #except Exception as e:
    #    pass

    # process event payload and do something like this
    fname = event.get('filename', test_filename)
    # open and return metadata
    ds = gdal.Open(fname)
    return ds.GetMetadata()



if __name__ == "__main__":
    """ Test lambda_handler """
    event = {'filename': test_filename}
    metadata = lambda_handler(event)
    print(metadata)
