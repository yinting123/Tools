// AS ThriftProxy(代理服务)

include "se.thrift"
include "cm.thrift"
include "sug.thrift"
include "dss.thrift"
include "dynamic_search.thrift"

namespace cpp  se
namespace csharp se
namespace java com.elong.hotel.searchagent.thrift.rpcservice
// ThriftProxy
service DSServiceProxy {

    //国内酒店
	se.InnerSearchResponse SearchInner(1:se.InnerSearchRequest request,2:se.InnerSearchResponse response);
    dss.DSSInnerSearchResponse SearchInner2(1:se.InnerSearchRequest request,2:dss.DSSInnerSearchHotel hotelidAttr);
	dss.VerifyPriceResponse SearchInnerVerifyPrice(1:dss.VerifyPriceRequest request);
	//成单时,预付产品无脑定价接口
	dss.VerifyPriceResponse ChangePrice4Order(1:dss.VerifyPriceRequest request);
	dss.DSSSearchCanBookResponse SearchCanBook(1:se.InnerSearchRequest request,2:dss.DSSSearchCanBookRequest cbRequest);
	dynamic_search.SearchResponse SearchDebugDetail(1:se.InnerSearchRequest request);
	dynamic_search.SearchResponse SearchDsTransportTest(1:dynamic_search.SearchResponse searchResponse);
	dynamic_search.StringModel SearchGsTransportTest(1:dynamic_search.StringModel content);
	// 获取产品基本信息
	dss.GetProductBaseInfoResponse GetProductBaseInfo(1:dss.GetProductBaseInfoRequest request);
	// 获取库存和及时确认
	dss.GetInvAndInstantConfirmResponse GetInvAndInstantConfirm(1:dss.GetInvAndInstantConfirmRequest request);
}
