insert into object_change_log
(hotel_id,rate_plan_id,change_time,object_name,op_type)
values(%s,%s,NOW(),%s,%s)
