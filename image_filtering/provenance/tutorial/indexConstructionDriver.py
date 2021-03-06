from indexConstruction import indexConstruction
import argparse
import os
import sys
import logging
import traceback
from resources import Resource

parser = argparse.ArgumentParser()
parser.add_argument('--FeatureFileList', help='provenance index file')
parser.add_argument('--IndexOutputFile', help='output directory for the Index')
parser.add_argument('--TrainedIndexParams', help='file generated by indexTraining.py')


args = parser.parse_args()

indexConstructor = indexConstruction()
if args.TrainedIndexParams is not None:
    indexparameters = open(args.TrainedIndexParams,'rb')
    indexResource = Resource('indexparameters', indexparameters.read(),'application/octet-stream')
    indexConstructor.loadIndexParameters(indexResource)
else:
    indexConstructor.loadIndexParameters(None)

indexDict = indexConstructor.buildIndex(args.FeatureFileList)

with open(args.IndexOutputFile,'wb') as of:
    of.write(indexDict['supplemental_information']['value']._data)
