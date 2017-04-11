#!/usr/bin/expect -f 

set timeout 20
set timeStamp [lindex $argv 0]
set src "/home/work/hotel/pulled_data/all/$timeStamp"
set des "/home/work/hotel/goods-data/all"
set script "/home/work/hotel/goods-ds/script"

spawn ssh root@192.168.233.83
expect "*assword*"
send "Nopass@test\r"
#"*(yes/no)*" {send "yes\r";exp_continue }
puts "come to yes/no"
#"*asspord*"  {send "Nopass@test\r"}
#puts "come to password"

#拷贝+改名+创建status+修改时间戳
expect "*#"
send "scp -r 192.168.233.17:$src $des \r"
#expect "*assword*"
#send "Nopass@test\r"
expect "*#"
send "cd /home/work/hotel/goods-data/all/$timeStamp/ \r"
expect "*#"
send "mkdir status \r"
expect "*#"
send "touch status/status.txt\r"
expect "*#"
send "mv shard_0 1270101 \r"
expect "*#"
send "echo $timeStamp >../../../full_index.version\r"
#"*(yes/no)*" {send "yes\r" ;exp_continue}
#puts "come to yes/no2"
#"*assword*" {send "Nopass@test\r"} 
#expect "*#"
#send ""
#cd /home/work/hotel/goods-data/all/$timeStamp/
##out `($PWD)`
#mkdir status
#touch status/status.txt
#mv shard_0 1270101
#cd /home/work/hotel/goods-data
#cat $timeStamp full_index.version

expect "*#"
send "sh $script/stop_runjar.sh  \r"
expect "*#"
send "sh $script/test/start_runjar_test.sh  \r"
expect eof
