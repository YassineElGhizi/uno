#!/bin/bash

DBNAME=supero_datalake2
DATE=`date +"%Y%m%d%H%M"`
SQLFILE=$DBNAME-${DATE}.sql

mysqldump --opt --user=root --password='' $DBNAME > /root/Supero/exported_db/$SQLFILE

