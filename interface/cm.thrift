// 类型定义文件

namespace cpp  se
namespace csharp  se
namespace java  com.elong.hotel.searchagent.thrift.bean

enum LangType {
    LANG_CN  = 0,
    LANG_EN  = 1,
}

enum FilterRegionType {
    DOWNTOWN  = 0,
    ADMIN_AREA = 1,
}

// 酒店预订状态
enum BookingStatus {
    // 不可订
    BOOKING_FAIL        = 0,
    // 部元可定
    //BOOKING_PARTIAL     = 1,
    // 可能可订
    //BOOKING_MAYBE       = 2,
    // 可定
    BOOKING_SUCC        = 3,
}

// 促销政策
enum PromotionType {
    SCORECARD = 0;  // 积分卡
    CASHBACK  = 1;  // 反现
    GIFTCARD  = 2;  // 礼品卡
    DISCOUNT  = 3;  // 立减
    PROMOTION_UNKNONW   = 9;  // 未知
}

struct CancelPolicy {
    // 取消政策ID
    1: i16                  id,
    // 取消政策描述
    2: string cancel_policy_cn,
    // 取消政策描述
    3: string cancel_policy_en,
    // 取消政策明细
    4: string other_info_cn,
    // 取消政策明细
    5: string other_info_en,
}

//价格日历中的一天的价格
struct PriceDay{
    // 日期
    1: string date,
    // 价格，精确到货币单位：元
    2: double price,
}

// rate plan
struct RatePlan {
    // rp id
    1: i32                   rp_id,
    // rp 名称
    2: string                rp_name,
    // 减免类型
    3:  PromotionType        promotion_type,
    // 减免部元[单位:元]
    4:  i32                  price_breaks,
    // 早餐
    7:  string               breakfast_info_cn,
    // 早餐(英文)
    8:  string               breakfast_info_en,
    // 上网
    9:  string               internet_cn,
    // 上网(英文)
    10: string               internet_en,
    // 取消政策
    11: CancelPolicy         cancel_policy,
    // 价格日历
    12: list<PriceDay>       price_detail,
    // 到店时间担保,开始
    13: string               arrive_start_time,
    // 到店时间担保,结束
    14: string               arrive_end_time,
    // 剩余房量
    15: i32                  room_inventory,
    // 最多入住人数
    16: i32                  max_person,
    // 床型信息
    17: string               bed_type_cn,
    // 床型信息
    18: string               bed_type_en,
}

// POI类型
enum POIType {
    // 飞机
    AIR             = 0,
    // 地铁
    METRO           = 1,
    // 公交
    BUS             = 2,
    // 景点
    SIGHT           = 3,
}

// 排序类型
enum RankType {
    // 默认排序
    DEFAULT             = 0,
    // 价格,从低到高
    PRICEASC            = 1,
    // 价格,从高到低
    PRICEDESC           = 2,
    // 星级,从低到高
    STARASC             = 3,
    // 星级,从高到低
    STARDESC            = 4,
    //评元,从高到低
    SCOREDESC           = 5,
    // 距离,从近到远
    DISTANCEASC         = 6,
    // Unkonw，由AS确定排序方式
    UNKONWN             = 7,
}

// 枚举酒店星级
enum HotelStarType {
    // 不限
    NOLIMITED           = 0,
    STAR1               = 1,
    STAR2               = 2,
    STAR3               = 3,
    STAR4               = 4,
    STAR5               = 5,
}

// 返回状态
enum CrawStatus {
    //初始
    NORMAL              = 0,
    // 抓取中
    CRAWLING            = 1,
    // 抓取完成,且有价格
    CRAW_SUCC           = 2,
    // 抓取失败,不要重试
    CRAW_FAILED         = 3,
    // PA失败
    PA_FAILED           = 4,
    // TIMOUT
    TIMEOUT             = 5,
    //过载丢弃
    TOOBUSY             = 6,
}

struct PictureInfo {
    // 图片类型,目前有九种,对应(201~209)
    1: string type,
    // 图片url
    2: string url,
}

struct PictureList {
    1: list<PictureInfo> picture,
}

// 供应商Brief信息(Brief信息, 列表页的OTA价格信息)
struct ProviderBrief {
    // 供应商ID
    1:  i32                   provider_id,
    // 供应商中文名
    2:  string                provider_name_cn,
    // 供应商英文名
    3:  string                provider_name_en,
    // 所有房型最低价[单位:元]
    4:  i32                   lowest_price,
    // 供应商缩略图
    5:  PictureInfo           picture,
}

// 经纬度信息
struct GeoInfo {
    // 经度
    1:  double              geo_longitude,
    // 纬度
    2:  double              geo_latitude,
}

// 区域信息
struct RegionInfo {
    // 区域ID
    1: i32                  region_id,
    // 区域中文名
    2: string               region_name_cn,
    // 区域英文名
    3: string               region_name_en,
    // 区域(目的地)中心点
    4: GeoInfo              region_center_coordinate,
    // 国家编码, "cn"
	5: string               country_code,
	// 国家中文名
	6: string               country_name_cn,
	// 国家英文名
	7: string               country_name_en,
}

// 点评信息
struct CommentInfo {
    // 点评元数
    1:  string              comment_score,
    // 点评数量
    2:  i32                 comment_count,
    // 来自网站个数
    3:  i32                 comment_site_num;
}

// 周边响应中的POI数据
struct POIData {
    // 地标ID
    1: i32                   poi_id,
    // 地标名[中文]
    2: string                poi_name_cn,
    // 地标名[英文]
    3: string                poi_name_en,
    // 距离(单位: 0.1公里)
    4: string                distance,
    // 经纬度
    5: GeoInfo               geo_info,
}

// POI距离信息
struct NearbyPOI {
    // 地标类型
    1:  POIType             poi_type,
    // 该类型下的地标集合
    2:  list<POIData>       poi_data,
}

// 定义一个价格区间[单位:元]
struct PriceRange {
    // 价格区间上界
    1:  i32                    price_low,
    // 价格区间下界
    2:  i32                    price_high,
}

struct AllBuyRoomMessage {
1: optional bool has_allbuyroom_pro=1,
2: optional i32 type,
}

// 元页信息
struct PageInfo {
    // 当前页
    1:  i32                 page_no = 1,
    // 每页酒店个数
    2:  i16                 page_size = 15,
}

// 酒店设施
struct HotelFacility {
    // 设施对应ID
    1: i32                  id,
    // 设施中文名
    2:  string              facility_name_cn,
    // 设施英文名
    3:  string              facility_name_en,
}

struct HotelLeisure {
    // 休闲对应ID
    1: i32                  id,
    // 休闲中文名
    2:  string              leisure_name_cn,
    // 休闲英文名
    3:  string              leisure_name_en,
}

// 酒店服务
struct HotelService {
    // 服务对应ID
    1: i32                  id,
    // 服务中文名
    2:  string              service_name_cn,
    // 服务英文名
    3:  string              service_name_en,
}

// 地图上的酒店列表
struct HotelInfoMap {
    // 酒店ID
    1:  i32                 hotel_id,
    // 经纬度
    2:  GeoInfo             geo_info,
}

// 列表页酒店基信息
struct HotelInfoList {
    // 酒店ID
    1:  i32                 hotel_id,
    // 酒店中文名称
    2:  string              hotel_name_cn,
    // 酒店英文名称
    3:  string              hotel_name_en,
    // 酒店星级 (支持类似 3.5星）
    5:  string              hotel_star,
    // 酒店经纬度
    6:  GeoInfo             hotel_geo_info,
    // 酒店地址
    7:  string              hotel_address_cn,
    // 酒店地址(英文)
    9:  string              hotel_address_en,    
    // 点评信息
    10: CommentInfo         hotel_comment_info,
    // 最低价格[单位:元]
    11: i32                 hotel_lowest_price,
    // 地标距离信息
    12: string              distance,
    // 酒店缩略图
    13: PictureInfo         hotel_picture_id,
    // 酒店预订状态
    14: BookingStatus       hotel_booking_status,
    //  供应商信息(包括供应商中英文名称,价格)
    15: list<ProviderBrief> provider_brief,
    //  是否自签酒店 >0:自签酒店
    16: i32                 self_signed,
    // for Ean
    17: PromotionType       ean_promotion_type;
}

// 酒店详情信息
struct HotelInfoDetail {
    // 酒店ID
    1:  i32                 hotel_id,
    // 酒店中文名称
    2:  string              hotel_name_cn,
    // 酒店英文名称
    3:  string              hotel_name_en,
    //  开业时间
    5:  string              hotel_openning_date,
    //  最后装修时间
    6:  string              hotel_last_decorate_date,
    // 酒店星级 (支持类似 3.5星）
    7:  string              hotel_star,
    // 酒店经纬度
    8:  GeoInfo             hotel_geo_info,
    // 点评信息
    9:  CommentInfo         hotel_comment_info,
    // 最低价格[单位:元]
    10: i32                 hotel_lowest_price,
    // 地标距离信息
    //11: list<DistancePOI>   hotel_distance_poi,
    // 酒店介绍
    12: string              hotel_summary_cn,
    // 酒店介绍
    13: string              hotel_summary_en,
    // 图片集合信息
    14: list<PictureList>   hotel_picture_id,
    // 酒店地址[中文]
    15: string              hotel_address_cn,
    // 酒店地址[英文]
    16: string              hotel_address_en,
    // 酒店预订状态
    17: BookingStatus       hotel_booking_status,
    // 酒店设施
    18: list<HotelFacility> hotel_facility,
    // 酒店服务
    19: list<HotelService>  hotel_service,
    // 可接受信用卡
    20: list<string>        accept_credit_card,
    // 酒店休闲娱乐 
    21: list<HotelLeisure>  hotel_leisure,
    // 酒店对应的OTA个数
    23: i32                 mapped_ota_count,       
    // 是否自签酒店
    24: i32                 self_signed,
}

struct PriceRangeStat {
    // 价格范围 [单位:元]
    1:  PriceRange price_range,
    // 酒店个数
    2:  i32        count,
}

struct HotelStarStat {
    // 星级
    1:  HotelStarType hotel_star,
    // 酒店个数
    2:  i32           count,
}

struct HotelBrandStat {
    // 酒店品牌ID
    1:  i32           hotel_brand,
    // 酒店个数
    2:  i32           count,
    // 品牌中文名
    3:  string        brand_name_cn,
    // 品牌英文名
    4:  string        brand_name_en,
}

struct HotelTypeStat {
    // 酒店类型ID
    1:  i32           hotel_type,
    // 酒店个数
    2:  i32           count,
    // 类型中文名
    3:  string        type_name_cn,
    // 类型英文名
    4:  string        type_name_en,
}

struct HotelFacilityStat {
    // 酒店设施ID
    1:  i32           hotel_facility,
    // 酒店个数
    2:  i32           count,
    // 设置中文名
    3:  string        facility_name_cn,
    // 设施英文名
    4:  string        facility_name_en,
}

// 一次检索中每个筛选条件对应的酒店个数统计
struct HotelFilter {
    // 价格区间对应酒店个数
    1:  list<PriceRangeStat>      price_range_stat,
    // 星级对应酒店个数
    2:  list<HotelStarStat>       hotel_star_stat,
    // 品牌对应酒店个数
    3:  list<HotelBrandStat>      hotel_brand_stat,
    // 酒店类型对应酒店个数
    4:  list<HotelTypeStat>       hotel_type_stat,
    // 酒店设施对应酒店个数
    5:  list<HotelFacilityStat>   hotel_facility_stat,
}

