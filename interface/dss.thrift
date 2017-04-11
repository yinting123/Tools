
include "se.thrift"
include "cm.thrift"
include "sug.thrift"

namespace cpp  se
namespace csharp se
namespace java com.elong.hotel.searchagent.thrift.dss

struct  DSSInnerSearchResponse
{
1:se.InnerSearchResponse response,
2:list<i64> pageHotelIds,//list的酒店id顺序
}

struct HotelIdAttr {
    1:optional i64 mhotel_id,
    2:optional i64 attr, //第0位:是否参加排序分页
}

struct SelectedProduct
{
1: required i32 shotel_id,
2: required i32 sroom_id,
3: required i32 rate_plan_id,
}

struct  DSSInnerSearchHotel
{
1:list<HotelIdAttr> mhotel_id_attr,
2:optional string traceId,
3:optional bool is_list_detail,
4:list<cm.FilterCondition> filter_conditions,
5:optional map<i64, list<SelectedProduct>> selected_product_ids, // key: mhotel_id, value : 产品信息
}
struct DayPriceReq
{
1:optional i64 availableDate,//秒，日期不带时分秒
2:optional double salePrice,//drr后卖价
3:optional double salePriceBeforeDrr,//drr前卖价
4:optional double saleCostBeforeDrr,//drr前底价
5:optional double saleCost,//drr后底价
}
struct VerifyPriceRequest
{
1:optional string dynamicId,//马甲ID
2:optional i64 hotelId,
3:optional i64 roomTypeId,
4:optional i64 ratePlanId,
5:optional i64 mHotelId,
6:optional i64 checkinDate,//秒，日期不带时分秒
7:optional i64 checkoutDate,//秒，日期不带时分秒
8:list<DayPriceReq> dynamicProductDetailList,
}

struct DayPriceResp
{
1:optional string date,//2016.01.01
2:optional double price,
}
struct VerifyPriceResponse
{
1:list<DayPriceResp> data,
2:optional string desc,//描述
3:optional i32 retcode,//0代表正确 -1代表错误 1代表参数异常
4:optional cm.Price price,//正价产品价格
}
struct  DSSSearchCanBookRequest
{
1:list<i64> mhotel_ids,
2:optional string traceId,
3:list<cm.FilterCondition> filter_conditions,
4:list<i64> return_mhotel_ids,
5:optional map<i64, list<SelectedProduct>> selected_product_ids, // key: mhotel_id, value : 产品信息
}

struct SimplePromotion
{
1:optional i32 promotion_id,
2:optional i32 uper_limit,
3:optional string date,
}

struct SimpleProduct
{
1:optional i32 sale_cost,//底价
2:optional i32 sale_price,//卖价
3:list<SimplePromotion> promotion_type,
4:list<cm.Inventory> inventorys,
5:optional i32 sroom_id,
6:optional i32 rp_id,
7:optional i32 shotel_id,
}

struct SimpleMRoom
{
1:optional i32 mroom_id,
2:list<SimpleProduct> products,
}

struct HotelBookDetail
{
1:optional i64 mhotel_id,
2:optional bool is_can_booking,
3:list<i32> hotel_flag,
4:optional i32 min_price_sub_coupon,
5:optional double min_price_sub_coupon_sale_cost,
6:list<SimpleMRoom> simple_mrooms,
}


struct DSSSearchCanBookResponse
{
1:optional cm.ServerStatus status,
2:optional cm.Statistics statistics,
3:cm.FilterResult filter_result,
4:optional list<se.FastFilterInfo> fast_filter_info,
5:list<cm.FilterList> filter_list,
6:list<HotelBookDetail> hotel_book_detail,
7:list<double>	discounts,
8:optional list<cm.PriceRangeStatistic> price_range_statistic, // 价格范围统计信息
}


//start  

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
2:optional string mhotel_name,
3:optional i32 city_id, //
4:optional string city_name,
5:optional i32 star,
6:optional list<ProductInfo> product_info,
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
 // end -GetProductBaseInfoResponse


struct ShotelAttr
{
1:required i32 shotel_id,
2:optional list<i32> sroom_ids,
}

struct MhotelAttr
{
1:required i32 mhotel_id,
2:optional list<ShotelAttr> shotel_attr,
}


struct GetInvAndInstantConfirmRequest
{
1:required list<MhotelAttr> mhotel_attr,
2:required i64 start_date,
3:required i64 end_date,
4:optional bool need_instant_confirm,
5:optional i64 order_from,
6:optional i32 search_from, //3：NBAPI
}

struct InvDetail
{
1:optional i64 begin_date,
2:optional i64 end_date,
3:optional string begin_time,
4:optional string end_time,
5:optional i32 available_amount,
6:optional i64 available_date,
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

struct MhotelDetail
{
1:required i32 mhotel_id,
2:optional list<ShotelDetail> shotel_detail,
}

struct GetInvAndInstantConfirmResponse
{
1:optional list<MhotelDetail> mhotel_detail, // 酒店信息
2:optional i32 return_code, //0：正常
3:optional string return_msg, //
}
