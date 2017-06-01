include "dss.thrift"
include "cm.thrift"
namespace java com.elong.hotel.goods.ds.thrift

struct RequestPriceRange
{
    1:optional i32 low_price,  //筛选规则的低价
    2:optional i32 high_price,  //筛选规则的高价
}

struct SelectPrice
{
    1:required i32 type, //1是对酒店，2是对产品
    2:list<RequestPriceRange> request_price_range,
}

struct SHotelInvoiceInfo
{
    1:required i64 shotel_id,
	2:optional i32 type, //0:没有维护开发票的信息；1：由艺龙开具发票；2：由酒店开具发票
}

struct SHotelHelpfulTips
{
1:    required i64 shotel_id,  //shotel id
2:    optional string helpful_tips_cn, //温馨提示中文
3:    optional string helpful_tips_en, //温馨提示英文
4:    optional string start_date, //温馨提示开始时长
5:    optional string end_date,  //温馨提示结束时间
}

struct GiftSecondTag {
1:    optional i32    sub_bit_number,
2:    optional i32    sub_gift_price,
}

struct GiftFirstTag {
1:    optional i32   bit_number,
2:    optional i32   priority,
3:    optional list<GiftSecondTag> gift_second_tag,
}

struct GiftInfo
{
    1:optional i64 shotel_id,  //s酒店id
	2:optional i64 sroom_type_id,  //s房型id
3:	optional i64 rateplan_id,  //rp id
5:    optional string gift_content_cn,  //礼包内容 中文
6:    optional string gift_content_en,  //礼包内容 英文
7:    optional i32 way_of_giving,  //赠送方式  0:每间房赠送一次 1:每间房每日赠送一次 2:其他
8:    optional string way_of_giving_other_cn,  //其他赠送方式中文描述
9:    optional string way_of_giving_other_en,  //其他赠送方式英文描述
10:    optional i32 gift_types,  //送礼内容类型，bitmap存储：从第0位到第n位表示：送餐相关、延迟退房等
11:    optional i32 status,  //礼包状态：1为有效，0为无效
12:    optional string begin_date,  //开始日期
13:    optional string end_date,  //结束日期
14:    optional i32 date_type,  //日期有效类型: 1：预定日期 2：入住日期 3：在店日期
15:    optional i32 bit_sum4_week,  //星期几：bitmap存储，第0位表示周日，第1位表示周一，依次类推
16:    optional i32 hour_type,  //时间有效类型  0:24小时有效; 1：xx小时前; 2:xx小时后
17:    optional i32 hour_number,  //小时数字，与hour_type一起使用，当然只有hour_type等于2或3时，hour_number才有意义
18:    optional list<GiftFirstTag> gift_first_tag,//礼包一级标签（其中包含二级标签）
}

struct GiftInfoPreview
{
2:    optional string gift_preview_string,  //按规则拼接的礼包预览字符串
3:    optional bool is_next7_days,  //是否离店日期后七天之内的礼包
}

struct Gift
{
1:    required i64 gift_id,
2:	optional GiftInfo gift_info,
3:	optional GiftInfoPreview gift_info_preview,
}

struct SHotelBookingRule
{
1:    required i64 id, 
2:    required i64 shotel_id,  
4:    optional string cn_description,  //预定规则的中文描述(hotel_restrictions表当中的notes1字段)
5:    optional string en_description,  //预定规则的英文描述(hotel_restrictions表当中的notes1_en字段)
6:    optional string start_date,    
7:    optional string end_date,
8:    optional i32 booking_date_type,  // (写死了是预定日期类型)  1：预定日期 2：入住日期 3：在店日期
9:    optional i32 booking_rule_type, //1:没有规则；2：客人需要提供国籍;3:预定N间房便需要提供N个客人的名字;4:外宾必须提供英文名字；5:酒店不接受几点到几点的预定;6:需要提供客人手机号
10:    optional string start_hour,
11:    optional string end_hour,
 12:    optional string note2        ,   // 标准提示语一
 13:    optional string limit1       ,   // 限制一
 14:    optional string limit2       ,   // 限制二
}

struct AddValueInfo
{
1:    required i64 id,  //增值服务id
2:    optional string business_code,  //业务代码: 01：早餐；02：午餐；03：晚餐；04：宽带上网；05：服务费；06：政府税, 目前主要是01、05、06
3:    optional string add_value_eng_name,  //增值服务英文名称(AddValueInfo表的 AddValueENGName字段)
4:    optional string add_value_cn_name,  //增值服务中文名称(AddValueInfo表的 AddValueCNName字段)
5:    optional i32 is_include,  //是否包含
6:    optional i32 share,  //份数
7:    optional i32 price_default_option, //是按“单价”还是按照“比例”：1表示按照单价；2表示按照比例
8:    optional double price,  //单价或者比例的数字
9:    optional bool is_add,  //是否可以单加
10:    optional i32 single_price_defaultoption,  //单加是按照“单价”还是按照“比例”：1表示按照单价；2表示按照比例
11:    optional double single_price,  //单价或者比例的数字
12:    optional string memo,  //备注
13:    optional i32 is_forbidden,  //是否禁用:1表示不禁用，0表示禁用  (AddValueInfo表的IsForbidden字段)
}

//担保规则数据使用：
//担保方式： 使用VouchWay字段
//担保规则的有效日期： 
//                   日期类型使用 date_type字段， 
//                   起始结束日期使用start_date和end_date字段
//担保规则一周的哪几天有效： is_week_effective字段，第0位表示周日、第1位表示周一、第2位表示周二、依次类推
//担保是到店时间担保还是房量担保：
//                   is_arrive_time_vouch为true表示到店时间担保，此时使用arrive_start_time 和 arrive_end_time
//                   is_room_count_vouch为true表示按房量担保，此时使用room_count
//担保金额：  使用money_type字段
//变更规则：
//            rule_type=1:  不允许变更
//            rule_type=2： 允许变更取消,需要在xx日期xx时间前通知: xx日期使用rule_data_date_time变量，xx时间使用rule_data_date_string变量
//            rule_type=3： 允许变更/取消,需在最早到店时间前xx小时通知：xx小时使用rule_data_int变量
//            rule_type=4:  允许变更/取消,需在到店日24点之前xx小时通知: xx小时使用rule_data_int变量
//举例： 比如担保方式是信用卡担保，担保有效日期是 2014-04-01 到 2014-05-01，入住日期有效，每周的周二、周三、周四有效，是按照到店时间担保，如果是
//       到店时间在10:00到12:00，则需要担保，担保金额为首晚房费，变更取消规则为：规则3，允许变更取消，需要在最早到店日期前2个小时通知
//拼凑字符串如下：
//    在2014-04-01到2014-05-01期间的周二、周三、周四入住，如果您的到店时间在10:00到12:00，则需要使用信用卡担保，担保金额为首晚房费，订单可以取消，
//    不过需要在您的到店日期前2个小时通知酒店才行，过期不能取消订单
struct VouchInfo
{
1:    required i64 id,  //担保id
2:    optional i64 rateplan_id,
3:    optional i32 vouch_way,  //担保方式: 1:信用卡担保
4:    optional string start_date,
5:    optional string end_date,
6:    optional i32 date_type, // 1：预定日期 2：入住日期 3：在店日期
7:    list<i32> is_week_effective,  //周有效
8:    optional string arrive_start_time,  //到店日期担保(开始时长
9:    optional string arrive_end_time,  //到店日期担保(结束时间)
10:    optional i32 room_count, // 担保房量
11:    optional i32 money_type, //担保金额: 1:首晚房费；2：全额房费
12:    optional i32 rule_type,  //担保规则: 1：不允许变更取消；2：允许变更取消,需要在约定之日前通知；3:允许变更/取消,需在最早到店时间前小时通知;4:允许变更/取消,需在到店日24点之前小时通知
13:    optional i32 rule_data_int, //相关担保规则数据(int)  (其实就是HourNum变量) （这个名称写的太含糊了，后面会改掉这个名字）
14:    optional string rule_data_date_time, //相关担保规则数据(DateTime)   （其实就是DayNum变量?（这个名字写得太含糊了，后面会改掉这个名字)
15:    optional string rule_data_date_string, //相关担保规则数据(string)   （其实就是TimeNum变量?（这个名字写得太含糊了，后面会改掉这个名字)?
16:    optional string rule_description_cn,  //中文描述   (PolicyBaseInfo表当中的CNDescription字段)
17:    optional string rule_description_en,  //英文描述  (PolicyBaseInfo表当中的ENGDescription字段)
18:    optional bool is_arrive_time_vouch, //是否要店时间担保
19:    optional bool is_room_count_vouch,  //是否房量担保
}