enum StatusCode {
     SUCCESS           = 0,
     PARAMETER_ERR     = 1,
     INTERNEL_ERR      = 2,
}
     
// 执行状态
struct ServerStatus {
    1: optional i32              code;
    2: optional string           msg; 
}

struct EanRoomPrice {
    // 减免类型
    1:  PromotionType        promotion_type,
    // 减免部元[单位:元]
    2:  i32                  price_breaks,
    // 原始价格
    3:  i32                  origin_price,
    // room code
    5:  i32                  room_code,
    // cuppon code
    6:  string               coupon_code,
    // todo delete begin
    // 早餐
    7:  string               breakfast_info_cn,
    // 早餐(英文)
    8:  string               breakfast_info_en,
    // 上网
    9:  string               internet_cn,
    // 上网(英文)
    10: string               internet_en,
    // 取消政策
    11: CancelPolicy         cancel_policy
    // todo delete end
}

// 供应商房型增量信息
struct ProviderRoomDetailInc {
    // 房型ID
    1:  i64                       room_id,
    // 每晚均价[已扣除了减免部元,单位:元]
    2:  i32                       average_price,
    // 库存状态
    3:  BookingStatus             booking_status,
    // 产品ID
    4:  i32                       product_id,
    // for Ean
    7:  EanRoomPrice              ean_price,
    // 早餐
    8:  string                    breakfast_info_cn,
    // 早餐(英文)
    9:  string                    breakfast_info_en,
    // 上网
    10:  string                    internet_cn,
    // 上网(英文)
    11: string                    internet_en,
    // 取消政策
    12: CancelPolicy              cancel_policy
}

// 供应商价格信息(Detail信息, 详情页的OTA价格信息)
struct ProviderDetailInc {
    // 供应商ID
    1: i32                         provider_id,
    // url
    2: string                      booking_url;
    // 抓取状态
    3: CrawStatus                  craw_status,
    // 供应商的酒店ID
    4: i32                         provider_hotel_id,
    // 增量价格变化信息
    5: list<ProviderRoomDetailInc> room_detail_inc,
}

// 供应商房型信息(含报价信息)
struct ProviderRoomDetail {
    // 房型ID
    1:  i64                  room_id,
    // 库存状态
    2:  BookingStatus        booking_status,
    // 房型中文名
    3:  string               room_name_cn,
    // 房型英文名
    4:  string               room_name_en,
    // 床型
    5:  string               bed_type_cn,
    // 床型(英文)
    6:  string               bed_type_en,
    // 早餐
    7:  string               breakfast_info_cn,
    // 早餐(英文)
    8:  string               breakfast_info_en,
    // 上网
    9:  string               internet_cn,
    // 上网(英文)
    10: string               internet_en,
    // 取消政策
    11: CancelPolicy         cancel_policy,
    // 每晚均价[已扣除了减免部元,单位:元]
    12: i32                  average_price,
    // 房间面积
    15: i32                  room_area,
    // 楼层信息
    18: string               floor_info_cn,
    // 楼层信息(英文)
    19: string               floor_info_en,
    // 其他信息
    21: string               other_info_cn,
    // 其他信息(英文)
    22: string               other_info_en,
    // 图片信息[第1张为房型缩略图]
    25: list<PictureList>    picture,
    // booking url
    26: string               booking_url,
    // Ean 房型价格
    27: EanRoomPrice         ean_price,
    // 产品ID
    28: i32                  product_id,
    // RP
    29: RatePlan             rp_info,
}

// 供应商价格信息(Detail信息, 详情页的OTA价格信息)
struct ProviderDetail {
    // 供应商基本信息
    1:  ProviderBrief             provider_brief,
    // url
    2: string                     booking_url;
    // 供应商的酒店ID
    3: i32                        provider_hotel_id,
    // 房型价格信息
    4:  list<ProviderRoomDetail>  provider_room_info,
    // Ean酒店粒度促销类型(自签酒店的Ean由前段自行通过API查找，
    // 但是促销类型api取不到，需要由后端传递
    5: PromotionType              ean_promotion_type = PromotionType.DISCOUNT,
}

// 供应商报价信息
struct ProviderRtsPrice {
    // 供应商ID
    1: i32  provider_id,
    // 价格
    2: i32  price,
}

// 实时酒店抓取信息(酒店粒度)
struct HotelRtsInfo {
    // 酒店ID
    1: i32                      hotel_id,
    // 抓取状态                  
    2: CrawStatus               craw_status,
    // 最低价
    3: i32                      price,
    // 供应商报价, 已排序,第0个是最低报价
    4: list<ProviderRtsPrice>   provider_price,
    // 库存状态
    5: BookingStatus            booking_status,
    // for Ean
    12: PromotionType           ean_promotion_type;
}

// 热门酒店信息
struct HotHotelInfo {
    // 目的地ID
    1:  i32                         region_id,
    // 目的地酒店数
    2:  i32                         hotel_num,
    // 最低价 (暂不使用)
    3:  i32                         price,
}

// 用户信息
struct UserInfo {
    // 用户IP
    1: string           user_ip,
    // Session id
    2: string           session_id,
    // Cookie id
    3: string           cookie_id,
    // user agent
    4: string           user_agent,
    // user account
    5:optional string           account,
    // card number
    6:optional string           card_number,
    // user level
    7:optional i32              level,
    // 注册日期: 2014-08-15
    8:optional string           reg_date,
    // referer
    9:optional string           referer,
    // mobile device id
    10:optional string          idfa,
    // mobile app id
    11:optional string          appid,
    // OS
    12:optional string          os,
    // OS version: e.g. 3.0
    13:optional string          os_version,
    // mobile device brand: e.g. Apple
    14:optional string          brand,
    // mobile device model: e.g. iPhone
    15:optional string          model,
    // mobile service carrier: e.g. China Mobile
    16:optional string          carrier,
    // visit channel
    17:optional string          channel,
    18:optional GeoInfo         geo_info,
    // search id
    19:optional string          session_flow_id,
    20:optional bool            at_current_city,
}

// 预定酒店的客人信息
struct RoomInfo {
    // 成人数
    1: i16             adult_num,
    // 儿童数
    2: i16             children_num,
}

//国内酒店检索相关message定义
struct  ReturnAttribute
{
1:optional bool return_hotel_id_only,
2:optional bool return_products,
3:optional bool return_hotel_static_info,
4:optional bool return_rateplan_info,
5:optional i32  return_static_info_level,
6:optional bool return_fast_filter_info, // 返回快速筛选项
8:optional bool return_new_recall_info, //返回新的酒店召信息
}

// 限定属性的模糊搜索
// query的限定属性, 如只搜query, 只搜品牌
enum FuzzySearchType
{
    kUndefined        = 0;  // 关闭模糊搜索
    kTitle            = 1;  // 酒店名模糊搜索
    kGeo              = 2;  // 在地标模糊搜索
}
struct PromotionDescription
{
1: required string key,
2: required string value,
}

struct PromotionTypeMsg
{
1: required i32 id,
2: required bool is_effective_price,
3: optional i32 priority_level,  //优先级
4: optional i32 is_special,   //是否属于特殊处理组(1代表数据特殊处理组)
5: optional map<i32,i32> promotion_cities,
}

struct PromotionGroupRelation 
{
1: required i32 group_id,
2: list<PromotionTypeMsg> type_list,
}

struct PromotionGroupType 
{
1: required i32 group_type_type,  // 0: 间夜  1:订单
2: list<PromotionGroupRelation> promotion_group_relation,
}

struct PromotionBusiness 
{
1: required i32 business_type, //1005: 预付 1001:现付 
2: list<PromotionGroupType> promotion_group_type,
}


struct PromotionCount
{
1: required i32 promotion_type,
2: required i32 count,
}

struct PromotionOrderFromLine 
{
1: required i32 order_from_type,   //  108101: web 108102: mobile
2: list<PromotionBusiness>  promotion_business,
}

struct PromotionGroupRoot 
{
1: list<PromotionOrderFromLine> promotion_order_from_line,
}

struct CommonConf 
{
1: required PromotionGroupRoot promotion_group_root,
2: optional list<i32> wechat_for_new_user_promotion_ids,//微信新用户专享促销配置
}

struct DebugPromotion
{
1: required string  date, 
2: required i32 promotion_id,
3: required i32 promotion_type,
4: required bool use_ok,
5: optional string reason,
6: optional i32 upperlimit,
}

struct DebugDrr
{
1: optional string type,
2: optional double drrnum,
}

struct DebugPrice
{
1: required string date,              //价格对应日期
2: optional i32 status,            //1为有效，其他位无效
3: optional i32 add_bed_price,     //加床价格
4: optional string currency,          //币种
5: optional double gen_sale_cost,   //平日低价
6: optional double gen_sale_price,   //平日卖家
7: optional bool is_add_bed,  //是否允许加床，true表示允许加床，false表示不允许加床
8: optional bool is_hotel_weekend,   //是否酒店的周末
9: optional bool is_price_promotion, //是否促销  (特别注意，这里不是指promotion，而是指是否经过DRR的促销)
10: optional double real_cost, //真实成本价（初始值为底价）在计算drr的时候，根据金额或者比例，在自身的>基础上进行计算
11: optional double sale_cost, //底价  （这个如果是平日，则为gen_sale_cost,如果为周末，则为weekend_sale_cost)
12: optional double sale_price, //卖价(这个如果是平日为gen_sale_price, 如果为周末，则为weekend_sale_price)
13: optional double sale_price_with_drr, //计算过促销后的价格 (最终给用户显示的每一天的房价就是这个字段)
14: optional double weekend_sale_cost,  //周末底价
15: optional double weekend_sale_price,  //周末卖价
16: optional double weekend_price_origin, //周末卖价的原始币种价格
17: optional double general_price_origin, //平日卖价的原始币种价格
18: optional double sale_price_with_drr_origin, //经过促销后的价格（原始>币种
19: optional double add_bed_price_origin,//加床价格(原始币种)
20: optional double sale_price_with_drr_sub_coupon,
21: optional DebugPromotion used_promotion,     //返后价计算使用的是哪个promotion
22: optional double used_drr,                //使用到的drr
}

struct DebugProduct
{
1: required i32 product_id,
2: required i32 rp_id,
3: required i32 mroom_id,
4: required string mroom_name,
5: required i32 shotel_id,
6: required i32 sroom_id,
7: required string rp_name,
8: required bool return_ok,
9: optional string reason,
10: optional string promotion_all,
11: list<DebugDrr> drr,
12: list<DebugPromotion> promotion,
13: list<DebugPrice> price,
}

struct DebugSRoom
{
1: required i32 sroom_id,
2: required bool return_ok,
3: optional string reason,
4: list<DebugProduct> product,
}

struct DebugSHotel
{
1: required i32 shotel_id,
2: required bool return_ok, //该shotel是否出了
3: optional string reason,  //该shotel没出的原因
4: optional string promotion_all,
5: list<DebugSRoom> sroom,
6: list<DebugPromotion> promotion,
}

struct DebugMHotel
{
1: required i32 mhotel_id,
2: list<DebugSHotel> shotel,
}

