// Copyright 2013 ELong Inc. All rights Reserved.
// 检索接口定义
include "cm.thrift"

namespace cpp  se
namespace csharp se
namespace java  com.elong.hotel.searchagent.thrift.bean

// 列表检索请求
struct ListRequest {
    //  区域ID, 对应city/multicity
    1:  i32                    region_id,
    //  入住时间
    2:  i64                    check_in_date,
    //  离开时间
    3:  i64                    check_out_date,
    //  POI信息
    4:  i32                    poi_id,
    //  POI字符串
    5:  string                 poi_str,
    //  请求返回酒店个数(默认-1:全部)
    6:  i32                    hotel_num = -1,
    //  酒店名(包含中英文)
    7:  string                 hotel_name,
    //  价格区间[单位:分]
    8:  list<cm.PriceRange>    hotel_price_range,
    //  酒店星级
    9:  list<cm.HotelStarType> hotel_star,
    //  酒店品牌(酒店品牌较多,无法枚举)
    10:  list<i32>              hotel_brand,
    //  酒店类型
    11: list<i32>              hotel_type,
    // 酒店设施
    12: list<i32>              hotel_facilitie,
    // 排序类型, 默认使用"默认"排序
    13: cm.RankType            rank_type,
    // 距离筛选时, 距离(公里)
    14: i32                    rank_distance,
    // 分页信息
    16: cm.PageInfo            page_info,
    // 距离筛选[0：不做距离筛选]
    17: i32                    hotel_distance,
    // Session ID(todo:del)
    18: string                 session_id,
    // user info
    19: cm.UserInfo            user_info,
    // OTA开关(位表示， 只看elong传入4(0100))
    20: i64                    filter_ota,
    // 入住人数相关信息,不传此参数则按照1房间1成人0儿童
    21: list<cm.RoomInfo>      room_info,
}

struct ListResponse {
    //  检索ID,唯一标识每个PV,由AS生成并返回 
    //  [注意:无符号长整数,因thrift不支持无符号,需要自己转换]
    1:  i64                search_id,
    //  最低价(本次检索对应的酒店最低价,单位:分)
    2:  i32                lowest_price,
    //  总共检索出的酒店家数
    3:  i32                result_hotel_num,
    //  总页数
    4:  i32                page_num,
    //  酒店列表
    5:  list<cm.HotelInfoList> hotel_list,
    //  酒店统计
    6:  cm.HotelFilter     hotel_filter,
    //  识别出位置用户输入的位置对应的中心点[默认(0,0)]
    7:  cm.GeoInfo         center_coordinate,
    // 区域外包多边形
    8:  list<cm.GeoInfo>   region_polygon,
    // 区域其他信息
    9:  cm.RegionInfo      region_info,
    // 请求的POIID, -1为不识别,否则为POIID
    10: cm.POIData         poi_info,
    // 实际排序类型（当前端使用Unkonw时这个值有效）
    11: cm.RankType        rank_type,
    // 用户输入的POI语言类型（对应实际有结果的POI），默认中文
    12: cm.LangType        poi_lang,
    // 执行状态
    13: cm.ServerStatus    status,
}

// 地图列表检索请求
struct ListMapResponse {
    // search_id
    1:  i64                     search_id,
    // 酒店列表
    2:  list<cm.HotelInfoMap>   hotel_info,
    // 执行状态
    13: cm.ServerStatus         status,
}

// 实时检索请求, 增量请求
struct ListRtsRequest {
    // 酒店ID列表,每次传输未被抓取部分
    1:  list<i64>         hotel_list,
    // 入住时间
    2:  i64               check_in_date,
    // 离开时间
    3:  i64               check_out_date,
    // Search ID,检索ID,第一次实时检索置0. 
    // [注意:无符号长整数,因thrift不支持无符号,需要自己转换]
    4:  i64               search_id,
    // Session ID(todo:del)
    7: string             session_id,
    // user info
    9: cm.UserInfo        user_info,
    // OTA开关(位表示， 只看elong传入4(0100))
    10: i64               filter_ota = 0,
}