//预付规则数据使用：
//预付规则的对象：  使用target_type对象(对酒店还是对客人)
//预付规则的有效日期： 
//                   使用date_type字段，日期类型只有一种：都是入住日期
//                   使用start_date 和 end_date字段
//预付规则一周的哪几天有效：使用is_week_effective字段，第0位表示周日、第1位表示周一、第2位表示周二、依次类推
//变更规则：
//           rule_type = 1: 不允许变更/取消
//           rule_type = 2: 允许变更取消，
//                          在到店日xx小时前不收取罚金（xx小时使用rule_data_int字段）；
//                          在xx小时到yy小时(yy小时使用rule_data_second_int变量)之间进行变更取消：是否扣费(使用cut_after_change_time变量),
//                                扣费是按照比例还是金额(使用cut_type_after字段)，比例或者金额的数字（使用cut_num_after字段);
//                          yy小时之后不能变更取消
//           rule_type = 3: 允许变更取消，
//                          在xx日期（使用rule_data_date_time字段）yy时间（使用rule_data_string字段）之前变更取消不收取罚金；
//                          在此日期之后变更取消: 是否扣费（使用cut_after_change_time变量），扣费是按照比例还是金额（使用cut_type_after字段）,
//                          比例或者金额的数字（使用cut_num_after字段）
//                          xx日期yy小时之后不能够变更取消
//举例：  比如预付规则是酒店和客人的一致，有效日期是入住日期为 2014-04-01 到 2014-05-01，周有效是周二、周三、周四，
//        变更取消: rule_type=2, 允许变更取消，在到店日前的22小时变更取消不收取罚金，在到店日前22小时到2小时之间变更取消收取首晚房费作为罚金，
//                  在到店日前的2小时之后不能变更取消
//拼凑字符串：
//        在 2014-04-01到2014-05-01的周二、周三、周四入住，需要进行预付，在到店日期前的22小时之前取消订单不收取罚金，到店日期前的22小时到2小时之间取消
//        订单收取首晚房费作为罚金，在到店日前的2小时之后不能变更取消订单
struct PrePayInfo
{
1:    required i64 id,  //预付id
2:    optional i64 rate_plan_id,
3:    optional i32 target_type, //针对对象，对客人，对酒店 (Target变量): 1：对酒店；2：对客人
4:    optional string start_date,
5:    optional string end_date,
6:    optional i32 date_type,  // 1：预定日期 2：入住日期 3：在店日期
7:    optional i32 rule_type, //1:不允许变变更;2:允许变更/取消,在到店日24点之前的...个小时可以变更取消;3:允许变更/取消,在指定日期指定时间之前可以变更取消
8:    optional bool cut_before_change_time,  //在变更时间点前是否扣貿 (DeductFeesBefore变量)
9:    optional bool cut_after_change_time,  //在变更时间点后是否扣貿  (DeductFeesAfter变量)
10:    optional i32 cut_type_before,  //扣费类型，首晚，金额，比伿时间点前)  (CashScaleFirstBefore变量): 1:扣费类型：金额；2：扣费类型：比例；3：扣费类型：首晚房费
11:    optional i32 cut_type_after,  //扣费类型，首晚，金额，比伿时间点后)  (CashScaleFirstAfter变量): 1:扣费类型：金额；2：扣费类型：比例；3：扣费类型：首晚房费
12:    optional i32 cut_num_before, //金额/比例（时间点前）  (DeductNumBefore变量)
13:    optional i32 cut_num_after, //金额/比例（时间点后）  (DeductNumAfter变量)
14:    optional i32 rule_data_int,  //相关预付规则数据(int)(第一阶段提前几小时  (HourNum变量)
15:    optional i32 rule_data_second_int,  //相关预付规则数据(int)(第二阶段提前几小时  (HourNum2变量)
16:    optional string rule_data_date_time,  //相关预付规则数据(DateTime)(具体取消时间日期部分)  (DateNum变量)
17:    optional string rule_data_string, //相关预付规则数据(string)(具体取消时间小时部分) (TimeNum变量)
18:    optional string rule_description_cn, //预付规则中文描述
19:    optional string rule_description_en, //预付规则英文描述
20:    list<i32> is_week_effective,  //周有效
}

struct AddBreakfastInfoOfDay
{
1:    optional bool is_include,  //是否包含早餐
2:    optional i32 share,  //包含几份早餐
3:    optional i32 price_default_option,  //早餐的价格：（是金额还是按照比例（对比原来的早餐））
4:    optional double price, //单价或者比例的数字
5:    optional string date,  //日期
6:    optional i64 policy_id,
}

struct AddBreakfasePolicyInfo
{
1:    optional i64 rate_plan_id,
2:    required i64 policy_id,
3:    optional i32 sub_policy,
4:    optional string policy_name,  //规则中文名称
5:    optional string policy_name_eng,
6:    optional i32 is_customer_visible,  //是否客户可见
7:    optional string cn_description,  //中文描述
8:    optional string eng_description,  //英文描述
9:    optional i32 date_type,  //日期类型  （这个日期类型在页面上其实是没有的，我们直接去取数据库PolicyBaseInfo的DateType字段即可)
10:    optional string start_date, //开始日期
11:    optional string end_date,  //结束日期
12:    list<i32> is_week_effective, //周有效
13:    optional i32 status,
14:    optional i32 is_include,  //是否包含早餐(IsInclude变量)
15:    optional i32 share, //包含几份早餐  (Share变量)
16:    optional string currency_code, //货币单位(CurrencyCode变量，默认是RMB)
17:    optional i32 price_default, //单价还是比例 (PriceDefaultOption变量)
18:    optional double price,  //单价或者比例的数字 (Price变量)
19:    optional i32 is_add, //是否单加 (IsAdd变量)
20:    optional i32 single_price_default_option, //单加按照单价还是按照比例 (SinglePriceDefaultOption变量)
21:    optional double single_price, //单价或者比例的数字 (SinglePrice变量)
22:    optional string memo,  //备注 (Memo变量)
23:    optional i64 add_value_id, //增值服务id (AddValueID变量)
}

struct HoursRoomInfo {
1:    optional string earliest_arrival_time,
2:    optional string latest_arrival_time,
3:    optional string stay_time,
}

//addition_id = 11 去哪儿最早最晚到店时间项目
//addition_id = 10 活动打标
//addition_id = 9 rp是否隐藏
//addition_id = 7 是否是集团id
struct RatePlanAddtion {
1:   optional i32 addition_id,     //addition_id=8，addition_value=1的情况是酒店开发票。
2:   optional i32 addition_value,  //其他情况发票模式从SHotelInvoiceInfo取。
3:    optional string addition_value_str, //string类型的value，目前只有addition_id = 11时使用（qunar最早最晚到店时间项目）

}

struct RPRatePlan
{
1:    required i64 rateplan_id,
2:    optional i32 booking_channel,  //预定渠道
3:    optional i32 sell_channel,  //分销渠道
4:    optional i32 product_type, //产品类型
5:    optional i32 customer_level,  //会员级别
6:    optional i32 settlement_type,  //支付方式  
7:    optional i32 price_model,  //定价模式 
8:    optional i32 price_type,  //客人类型  
9:    optional string rateplan_name_cn,  //rateplan 中文名称
10:    optional string rateplan_name_en,  //rateplan 英文名称
11:    optional string rateplan_description_cn, //中文描述
12:    optional string rateplan_description_en,  //英文描述
13:    optional i32 min_advance_booking_days,  //最少提前预定天数
14:    optional i32 max_advance_booking_days,  //最多提前预定天数
15:    optional string start_date,  //rateplan表当中的datetime，只取time字段，不取date字段，并且只有点击尾房销售的时候，这个字段才有意义
16:    optional string end_date,  //rateplan表当中的datetime，只取time字段，不取date字段，并且只有点击尾房销售的时候，这个字段才有意义
17:    optional i32 min_stay_days, //最少预定天数
18:    optional i32 max_stay_days, //最大预定天数
19:    optional bool is_limit_time_sale,  //是否尾房
20:    optional i32 min_checkin_rooms, //首日最少预定房间数
21:    optional i32 inventory_limit,  //受限房量  // （rateplan表当中的字段，直接返回即可）
22:    optional i32 status,  //rateplan的状态
23:    optional i32 date_type, //预定条件中选中的时间类型// 直接返回
25:    optional string expected_confirm_time, //预定确认时间  （这个需要delong这边计算得出，通过附加时间规则来计算）
26:    list<AddValueInfo> add_value_infos,  //rateplan 附加增值服务规则
27:    list<VouchInfo> vouch_infos,  //rateplan 担保规则
28:    list<PrePayInfo> prepay_infos,  //rateplan 预付规则
29:    optional bool is_special_breakfast,  //是否有差异化早餐
30:    list<AddBreakfastInfoOfDay> add_breakfast_info_of_days,  //差异化早餐列表每天包含的早餐信息
31:    list<AddBreakfasePolicyInfo> add_breakfast_policy_infos,  //差异化早餐规则列表
32:		list<RatePlanAddtion> additions,  //发票规则等信息    
33:    optional i32 max_checkin_rooms, //首日最多预定房间数                   

}

struct PromotionDescription
{
 1:    required string key ,
 2:	required string value ,
}

//活动渠道
struct ActivityChannel 
{
 1:   optional i32 type, //操作类型. 1, 排除 2, 接受
 2:   list<i64> order_from_ids, //渠道ids
 3:   list<string> proxy_ids,      //proxy ids
 4:   list<string> promotion_channel_codes,   //promotion_channel_codes
}

// 满返红包
struct HongbaoFullBackRule 
{
1:	optional double full_amount, // 满额
2:	optional double back_amount, // 返额
}


//红包信息
struct HongbaoRecord                                                                                                  
{
1:    optional i32 record_id, //红包ID
2:    optional i32 recharge_type,  //红包类型
3:	  optional i32 tag,          //专享标签，0是普通红包，
4:    optional double face_value, //红包金额
5:    optional i64 income_id, //交易ID
6:    optional string valid_date, //红包有效期 yyyy-MM-dd HH:mm:ss
7:    optional i32 activity_id, // 活动ID
9:    optional i32 status,     //状态 -1表示红包过期，1可用，2已用
11:    optional string order_time_from, //预订起始时间HH:mm:ss
12:    optional string order_time_to, // 预订结束时间HH:mm:ss
13:    optional bool is_order_valid, //预订时间是否有效 true为有效 false 无效
14:    optional string check_in_abs_date_from, // 入住绝对起始时间 yyyy-MM-dd HH:mm:ss
15:    optional string check_in_abs_date_to, // 入住绝对结束时间 yyyy-MM-dd HH:mm:ss
16:    optional bool is_check_in_abs_valid,   //入住绝对时间是否有效 true为有效 false 无效
17:    optional i32 order_relative_days_from, //相对预订日期起始偏移
18:    optional i32 order_relative_days_to, //相对预订日期结束偏移
19:    optional bool is_check_in_relative_valid,  //入住相对日期是否有效 true为有效 false 无效
20:    list<ActivityChannel> activity_channel, //活动渠道信息
21:    list<string> pay_types, //支付类型
22:	optional HongbaoFullBackRule hongbao_full_back_rule, // 满返红包规则
}

//具体业务含义还不清楚，在过滤之后，各个字段按照索引接口进行填充
struct MarketingPromotion
{
1:    required i64 id,
2:    optional i32 promotion_type,  //促销的类型，对应平台组的preferentialType:1=coupon,2=point,3=discount,4=gift,5=返现,6=特殊优惠1,7=特殊优惠2,9=立减项目,9999=现金账户
3:    optional string description,  //描述
4:    optional double upper_limit, //上限
5:    optional string offer_desc, 
6:    optional i32 exclusive_type, //0:kInclusive; 1:kExclusive
7:    optional i32 actiontype, //0: send; 1:use
8:    optional string short_struct, //
9:    optional string short_struct_eng,
10:    optional string short_struct_big5,
11:    optional i64 pro_hotel_product_id,
12:    list<PromotionDescription> promotion_description ,
13:    optional bool has_inv_limit,    //平台是否限制库存
14:    optional i32 inv_left,      //可用几间库存
15:    optional i32 priority,      //promotionId的优先级
16:    list<HongbaoRecord> hongbao_records , //红包信息, 只返回activity_id(含activity_id)之前字段 
}

