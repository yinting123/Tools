#!/bin/sh
allfile=/home/work/hotel/pulled_data/all/
datafile=/home/work/hotel/goods-data/all/
newfile=`ls -t $allfile | head -1`
base=/root/tool
tmp=`cat alltmp`
if  [ "$1" = "" ] && [ "$newfile" != "$tmp" ];then
echo $newfile > $base/alltmp
cp -r $allfile$newfile $base/
mkdir $base/$newfile/status
cd $base/$newfile/status
touch  status.txt
mv $base/$newfile/shard_0 $base/$newfile/1270101
mv $base/$newfile $datafile
elif [ "$1" != "" ];then
cp -r $allfile$1 $base/
mkdir $base/$1/status
cd $base/$1/status
touch  status.txt
mv $base/$1/shard_0 $base/$1/1270101
mv $base/$1 $datafile
fi