struct ListRtsResponse {
    // Search ID [注意:无符号长整数,因thrift不支持无符号,需要自己转换]
    1: i64                      search_id,
    // 酒店价格/实时抓取状态信息
    2: list<cm.HotelRtsInfo>    hotel_rts_info,
    // 执行状态
    13: cm.ServerStatus         status;
}

// 详情页静态检索请求
struct DetailRequest {
    // Hotel ID
    1: i32                hotel_id,
    // 入住时间
    2: i64                check_in_date,
    // 离开时间
    3: i64                check_out_date,
    // Region name
    4: string             region_str,
    // Region id(优先使用region_id,当region_id为0时使用region_str)
    5: i32                region_id = 0,
    // Session ID(todo:del)
    7: string             session_id,
    // user info
    9: cm.UserInfo        user_info,
    // OTA开关(位表示， 只看elong传入4(0100))
    10: i64               filter_ota = 0,
}

// 详情页静态检索响应
struct DetailResponse {
    //  Search ID [注意:无符号长整数,因thrift不支持无符号,需要自己转换]
    1:  i64                         search_id,
    // 酒店静态信息
    2:  cm.HotelInfoDetail          hotel_info,
    //  供应商信息(包括供应商中英文名称,价格)
    3:  list<cm.ProviderDetail>     provider_detail,
    // 区域其他信息
    4:  cm.RegionInfo               region_info,
    // 执行状态
    13: cm.ServerStatus             status,
}

struct HotHotelResponse {
    //  Search ID [注意:无符号长整数,因thrift不支持无符号,需要自己转换]
    1: i64                          search_id,
    // 热门酒店列表
    2: list<cm.HotHotelInfo>        hot_hotel,
    // 执行状态
    13: cm.ServerStatus    status;
    
}

// 详情页实时检索请求
struct DetailRtsRequest {
    // Hotel ID
    1:  i32                hotel_id,
    // 入住时间
    2:  i64                check_in_date,
    // 离开时间
    3:  i64                check_out_date,
    // Search id [注意:无符号长整数,因thrift不支持无符号,需要自己转换]
    4:  i64                search_id,
    // Provider ID列表,每次传输未被抓取部分
    5:  list<i64>          provider_list,
    // Session ID(todo:del)
    8: string              session_id,
    // user info
    9: cm.UserInfo        user_info,
    // OTA开关(位表示， 只看elong传入4(0100))
    10: i64               filter_ota = 0,
}

// 详情页实时检索响应
struct DetailRtsResponse {
    // Search ID [注意:无符号长整数,因thrift不支持无符号,需要自己转换]
    1:  i64                       search_id,
    //  供应商信息(包括供应商中英文名称,价格)
    2: list<cm.ProviderDetailInc> provider_detail,
    // Session ID (实际是cookie id 取名不好，下一版本修改) (todo:del)
    7: string                 session_id,
    // 执行状态
    13: cm.ServerStatus    status,
}

struct FastFilterInfo {
    1: optional i32 type_id,        // 0:全部; 1:附近; 99:普通筛选项，
                                    // 中文版直接传keyword_cn, 英文版keyword_en
    2: optional string keyword_cn,  // 快速筛选项中文名
    3: optional string keyword_en,  // 快速筛选项英文名
    4: optional i32    count,       // 对应的酒店个数
}

struct HotHotelRequest {
    // 酒店列表
    1: list<i32>        region_id,
    // user info
    2: cm.UserInfo      user_info,
    // Session ID (实际是cookie id 取名不好，下一版本修改) (todo:del)
    7: string                 session_id,
}

// 周边信息请求(机场/地铁/公交/景点)
struct NearbyRequest {
    // 酒店ID
    1: i32                    hotel_id,
    // 酒店所在城市ID
    2: i32                    region_id,
    // Session ID (实际是cookie id 取名不好，下一版本修改) (todo:del)
    7: string                 session_id,
    // user info
    9: cm.UserInfo            user_info,
}

struct NearbyResponse {
    // Search ID [注意:无符号长整数,因thrift不支持无符号,需要自己转换]
    1:  i64                search_id,
    // 酒店中文名
    2:  string             hotel_name_cn,
    // 酒店英文名
    3:  string             hotel_name_en,
    // POI信息
    4:  list<cm.NearbyPOI> poi,
    // 执行状态
    13: cm.ServerStatus    status,
}