struct Inventory
{
1:	optional string date, //对应日期
2:	optional i32 amount, //可用的预留房数量
3:	optional i32 status, //每日的库存状态：0为可用，其他为不可用
4:	optional i32 is_over_booking,  //是否允许超售:0为可以超售；
5:	optional i32 allbuyroom_amount, // 买断房的库存数量
6:	optional i32 over_sold_limit,  // 超售库存限量数值
}

struct PriceDays
{
1:	optional i32 status, //1为有效，其他为无效
2:	required string date,  //价格对应日期
3:	optional i32 add_bed_price,  //加床价格
4:	optional string currency,  //币种类型：RMB、USD等
5:	optional double gen_sale_cost_origin, //平日底价(原始币种)
6:	optional double gen_sale_price, //平日卖价
7:	optional bool is_add_bed,  //是否允许加床，true表示允许加床，false表示不允许加床
8:	optional bool is_hotel_weekend,  //是否酒店的周末
9:	optional bool is_price_promotion,  //是否促销  (特别注意，这里不是指promotion，而是指是否经过DRR的促销)
10:	optional double real_cost_origin, //真实成本价(原则上应该是计算DRR后的底价. 但目前等于sale_cost_origin)
11:	optional double sale_cost_origin,  //底价(原始币种, 视平日/周末, 取gen_sale_cost_origin/weekend_sale_cost_origin)
12:	optional double sale_price, //卖价(视平日/周末, 取gen_sale_price/weekend_sale_price)
13:	optional double sale_price_with_drr, //计算DRR后的卖价
15:	optional double weekend_sale_cost_origin,  //周末底价(原始币种)
16:	optional double weekend_sale_price,  //周末卖价
17:	optional double weekend_price_origin, //周末卖价的原始币种价格 
18:	optional double general_price_origin, //平日卖价的原始币种价格
19:	optional double sale_price_with_drr_origin, //经过促销后的价格（原始币种）
20:	optional double add_bed_price_origin,//加床价格(原始币种)
21:	optional double sale_price_with_drr_sub_coupon,// 计算DRR和coupon后的卖价
22: optional double sale_cost = 22,  // 底价(考虑平日/周末后的取值)
23: optional double sale_price_with_drr_d_before,//衍生品修改之前的价格
24: optional double sale_price_with_drr_origin_d_before,//衍生品修改之前的原始币种价格
}

struct Price
{
1:	optional i32 audit_status,  //审核状态:0待审核，1已审核(priceinfo表当中的字段)
2:	optional bool is_effective,  //是否有效：0无效 1有效
4:	list<PriceDays> day_prices, //价格信息，拆分到每一天
5:	optional i32 price_status,  //房价状态: 1:每天都有价格；2：部分日期有价格；3：每一天都没有价格
}

struct HotelProductRelation
{
 1:	optional	i32 product_id , 
 2:	optional	i32 sroom_id ,
 3:	optional	i32 rp_id ,
 4:    required	i32 relation_type ,//1 龙翠产品关联 4 尾房关联 7限时抢关联 12升级产品关联房型13铂涛产品房型关系
5:	optional    double relation_product_price, //关联的产品的均价
 6:    optional    i32 mroom_id ,
}

// DRR促销的属性
//
// 各种DRR所包含的key：
// drr_id=1: DayNum、CashScale、DeductNum
// drr_id=2: CheckInNum、CashScale、DeductNum
// drr_id=3: CheckInNum、LastDayNum、CashScale、DeductNum
// drr_id=4: CheckInNum、WhichDayNum、CashScale、DeductNum
// drr_id=5: EveryCheckInNum、LastDayNum、CashScale、DeductNum
// drr_id=6: week_effective、FeeType
// drr_id=7: week_effective、FeeType
// 
// key的各种取值的含义如下：
// DayNum: 提前几天
// CashScale: 优惠方式（1: 金额， 其它: 百分比）
// DeductNum: 优惠额度
// CheckInNum: 连住天数
// LastDayNum: 最后几天
// WhichDayNum: 第几天
// EveryCheckInNum: 每连住几天
// week_effective: 周几有效，按位与的方式进行判断，第0到6位分别表示周日到周六
// FeeType: 价格方式（1：周末价，其它：平日价）
struct DrrAttr
{
 1:	required	string		key		,
 2:	required	string		value	,
}

// dynamic rate rule
struct DrrMsg
{
 1:	required	i32		id			,	// 取值范围 1 ~ 7
 2:	list<DrrAttr>		drrAttr		,
 3:	required	i32		date_type	,	// 1:入住日期, 2:在店日期, 3:预定日期
 4:	required	i64		start_date	,
 5:	required	i64		end_date	,
}

struct DayMarketingPromotion
{
1:    required string date ,     //日期
2:    list<MarketingPromotion> day_marketing_promotion , 
}

struct TicketInfoes
{
1: optional i64 resource_id, // 景点资源Id
2: optional i32 resource_count, // 门票张数
}

struct Product
{
1:    optional i64 sroomtype_id, //sroomtype id;
2:    optional i64 shotel_id,  //shotel id;
3:    optional i64 supplier_id,  //supplier id;
4:	optional i32 online_search_type,  //直连酒店类型(0=eLong自有?1=EAN?2=万豪),直连酒店即非elong自有的酒店，目前只有EAN和万豪两个，以后可能多个
5:    optional bool sroomtype_status,  //mmap当中的available字段，表示sroomtype的状态：0表示无效, 1表示有效(room_type_num表当中的Available字段)
6:    optional bool has_breakfast, //是否有早餐
7:	optional RPRatePlan rateplan,
8:	optional string rp_code, //这个字段仅仅供团购使用，团购没有productid，然后每个rateplan仅仅对应一个product，所以可以使用rateplancode代替productid供团购使用
9:    list<Inventory> room_inventory_days, //该产品的每一天库存信息
10:    optional i32 room_num_status,   //该产品的库存状态: 1:每天都有库存；2：部分日期有库存；3：每一天都没有库存
11:    optional Price price,   //该产品的价格
12:	list<MarketingPromotion> marketing_promotions,  //市场部促销列表
13:	list<Gift> gifts,
14:	optional HotelProductRelation relations,
15:	optional i64 supplier_type,
16:    list<SHotelBookingRule> shotel_booking_rules,
17:	optional bool is_freesale, //是否即时确认，为true表示即时确认
18:	optional bool firstnight_has_discount,
19:	optional double firstnight_discount,
20:	optional i32 firstnight_discount_upper,
21:	optional i32 freesale_num, //即时确认的房量，为-1表示是因为超售而引起的可以即时确认的房量
 22:	optional i32 cooperation_type , // 0:未定义, 1:直签 2:非直签
23:    optional string supplier_name,
24:    optional string supplier_short_name,
25:    optional string supplier_alias,
26:    optional string supplier_telphone,
 27:	optional i64 confirm_way , // 67108864:直连, 536870912:ECM, 128:Ebooking, 1073741824:Ebooking(免确认); 判断方法: (confirm_way & val) == val 
28:    optional string shotel_contacter,
29:    optional HoursRoomInfo hours_room_info,
30:    optional string supplier_fax,
 32:	optional DrrMsg drrMsg , // DRR描述信息
33:    optional i32 weekend_start,
34:    optional i32 weekend_end,
35:    list<DayMarketingPromotion> day_marketing_promotions,   //每一天的promotion
 36:    optional i32 price_origin , //返前价
 37:    optional i32 price_sub_coupon , //返后价  
 38:    optional bool  is_min_price_product , //是否是最低价产品. true:是; false:不是 
39:		optional double weight, // 产品权重
40:    optional i32 id,
41:    optional double cvr, // 转化率
42:    optional i64 supplier_confirm_avg_time, //供应商平均确认时长
43:    optional string rateplan_structure_name_cn,  //rp结构化名称:早餐内容＋预订条件＋客人类型
44:		optional bool is_resale_product,//是否是二手房产品
45:		optional i64 	order_id,//二手房产品原单id
46: optional i32 	sign_type, // 签约状态。 0：艺龙产品，1：ctrip 直签；2：ctrip非直签；3：qunar直签；4：qunar非直签
47: optional double 	cost_point, // 产品底价分值
48: optional double 	hotel_service_point, // 酒店服务指标分值
49: optional double 	total_point, //  房型聚合总分数
50: optional double 	commission_value, // 佣金额  
// add by majia
134: optional bool is_majia,
135: optional string majia_id,
/*
前缀不要重复
0:非衍生品 
1:马甲
2:中央定价
3:马甲中央定价
4:预付定价
5:预付定价马甲
6:预付定价中央定价
7:预付定价马甲中央定价
811:高定高返
812:高定高返预付定价
813:高定高返中央定价
814:高定高返预付定价中央定价
*/
136: optional i32 derivative_type,//衍生品类型
137: optional bool is_hotel_ticket_product, // 是否景酒打包产品
138: optional byte force_show,//0默认,1强制露出,
139: optional list<TicketInfoes> ticket_resource_infoes, // 景点门票资源信息
140: optional bool is_support_flash_live,//是否支持闪住
141: optional bool is_support_credit_live,//是否支持信用住
142: optional bool is_dc_product, //是否直连产品
143: optional double extras, // 信用住、闪住产品杂费
144: optional i32 resale_product_original_price, // 转让房原产品卖价均价
145: optional i32 product_yield,//产品产量
146: optional double product_gains,//产品收益
147: optional bool has_coupon_enhance,//是否有额外返现
148: optional i32 product_flag,//二进制位表示(从0开始数):0 被动马甲，1 主动马甲 2 高定高返
149: optional i32 coupon_enhance_member_type,//产品的额外返现用的是什么会员类型的策略
}

struct SelectedProduct
{
1: required i32 shotel_id,
2: required i32 sroom_id,
3: required i32 rate_plan_id,
}

struct MHotelAttr
{
 1:    required i64 mhotel_id ,
 2:    optional bool mroom_filter , //; 
 3:	list<i32> selected_mroom_ids ,
 4: list<SelectedProduct> selected_product_ids, // 指定的产品id，目前只给活动页面用
}

