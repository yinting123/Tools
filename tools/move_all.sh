#!/bin/sh
allfile=/home/work/hotel/pulled_data/all/
datafile=/home/work/hotel/goods-data/all/
script=/home/work/hotel/goods-ds/script/
newfile=`ls -t $allfile | head -1`
tmp=`cat alltmp`
if  [ "$1" = "" ] && [ "$newfile" != "$tmp" ];then
    echo $newfile > ./alltmp
    cp -r $allfile$newfile ./
    mkdir -p ./$newfile/status
    cd ./$newfile/status
    echo $(pwd)
    touch status.txt
    mv ./$newfile/shard_0 ./$newfile/1270101
    mv ./$newfile $datafile
elif [ "$1" != "" ];then
    if [ -f $datafile/$1 ];then
        rm $datafile/$1 -rf
    fi
    echo "文件不存在"
    cp -r $allfile$1 ./
    if [ -d ./$newfile/status ];then
        rm ./$newfile/status -rf
    fi
    mkdir -p ./$newfile/status
    touch ./$newfile/status/ status.txt
    mv ./$newfile/shard_0 ./$newfile/1270101
    mv ./$newfile $datafile$newfile
fi
cd $script
echo $(pwd)
sh $script/stop_runjar.sh
cd test
echo $(pwd)
sh $script/test/start_runjar_test.sh