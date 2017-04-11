#!/bin/sh
incfile=/home/work/hotel/pulled_data/inc/
datafile=/home/work/hotel/goods-data/inc/
base=/root/tool/
newfile=`ls -t $incfile | head -1`

line=`cat /root/tool/inctmp`

if [ "$newfile" = "$line" ];then
echo "="
else 
echo $newfile > $base/inctmp
cp -r $incfile$newfile $base
mkdir $base$newfile/status
cd $base$newfile/status
touch  status.txt
mv $base$newfile/shard_0 $base$newfile/1270101
mv $base$newfile $datafile
fi