struct MRoomTypes
{
1:    required i64 mroomtype_id,  //mroomtype id
2:    optional string mroom_name,  //mroontype name
3:    list<Product> products,  
4:    optional i32 bed_type,   // 36: big bed, 37: double bed, 38: single bed, 39: special bed, 40: other
5:    optional i32 priority,
}

struct Longcuistruct
{
    //最低价格产品：当且仅当type为1，且has_longcuionly为true，这时才表示最低价格是龙翠专享，否则，最低价格不是龙翠专享
	//酒店：只要has_longcuionly为true，则表示酒店有龙萃专享
1:    optional bool has_longcuionly, 
2:	optional i32 type, //1：表示该标志位是对最低价格产品的；2:表示该标志位是对酒店的
}

struct Tejiastruct
{
    //最低价格产品：当且仅当type为1，且has_weifang为true，才表示最低价格是特价房，否则不是；
1:    optional bool has_weifang,
2:	optional i32 type, //1：表示该标志位是对最低价格产品的；2:表示该标志位是对酒店的
}

struct ManJianstruct
{
1:    optional bool has_manjian,
2:	optional i32 type,  //1: the product who has min price has manjian; 2: the product(not min price) has manjian)
 3:    list<PromotionDescription> promotion_description , 
}

struct Confirmstruct
{
1:    optional bool has_confirm, //true means this mhotel has confirm product;
2:    optional i32 type,  //1: the product who has min price has confirm; 2: the product(not min price) has confirm
}

struct Danbaostruct
{
    //最低价格的产品：当且仅当type为1的时候，且need_guarantee为true，才表示最低价格是特价房，否则不是
1:    optional bool need_guarantee,
3:	optional i32 type, //1:表示该标志位是对最低价格产品的；2:表示该标志位是对酒店的
}

struct MobileOnlystruct
{
    //最低价格的产品：当且仅当type为1的时候，且has_mobileonly为true，才表示最低价格是手机专享，否则不是
1:    optional bool has_mobileonly,
2:    optional i32 type, //1:表示该标志位是对最低价格产品的；2表示该标志位是对酒店的
}

struct Couponstruct
{
    //最低价格产品：当且仅当type为1，且has_coupon为true，才表示最低价格有消费券，否则不是
1:    optional bool has_coupon,
2:	optional double upper_limit, //上限
3:	optional i32 type, //1:表示该标志位是对最低价格产品的；2:表示该标志位是对酒店的
}

struct HongBaostruct
{
    //最低价格产品：当且仅当type为1，且has_coupon为true，才表示最低价格有红包，否则不是
1:    optional bool has_hongbao,
2:	optional double upper_limit, //上限
3:	optional i32 type, //1:表示该标志位是对最低价格产品的；2:表示该标志位是对酒店的
4:	optional i32 promotion_type,
}

struct ZhoubianProduct
{
    //最低价格的产品：当且仅当type为1的时候，且has_zhoubian_pro为true，才表示最低价格是周边价格产品，否则不是
1:	optional bool has_zhoubian_pro,
2:	optional i32 type, //1:表示该标志位是对最低价格产品的；2表示该标志位是对酒店的
}

struct CheckInPersonForOneRoom
{
1:    optional i32 min_checkin_person_for_oneroom,
2:	optional i32 max_checkin_person_for_oneroom,
}

struct AllBuyRoomstruct
{
    //最低价格的产品：当type为1且has_allbuyroom_pro为true的时候，才表示最低价格是买断房产品，否则不是
1:	optional bool has_allbuyroom_pro,
2:	optional i32 type, //1:表示该标志位是对最低价格产品的；2表示该标志位是对酒店的
}

struct PromotionCount
{
 1:    required i32 promotion_type , //
 2:	required i32 count ,
}

struct PromotionTypeMsg
{
 1:	required i32 id ,
 2:	required bool  is_effective_price , // 是否加入返后价计算
3:    optional i32 priority_level     ,  //优先级
4:    optional i32 is_special         ,  //是否属于特殊处理组(1代表数据特殊处理组)
5:        optional map<i32,i32> promotion_cities,
}

struct PromotionGroup
{
 1:    required i32 group_id ,
 2:	list<i32> promotion_type ,
 3:	list<PromotionTypeMsg> type_list , // 拟废弃字段promotion_type，以本字段替换
 4:	optional i32 businessType ,  //产品支付方式 ：1001:现付， 1005:预付
 5:	optional i32 orderFromGroupId , //产品线：108101：网站，  108102:手机
6:    optional i32 group_type ,            //0:间夜纬度   1:订单纬度
}


//活动打标（如5.1大促，端午大促等）
struct ActivityTag
{
1:	optional i32 tag_id,          //活动标识
2:	optional string tag_name,        //活动名称
3:	optional i32 priority_level,  //优先级
}

// 标志struct
// flag_type: 1, 铂涛可用红包; 2, 铂涛可返红包;3，Longcuistruct；4，TeJiastruct；5，Danbaostruct；
// 6，MobileOnlystruct；7，Couponstruct；8，HongBaostruct；9，ZhoubianProduct；10，AllBuyRoomstruct；
// 11，ManJianstruct；12，Confirmstruct，object只支持2；13，MaxDiscount,object只支持2;14,MemberBenefits,会员优惠标 15,五折
//16:N折起，最高可省 17:铂涛会员价标签18, 活动打标 19: 钟点房  1019:转让房, 1020:中大网视促销, 1021:闪住, 1022：信用住,1023:微信专享,1024:微信钱包新客专享N折活动标识 1025:铂涛新会员
struct HotelFlag
{
 1:    required    i32   flag_type   , // 表示标记类型
 2:    optional    bool    effective   , // 标志的有效性, true: 有/是, false: 无／否
 3:    optional    i32   object      , // 标志的对象, 1: 最低价格产品, 2: 酒店
 4:    optional    double  upper_limit , // Coupon,HongBao 上限
 5:    optional    i32   promotion_type ,  //HongBao: 促销类型
 6:    list<PromotionDescription> promotion_description ,  //ManJian
 7:    optional    i32   price ,    // 最大折扣对应原价
 8:    list<double> discount_rates , //折扣率集合
 9:    optional    double  low_discount_rate,//N折起
 10:   optional    i32   high_sub,//最高可省
 11:	list<ActivityTag> activity_tags,//活动打标
}

//定制输出产品信息
//type: 1,公寓top2房型返后价展示信息.
struct CustomizedProductInfo
{
 1:    optional i32 type ,     //类型
 2:    optional i32 price ,      //返前价格
 3:    optional i32 price_sub_coupon ,  //返后价格
 4:    optional i64 roomtypeid ,     //sroomid   
 5:    optional i64 rateplan_id , // rpid
 6:    optional i64 mroom_id ,  //mroomid
7:    optional i32 shotel_id ,  //shotelid
}

//最低价信息
//type:1, 预付可卖产品最低价（返前价）
//type:2, 预付可卖产品最低价（返后价）
//type:3, 现付可卖产品最低价（返前价）
//type:4, 现付可卖产品最低价 (返后价)
//type:5, 钟点房可卖产品最低价 (返前价)
//type:6, 钟点房可卖产品最低价 (返后价)
struct MinPriceInfo
{
1:    optional i32 type,
2:    optional i32 min_price,
3:    optional i64 min_price_rpid,
4:    optional i32 min_price_sroomid,
5:    optional i32 min_price_mroomid,
}

//挂在MHOTEL下的一些附带的价格信息
struct IncidentalPriceInfo
{
 1:    optional i32 min_price_cansale_sub_coupon_origin , //可卖的返后价最低价产品的原价（底价）
 2:    optional i32 min_price_cansale_sub_coupon ,  //可卖的返后价最低价产品的卖价（返后价）
 3:    list<MinPriceInfo> min_price_info ,
}

//酒店统计信息
//type：1 无早，2，单早，3，双早，4，3早及以上，5，免费取消，6，立即确认，7，艺龙直销，8，礼品
//count:产品数量
struct StatisticsInfo
{
 1:   optional i32 type,
 2:   optional i32 count, 
}

struct PromotionRange
{
	1: optional i32 promotionStatsType,  //优惠类型 0-红包 1-返现 2-立减 3-N折
	2: optional double minPromotion, //最小优惠额
	3: optional double maxPromotion, //最大优惠额 
}