struct DebugResponse
{
1: optional DebugMHotel mhotel,
}




struct PromotionGroup
{
1: required i32 group_id,
2: list<i32> promotion_type,
3: list<PromotionTypeMsg> type_list, // 拟废弃字段promotion_type，以本字段替换
4: optional i32 businessType,  // 产品支付方式：1001: 现付, 1005: 预付
5: optional i32 orderFromGroupId,  // 产品线：108101: 网站, 108102: 手机
6: optional i32 group_type,     //1:间夜纬度   2:订单纬度
}

struct ManJianMessage
{
1: optional bool has_manjian,
2: optional i32 type,  //1: the product who has min price has manjian; 2: the product(not min price) has manjian)
3: list<PromotionDescription> promotion_description, 
}


struct ConfirmMessage
{
1: optional bool has_confirm,
2: optional i32 type,
    //1: the product who has min price has confirm; 
    //2: the product(not min price) has confirm
}

struct RoomSelected
{
1:list<i32> select_room_ids, 
}

struct  HotelAttribute
{
1: list<i32> mhotel_ids,
2:optional string keyword,
3:optional i32 keyword_type,
4: list<i32> theme_ids,
5: list<i32> facility_ids,
6: list<i32> star_rates,
7:optional i32 hotel_group_id,
8: list<i32> hotel_brand_id,
9:optional bool return_no_product_hotel,
10:optional bool need_hotel_without_service,
11:list<i32> online_search_types,
12:list<i32> supplier_type,
13:optional i32 hotel_service_status,
14:optional bool return_has_yufu_hotel,
15:optional bool return_has_timerush_product_hotel,
16:optional bool price_sub_coupon,
17:optional FuzzySearchType fuzzy_search_type,
18:optional i32 economic_hotel,
19:optional bool return_has_manjian_hotel,
20:optional list<string> fast_filter_keywords, // 注意，这个字段被复用了, 用于DA解析使用
                                               // 1. 快速筛选项,比如: 低价高星，确认快，连锁
                                               // 2. 集团名
23:optional i32 hotel_tag,
24: optional i32 return_discount_hotel,     
    // 1：只要该酒店包含1个预付五折的产品，这个酒店就返回（不用考虑现付五折的情况）;
    // 2:只要该酒店包含1个现付五折的产品，这个酒店就返回（不用考虑预付五折的情况）；
    // 3：这个酒店必须同时包含一个预付五折和一个现付五折的产品，这个酒店才返回；
    // 4：这个酒店只要有1个预付五折或者1个现付五折的产品，这个酒店就返回
25:list<i32> fast_filter_ids, 
26:list<i32> talent_recommend_ids,
27:optional bool only_consider_salable, // (最低价计算/酒店打标)是否只考虑可售产品,true：是；false：否（包括售完的）
28:list<i32> return_assemble, //只看优惠: 0:今日特价  1：可用红包  2:返现  3:五折限购 4:限时抢 5:周边抢 6: 转让房
29:optional i32 return_has_breakfasts_hotel, //返回有早餐酒店，bitmap方式控制。
    //第1位为1返回含单早,第2位为1返回含双早，第3位为1返回含三早及以上。第4位表示不含早  默认情况不进行早餐过滤。
30:optional bool return_has_xianfu_hotel,
31:list<RoomSelected> mroom_selected, //每个mhotel筛选的mroomid集合 
32:list<i32> service_filter_ids, // 快筛项服务的筛选：免费取消 . 艺龙直销. 立即确认. 含礼包
34:optional bool return_price_range_statistic, // 是否返回价格区间统计
35:optional list<i32> privilege_return_assemble,//特权服务筛选项: 0:闪住, 1:信用住
38:optional bool return_has_gdgf_hotel,//是否只返回有高定高返的酒店
}

struct PriceRangeStatistic
{
1:optional i32 star_type, // 酒店类型 1：经济， 2：三星/舒适， 3：四星/高档， 4：五星/豪华， 6：其他
2:optional PriceRange price_range, // 价格范围 每50元区间（最大到1000，1000以上一个段） eg: 1~50、51~100、101~150……
3:optional i32 hotel_count, // 酒店数量
}

enum BedLargeType
{
    kBedLargeTypeAll = 0;
    //所有，不限 
    kSingeBed = 1; 
    //大床
    kDoubleBed = 2;
    //双床
}

struct  CheckInPersonForOneRoom 
{
1:optional i32 min_checkin_person_for_oneroom,
2:optional i32 max_checkin_person_for_oneroom,
}


struct  RoomAttribute
{
1:optional CheckInPersonForOneRoom checkin_person_for_oneroom,
2:optional bool is_hotel_apartment,
3: list<i32> bed_large_types,
4: list<i32> facility_ids,
5: string keyword,
}

struct  PricePair 
{
1:optional i32 min,
2:optional i32 max,
}

struct StayDate 
{
1: i64 check_in,
2: i64 check_out,
}

enum PaymentMethods
{
 kAllPaymentMethods=0,
 kThePackage=1,
 kCollectionAndPayment=2,
}

enum PriceType
{
 kAllPriceType=0,
 kUnified=1,
 kWith=2,
 kForeign=3,
 kSpecialDistrict=4,
 kJappan=5,
}


enum DistrictType 
{
 kBussiness=1,
 kAdministration=2,
 kTrafficHub=3,
 kSubway=4,
 kScenicArea=5,
}

enum GeoType
{
 kNull=0,
 kNearBy=1,
 kBound=2,
 kMulPoi=3,
}

struct  Location
{
1: double latitude,
2: double longitude,
}

struct  NearBy
{
1: Location center,
2: i32 radius,
}

struct POIInfo{
    1: optional i32  id,
    2: optional string name_cn,
    3: optional string name_en,
    4: optional double distance,
    5: optional GeoInfo geo_info,
}

struct NearBySearchInfo
{
1:optional i32 item_type, //1表示机场，2表示火车站，3表示汽车站，4表示地铁站，5表示景区，6表示大学，7表示医院
2:optional NearBy nearby, //请求的地点的x、y坐标值，以及请求的距离半径；
//2:optional i32 radius,
3:optional i32 region_id, //需要得到哪个region内的内容
4:optional i32 region_result_num_uplimit, //如果是请求指定region内的内容，这个表示指定region内的内容的返回的上限个数值。（按照距离远近排序）
5:optional i32 nearby_result_num_uplimit, //如果是请求指定半径内的内容，这个表示指定半径内的内容的返回的上限个数值。（按照距离远近排序）
6:optional i32 optype, //-1表示只取按照半径计算的poi；-2表示只取按照region计算出来的poi；1表示两者都去，并且是“与”关系；2表示两者都取，并且是“或”关系
}

struct NearBySearchResult
{
1:optional i32 item_type, //1表示机场，2表示火车站，3表示汽车站，4表示地铁站，5表示景区，6表示大学，7表示医院
2:list<POIInfo> poi_info,
}

struct  Bound
{
1: Location left_top,
2: Location right_bottom,
}

struct MulPOI
{
1:list<NearBy> mul_pois,
2:optional i32 mul_poi_releation,
3:optional i32 display_poi,
}

struct  GeoAttribute
{
1:optional string language,
2:optional i32 region_id,
3:optional string region_str,
4:optional i32 poi_id,
5:optional string poi_str,
6:optional bool is_only_main_city,
7:optional DistrictType district_type,
8:optional i32 district_id,
9:optional GeoType geo_type,
10:optional NearBy nearby,
11:optional Bound bound,
12:optional MulPOI mulpoi,

}

enum BookingChannel
{
 kAllBookingChannel=0,
 kOnline=1,
 kOffline=2,
 kScoreSquare=3,
 kPhone=4,
 kSupply=5,
}

enum SellChannel
{
    kAllSellChannel=0,
    kA = 1,//B
    kB = 2,//B
    kC = 3,//C
    kD = 4,//D
    kE = 5,//E
    kF = 6,//F
    kG = 7,//G
    kH = 8,//H
    kI = 9,//I
    kJ = 10,//J
}

enum MemberLevel
{
    kAllMemberLevel=0,
    kCommon=1,
    kVip=2,
    kLong=3,
    kMuser=4,
}
enum ProductType 
{
 kAllProductType=0,
 kSalesAlone=1,
 kInternational=2,
 kTimeRush=3,
 kSalesPackage=4,
 kPartOfHousing=5,
 kImplicitPrice=6,
 kGroupPurchase=7,
 kHotelPrice=8,
 kNearyByPrice = 9,
 kNineYuan = 10,
}

//用户集团信息
struct GroupInfo
{
1:required i32 group_id,
2:optional i32 elong_level,
}

struct  CustomerAttribute
{
1:optional i64 booking_date,
2:optional i32 member_level,
3:optional string proxy_id,
4:optional i64 order_id,
5:list<i32> booking_channel,
6:optional i32 request_origin,
7:optional i32 botao_customer_level,
8:optional bool use_botao_promotion,
9:list<GroupInfo> group_info, //集团信息
}

enum SortingMethod 
{
 kDefault=0,
 kPrice=1,
 kDistance=2,
 kWordOfMouth=3,
 kStarRate=4,
 kSalesVolume=5,
 kFromMe=7,
 //其他等待补充todo
}
enum SortingDirection
{
 kAsc=1,
 kDesc=2,
}

enum SortItem
{
    kWeiFang = 1,  //尾房 
    kLongCui = 2,  //龙翠 
    kClose = 3,    //酒店服务关闭状态
    kSigned = 4,   //酒店签约 
    kBooking = 5,  //是否可预定
    kSubCity = 6,  //是否子城市 //目前再默认排序下该项默认生效，优先级低于用户设置的其他选项
    kNearByProduct = 7,  //是否有周边价产品
    kThemes = 8, //是否有某些主题
    kStars = 9,  //是否某些星级
    kUserCollection = 10, //用户收藏关注的酒店
    kOrange = 11, //橙色酒店
    kAllBuyRoom = 12 ; //是否是买断房
    kUserPrice = 13; // 用户历史价格
    kBrands = 14;  //是否有某些品牌
}

enum BookingMenu
{
    kGeneralMenu    = 1,    //常规频道
    kHourRoomMenu   = 2,    // 钟点房频道
    kGroupBuyMenu   = 3,    // 团购频道
}

enum SortItemPolicy
{
    kPriority = 1, //优先排前面 (置顶)
    kDelay = 2,  //优先排后面 (置底)
}

enum PTPromotionType
{
 kCoupon=1,
 kPoint=2,
 kDiscount=3,
 kGift=4,
 kReturnMoney=5,
 kS1=6,
 kS2=7,
 kImmediateDiscount=9,
 kHongBao = 10,
 kHongBaoPrepay = 11,
 kBuy5Send1 = 12,
 kCashAccount=9999,
}


struct ListProductInfo
{
    1:optional bool return_min_price_product,
    2:optional bool need_sorted_top_product,
    3:optional i32 top_product_num,
    4:optional i32 sort_types, //强行指定排序方
    5:optional bool return_min_stay_product,
}

// Promotion过滤黑名单
struct PromotionBlackList
{
1:optional i32 method_type,    //0或者不传：表示都要过滤；1:针对预付promotion；2：针对现付promotion
2:required i32 promotion_type, //标记黑名单中的promotion_type
}