enum InnerSearchType
{
    kRegionSearch = 1,  //本地检索  (带cityid的，可同事支持文本模糊检索) 
    kNearBySearch = 2,  //周边检索 （不需要带region,目前不同时支持文本模糊检索）
    kBoundSearch = 3,   //矩形检索（不需要带城市编号，目前只支持正南正北矩形，目前不同时支持模糊检索）
    kDetailSearch = 4,  //详情检索 (可一次传入多个酒店,可选择是否返回静态信息,也即静态摘要) 
    kStaticDigest = 5,  //静态摘要获取 (可一次传入多个酒店)
}

struct  InnerSearchRequest
{
1:InnerSearchType inner_search_type,
2:optional cm.HotelAttribute hotel_attr,
3:optional cm.RoomAttribute room_attr,
4:optional cm.ProductAttribute product_attr,
5:optional cm.GeoAttribute geo_attr,
6:optional cm.CustomerAttribute customer_attr,
7:optional cm.PageRankAttribute page_rank_attr,
8:optional cm.CallerAttribute caller_attr,
9:optional cm.ReturnAttribute return_attr,
10:optional cm.UserInfo user_info,
11:optional cm.FilterAttribute filter_attr,
12:optional cm.RecommendAttribute rec_attr,
13:optional cm.FastFilterAttribute fastfilter_attr, //快筛项的属性
}

struct  InnerSearchResponse
{
1:optional cm.ServerStatus status,
2:optional i32 total,
3:optional i32 count,
4:optional i32 page_size,
5:optional i32 page_index,
6:list<cm.HotelDetail> hotels_details,
7:optional cm.Statistics statistics,
8:optional cm.QueryParseResult query_parse_result,
9:optional i32 min_weifang_price,
10:optional list<cm.PromotionGroup> promotion_group,
21:optional string debug_info,
12:cm.FilterResult filter_result,

// 快速筛选项，顺序已排好
// 注意特例：
//    1. 第一项一般是 “不限”， 也当所有快筛项目个数为0时不展示
//    2. 后端会返回“近的”前端（app）特殊处理，根据经纬度搜索
//    3. 只有检索接口有这份数据,筛选接口没有
13:optional list<FastFilterInfo> fast_filter_info,
22:list<cm.DebugResponse> debug_response,
23:list<cm.FilterList> filter_list,
24:optional cm.Recommend rec_response,
25:optional cm.CommonConf common_conf,  //公共配置，目前里面只有promotion_group树
26:optional cm.UserTrack user_track,
27:optional i32 grandson,
28:list<double> discounts, //这个城市下面的折扣率汇总
29:optional bool use_new_recall_reason,
30:optional map<i32,cm.CommonConf> cities_common_conf,
}

enum FilterSearchType
{
    kFilterSearch = 1,  //纯筛选接口类型 
}

struct  FilterSearchRequest
{
1:optional FilterSearchType filter_search_type,
2:optional cm.GeoAttribute geo_attr,
3:optional cm.CallerAttribute caller_attr,
4:optional cm.FilterAttribute filter_attr,
5:optional cm.UserInfo user_info,
}
 
struct  FilterSearchResponse
{
1:optional cm.ServerStatus status,
2:optional cm.FilterResult filter_result,
}

struct NearByInfoRequest
{
1:list<cm.NearBySearchInfo> nearbyitem_list,
}

struct NearByInfoResponse
{
1:list<cm.NearBySearchResult> nearbyitem_list,
}

enum StrategyMode {
    // 用户真实行为组合优先
    kBoundTraitPriority     = 1,
    // 用户单项行为混合优先
    //kMixedTaritPriority     = 2,
    // 无效值
    kInvalidStrategyMode    = 999,
}

enum TraitType {
    // 推荐特征
    kCommendTrait       = 1,
    // 无效值
    kInvalidTraitType   = 999,
}

struct PersonalTraitRequest {
    1: optional    cm.PersonalInfo personal_info,
    2: optional    TraitType       trait_type,
    3: optional    StrategyMode    strategy_mode,
}

struct PersonalTraitResponse {
    1: list<cm.PersonalTraitResult> personaltrait_list,
}