struct MHotelDetail
{
1:    required i64 mhotel_id, //mhotel id
2:    optional bool has_drr,  //是否有drr促销规则
3:    optional Longcuistruct longcui_info,  //是否有龙萃专享产品
4:    optional Tejiastruct weifang_info,  //是否有尾房产品（即特价产品）
5:	optional bool has_tuan,  //是否有团购产品
6:    optional i32 inventory_type,  //库存类型： 0表示全部无房，1部分有房，2全部有房
7:    optional i32 min_price,    //最低价格  
9:    optional i64 min_price_rpid,  //最低价格的rateplanid
10:    optional i64 min_price_roomtypeid,  //最低价格的房型ID
11:    optional Danbaostruct need_guarantee,  //是否有需要担保的产品
12:    optional i32 product_count,  //可预订的产品总数
22:	optional i32 product_can_be_showed, //可被展示的产品总数(product_count为0的情况下，这个参数也可能不是0，有种情况)
13:	optional i32 promotion_type_count, 
14:	list<MRoomTypes> room_types, //mroom type id list
15:    list<SHotelHelpfulTips> shotel_helpfultips,
16:    list<SHotelBookingRule> shotel_booking_rules,
17:	list<SHotelInvoiceInfo> shotel_invoice_info, //酒店开发票信息：0表示没维护,1表示艺龙开发票,2表示酒店开发票
18:    optional MobileOnlystruct mobileonly_struct,  //是否有手机专享产品
19:    optional bool has_yufu,  //有预付产品
20:	optional i32 product_count_reason,// product_count计数的原因：1：正常；2：因为该mhotel下面存在暂停服务的酒店；
21:	optional Couponstruct coupon_struct,
28:	optional HongBaostruct hongbao_struct,
23:	optional bool has_timerush_product,//是否有可卖的限时抢产品
24:	optional i32 min_price_pro_relation_price, //最低价格产品的关联价格, 如果没有这个字段，这表示最低价格的产品没有相关联的产品。
25:	optional i32 mroom_count, //mroom房型的总数：用于list搜索
26:	optional bool is_hotel_inventory_full, //酒店是否满房
27:	optional i32 min_price_mroomtypeid,//code和min_price的code是一样的
29:	optional ZhoubianProduct zhoubian_struct,
30:	optional bool has_buy5send1_promotion,  //是否有买五赠送一活动
31:	optional bool has_halfdiscount_promotion, //是否有半价促销活动
32:	optional i32 min_price_sub_coupon,
33:	optional i64 min_price_sub_coupon_rpid,
34:	optional i64 min_price_sub_coupon_roomtypeid,
35:	optional i32 min_price_sub_coupon_mroomtypeid,
36:	optional bool firstnight_has_discount, 
37:	optional bool has_danbao_product,
38:	optional AllBuyRoomstruct allbuyroom_struct,
39:	list<PromotionCount> promotion_count, //only mobile has this function; web/mis etc has not;(through code crontol this)
40:	optional ManJianstruct manjian_struct, //only mobile has this function; web/mis etc has not;(through code crontol this)
41:	optional i32 min_price_sub_coupon_origin, // 最低返后价的原价（返前价）
42:    optional Confirmstruct confirm_struct,
 43:    list<HotelFlag> hotel_flag , // 酒店层面的标志
 44:    optional bool has_moremember_products ,   //提示非登录用户是否登录有更多产品 
 45:    list<CustomizedProductInfo> cp_info , //定制输出产品信息
 46:    optional IncidentalPriceInfo incidental_price_info ,//附带的价格信息
 47:    list<StatisticsInfo> statistics_info, //统计数组
48:optional i32 hotel_service_status,//酒店服务状态
49:optional i32 min_price_sale_cost,
50:optional i32 min_price_sub_coupon_sale_cost,
51:optional i32 min_weifang_price,
52: list<MinPriceInfo> hours_room_min_price_cansale,   //钟点房可卖的最低价(包含返前价和返后价)
53: optional string simple_mrooms,
54: list<Inventory> min_price_inventories, // 最低价产品库存列表
55: list<Inventory> min_price_sub_coupon_inventories, // 返后最低价库存列表
56:optional i32 star_type, // 星级类型（1：真、0：准）
57:optional i32 star, // 星级信息
58:optional bool is_economic, // 是否经济型
59:optional list<PromotionRange> promotionStats, //酒店促销信息统计(按优惠类型得到酒店底下最小最大优惠金额)
}

struct SimplePromotion
{
1:optional i32 promotion_id,
2:optional i32 uper_limit;
}

struct SimpleProduct
{
1:optional i32 sale_cost,//底价
2:optional i32 sale_price,//卖价
3:list<SimplePromotion> promotion_type,
4:optional list<Inventory> inventorys,//库存信息
5:optional i32 sroom_id;
6:optional i32 rp_id;
7:optional i32 shotel_id;
}

struct SimpleMRoom
{
1:optional i32 mroom_id,
2:list<SimpleProduct> products,
}


struct ListProductInfo
{
1:    optional bool return_min_price_product,
2:	optional bool need_sorted_top_product,
3:	optional i32 top_product_num,
4:	optional i32 sort_types, //强行指定排序方法：0默认排序；1价格排序；2房间入住人数排序；3预付排序；4限时抢排序；5消费券排序；6龙萃排序；7早订省排序；8连主省排序
 5:    optional bool return_min_stay_product , // 是否返回最小入住天数最低 但大于入离店时间差 产品
 6: optional bool return_min_ac_price_simple_product , // 是否返回最低价简单产品信息,搜索排序使用
}

// Promotion过滤黑名单
struct PromotionBlackList
{
 1:    optional i32 method_type ,   //0或者不传：表示都要过滤；1:针对预付promotion；2：针对现付promotion
 2:    required i32 promotion_type , //标记黑名单中的promotion_type
}

struct ProductTypeBlackList
{
1:    optional i32 product_type, //产品类型
2:    list<i64> supplier_ids, //供应商id数组
3:    optional bool  partial_match,  // 是否部分匹配，true:是，false：否
}

//FilterCondition 筛选条件
// type：
//1,最小入住天数限制;
//2,N间起订;
//3, 早餐筛选. filter_value:1,筛选单早。2,筛选双早 3,筛选3早及以上
//4, 床型筛选.filter_value:36,大床。37，双床。38，单人床。39，特殊床型。40，其他。
//5, 支付方式筛选. filter_value: 1,现付。2，预付
//6, 给定一个product_type，过滤给定的supplierID 产品
//7,取消规则筛选;   filter_value：139，表示免费取消
//8,确认方式筛选;   filter_value：141，立即确认
//9,供应商类型筛选; filter_value: 138，表示艺龙直销
//10,礼包筛选;      filter_value: 140，有礼品
    //use_or_not 传1表示使用此条件
    //filter_value 要排除的 product_type,
    //exclude_value_array传要过滤的supplierID集合 
    //apply_level 传1 表示产品过滤
    //partial_match 传false表示过滤 产品的rp的product_type 与 filter_value相等的产品
                  //传true表示过滤 产品的rp的product_type 与 filter_value 相与不为0的产品
//11, 发票模式筛选  filter_value: 1, 艺龙开发票. 2, 酒店开发票, 
//12,二手房筛选;      filter_value: 1，有二手房
//13,钟点房  filter_value:1
//14,闪住 filter_value:1
//15,信用住 filter_value:1
//17,含有景酒产品的酒店,filter_value:1

struct FilterCondition
{
 1:    optional i32 type , //过滤条件类型,
 2:    optional i32 use_or_not ,  //1:使用，0：默认原来逻辑，-1：不使用[default=1];
 3:    optional i32 filter_value, //按filter_value筛选
4:    optional i32 apply_level, // 应用级别：1,产品 2,酒店 (目前“供应商类型,取消规则，礼包,立即确认”支持酒店筛选)
5:    list<i64> exclude_value_array,//
 6:   optional bool  partial_match,// 是否部分匹配，true:是，false：否
  7:  list<ProductTypeBlackList> ptb_array, //产品类型的黑名单
}


//ReturnCondition 返回条件数组
//type: 1,定制产品信息
//struct ReturnCondition
//{
 //1:    optional i32 type , //条件
 //2:    optional bool use_or_not , // true:使用，flase:不使用
//}

enum BookingMenu
{
	kGeneralMenu = 1,    // 常规菜单
	kHourRoomMenu = 2,    // 钟点房频道
	kGroupBuyMenu = 3,    // 团购频道
}

// 产品排序+特征分策略
// code = 默认值 + 排序值 + 特征值
// 默认值: 2000
// 特征值是bitmap存储, 各位依次为:
// 第1位(最低位): 支付方式, 第2位: 早餐, 第3位: 供应商
// 第4位: 立即确认, 第5位: 收益/CVR(0: 收益, 1: CVR)
// 并且第5位同时表示排序策略
// code的取值与含义如下:
// 2000: 收益
// 2001: 收益 + 支付
// 2002: 收益 + 早餐
// 2003: 收益 + (支付 + 早餐)
// 2004: 收益 + 供应商
// 2005: 收益 + 供应商 + 支付
// 2006: 收益 + 供应商 + 早餐
// 2007: 收益 + 供应商 + 支付 + 早餐
// 2016: cvr
// 2017: cvr + 支付
// 2018: cvr + 早餐
// 2019: cvr + (支付 + 早餐)
// 2020: cvr + 供应商
// 2021: cvr + 供应商 + 支付
// 2022: cvr + 供应商 + 早餐
// 2023: cvr + 供应商 + 支付 + 早餐
struct Grandson
{
1:    list<i32> codes,   // 取值范围: [2000, 2031]
}

// 用户特征单元
// 支付特征:    1, 取值: 0: 预付, 1: 现付
// 早餐特征:    2, 取值: 0: 无早, 1: 单早, 2: 双早, 3: 三早及以上
// 供应商特征:  3, 取值: 1: elong, 2: 其他
struct CustomerTraitUnit
{
 1:   required    i32   code, // 用户属性编号
 2:   list<i32>   values, // 用户属性值
}

struct CustomerTrait
{
 1:   list<CustomerTraitUnit>   trait_units,
}

//用户集团信息
struct GroupInfo
{
 1:   required    i32   group_id,//集团id,
 2:   optional    i32   elong_level,//用户集团等级对应的艺龙等级
}


struct PromotionGroupRelation {
 1:    required    i32    group_id             ,
 2:    list<PromotionTypeMsg>  type_list      ,
}

struct PromotionGroupType {
 1:    required    i32    group_type_type ,  // 0: 间夜  1:订单
 2:    list<PromotionGroupRelation> promotion_group_relation ,
}

struct PromotionBusiness {
 1:    required    i32    business_type ,  // 1005: 预付 1001:现付
 2:    list<PromotionGroupType> promotion_group_type ,
}

struct PromotionOrderFromLine {
 1:    required    i32    order_from_type ,   // 108101: web 108102: mobile
 2:    list<PromotionBusiness>    promotion_business ,
}

struct PromotionGroupRoot {
 1:    list<PromotionOrderFromLine> promotion_order_from_line ,
}

struct CommonConf {
 1:    list<PromotionGroupRoot> promotion_group_root   ,
}



struct DcPriceRequest {
    //  m酒店id
    1:  i32 mhotel_id,
    //  s酒店id
    2:  i32 shotel_id,
    //  s房型id
    3:  i32 sroom_type_id,
    //  rpid
    4:  i32 rateplan_id,
    //  入店日
    5:  string checkin_date,
    //  离店日期
    6:  string checkout_date,
}

struct DcPriceResponse {
    //  卖价
    1:  double sale_price,
	//  返回码
	2:  required i32 return_code, //0:成功;1:入参错误;2:业务异常;-1:系统异常
	//  返回信息描述
	3:  string return_msg, 
}


struct DebugPromotion
{
1:    required string  date ,
2:    required i32  promotion_id,
3:    required i32  promotion_type,
4:    required bool   use_ok,//[default=true]
5:    optional string  reason,
6:    optional i32  upperlimit,
}


struct DebugDrr
{
1:    optional string type,
2:    optional double drrnum,
}