struct ActivityChannel
{
1:optional i32 type, //操作类型. 1, 排除 2, 接受
2:list<i64> order_from_ids,
3:list<string> proxy_ids,
4:list<string> promotion_channel_codes,
}

// 满返红包
struct HongbaoFullBackRule
{
1:      optional double full_amount, // 满额
2:      optional double back_amount, // 返额
}

struct HongbaoRecord
{
1:optional i32 record_id, //红包ID
2:optional i32 recharge_type, //红包类型
3:optional i32 tag, //专享标签，0是普通红包
4:optional double face_value, //红包金额
5:optional i64 income_id, //交易ID
6:optional string valid_date, //红包有效期 yyyy-MM-dd HH:mm:ss
7:optional i32 activity_id, //活动ID
9:optional i32 status, //状态 -1表示红包过期，1可用，2已用
11:optional string order_time_from, //预订起始时间HH:mm:ss
12:optional string order_time_to, //预订结束时间HH:mm:ss
13:optional bool is_order_valid, //预订时间是否有效 true为有效 false 无效
14:optional string check_in_abs_date_from, //入住绝对起始时间 yyyy-MM-dd HH:mm:ss
15:optional string check_in_abs_date_to, //入住绝对结束时间 yyyy-MM-dd HH:mm:ss
16:optional bool is_check_in_abs_valid, //入住绝对时间是否有效 true为有效 false 无效
17:optional i32 order_relative_days_from, //相对预订日期起始偏移
18:optional i32 order_relative_days_to, //相对预订日期结束偏移
19:optional bool is_check_in_relative_valid, //入住相对日期是否有效 true为有效 false 无效
20:list<ActivityChannel> activity_channel,
21:list<string> pay_types, //支付类型
22:optional HongbaoFullBackRule hongbao_full_back_rule, // 满返红包规则
}
struct ProductTypeBlackList
{
1:optional i32 product_type,
2:list<i64> supplier_ids,
3:optional bool partial_match,
}

