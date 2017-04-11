// AS ThriftProxy(代理服务)

include "se.thrift"
include "cm.thrift"
include "sug.thrift"

namespace cpp  se
namespace csharp se
namespace java com.elong.hotel.searchagent.thrift.rpcservice
// ThriftProxy
service ThriftProxy {
    //suggestion for region(city,multicity,multiregion,province,state,country) 
    sug.RegionResponseData GetSugRegion(1:sug.RegionRequest region_request);
    
    //suggestion for keyword
    sug.KeywordResponseData GetSugKeyWord(1:sug.KeywordRequest keyword_request);

    // suggestion for poi, neighbor in ean region sysytem
    //sug.LocationResponseData GetSugLocation(1:sug.LocationRequest location_request);
    
    // suggestion for hotel
    //sug.HotelResponseData GetSugHotel(1:sug.HotelRequest hotel_request);
    
    /*location detail  for region*/
    //sug.DetailLocationResponseData GetSugLocationDetail(1:i32 region_id);

    // 热门酒店搜索
    // region_id      区域ID, 对应city/multicity
    // num            请求热门酒店个数
    se.HotHotelResponse SearchHotHotel(1: list<i32> region_id);
    se.HotHotelResponse SearchHotHotel1(1:se.HotHotelRequest request);

    // 列表搜索
    se.ListResponse SearchList(1:se.ListRequest request);

    // 列表实时搜索
    se.ListRtsResponse SearchListRts(1:se.ListRtsRequest request);

    // 详情搜索
    se.DetailResponse SearchDetail(1:se.DetailRequest request);

    // 详情实时搜索
    se.DetailRtsResponse SearchDetailRts(1:se.DetailRtsRequest request);

    // 地图列表搜索 (todo:暂时不做,未实现)
    se.ListMapResponse SearchListMap(1:se.ListRequest request);

    // 酒店周边
    se.NearbyResponse SearchNearby(1:se.NearbyRequest request);

    //国内酒店
    se.InnerSearchResponse SearchInner(1:se.InnerSearchRequest request);
    //筛选
    se.FilterSearchResponse SearchFilter(1:se.FilterSearchRequest request);

    se.NearByInfoResponse SearchNearByInfo(1:se.NearByInfoRequest request);

    // 个人特征检索
    se.PersonalTraitResponse SearchPersonalTrait(1:se.PersonalTraitRequest request);
	
}