struct DebugPrice
{
1:    required string date,              //价格对应日期
2:    optional i32 status,            //1为有效，其他位无效
3:    optional i32 add_bed_price,     //加床价格
4:    optional string currency,          //币种
5:    optional double gen_sale_cost,   //平日低价
6:    optional double gen_sale_price,   //平日卖家
7:    optional bool is_add_bed,  //是否允许加床，true表示允许加床，false表示不允许加床
8:    optional bool is_hotel_weekend,   //是否酒店的周末
9:    optional bool is_price_promotion, //是否促销  (特别注意，这里不是指promotion，而是指是否经过DRR的促销)
10:    optional double real_cost, //真实成本价（初始值为底价（平日或者周末）），在计算drr的时候，根据金额或者比例，在自身的基础上进行计算
11:    optional double sale_cost,  //底价  （这个如果是平日，则为gen_sale_cost,如果为周末，则为weekend_sale_cost)
12:    optional double sale_price, //卖价   (这个如果是平日，则为gen_sale_price, 如果为周末，则为weekend_sale_price)
13:    optional double sale_price_with_drr, //计算过促销后的价格 (最终给用户显示的每一天的房价就是这个字段)
14:    optional double weekend_sale_cost,  //周末底价
15:    optional double weekend_sale_price,  //周末卖价
16:    optional double weekend_price_origin, //周末卖价的原始币种价格
17:    optional double general_price_origin, //平日卖价的原始币种价格
18:    optional double sale_price_with_drr_origin, //经过促销后的价格（原始>币种
19:    optional double add_bed_price_origin,//加床价格(原始币种)
20:    optional double sale_price_with_drr_sub_coupon,
21:    optional DebugPromotion used_promotion,     //返后价计算使用的是哪个promotion
22:    optional double used_drr,                //使用到的drr
}

struct DebugBaseMajiaStrategy
{
1:  required i32 key,
2:    optional i32  version,
3:    optional double  cashbackAmount,
4:    optional double  cashbackMaxCmsRatio,
5:    optional double  cashbackMaxDiff,
6:    optional i32  cashbackAboveQuota,
7:    optional double  prepayDiscount,
8:    optional double  prepayMinPriceRatio,
9:    optional double  prepayMinPriceDiff,
10:    optional i32  prepayBelowQuota,
11:    optional i32  majiaComfirmFlag,
12:    optional double  majiaAvgProcTimeDiff,
13:    optional i32  majiaDisplayChannel,
14:    optional i64  majiaValidDateStart,
15:    optional i64  majiaValidDateEnd,
16:    optional i64  updateTime,
17:    optional string  operator,
}


struct DebugMajiaProductDescription
{
1:    optional i32  MajiaProductType, // 最终从马甲出来的产品类型。 0：马甲未做处理；1：马甲；2：中央定价；3：马甲+中央定价
2:    optional i32  filteredProductType, //马甲从计算过程中出来被过滤掉的产品。同MajiaProductType
3:    optional string description, //
}


struct DebugMBL
{
1:    required i64  date, //日期
2:    optional double price, 
3:    optional i32 priceFrom, //来源0去哪,1携程
}

struct DebugZYDJ
{
1:    required i64  date, //日期
2:    optional double price,
}

struct DebugMajia
{
1:    required i32  payType, //支付类型。0：现付；1：预付
2:    required i32  breakfast, //0：无早；1：含早
3:    optional double basePrice, //底价
4:    optional double salePrice, //马甲前卖价
5:    optional double majiaSalePrice; // 马甲后卖价
6:    required bool   baseFlag,//是否马甲基础产品
7:    list<DebugMBL> mbls,
8:	  optional DebugZYDJ zydj,
9:    optional string strategyType,//
10:   optional DebugBaseMajiaStrategy baseMajiaStrategy,
11:   optional DebugMajiaProductDescription majia_description

}

struct DerivativeDesc 
{
1:		required i32  type,  //1预付定价 2高定高返 3中央定价 4马甲
2:		optional string reason,
}

struct PriceDealStep
{
1:	required i32  main_type,//1DRR 2促销 3衍生品
2:	required i32  sub_type,//1:DRR
							//2: 促销type
							//3: 1预付定价 2高定高返 3中央定价 4马甲
3:	required bool is_handle,//是否经过此步骤
4:	optional double avg_sale_cost_before,
5: optional double avg_sale_price_before,
6: optional double avg_sale_price_drr_before,
7: optional double avg_sale_price_sub_coupon_before,
8:	optional double avg_sale_cost_after,
9: optional double avg_sale_price_after,
10: optional double avg_sale_price_drr_after,
11: optional double avg_sale_price_sub_coupon_after,
12:  optional string handle_desc,
13: list<DebugMBL> mbls,
14:	optional DebugZYDJ zydj,
15: optional double upper_limit,
}

struct DebugProduct
{
1:    required i32  product_id,
2:    required i32  rp_id,
3:    required i32  mroom_id,
4:    required string  mroom_name,
5:    required i32  shotel_id,
6:    required i32  sroom_id,
7:    required string  rp_name,
8:    required bool   return_ok,//[default=true]
9:    optional string  reason,
10:    optional string  promotion_all,
11:    list<DebugDrr> drr,
12:    list<DebugPromotion> promotion,
13:    list<DebugPrice> price,
14:	  optional DebugMajia majia,
15:   optional i32 derivative_type,
16:   optional double mis_avg_sale_cost,
17:   optional double mis_avg_sale_price,
18:	  optional i32 pay_type,//0：现付；1：预付
19:	  list<PriceDealStep> price_deal_steps,
20:   optional string  majia_reason,
21:		list<DerivativeDesc>  derivative_reason,
22:	  optional i32 breakfast,//早餐份数
23:	  optional map<string,bool> baseFlag, //各种标集合 key majia_is_base:马甲  gdgf_is_base:高定高返 						 //majia_prepay_low_product马甲预付最低价产品，majia_cash_low_product马甲现付最低价产品，
24:	  optional map<string,string> others, //各种数据集合 key 预付定价相关:prepay_* 高定高返相关:gdgf_* 马甲相关:majia_* 其他自定义不重复
25:   optional i32   reason_id,
26:   optional i16 inventory_type,  //库存类型： 0表示全部无房，1部分有房，2全部有房
}





struct DebugSRoom
{
1:    required i32           sroom_id,
2:    required bool            return_ok,//[default=true]
3:    optional string           reason,
4:    list<DebugProduct>    product,
5:    optional i32 inventory_type,  //库存类型： 0表示全部无房，1部分有房，2全部有房
6:    optional string           majia_reason,
7:		list<DerivativeDesc>  derivative_reason,
8:   optional string   mroom_name,
9:   optional i32   mroom_id,
10:   optional i32   reason_id,
}

struct DebugSHotel
{
1:    required i32          shotel_id,
2:    required bool           return_ok, //该shotel是否出了[default=true]
3:    optional string          reason ,  //该shotel没出的原因\
4:    optional string          promotion_all,
5:    list<DebugSRoom>     sroom,
6:    list<DebugPromotion> promotion,
7:     optional string supplier_name,
8:     optional i32 supplier_id,
9:    optional string           majia_reason,
10:		list<DerivativeDesc>  derivative_reason,
11:   optional i32   reason_id,
}

struct DebugMRoom
{
1:    required i32          mroom_id,
2:    required string      majia_reason,
3:    required bool           return_ok,
4:    optional string          reason ,
5:		list<DerivativeDesc>  derivative_reason,
6:	  optional map<string,bool> baseFlag, //标签集合
7:	  optional map<string,string> others, //其它
8:   optional i32   reason_id,
}

struct DebugMHotel
{
1:    required i32          mhotel_id,
2:    list<DebugSHotel>    shotel,
3:    optional string      majia_reason,
4:    list<DebugMRoom>    mroom,
5:    optional string      reason,  
6:		list<DerivativeDesc>  derivative_reason,
7:	  optional map<string,bool> baseFlag, //标签集合
8:	  optional map<string,string> others, //其它
9:   optional i32   reason_id,
}

struct DebugResponse
{
    1:optional DebugMHotel mhotel,
}

struct UserCreditLiveInfo
{
1:required bool flash_live_filter,//是否闪住
2:required bool credit_live_filter,//是否信用住
3:required bool credit_value_live_filter,//是否按信用住额度过滤
4:optional double user_credit_value,//用户信用额度
5:optional i32  flash_live_period,//闪住信用通道有效期
6:optional i32  credit_live_period,//信用住信用通道有效期
}

struct StringModel
{
1: optional string content,
}


struct ProductDayInfo
{
1:optional string date,
2:optional bool has_breakfast,
3:optional bool has_inventory, // 是否有库存， 满房的也参与比价 
4:optional i32 status, // 产品是否有效，产品无效判断优先级：酒店 > 房型 >  产品 > 价格 > 房态，需区分
5:optional double sale_cost, // 平日底价
6:optional double sale_price, // 平日卖价
7:optional bool is_weekend_price, // 是否周末价
}

struct ProductInfo
{
1:optional i32 shotel_id,
2:optional i32 mroom_id,
3:optional i32 sroom_id,
4:optional string mroom_name,
5:optional i32 rp_id,
6:optional string rp_name,
7:optional i32 settlement_type,
8:optional bool is_hours_room, // 是否小时房
9:optional bool is_direct_sign, // 是否直签
10:optional i32 supplier_type, // 0:艺龙  1:携程  2:去哪儿最早最晚到店时间项目
11:optional i32 supplier_id, // 供应商id
12:optional string supplier_name, // 供应商名称
13:optional list<ProductDayInfo> product_day_info, // 产品到天信息
}

struct MhotelInfo
{
1:required i32 mhotel_id,
2:optional list<ProductInfo> product_info,
}

struct GetProductBaseInfoRequest
{
1:required list<i32> mhotel_ids, // 酒店id
2:required i64 begin_date, // 开始日期
3:required i64 end_date, // 结束日期
}

struct GetProductBaseInfoResponse
{
1:optional list<MhotelInfo> mhotel_info, // 酒店信息
2:optional i32 return_code, //0：正常
3:optional string return_msg, //
}

struct ShotelAttr
{
1:required i32 shotel_id,
2:optional list<i32> sroom_ids,
}

struct MhotelShotelAttr
{
1:required i32 mhotel_id,
2:optional list<ShotelAttr> shotel_attr,
}

struct GetInvAndInstantConfirmRequest
{
1:required list<MhotelShotelAttr> mhotel_attr,
2:required i64 start_date,
3:required i64 end_date,
4:optional bool need_instant_confirm,
5:optional i64 order_from,
6:optional i32 search_from, //3：NBAPI
}