//FilterCondition 筛选条件
// type：
//1,最小入住天数限制;
//2, N间起订; filter_value:1, N间起订
//3, 早餐筛选. filter_value:1,筛选单早。2,筛选双早 3,筛选3早及以上 4.不含早
//4, 床型筛选.filter_value:36,大床。37，双床。38，单人床。39，特殊床型。40，其他。
//5, 支付方式筛选. filter_value: 1,现付。2，预付
//6, 给定一个product_type，过滤给定的supplierID 产品
//7, 服务. filter_value: 139，表示免费取消。
//8, 服务. filter_value: 141，立即确认
//9, 服务. filter_value: 138，表示艺龙直销。
//10,服务. filter_value: 140，礼品。
//11,发票模式筛选filter_value:1
//12,转让房 filter_value:1
//13,钟点房 filter_value:1
//14,闪住 filter_value:1
//15,信用住 filter_value:1
//use_or_not 传1表示使用此条件
//filter_value 要排除的 product_type,
//exclude_value_array传要过滤的supplierID集合
//apply_level 传1 表示产品过滤 2 表示针对酒店
//partial_match 传false表示过滤 产品的rp的product_type 与 exclude_value相等的产品
//传true表示过滤 产品的rp的product_type 与 exclude_value 相与不为0的产品
struct FilterCondition
{
1: optional i32 type, //过滤条件类型,  此字段需要赋值1
2: optional i32 use_or_not,  //1:使用，0：默认原来逻辑，-1：不使用   
3: optional i32 filter_value, //按filter_value筛选
4: optional i32 apply_level, //应用级别: 1 产品
5: list<i64> exclude_value_array, 
6: optional bool partial_match, //是否部分匹配，true是，false：否
7: list<ProductTypeBlackList> ptb,
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

//竞价排名相关
struct BiddingRankInfo{
   1:i16 pay_type,//支付类型,1.到店付,修改佣金额 2:预付,修改底价,
   2:i16 caculate_type,//计算类型: 1:减少, 2:增加
   3:i16 value_type,//值类型: 1:比率, 2:金额,
   4:double value,//值: 1:比率,单位%, 2:金额, 单位产品币种
}

struct  ProductAttribute
{
1: StayDate stay_date,
2: list<PricePair> price_pair,
18:i32 price_pair_type,
3:optional bool guarantee,
4: list<i32> payment_methods,
5:optional string promotion_channel_code,
6: list<i32> promotion_type_ids,
7:optional bool need_first_day_have_invertory,
8:optional bool only_limitime_sale,
9:optional PriceType price_type,
10: list<i32> product_type,
11: list<i32> sell_channel,
12: i32 search_price_type,
13: i32 inventory_type,
14: optional bool need7daygift,
15: optional bool return_noinv_or_noprice_product,
16: optional bool return_has_coupon_hotel,
17: optional bool return_has_no_danbao_hotel,
19: optional bool return_longcuionly_hotel,
20: optional bool return_has_hongbao_hotel,
21: optional ListProductInfo list_product_info,
22: optional bool return_has_lianzhu_pro_hotel, //返回有连住省产品的酒店 
23: optional bool return_has_zaoding_pro_hotel, //返回有早订省产品的酒店
24: optional bool half_discount_promotion,
25: optional bool return_has_discount_promotion_hotel,
26: optional bool return_freesale_msg,
27: optional bool return_has_allbuyroom_hotel,
28: optional i32 discount_method, //1: 只要预付五折；2：只要现付五折；3：既要预付五折又要现付五折；不传这个参数表示不要五折产品
29: optional i32 min_price_calc_with_halfdiscount_pro, //1：表示最低价计算既包含现付五折的产品也包含预付五折的产品；2：表示最低价计算只包含预付五折的产品，不包含现付五折的产品；3：表示最低价计算只包含现付五折的产品，不包含预付五折的产品；4：表示最低价计算即不包含预付五折的产品，也不包含现付五折的产品
30: optional bool use_day_promotion , //是否按天使用promotion
31: list<PromotionBlackList> promotion_black_list, //标记app端需要promotion_type黑名单
32: optional bool return_has_memberbenefits_hotel,   //是否返回有会员优惠的酒店,true:是 false: 否
33: list<FilterCondition> filter_conditions, // 过滤条件集合. 1:最小入住天数限制;
34: optional BookingMenu booking_menu, //预订菜单
35: optional i32 min_price_excluded_products, //计算最低价时要排除的产品, bitmap存储, 取值与product_type完全相同(默认排除钟点房产品)
36: list<i32> return_assemble_product, //0:今日特价（尾房）1:五折限购 2:限时抢 3:周边特价 4:转让房
37: list<HongbaoRecord> hong_bao_records, //用户红包列表
38: optional bool is_new_hongbao, //是否千人千价红包方式. true:采用千人千价方式，false:不采用
40: list<i32> cooperation_type,



// add by majia
100:optional bool has_majia,
101:optional bool has_zydj, // 是否使用中央定价
102:optional string mvt_strategy, // AB分流策略
103:optional bool return_has_resale_hotel, //二手房过滤
104:optional bool has_exclusive_price, //是否使用专属优惠
105:optional bool return_hotel_ticket_product, // 是否需要景酒打包产品
106: list<i32> pre_pay_hotel_level_filter,//控制分销使用,预付酒店等级过滤设置
107: list<i32> cash_pay_hotel_level_filter,//控制分销使用,现付酒店等级过滤设置
108: optional UserCreditLiveInfo order_by_user_credit_filter,//信用住相关参数过滤
109:list<double> promotion_percentage_range, //非常优惠－优惠力度区间 QuickScreenProduct
110:optional bool return_min_ac_price_simple_product , // 是否返回最低价简单产品信息,搜索排序使用
111:optional bool return_new_botao_member_product , // 是否返回铂涛新会员产品
112:optional map<i32,list<BiddingRankInfo>> biddingRanks4Ebk, //key:shotelid, ebk竞价排名相关
}

struct PriceInterval
{
1:required i32 upper_limit,
2:required i32 lower_limit,
}

struct SortPolicy
{
1:SortItem sort_item,
2:SortItemPolicy sort_item_policy,
3:list<i32> ids,
4:PriceInterval price_interval,
}

struct  PageRankAttribute
{
1:optional i32 page_size,
2:optional i32 page_index,
3:optional SortingMethod sorting_method,
4:optional SortingDirection sorting_direction,
5:optional i32 sort_order_id,
6:list<SortPolicy> sort_policys,
7:list<i32> feature_policy_ids,
8:optional i32 flow_id,
9:list<i32> new_flow_ids,
//todo排序抽样 
}

struct  CallerAttribute
{
1:optional i64 search_guid,
2:optional string ip,
3:optional string channel,
4:optional i32 SearchFrom,
5:optional bool old_filter,
6:optional i32 request_origin,
7:optional bool is_inner,
8:optional i32 searchFromEnd,//搜索来源端,0mis,1PC,2APP,3H5,4微信,5NBApi
41:optional i64 search_id,
42:optional bool is_debug,
43:optional bool onlydebug,
44:optional string loom,

// add by majia
100:optional string trace_id,
}

struct  FilterAttribute                                                                                   
{
1: required i32 region_id,
2: optional FilterRegionType region_type,
3: optional i32 parent_region_id,
4: optional i32 parent_region_type,
5: optional bool filter_element,
6: optional LangType language,
}

struct FastFilterAttribute
{
1: list<i32> unique_id, //快筛项的编号
}

struct RecommendAttribute
{
1:optional bool  rec_result, //是否需要推荐的结果，false:无
2:optional i32 min_price, //最低价格用于推荐过滤,不需要自己填写 
3:optional bool is_rec_request,//是否是推荐请求，不需要客户端设置本字段，程序自行判断设置 
4:optional bool return_talent_recommend, //是否需要返回达人推荐信息 
5:optional i32 hotel_num,// 返回的达人推荐的酒店数目 
6:optional bool rec_return_num_only,//只返回酒店数量
7:optional i32 talent_rec_list_num , //  榜单的数量
}



enum DateType
{
 kBookingDate=1,
 kCheckinDate=2,
 kAtRoomDate=3,
}

enum SHotelGiftWayOfGiving
{
 kEveryRoom=1,
 kEveryRoomPerDay=2,
 kOther=3,
}

enum HotelGiftHourType
{
 kHours24=0,
 kXHourBefore=1,
 kXHourAfter=2,
}

enum HotelBookingRuleType
{
 kNoneRule=1,
 kNeedNationality=2,
 kPerRoomPerName=3,
 kForeignerNeedEnName=4,
 kRejectCheckinTime=5,
 kNeedPhoneNo=6,
}

enum VouchWay
{
 kCreditCard=1,
}

enum VouchMoneyType
{
 kFirstNightCost=1,
 kFullNightCost=2,
}

enum VouchRuleType
{
 kVouchNoChange=1,
 kVouchNeedSomeDay=2,
 kVouchNeedCheckinTime=3,
 kVouchNeedCheckin24hour=4,
}

enum RuleTargetType
{
 kHotel=1,
 kCustomer=2,
}

enum PrePayRuleType
{
 kPrepayNoChange=1,
 kPrepayNeedSomeDay=2,
 kPrepayNeedOneTime=3,
}

enum CutType
{
 kMoney=1,
 kPercent=2,
 kFirstNight=3,
}
enum ActionType
{
 kSend=0,
 kUse=1,
}

enum ProExclusiveType
{
 kInclusive=0,
 kExclusive=1,
}

enum InventoryStatus
{
 kEveryDayHasInv=1,
 kPartialHasInv=2,
 kNoneInv=3,
}

enum PriceStatus
{
 kEveryDayHasPrice=1,
 kPartialHasPrice=2,
 kNonePrice=3,
}

enum ReturnCode
{
 kSuccess=0,
 kRequestIsNULL=1,
 kBeginSearchFailed=2,
 kEndSearchFailed=3,
 kCheckinSmallerBookingAndCheckoutNotLargerCheckin=4,
 kCheckinSmallerBooking=5,
 kCheckoutNotLargerCheckin=6,
 kCheckinIndexTooSmallOrTooLarger=7,
 kCheckoutIndexTooSmallOrTooLarger=8,
}

struct  SelectPrice
{
1:optional i32 low_price,
2:optional i32 high_price,
}

struct  SHotelInvoiceInfo
{
1: i64 shotel_id,
2: optional i32 type,
}

struct  SHotelHelpfulTips
{
1: i64 shotel_id,
2: optional string helpful_tips_cn,
3: optional string helpful_tips_en,
4: optional string start_date,
5: optional string end_date,
}

struct GiftSecondTag
{
1:optional i32 sub_bit_number,
2:optional i32 sub_gift_price,
}

struct GiftFirstTag
{
1:optional i32 bit_number,
2:optional i32 priority,
3:list<GiftSecondTag> gift_second_tag,
}

struct  GiftInfo
{
1: optional i64 shotel_id,
2: optional i64 sroom_type_id,
3: optional i64 rateplan_id,
5: optional string gift_content_cn,
6: optional string gift_content_en,
7: optional i32 way_of_giving,
8: optional string way_of_giving_other_cn,
9: optional string way_of_giving_other_en,
10: optional i32 gift_types,
11: optional i32 status,
12: optional string begin_date,
13: optional string end_date,
14: optional i32 date_type,
15: optional i32 bit_sum4_week,
16: optional i32 hour_type,
17: optional i32 hour_number,
18: list<GiftFirstTag> gift_first_tag,
}

struct  GiftInfoPreview
{
2: optional string gift_preview_string,
3: optional bool is_next7_days,
}

struct  Gift
{
1: i64 gift_id,
2:optional GiftInfo gift_info,
3:optional GiftInfoPreview gift_info_preview,
}

struct  SHotelBookingRule
{
1: i64 id,
2: i64 shotel_id,
4: optional string cn_description,
5: optional string en_description,
6: optional string start_date,
7: optional string end_date,
8: optional i32 booking_date_type,
9: optional i32 booking_rule_type,
10: optional string start_hour,
11: optional string end_hour,
12: optional string note2,  // 标准提示语一
13: optional string limit1,   // 限制一
14: optional string limit2,   // 限制二
}

struct  AddValueInfo
{
1: i64 id,
2: optional string business_code,
3: optional string add_value_eng_name,
4: optional string add_value_cn_name,
5: optional i32 is_include,
6: optional i32 share,
7: optional i32 price_default_option,
8: optional double price,
9: optional bool is_add,
10: optional i32 single_price_defaultoption,
11: optional double single_price,
12: optional string memo,
13: optional i32 is_forbidden,
}

struct  VouchInfo
{
1: i64 id,
2: optional i64 rateplan_id,
3: optional i32 vouch_way,
4: optional string start_date,
5: optional string end_date,
6: optional i32 date_type,
7: list<i32> is_week_effective,
8: optional string arrive_start_time,
9: optional string arrive_end_time,
10: optional i32 room_count,
11: optional i32 money_type,
12: optional i32 rule_type,
13: optional i32 rule_data_int,
14: optional string rule_data_date_time,
15: optional string rule_data_date_string,
16: optional string rule_description_cn,
17: optional string rule_description_en,
18: optional bool is_arrive_time_vouch,
19: optional bool is_room_count_vouch,
}

struct  PrePayInfo
{
1: i64 id,
2: optional i64 rate_plan_id,
3: optional i32 target_type,
4: optional string start_date,
5: optional string end_date,
6: optional i32 date_type,
7: optional i32 rule_type,
8: optional bool cut_before_change_time,
9: optional bool cut_after_change_time,
10: optional i32 cut_type_before,
11: optional i32 cut_type_after,
12: optional i32 cut_num_before,
13: optional i32 cut_num_after,
14: optional i32 rule_data_int,
15: optional i32 rule_data_second_int,
16: optional string rule_data_date_time,
17: optional string rule_data_string,
18: optional string rule_description_cn,
19: optional string rule_description_en,
20: list<i32> is_week_effective,
}

struct  AddBreakfastInfoOfDay
{
1: optional bool is_include,
2: optional i32 share,
3: optional i32 price_default_option,
4: optional double price,
5: optional string date,
6: optional i64 policy_id,
}

struct  AddBreakfasePolicyInfo
{
1: optional i64 rate_plan_id,
2: i64 policy_id,
3: optional i32 sub_policy,
4: optional string policy_name,
5: optional string policy_name_eng,
6: optional i32 is_customer_visible,
7: optional string cn_description,
8: optional string eng_description,
9: optional i32 date_type,
10: optional string start_date,
11: optional string end_date,
12: list<i32> is_week_effective,
13: optional i32 status,
14: optional i32 is_include,
15: optional i32 share,
16: optional string currency_code,
17: optional i32 price_default,
18: optional double price,
19: optional i32 is_add,
20: optional i32 single_price_default_option,
21: optional double single_price,
22: optional string memo,
23: optional i64 add_value_id,
}


struct HoursRoomInfo {
1: optional string earliest_arrival_time,
2: optional string latest_arrival_time,
3: optional string stay_time,
}
//addition_id = 11 去哪儿最早最晚到店时间项目 
//addition_id = 10 活动打标 
//addition_id = 9 rp是否隐藏 
//addition_id = 7 是否是集团id 
struct RatePlanAddtion
{
1: optional i32 addition_id,//addition_id=6，addition_value=1的情况是酒店开发票。//其他情况发票模式从SHotelInvoiceInfo取。
2: optional i32 addition_value,
3: optional string addition_value_str, //string类型的value，目前只有addition_id = 11时使用（qunar最早最晚到店时间项目)
}

struct  RPRatePlan
{
1: i64 rateplan_id,
2: optional i32 booking_channel,
3: optional i32 sell_channel,
4: optional i32 product_type,
5: optional i32 customer_level,
6: optional i32 settlement_type,
7: optional i32 price_model,
8: optional i32 price_type,
9: optional string rateplan_name_cn,
10: optional string rateplan_name_en,
11: optional string rateplan_description_cn,
12: optional string rateplan_description_en,
13: optional i32 min_advance_booking_days,
14: optional i32 max_advance_booking_days,
15: optional string start_date,
16: optional string end_date,
17: optional i32 min_stay_days,
18: optional i32 max_stay_days,
19: optional bool is_limit_time_sale,
20: optional i32 min_checkin_rooms,
21: optional i32 inventory_limit,
22: optional i32 status,
23: optional i32 date_type,
25: optional string expected_confirm_time,
26: list<AddValueInfo> add_value_infos,
27: list<VouchInfo> vouch_infos,
28: list<PrePayInfo> prepay_infos,
29: optional bool is_special_breakfast,
30: list<AddBreakfastInfoOfDay> add_breakfast_info_of_days,
31: list<AddBreakfasePolicyInfo> add_breakfast_policy_infos,
32: list<RatePlanAddtion> additions,
33: optional i32 max_checkin_rooms,//最大入住房间数
}

//具体业务含义还不清楚，在过滤之后，各个字段按照索引接口进行填充
struct  MarketingPromotion
{
1: i64 id,
2: optional i32 promotion_type,
3: optional string description,
4: optional double upper_limit,
5: optional string offer_desc,
6: optional i32 exclusive_type,
7: optional i32 actiontype,
8: optional string short_message,
9: optional string short_message_eng,
10: optional string short_message_big5,
11: optional i64 pro_hotel_product_id,
12: list<PromotionDescription> promotion_description,
13: optional bool has_inv_limit,  //平台是否限制库存
14: optional i32 inv_left,      //剩余几间库存
15: optional i32 priority,  //promotionId的优先级
16: list<HongbaoRecord> hongbao_records, //红包信息
}

struct  Inventory
{
1: optional string date,
2: optional i32 amount,
3: optional i32 status,
4: optional i32 is_over_booking,
5: optional i32 allbuyroom_amount,
6: optional i32 over_sold_limit,//超售库存限量数值
}

struct  PriceDays
{
1: optional i32 status,
2: string date,
3:optional i32 add_bed_price,
4:optional string currency,
5:optional double gen_sale_cost_origin,
6:optional double gen_sale_price,
7:optional bool is_add_bed,
8:optional bool is_hotel_weekend,
9:optional bool is_price_promotion,
10:optional double real_cost_origin,
11:optional double sale_cost_origin,
12:optional double sale_price,
13:optional double sale_price_with_drr,
15:optional double weekend_sale_cost_origin,
16:optional double weekend_sale_price,
17:optional double weekend_price_origin,
18:optional double general_price_origin,
19:optional double sale_price_with_drr_origin,
20:optional double add_bed_price_origin,
21:optional double sale_price_with_drr_sub_coupon,
22:optional double sale_cost,
23: optional double sale_price_with_drr_d_before,//衍生品修改之前的价格
24: optional double sale_price_with_drr_origin_d_before,//衍生品修改之前的原始币种价格
}

struct  Price
{
1: optional i32 audit_status,
2: optional bool is_effective,
4: list<PriceDays> day_prices,
5: optional i32 price_status,
}

struct  HotelProductRelation
{
1: optional i32 product_id,
2: optional i32 sroom_id,
3: optional i32 rp_id,
4: i32 relation_type,
5: optional double relation_product_price,
6: optional i32 mroom_id,   // M房型id
}


/*
struct NearNMonthMaxPrice
{
1:optional i32 month_num,
2:list<double> months_max_price,
}
*/


struct DrrAttr
{
1: required string key,
2: required	string value,
}

// dynamic rate rule
struct DrrMsg
{
    1: required	i32 id,	            // 取值范围 1 ~ 7
    2: list<DrrAttr> drrAttr,
    3: required	i32 date_type, 	    // 1:入住日期, 2:在店日期, 3:预定日期
    4: required	i64 start_date,
    5: required	i64 end_date,
}

struct  DayMarketingPromotion
{
1: required string date,     //日期
2: list<MarketingPromotion> day_marketing_promotion,
}

struct TicketCalendar
{
1: optional string date, // 日期
2: optional double cost_price, // 门票底价(单价)
3: optional double market_price, // 门票市场价 (单价)
4: optional double price, // 门票卖价(单价)
5: optional bool is_bookable, // 是否可定
}

struct TicketInfo
{
1: optional i32 ticket_num, // 票数
2: optional i64 product_id, // 产品id
3: optional string product_name, // 产品名称
4: optional i64 scenery_id, // 景区id
5: optional string scenery_name, //景区名称
6: list<TicketCalendar> ticket_calendar, // 门票价格日历
7: optional i32 status, // 门票产品状态  1：可售， 0: 不可售
}

struct MinTicketInfo
{
1: optional string date, // 最低价门票日期
2: optional i64 product_id, // 最低价门票产品id
3: optional string product_name, // 最低价门票产品名称
4: optional double min_ticket_sale_price, // 最低门票价卖价(单价)
5: optional double min_ticket_market_price, // 最低门票价市场价(单价)
6: optional i32 min_ticket_num, // 最低价门票张数
}

struct HotelTicketProduct
{
1: list<MinTicketInfo> min_ticket_info, // 最低价门票产品
2: optional double product_sale_price, // 打包产品价格(原产品均价+最低门票价卖价*最低价门票票数)
3: list<TicketInfo> ticket_infoes, // 门票详细信息 
4: optional i32 status, // 景酒打包产品状态  1：可售， 0: 不可售
}

struct  Product
{
1: optional i64 sroomtype_id,
2: optional i64 shotel_id,
3: optional i64 supplier_id,
4: optional i32 online_search_type,
5: optional bool sroomtype_status,
6: optional bool has_breakfast,
7: optional RPRatePlan rateplan,
8: optional string rp_code,
9: list<Inventory> room_inventory_days,
10: optional InventoryStatus room_num_status,
11: optional Price price,
12: list<MarketingPromotion> marketing_promotions,
13: list<Gift> gifts,
14: optional HotelProductRelation relations,
15:optional i64 supplier_type,
16: list<SHotelBookingRule> shotel_booking_rules,
17: optional bool is_freesale,
18: optional bool firstnight_has_discount,
19: optional double firstnight_discount,
20: optional i32 firstnight_discount_upper,
21: optional i32 freesale_num,
22: optional i32 cooperation_type,
23: optional string supplier_name,
24: optional string supplier_short_name,
25: optional string supplier_alias,
26: optional string supplier_telphone,
27: optional i64 confirm_way, // 67108864:直连, 536870912:ECM, 128:Ebooking, 1073741824:Ebooking(免确认); 判断方法: (confirm_way & val) == val 
28: optional string shotel_contacter,
29: optional HoursRoomInfo hours_room_info,
30: optional string supplier_fax,
32: optional DrrMsg drrMsg, // DRR描述信息
33: optional i32 weekend_start,
34: optional i32 weekend_end,
35: list<DayMarketingPromotion> day_marketing_promotions, //每天的promotion
36: optional i32 price_origin,
37: optional i32 price_sub_coupon,
38: optional bool is_min_price_product,
39: optional double weight,
40: optional i32 id,
41: optional double cvr,
42: optional i64 supplier_confirm_avg_time, //供应商平均确认时长
43: optional string rateplan_structure_name_cn, //rp结构化名称:早餐内容＋预订条件＋客人类型


// add by majia
134: optional bool is_majia,
135: optional string majia_id,
//add resale
136:optional bool is_resale_product, //是否二手房
137:optional i64 order_id, //原订单id

// add 新房型聚合
138:optional i32 	sign_type, // 签约状态。 0：艺龙产品，1：ctrip 直签；2：ctrip非直签；3：qunar直签；4：qunar非直签
139:optional double 	cost_point, // 产品底价分值
140:optional double 	hotel_service_point, // 酒店服务指标分值
141:optional double 	total_point, //  房型聚合总分数
142:optional double 	commission_value, // 佣金额  
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
143: optional i32 derivative_type,//衍生品类型
// 专属优惠，代理层实现
144:optional bool is_exclusive_rp, // 是否专属优惠产品
145: optional bool is_hotel_ticket_product, // 是否景酒打包产品
146: optional HotelTicketProduct hotel_ticket_product, // 景酒打包产品详情
147: optional byte force_show,//0默认,1强制露出,
148: optional bool is_support_flash_live,//是否支持闪住
149: optional bool is_support_credit_live,//是否支持信用住
150: optional bool is_dc_product, //是否直连产品
151: optional double extras, // 信用住、闪住产品杂费
152:optional i32 resale_product_original_price, // 转让房原产品卖价均价
153: optional i32 product_yield,//产品产量
154: optional double product_gains,//产品收益
155: optional bool has_coupon_enhance,//是否有额外返现
156: optional i32 product_flag,//二进制位表示(从0开始数):0 被动马甲，1 主动马甲 2 高定高返
}

struct  MRoomTypes
{
1: i64 mroomtype_id,
2:optional string mroom_name,
3: list<Product> products,
4: optional i32 bed_type,
5: optional i32 priority,
}


//静态详情相关

enum ERoomAdditionsType
{
kBedType=1,
kFloorType=2,
kInternetService=3,
kInternetServiceType=4,
kWindowType=5,
kSmokingRoom=6,
kBedNumbers=7,
kPersonNumber=8,
kBathroom=9,
kFaceDirection=10,
kScene=11,
kOtherservice=12,
kOpaqueHotel=13,
kLobbyAndBedRoom=14,
}
struct  HotelAirportPickUpService
{
1:optional string hotel_id,
2:optional string service_providing_department_contact,
3:optional string service_providing_department,
4:optional string service_providing_department_en,
5:optional string free_pick_up_service_notes,
6:optional string free_pick_up_service_notes_en,
7:optional string driver,
8:optional string driver_en,
9:optional string airport_name,
10:optional string airport_name_en,
11:optional string vehicle_type,
12:optional string vehicle_type_en,
13:optional string end_time,
14:optional string start_time,
15:optional string end_date,
16:optional string start_date,
}
struct  HotelAmenity
{
1:optional string amenity_name,
2:optional string amenity_name_en,
3:optional string amenity_detail,
}
struct  HotelAroundInformaiton
{
1:optional string name,
2:optional string name_en,
3:optional string distances,
4:optional string description,
}
struct  HotelConferenceAmenities
{
1:optional string overview,
2:optional string overview_en,
3: list<HotelAmenity> amenity_list,
}
struct  HotelCreditCategory
{
1:optional string cedit_category_name,
2:optional string credit_category_value,
}
struct  HotelDiningAmenities
{
1:optional string overview,
2:optional string overview_en,
3: list<HotelAmenity> amenity_list,
}

struct  HotelFacilities
{
1:optional i32 mhotel_id,
2:optional i32 shotel_id,
3:optional i32 facility_id,
4:optional i32 old_facility_id,
5:optional string facility_name_cn,
6:optional string facility_name_en,
7:optional i32 facility_type_id,
8:optional string facility_type_name,
9:optional string notes,
}
struct  HotelfeatureInfo
{
1:optional string hotel_id,
2:optional string driving_guide,
3:optional string driving_guide_en,
4:optional string property_other_hightlights,
5:optional string property_amenities_hightlights,
6:optional string location_highlights,
7:optional string overview,
8:optional string property_other_hightlights_en,
9:optional string property_amenities_hightlights_en,
10:optional string location_highlights_en,
11:optional string overview_en,
}
struct  HotelGeneralAmenities
{
1:optional string overview,
2:optional string overview_en,
3: list<string> amenity_simple_list,
4: list<string> amenity_simple_list_en,
}
struct  HotelLandMark
{
1:optional string land_mark_name,
2:optional string land_mark_name_en,
3:optional string hotel_id,
4:optional string land_mark_id,
}

struct  HotelRecreationAmenities
{
1:optional string overview,
2:optional string overview_en,
3: list<string> amenity_simple_list,
4: list<string> amenity_simple_list_en,
}
struct  HotelRoomAmenities
{
1:optional string overview,
2:optional string overview_en,
3: list<string> amenity_simple_list,
4: list<string> amenity_simple_list_en,
}
struct  HotelSurroundingAttractions
{
1:optional string name,
2:optional string name_en,
3:optional string distances,
}
struct  HotelTrafficAndAroundInformation
{
1:optional string name,
2:optional string name_en,
3:optional string distances,
4:optional i32 transportations,
5:optional i32 time_taken,
6:optional double transport_fee,
7:optional string note,
}
struct  HotelTrafficAndAroundInformations
{
1:optional string overview,
2:optional string overview_en,
3:optional string traffic_guide,
4: list<HotelTrafficAndAroundInformation> traffic_and_around_information_list,
}
struct  HotelSurroundingCommerces
{
1: list<HotelTrafficAndAroundInformation> traffic_and_around_information_list,
}

struct ServiceCityLevel
{
1:optional double complainrate,
2:optional double confirmrate,
3:optional double successrate,
4:optional double score,
}
struct  StructuredFacilityItem
{
1:optional i32 id,
2:optional string name_cn,
3:optional string name_en,
4:optional i32 parent_id,
5:optional string text_cn,
6:optional string text_en,
7:optional i32 rank,
8:optional i32 is_show_on_web,
 //repeated StructuredFacilityItem children=9,
}
struct  HotelTag
{
1:optional i32 tag_id,
2:optional string tag_name,
}
struct RecommendReason
{
1:optional i32 theme_id,
2:optional string theme_name,
3:optional string theme_name_en,
4:optional string reason,
}
struct NearByPoiInfo
{
1:optional i32 id,
2:optional i32 type,
3:optional string name,
4:optional string name_en,
5:optional double distance,
}
struct  MHotelInfo
{
1:optional i32 mhotel_id,
2:optional string hotel_name,
3:optional string hotel_name_en,
4:optional string address,
5:optional string address_en,
6:optional string post_code,
7:optional i32 star,
8:optional i32 real_star,
9:optional double latitude,
10:optional double longitude,
11:optional double baidu_latitude,
12:optional double baidu_longitude,
13:optional string province,
14:optional string city,
15: list<HotelCreditCategory> credit_category_list,
16:optional string description,
17:optional string description_en,
18:optional string photo_url,
19:optional string credit_card,
20:optional string credit_card_en,
21:optional string second_name,
22:optional string second_name_en,
23:optional string hotel_url,
24:optional i32 area_id,
25:optional i32 city_id,
26:optional bool is_reserve,
27:optional i32 admin_area_id,
28:optional bool is_show_out,
29:optional i64 additional_status,
30:optional i32 apartment,
31:optional i32 economic,
32:optional string open_date,
33:optional string decorate_date,
34:optional string notes,
35:optional i32 star_out,
36:optional i32 credit,
37:optional string lobby_fax,
38:optional HotelAirportPickUpService airport_pick_up_service,
39:optional HotelGeneralAmenities general_amenities,
40:optional HotelRoomAmenities room_amenitier,
41:optional HotelRecreationAmenities recreation_amenities,
42:optional HotelConferenceAmenities conference_amenities,
43:optional HotelDiningAmenities dining_amenities,
44:optional HotelTrafficAndAroundInformations traffic_and_around_informations,
45: list<HotelTrafficAndAroundInformation> surrounding_commerces_list,
46: list<HotelAroundInformaiton> surrounding_restaurants_list,
47: list<HotelSurroundingAttractions> surrounding_attractions_list,
48: list<HotelAroundInformaiton> surrounding_shops_list,
49:optional HotelfeatureInfo feature_info,
50: list<HotelLandMark> hotel_land_marks_list,
51:optional string lobby_tel,
52:optional i32 corp_group_id,
53:optional i32 hotel_brand_id,
54:optional string hotel_amenities,
55:optional string op_date,
56:optional string simple_traffic,
57:optional string simple_traffic_en,
58:optional string meetings,
59:optional string meetings_en,
60:optional string restaurants,
61:optional string restaurants_en,
62:optional string relaxs,
63:optional string relaxs_en,
64:optional string room_amenities,
65:optional string room_amenities_en,
66:optional string hotel_amenities_en,
67:optional string intro_editor_cn,
68:optional string intro_editor_en,
69:optional string hotel_group_id,
70:optional StructuredFacilityItem facility,
71: list<HotelCreditCategory> credit_category_list_en,
72:optional double complain_rate,
73:optional double fmc_rate,
74:optional double iot_rate,
75:optional double index_result_data_col,
76:optional i32 sum_order,
77:optional i32 total_comment,
78:optional i32 good_comment,
79:optional i32 bad_comment,
80:optional double comment_point32,
81:optional i32 old_area_id,
82:optional i32 old_city_id,
83:optional i32 old_admin_area_id,
84:optional string admin_area_name,
85:optional i64 days_credit_beign_date,
86:list<i32>  days_credit,
87:optional string area_name,
88:optional string short_name,
89:optional string short_name_en,
90:optional i32 serve_status,
91:optional i32 stop_serve_code,
92:optional string sellingpoints,
93:optional string overview,
94:optional string sellingpoints_en,
95:optional string overview_en,
96:optional string hotelfacility,
97:optional string hotelfacility_en,
98:optional string addition_info, // hotelmaster透传字段（不做任何解析)
99:optional ServiceCityLevel service_city_level,
100:list< RecommendReason> rec_reason,// 推荐理由相关
101:list< NearByPoiInfo> nearby_poi_info_list,
}
struct  RoomAdditionDefine
{
1:optional i64 addition_id,
2:optional string addition_name,
3:optional i32 eaddition_type,
4:optional string notes,
5:optional string addition_name_en,
6:optional i32 info_type,
7:optional i32 hotel_id,
8:optional i32 room_type_id,
}
struct  MRoomTypeInfo
{
1:optional i32 rid,
2:optional i32 room_type_id,
3:optional string room_type_name,
4:optional string room_type_name_en,
5:optional i32 mhotel_id,
6:optional i32 room_type_num,
7:optional string room_lines,
8:optional string room_unique_id,
9:optional string area,
10:optional string floor,
11:optional string other_notes,
12:optional i32 room_separate_nums,
13:optional i32 i_product_type,
14:optional string other_notes_en,
15:optional string available,
16:optional StructuredFacilityItem facility,
17: list<RoomAdditionDefine> room_addition_list,
}
struct  SHotelInfo
{
1:optional string shotel_id,
2:optional string is_reserve,
3:optional i32 auditing_type,
4:optional string audit,
5:optional string audit_name,
6:optional string phone,
7:optional string fax,
8:optional string contacter,
9:optional i32 auto_send_fax,
10:optional i64 additional_status,
11:optional i32 week_end_start,
12:optional i32 week_end_end,
13:optional string week_end_spe,
14:optional string bank_info,
15:optional i32 inventory_use_type,
16:optional i32 online_search_type,
}

struct  SRoomTypeInfo
{
1:optional string room_type_id,
2:optional string room_type_name,
3:optional string shotel_id,
4:optional i32 i_product_type,
5:optional string available,
6:optional string mroom_type_id,
7:optional string suffix_name,
}

struct  SupplierInfo
{
1:optional i32 supplier_id,
2:optional string supplier_name,
3:optional string supplier_abbr,
4:optional string supplier_code,
5:optional bool enabled,
6:optional string remark,
7:optional string address,
8:optional string post_code,
9:optional string post_address,
10:optional bool is_prepay,
11:optional bool is_direct_link,
12:optional i32 agreement_entity_id,
13:optional i32 type,
14:optional string self_operate,
15:optional i32 channel,
16:optional i64 additional_status,
}

struct  SHotelProductInfo
{
1:optional SHotelInfo shotel_base_info,
2:optional SupplierInfo shotel_supplier_info,
3:optional string hotel_special_info,
4:optional string hotel_special_info_start_date,
5:optional string hotel_special_info_end_date,
6: list<SRoomTypeInfo> room_base_infos,
}

struct  StaticDetail
{
1: optional MHotelInfo mHotel_base_info,
2: list<MRoomTypeInfo> mroom_type_list,
3: list<HotelFacilities> hotel_facility_list,
4: list<SHotelProductInfo> shotel_list,
5: optional string create_time,
}

struct LongcuiMessage {
1: optional bool has_longcuionly,
2: optional i32 type,
}

struct TejiaMessage {
1: optional bool has_weifang,
2: optional i32 type,
}

struct DanbaoMessage {
1: optional bool need_guarantee,
2: optional i32 type,
}

struct MobileOnlyMessage {
1: optional bool has_mobileonly,
2: optional i32 type,
}

struct ZhoubianProduct
{
    1:optional bool has_zhoubian_pro,
    2:optional i32 type,
}


struct CouponMessage {
1: optional bool has_coupon,
2: optional double upper_limit,
3: optional i32 type,
}

struct HongBaoMessage {
1: optional bool has_hongbao,
2: optional double upper_limit,
3: optional i32 type,
4: optional i32 promotion_type,
}

struct DistancePoi  
{
1:optional i64 id,  
2:optional i64 old_id, 
3:optional Location location, 
4:optional string name,
5:optional i32 distance,
6:optional string bigpoi_name,
7:optional i32 rank_score,
}

struct ActivityTag
{
1:optional i32 tag_id,         //活动标识
2:optional string tag_name,       //活动名称
3:optional i32 priority_level,     //优先级
}

// 标志struct
// flag_type: 1, 铂涛可用红包; 2, 铂涛可返红包;3，Longcuistruct；4，TeJiastruct；5，Danbaostruct；
// 6，MobileOnlystruct；7，Couponstruct；8，HongBaostruct；9，ZhoubianProduct；10，AllBuyRoomstruct；
// 11，ManJianstruct；12，Confirmstruct，object只支持2；13，MaxDiscount,object只支持2;14,MemberBenefits,会员优惠标 15,五折
//16:N折起，最高可省 17:铂涛会员价标签18, 活动打标 19: 钟点房 120:专属优惠标  1019:转让房 1020:中大网视促销, 1021:闪住, 1022：信用住
//1023:微信专享标识, 1024:微信钱包新客专享N折活动标识 1025:铂涛新会员
struct HotelFlag
{
1:required i32 flag_type,
2:optional bool effective,
3:optional i32 object,
4:optional double upper_limit, // Coupon,HongBao 上限
5:optional i32 promotion_type, //HongBao: 促销类型
6:list<PromotionDescription> promotion_description,//ManJian
7:optional i32 price,
8:list<double> discount_rates, //折扣率集合
9:optional double low_discount_rate, //N折起
10:optional i32 high_sub, //最高可省
11:list<ActivityTag> activity_tags, //活动打标
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
1:optional i32 type,
2:optional i32 min_price,
3:optional i64 min_price_rpid,
4:optional i32 min_price_sroomid,
5:optional i32 min_price_mroomid,
}

struct IncidentalPriceInfo
{
1:optional i32 min_price_cansale_sub_coupon_origin,
2:optional i32 min_price_cansale_sub_coupon,
3:list<MinPriceInfo> min_price_info,
}

struct RankDebug
{
1:optional i32 mhotel_id,
2:optional i32 base_hotel_id,
3:optional double model_score,
4:optional double min_price_sub_coupon,
5:optional double min_price_product_cost,
6:optional i32 position,
7:optional i32 default_score,
8:optional string feature_vector,
}

struct CustomizedProductInfo
{
1: optional i32 type,
2: optional i32 price,
3: optional i32 price_sub_coupon,
4: optional i64 roomtypeid,
5: optional i64 rateplan_id,
6: optional i64 mroom_id,
7: optional i32 shotel_id,
}

//酒店统计信息
//type：1 无早，2，单早，3，双早，4，3早及以上，5，免费取消，6，立即确认，7，艺龙直销，8，礼品
//count:产品数量
struct StatisticsInfo
{
1: optional i32 type,
2: optional i32 count,
}

struct RecallReason
{
1: optional i32 id,
2: optional string name,
3: optional i32 distance,
4: optional GeoInfo geo,
5: optional NearByPoiInfo introduce,
}

struct RecallInfo
{
1: optional i32 type,
2: optional RecallReason reason,
}

struct PromotionRange
{
    1: optional i32 promotionStatsType,  //优惠统计类型 0-红包 1-返现 2-立减 3-N折
    2: optional double minPromotion, //最小优惠额
    3: optional double maxPromotion, //最大优惠额 
}

//detail相关
struct  HotelDetail
{
1: i64 mhotel_id,
2:optional bool has_drr,
3:optional LongcuiMessage longcui_info,
4:optional TejiaMessage weifang_info,
5:optional i32 inventory_type,
6:optional i32 min_price,
8:optional i64 min_price_rpid,
9:optional i64 min_price_roomtypeid,
10:optional DanbaoMessage need_guarantee,
11:optional i32 product_count,
12:optional i32 promotion_type_count,
13: list<MRoomTypes> room_types,
14: list<SHotelHelpfulTips> shotel_helpfultips,
15: list<SHotelBookingRule> shotel_booking_rules,
16:optional StaticDetail hotel_static_info,
17:optional i32 distance,
18:optional i32 hotel_service_status,
19:optional bool tuan_gou,
20: list<SHotelInvoiceInfo> shotel_invoice_info,
21: optional MobileOnlyMessage mobileonly_message,
22: optional bool has_yufu,
23: optional i32 product_count_reason,
24: optional CouponMessage coupon_message,
25: optional i32 product_can_be_showed,
26:optional DistancePoi distance_poi,
27: optional bool has_timerush_product,
28: optional i32 min_price_pro_relation_price,
29: optional i32 min_price_mroomtypeid,
30: optional HongBaoMessage hongbao_message,
31: optional bool is_hotel_inventory_full, //酒店是否满房
32: optional i32 mroom_count, //房型数，list搜索使用
33: optional ZhoubianProduct zhoubian_message,
34: optional bool has_buy5send1_promotion,
35: optional bool has_halfdiscount_promotion,
36: optional i32 min_price_sub_coupon,
37: optional i64 min_price_sub_coupon_rpid,
38: optional i64 min_price_sub_coupon_roomtypeid,
39: optional i32 min_price_sub_coupon_mroomtypeid,
40: optional bool firstnight_has_discount,
41: optional AllBuyRoomMessage allbuyroom_message,
42: list<PromotionCount> promotion_count,
43: optional ManJianMessage manjian_message,
44: optional i32 min_price_sub_coupon_origin,
45: optional ConfirmMessage confirm_message,
46: list<HotelFlag> hotel_flag,
47: optional bool has_moremember_products,  //是否提示非登录用户登录有更多产品. 为true 表示提示， 为false 不提示
48: optional RankDebug rank_debug,
49: optional IncidentalPriceInfo incidental_price_info, 
50: list<CustomizedProductInfo> cp_info,
51: list<StatisticsInfo> statistics_info,
52: optional string loom,
53: list<DistancePoi> mul_distance_pois,
54: optional RecallInfo recall_info,
55: list<MinPriceInfo> hours_room_min_price_cansale,   //钟点房可卖的最低价(包含返前价和返后价)
100: optional i32 min_price_cost,//最低价产品底价
101: optional i32 min_price_sub_coupon_cost,//折后最低价产品底价

// 专属优惠，代理层实现
102: optional list<HotelDetail> exclusive_bhotels,
103: optional i32 exclusive_discount,

105: list<Inventory> min_price_sub_coupon_inventories, // 返后最低价库存列表
106: list<Inventory> min_price_inventories, // 最低价产品库存列表
107:optional list<PromotionRange> promotion_stats, //酒店促销信息统计(按优惠类型得到酒店底下最小最大优惠金额)
}

struct TalentRecommend
{
1:optional i32 theme_id,
2:optional string theme_name,
3:optional string theme_name_en,
4:list<HotelDetail> hoteldetail,
}

struct Recommend
{
1:required i32 type,  //推荐类型 1.达人推荐  2 详情页推荐
2:list<TalentRecommend> talent_rec,// 达人推荐
3:list<HotelDetail> rec_hotel_details,
4:optional i32 rec_all_num,//召回推荐酒店数量
}

//统计元素项
struct StatisticsItem
{
1:optional i32 id,
2:optional i32 old_id,
3:optional i32 num,
4:optional i32 all_num,
}

//统计信息
struct Statistics
{
1:list<StatisticsItem> brand,
2:list<StatisticsItem> star,
3:list<StatisticsItem> facility,
4:list<StatisticsItem> sheme,
5:list<StatisticsItem> static_count,
6:optional double booking_rate,
7:list<StatisticsItem> promotions,
}

enum  ParseItemType {
    kPoi     = 1, 
    kRegion  = 2, 
    kTitle   = 3, 
    kBrand   = 4,
    kBigPoi   = 5,
    kStar    = 6, 
    kFacility = 7, 
    kTheme = 8,
    kHotelName = 9 
}

struct Term
{
1:required string term_word, 
2:optional double weight,
3:optional bool omit_flag,
4:optional bool phrase_flag, // 1 意味着term不可分割。
}

struct SubASPoi
{
1:required  i64  id,
2:optional  string name,
3:optional  Location location, 
4:optional  i32 weight,
}

struct  ParseItem
{
1:required ParseItemType type ,   // poi, region, title, brand
2:optional  i64  id ,
3:optional  i64   old_id ,
4:optional  string name,
5:list<Term>  terms ,
6:optional  Location center_point,
7:list<SubASPoi> sub_pois,
8:optional i32  region_type, 
}

struct QueryParseResult
{
1:list<ParseItem> parse_item,
}

enum FPoiType {
    //滑雪场
    SKI_PARK = 0,
    //温泉
    SPRING  = 1,
    //周边游
    ZBY = 2,
    //大学
    COLLEGE = 3,
    //机场车站
    STATION = 4,
    //大地点的子地点
    SUBPOI = 5,
}

enum BigPoiType {
    //地铁
    SUBWAY = 0,
}


enum FILTYPE {
    //星级
    F_STAR  = 0,
    //品牌
    F_BRAND  = 1,
    //人数
    F_RENSHU = 2,
    //设施
    F_FACILITY = 3,
    //主题
    F_THEME = 4,
 }   

enum PAYTYPE {
    //预付
    PREPAY  = 0,
    //免担保
    NOVOUNCH = 1,
 }   

enum FPROMOTIONTYPE {
    //可返现
    COUPON  = 0,
    //限时抢
    FLASH_SALE = 1,
 }   


struct FilterRegionResult
{
1: optional i32 region_id,
2: optional FilterRegionType region_type,
3: optional i32 v4_region_id,
4: optional string region_name,
5: optional string region_name_en,
6: optional LangType language,
7: optional i32 hotel_num,
8: optional i32 weight,
9: optional string show_name,
10:optional i32 sub_v4_region_id,
11: optional string type_name,
12: optional string type_name_en,
}

struct  FilterPoiResult
{
1: optional FPoiType poi_type,
2: optional string poi_name,
3: optional string poi_name_en,
4: optional LangType language,
5: optional i32 hotel_num,
6: optional GeoInfo  geo_info,
7: optional i32 weight,
8: optional string show_name,
9: optional string type_name,
10: optional string type_name_en,
}

struct BigPoiResult
{
1: optional string poi_name,
2: optional string poi_name_en,
3: optional LangType language,
4: optional i32 hotel_num,
5: list<FilterPoiResult> subpoi,
6: optional BigPoiType type,
7: optional i32 weight,
8: optional string show_name,
9: optional string type_name,
10: optional string type_name_en,
}

struct  PriceResult
{
1: optional PricePair price_pair,
2: optional i32 hotel_num,
}

struct  FilResult
{
1: optional i32 id,
2: optional i32 old_id,
3: optional i32 hotel_num,
4: optional FILTYPE type,
5: optional string name,
6: optional string name_en,
7: optional LangType language,
8: optional i32 weight_web,
9: optional i32 weight_app,
10: optional string show_name,
11: optional string type_name,
12: optional string type_name_en,
}

struct  PayResult
{
1: optional i32 id,
2: optional i32 old_id,
3: optional PAYTYPE type,
4: optional i32 hotel_num,
5: optional string name,
6: optional string name_en,
7: optional LangType language,
8: optional i32 weight_web,
9: optional i32 weight_app,
10: optional string show_name,
11: optional string type_name,
12: optional string type_name_en,
}

struct  PromotionResult
{
1: optional i32 id,
2: optional i32 old_id,
3: optional FPROMOTIONTYPE type,
4: optional i32 hotel_num,
5: optional string name,
6: optional string name_en,
7: optional LangType language,
8: optional i32 weight_web,
9: optional i32 weight_app,
10: optional string show_name,
11: optional string type_name,
12: optional string type_name_en,
}

struct FilterItem {
    1: optional i32 id,                 // 筛选项V5 ID
    2: optional i32 id_v4,              // 筛选项V4 ID(行政区:对应V4行政区ID)
    //3: optional string name_cn,       // 筛选项名字(中文)
    //4: optional string name_en,       // 筛选项名字(英文）
    6:optional i32 hotel_num,           // 检索结果中对应筛选项酒店个数
    7:optional GeoInfo  poi_info,       // 地理信息（POI类型需要）
    8:optional i32 weight,              // 权重，用于排序(App/Web不同的权重)
    9:optional i32 id_city_v4,          // 当类型是行政区时，对应V4的城市ID
    10:list<GeoInfo> region_info,       // 当类型为region时，对应的多边形（备用字段）
    11:optional string name_ext_cn,     // 筛选项附加信息(中文），如国庆大促、母亲节
    12:optional string name_ext_en,     // 筛选项附加信息(英文）
    13:optional PricePair price_pair,   // 价格区间
    //14:optional BigPoiResult big_poi, // 大地点
    15:optional i32 weight_hot;         // 权重，用于热门排序(App才有权重)
                                        // 热门景点、机场车站使用这个权重前端排序
    16:optional i32 type;               // 类型 1 主题 2 关键字
    17:optional i32 unique_id,          //所有快筛项的编号
}

struct FilterMeta {
    1: string name_cn,       // 中文名
    2: string name_en,
    4: string type_name_cn,  // 目前未使用
    5: string type_name_en,
    6: optional string ext_str, // 扩展字段， 目前只有该项目对应的图标.
                                // 业务端可以根据需要添加、自行解析
                                // json格式 {"icon_url":"http://elongstatic...",
                                //           "option": "1"}  # 1:单选,2多选,默认:多选
    7: optional i32 icon_id,    // 筛选项打标
    8: optional i32 show_type,  //  展示类型：第0为表示快筛项 第1位表示达人推荐
    9: optional string talent_rec_name_cn, // 榜单中文名
    10:optional string talent_rec_name_en,
    11:optional i32 purpose,    // 表示用途, 采用bitmap存储, 每一个bit位值为1表示是, 为0表示否
                                // 第1位: 最低位, 表示是否回传搜索
                                // 第2位: 表示是否前端展示
                                // 第3位: 表示是否前端其他用途(目前是挑选图片)
}

struct FilterInfo1 {
    1: FilterMeta filter_meta;        // 名字/类型信息
    2: FilterItem filter_item;        // 筛选项
}

struct FilterInfo2 {
    1: FilterMeta filter_meta;        // 名字/类型信息
    2: list<FilterInfo1> filter_info1;
}
struct FilterInfo3 {
    1: FilterMeta filter_meta;        // 名字/类型信息
    2: list<FilterInfo2> filter_info2;
}

struct FilterInfo {
    1: FilterMeta filter_meta;        // 名字/类型信息
    11: FilterItem filter_item;        // 筛选项
    2: optional i32 type_id,// 类型
                            // -1. 无类型、中间节点、比如区域根节点
                            // 3. 品牌 (跟Sug保持一致,并预留ID区间)
                            // 4. 行政区（V4ID计算逻辑不一致，独立处理）
                            // 5. 商圈
                            // 6. POI(大学、风景区、汽车站、火车站, 地铁站等)
                            // 后面的ID不一定正确，后续补充
                            // 1006.价格筛选
                            // 1007.支付类型(1:预付, 2:到店付）
                            // 1008.星级(id=-1 不限，否则为对应星级)
                            // 1010.人数(id=-1 不限)
                            // 1011.设施(id=-1 不限)
                            // 1012.主题(id=-1 不限)
                            // 1013.0:返现  特价 2:红包 3:龙粹
                            // 1014.限时抢
                            // 1015.主题推荐
                            // 1016.城市
                            // 1017.最低价
                            // 1100.其他
    3: i32 depth,           // 深度,目前最大3级(一般只用到了1,2）,决定使用filter_itemX
    4: list<FilterInfo1> filter_item1;  // 筛选项(1级,比如大学/周边游/)
    5: list<FilterInfo2> filter_item2;  // 筛选项(2级,比如二级的机场车站)
    6: list<FilterInfo3> filter_item3;  // 筛选项(3级别,目前没有用到)
    7: i32 web_weight;                  // web大类的排序位置,目前只用于控制是否展示(-1:不展示)
    8: i32 app_weight;                  // app大类的排序位置,目前只用于控制是否展示(-1:不展示)
    9: i32 app_weight_hot;              // app大类是否在关键词页展示【保存的是销量 或者 热度】
                                        // Web在需要自己聚合时，可以根据这个值进行排序
                                        //-1:不展示 >=0 按权重排序，权重越小排在越前
    10: optional i32 show_depth,        // 展示深度, 是否需要把N级数据在前端按照N-1级展示，
                                        // 比如机场车站， app需要把二级数据展示为一级
}

struct FilterResult
{
    1: optional i32 city_id,
    2: list<FilterRegionResult>  region,
    3: list<FilterPoiResult>  poi,
    4: list<BigPoiResult>  bigpoi,
    5: list<PriceResult>  price,
    6: list<FilResult>  filter,
    7: list<PayResult>  pay,
    8: list<PromotionResult>  promotion,
    
    9: optional i32 city_idv4,
    20:list<FilterInfo> filter_info,
}
struct FilterList
{
1:required i32 type,     // 类型 1.快筛
2:optional FilterResult filter,  // 快筛的实现
}
struct UserTrack
{
1:optional string session_flow_id, // 检索id
}

struct PersonalInfo {
    1: optional    string      idfa,
    2: optional    string      card_number,
    3: optional    Location    location,
}

struct PersonalTraitResult {
    1: list<FilterInfo>         filter_info,
    2: optional    i32          source,     // 特征来源: 1: 筛选行为, 2: 浏览行为
    3: optional    i32          weight,
    4: optional    i32          city_id,
    5: optional    i32          method,     //1表示末次算法，2表示频次算法
}