struct InvDetail
{
1:optional string begin_date,
2:optional string end_date,
3:optional string begin_time,
4:optional string end_time,
5:optional i32 available_amount,
6:optional string available_date,
7:optional i32 is_over_booking,
8:optional i32 status, // 库存状态
9:optional bool instant_confirm, // 是否可立即确认
10:optional string ic_begin_time, // 立即确认开始时间
11:optional string ic_end_time, // 立即确认结束时间
}

struct SroomDetail
{
1:required i32 sroom_id,
2:optional list<InvDetail> inv_detail,
}

struct ShotelDetail
{
1:required i32 shotel_id,
2:optional list<SroomDetail> sroom_detail,
}

struct MhotelInfoDetail
{
1:required i32 mhotel_id,
2:optional list<ShotelDetail> shotel_detail,
}

struct GetInvAndInstantConfirmResponse
{
1:optional list<MhotelInfoDetail> mhotel_detail, // 酒店信息
2:optional i32 return_code, //0：正常
3:optional string return_msg, //
}

//价格元数据

struct HotelBasePriceRequest
{
1: required i32 mhotel_id,
2: optional i32 shotel_id,
}

struct GetBasePrice4NbRequest
{
1: optional list<HotelBasePriceRequest> hotel_base_price_request,
2: required i16 payment_type, //0 所有，1:现付 2:预付
3: required i32 start_date,//必填，单位秒
4: required i32 end_date,//必填，单位秒
5: required i32 booking_channel,//非0，必填
6: required i32 sell_channel,//非0，必填
7: required i32 member_level,//非0，必填
8: optional string traceId,//选填，用于区分一次请求的标识uuid
}

struct BasePrice
{
1: required i32 start_date,
2: required i32 end_date,
3: optional i16 status,
4: optional i64 price_id,
5: optional bool allow_add_bed,
6: optional i32 add_bed_price,
7: optional string currency_code,
8: optional i32 general_cost_origin,
9: optional i32 general_price_origin,
10: optional i32 weekend_cost_origin,
11: optional i32 weekend_price_origin,
}

struct RatePlanBasePrice
{
1: optional i32 rateplan_id,
2: optional list<BasePrice>  base_price;
}

struct SRoomBasePrice
{
1: optional i32 sroom_id,
2: optional list<RatePlanBasePrice> rateplan_base_price,
}

struct SHotelBasePrice
{
1: optional i32 shotel_id,
2: optional list<SRoomBasePrice> sroom_base_price,
}

struct MHotelBasePrice
{
1: optional i32 mhotel_id,
2: optional list<SHotelBasePrice> shotel_base_price,
}

struct GetBasePrice4NbResponse
{
1: optional list<MHotelBasePrice> mhotel_base_price,
2: optional i32 return_code, //0：正常
3: optional string return_msg, //
}
//价格元数据 -end


struct SearchRequest
{
1:    list<i64> mhotel_ids, // 已废弃，替换为mhotel_attrs字段
2:	optional i64 booking_datetime,  //预订时间日期, 时间戳
3:	required i64 checkin_date,  //日期类型为：2013-11-21
4:	required i64 checkout_date,  //日期类型为：2013-11-21
5:	optional i32 booking_channel,  //预定渠道：bitmap存储：第0位：没有使用；第1位：线上；第2位：线下；第3位：积分广场；第4位：手机；第5位：SEM特殊?
6:	optional i32 sell_channel,  //分销渠道：bitmap存储：第0位：；第1位：A；第2位：B；第3位：C；第4位：D；第5位：E；第6位：F；第7位：G；第8位：H；第9位：I；第10位：J
7:	optional i32 customer_level,  //会员级别：bitmap存储：第0位：普通会员；窿位：vip；第2位：龙萃会员；第3位：M会员
8:	optional SelectPrice select_price,
9:	optional bool is_limit_timesale,  //为true表示只输出包含尾房产品的酒店，为false表示此项不涉及到搜索的过湿(今日特价)
10:	optional i32 price_type,  //价格类型?表示统一价；2表示内宾价格?表示外宾价格?表示港澳台客人价?表示日本客人价格。注意这个不是bitmap存储的?
11:    optional i32 product_type,  //产品类型：bitmap存储? 第0位：单独销售；第1位：打包销售；第2位：隐价产品；第3位：酒店杀价；第4位：限时抢；第5位：钟点房；第6位：团购产品; 第7位：国际酒店产品； 第8位：周边价格； 第9位：9元/半价抢
12:    optional i32 settlement_type, //支付类型:1表示前台自付，2表示代收代付。注意：非bitmap存储
13:	list<i32> supplier_type,  //供应商类型：（空?所有，1、3=elong自有,?2=非elong
14:    list<i32> online_search_type,  //直连酒店类型：0=elong自有?1=EAN?2=万豪。直连酒店即非elong自有的酒店，目前只有EAN和万豪两个，以后可能多个
15:    optional i32 promotion_type, //promotion类型：1：coupon(消费券)；2：point(积分)；3：discount(折扣)；4：gift(礼品)；5：cash(返现)；6：特殊优惠1；7：特殊优惠2；9：立减项目；10：红包。
16:    optional i64 order_from_id,  //订单来源ID：各个商家的ID编号，各个与elong有合作的商家的编号，用于在订单确认的时候搜索过滤?
17:    optional string proxy_id,   //代理ID
18:    optional string promotion_channel_code,  //promotion渠道代码
19:    optional bool need7daygift,  //为true表示，如果礼包是7天内的，也需要返回，为false表示不涉及搜索过滤
22:    list<i32> codes,  //定制化输出的代码数组
23:    optional bool return_noinv_or_noprice_product, //需要返回每一天都没有库存和价格的产品（检索默认返回检索中的全部都库存价格和部分有库存价格的产品）
24:    optional bool return_has_coupon_hotel, //只返回有消费券产品的酒店
25:	optional bool return_has_no_danbao_hotel, //只返回有非担保产品的酒店
26:	optional CheckInPersonForOneRoom checkin_person_for_oneroom,  //每间房入住的人数
27:	optional bool return_has_yufu_hotel, //只返回有预付产品的酒店
28:	optional bool onlydebug,//后台bug设置，仅仅供ds服务器自测使用，请as端不要传递此参数给前端。
29:	optional bool return_has_timerush_product_hotel, // (限时抢)
30:	list<i32> bed_type, //36   大床   37  双床        38  单人床      39  特殊床型       40  其他 
31:	optional ListProductInfo list_product_info, //top2排序相关
32:	optional bool return_has_lianzhu_pro_hotel, //返回有连住省产品的酒店
33:	optional bool return_has_zaoding_pro_hotel, //返回有早订省产品的酒店
34:	optional i32 request_origin, //检索请求来源： 1.PC；2.国际自签；3.h5；4.手机app;5.团购;6.公寓[default=3]
35:    optional bool return_longcuionly_hotel, //返回包含龙萃专享产品的酒店: 0表示否，1表示是
36:    optional bool return_has_hongbao_hotel, //返回包含红包产品的酒店
37:	optional bool judge_only_has_product, //如果为true，该酒店只要有一个产品可预订则返回，不需要考虑其他产品了.
38:	optional bool half_discount_promotion, //是否展示半价促销活动的产品
39:    optional i32 search_method,
40:    optional bool return_has_discount_promotion_hotel,
41:	optional i64 search_id,
42:	optional bool price_sub_coupon,//[default=false]
43:	optional bool return_freesale_msg,//[default=false]
44:	list<MHotelAttr> mhotel_attrs, // 酒店属性，包含酒店ID、房型ID，用于替换mhotel_ids字段
45:    optional bool return_has_allbuyroom_hotel, // 用于买断房过滤[default=false]
46:	optional bool return_has_manjian_hotel,//[default=false]
47:    optional i32 language, //CH:0; EN:1[default=0]
48:    optional i32 discount_method, //1: 只要预付五折；2：只要现付五折；3：既要预付五折又要现付五折；不传这个参数表示不要五折产品
49:    optional i32 return_discount_hotel, //1：只要该酒店包含1个预付五折的产品，这个酒店就返回（不用考虑现付五折的情况）;2:只要该酒店包含1个现付五折的产品，这个酒店就返回（不用考虑预付五折的情况）；3：这个酒店必须同时包含一个预付五折和一个现付五折的产品，这个酒店才返回；4：这个酒店只要有1个预付五折或者1个现付五折的产品，这个酒店就返回
50:    optional i32 min_price_calc_with_halfdiscount_pro,//1：表示最低价计算既包含现付五折的产品也包含预付五折的产品；2：表示最低价计算只包含预付五折的产品，不包含现付五折的产品；3：表示最低价计算只包含现付五折的产品，不包含预付五折的产品；4：表示最低价计算即不包含预付五折的产品，也不包含现付五折的产品[default=1]
 51:    optional i32 botao_customer_level ,   // 铂涛会员等级
 52:    optional bool use_botao_promotion ,  //是否使用铂涛红包
 53:    optional bool use_day_promotion ,   //是否使用按天返的promotion
 54:    optional bool only_consider_salable , // (最低价计算/酒店打标)是否只考虑可售产品,true：是；false：否（包括售完的）
 55:    list<PromotionBlackList> promotion_black_list ,    //Promotion过滤黑名单
 56:    optional bool return_has_memberbenefits_hotel ,    //是否返回有会员优惠的酒店,true:是 false: 否
 57:    list<FilterCondition> filter_conditions , // 过滤条件集合. 1:最小入住天数限制;
 58:    list<i32> return_assemble ,//0:今日特价  1：可用红包  2:返现  3:五折限购 4:限时抢 5:周边特价(酒店层面的过滤)
 59:    list<HongbaoRecord> hong_bao_records , //用户红包列表
 60:    list<i32> return_assemble_product ,//0:今日特价（尾房）1:五折限购 2:限时抢 3:周边特价
 61:	optional BookingMenu booking_menu , // 预定菜单 [default = kGeneralMenu]
    // 计算最低价时要排除的产品, bitmap存储, 取值与product_type完全相同(默认排除钟点房产品)
 62:    optional i32 min_price_excluded_products ,// [default = 0x20]
 63:   optional    Grandson        grandson,
 64:   optional    bool            is_new_hongbao,  //是否千人千价红包方式. true:采用千人千价方式，false:不采用
 65:   optional    i32 return_has_breakfasts_hotel,  //[default = 0]返回给定早餐份数酒店，bitmap方式控制。第1位为1返回含单早，第2位为1返回含双早，第3位为1返回含三早及以上。第4位为1 表示筛选不含早的酒店。 默认情况不进行早餐筛选。
  66:  optional    bool            return_has_xianfu_hotel, //是否返回有现付产品的酒店， true返回
  67:  optional    CustomerTrait   customer_trait,
  68:  list<GroupInfo>       group_info,//集团信息
  69:  optional i32 request_type,  //请求类型,1:list,2:detail 
  70:  optional i32 searchFrom, //搜索来源
  71:  optional string traceId, //traceId
  72:  optional bool onlymajiadebug,//马甲debug
  73:  list<i32> cooperation_type,//供应商类型：1, 直签,2 非直签
  74:  optional bool return_has_resale_hotel,//用于二手房过滤[default=false]
  
  100:optional bool has_majia,
101:optional bool has_zydj, // 是否使用中央定价
102:optional i32 majia_zydj_switch,
103:optional bool return_hotel_ticket_product, // 是否需要景酒打包产品
104:list<i32> pre_pay_hotel_level_filter,//控制分销使用,预付酒店等级过滤设置
105:list<i32> cash_pay_hotel_level_filter,//控制分销使用,现付酒店等级过滤设置
106:optional UserCreditLiveInfo order_by_user_credit_filter,//信用住相关参数过滤
107:optional list<double> promotion_percentage_range, //非常优惠－优惠力度区间
108:optional bool return_price_range_statistic, // 是否返回价格区间统计
109:optional list<i32> privilege_return_assemble,//特权服务筛选项: 0:闪住, 1:信用住
110:optional bool return_exclusive_hotel_info, // 是否返回专属优惠信息
111:optional map<i64, i32> exclusive_discount_detail, // 专属优惠额度明细
112:optional bool return_new_botao_member_product,//是否返回铂涛产品
113:optional bool return_has_gdgf_hotel,//返回有高定高的返酒店
114:optional i64 gs_request_time,//service发送请求的时间戳
115:optional map<i32,list<cm.BiddingRankInfo>> biddingRanks4Ebk,//key:shotelid,ebk竞价排名相关
}


struct SearchResponse
{
1:    required i32 return_code, //0:成功;1:请求参数为空;2:BeginSearch函数失败，没办法给单一的一次搜索加锁;3:EndSearch函数失败，没办法给单一的一次搜索解锁
	//4:checkin的时间比预定时间早，而且checkout的时间不大于checkin的时间
	//5:checkin的时间比预定时间早
	//6:checkout的时间不大于checkin的时间
	//7:checkin的索引位置太小或者太大(太小是指比0小，太大是指大于索引当中存在的库存的最大天数)
	//8:checkout的索引位置太小或者太大(太小是指比0小，太大是指大于索引当中存在的库存的最大天数)
2:    list<MHotelDetail> hotels_detail,
3:	optional i64 search_id,
4:	list<PromotionGroup> promotion_group, //only mobile has this function; web/mis etc has not;(through code crontol this)
5:    list<DebugResponse> debug_response,
 6:    optional CommonConf common_conf ,  //公共配置，目前里面只有promotion_group树
 7:optional i32 grandson, // 产品排序策略: 0: 默认策略, 1: 收益排序, 2: cvr排序
}


struct MetaMhotel{
	1:required i32 mhotel_id,
	2:required list<i32> shotel_id,
}

struct GetBaseRatePlanDRRGiftRequest
{
1: optional list<MetaMhotel> mhotel,
2: required i16 payment_type, //0 所有，1:现付 2:预付
3: required i32 booking_channel,//
4: required i32 sell_channel,//
5: required i32 member_level,//
6: optional string traceId,//
}

struct MetaHotelBookingRule
{
1: required i64 id,
2: optional i16 date_type,
3: optional string cn_description,
4: optional string en_description,
5: optional i64 start_date,
6: optional i64 end_date,
7: optional string start_hour,
8: optional string end_hour,
9: optional string room_type_id,
}

struct MetaHotelInfo
{
1: required i32 shotel_id,
2: optional list<MetaHotelBookingRule> hotel_booking_rule_list,
3: required i16 week_end_start,
4: required i16 week_end_end,
}

struct MetaProductInfo{
1: required i64 product_id,
2: optional i32 rate_plan_id,
3: optional list<i32> drr_ids,
4: optional list<i32> gift_ids,
}

struct MetaRoomTypeInfo
{
1: required i32 room_type_id,
2: optional list<MetaHotelBookingRule> hotel_booking_rule_list,
3: optional list<MetaProductInfo> products,
}

struct MetaPrePayInfo
{
1: optional i32 target,
2: optional i32 prepay_change_rule,
3: optional i16 date_type,
4: optional i64 start_date,
5: optional i64 end_date,
6: optional i16 cut_type_after,
7: optional i16 cut_type_befor,
8: optional bool cut_after_change_time,
9: optional bool cut_befor_change_time,
10: optional double cut_num_after,
11: optional double cut_num_befor,
12: optional string cn_description,
13: optional string en_description,
14: optional i16 is_week_effective,
15: optional map<string,string> rule_values,
}

struct MetaAddValuePolicyInfo
{
1:	optional i64 start_date,
2:	optional i64 end_date,
3:	optional i16 is_include,
4:	optional i16 share,
5:	optional i32 price_default_option,
6:	optional i32 single_price_default_option,
7:	optional double price,
8:	optional double single_price,
9:	optional i16 is_add,
10:	optional string currency_code,
11:	optional i16 is_week_effective,
}

struct MetaVouchInfo
{
1: optional i16 date_type,
2: optional i64 start_date,
3: optional string arrive_start_time,
4: optional string arrive_end_time,
5: optional i32 room_count,
6: optional i32 vouch_change_rule,
7: optional string cn_description,
8: optional string en_description,
9: optional bool is_room_count_vouch,
10: optional bool is_arrive_time_vouch,
11: optional i32 vouch_money_type,
12: optional i16 is_week_effective,
13: optional map<string,string> rule_values,
14: optional i64 endDate,
}

struct MetaAddValueInfoSimple
{
1: required i32 rate_plan_id,
2:	optional i16 is_include,
3:	optional i16 share,
4:	optional string add_value_cn_name,
5:	optional string add_value_en_name,
9:	optional bool is_add,
10:	optional double single_price,
11:	optional string business_code,
12: optional i32 price_default_option,
13:	optional double price,
14: optional i32 single_price_default_option,
}

struct MetaRatePlanBaseInfo
{
1: required i32 rate_plan_id,
2: optional string settlement_type,
3: optional string cn_rate_plan_name,
4: optional string en_rate_plan_name,
5: optional string price_type,
6: optional i16 is_limit_time_sale,
7: optional string product_type,
8: optional i32 booking_channel,
9: optional i32 rate_plan_sell_channel,
10: optional i64 start_time,
11: optional i64 end_time,
12: optional i32 min_advance_booking_days,
13: optional i32 max_advance_booking_days,
14: optional i32 min_stay_days,
15: optional i32 max_stay_days,
16: optional i32 min_checkin_rooms,
17: optional i32 customer_level,
18: optional list<MetaAddValuePolicyInfo> add_value_policy_list,
19: optional list<MetaPrePayInfo> rate_plan_pre_pay_rule_list,
20: optional list<MetaVouchInfo> rate_plan_vouch_rule_list,
21: optional list<MetaAddValueInfoSimple> rateplan_relation_add_value,
22: optional string rate_plan_room_type_id,
}

struct MetaDRRInfo
{
1: required i32 drr_rule,
2: optional i32 money_or_percent,
3: optional double money_or_percent_value,
4: optional i16 date_type,
5: optional string cn_description,
6: optional string en_description,
7: optional i64 start_date,
8: optional i64 end_date,
9: optional i16 fee_type,
10: optional i16 is_week_effective,
11: optional map<string,string> ruleValues,
12: optional string room_type_ids,
}

struct MetaHotelGiftRelationDate
{
1: optional i64 begin_date,
2: optional i64 end_date,
3: optional i16 date_type,
4: optional i64 bit_sum4_week,
5: optional i32 hour_type,
6: optional i32 hour_number,
}
struct MetaHotelGiftModel
{
1: required i32 gift_id,
2: optional i16 status,
3: optional list<MetaHotelGiftRelationDate> relation_date_list,
4: optional bool is_all_product_related,
5: optional i32 way_of_giving,
6: optional string gift_content_cn,
7: optional string gift_content_en,
8: optional i32 gift_types,
9: optional string way_of_giving_other_cn,
10: optional string way_of_giving_other_en,
}

struct MetaSHotelBaseRpDrrGift
{
1: required MetaHotelInfo hotel_base_info,//S酒店基本信息
2: required list<MetaRoomTypeInfo> room_base_infos,//S房型信息
3: required list<MetaRatePlanBaseInfo> ratePlans,//RatePlan信息
4: required list<MetaDRRInfo> drrs,//DRR信息
5: required list<MetaHotelGiftModel> gifts,//礼包信息
}

struct MetaMHotelBaseRpDrrGift
{
1: optional list<MetaSHotelBaseRpDrrGift> shotel_detail,
2: optional i32 mhotel_id,
}

struct GetBaseRatePlanDRRGiftResponse
{
1: optional list<MetaMHotelBaseRpDrrGift> mhotel_detail,
2: optional i32 return_code, //0：正常
3: optional string return_msg, //
}

service ProductSearchService
{
    SearchResponse searchProducts(1:SearchRequest searchRequest);
	// 获取直连价格信息
    DcPriceResponse searchDcPrice(1:DcPriceRequest request);
	// 获取产品信息
	GetProductBaseInfoResponse getProductBaseInfo(1:GetProductBaseInfoRequest request);
	// 获取库存和及时确认信息
	GetInvAndInstantConfirmResponse getInvAndInstantConfirm(1:GetInvAndInstantConfirmRequest request);
    // 获取价格元数据信息
	GetBasePrice4NbResponse getMetaPrice4Nb(1:GetBasePrice4NbRequest request);
	GetBaseRatePlanDRRGiftResponse getMetaRatePlanDrrGift(1:GetBaseRatePlanDRRGiftRequest request);
}
