
include "cm.thrift"

namespace cpp se
namespace csharp se
namespace java com.elong.hotel.searchagent.thrift.bean
/* region_id is id of city or multicity
 * region_name_cn is  chinese name of  city or multicity
 * region_name_alpha is pinyin or english name of city or multicity
 * supercity_name_cn is chinese name of multiregion,province or country
 * supercity_name_alpha is pinyin or english name of multiregion,province or country
 * state_name_cn is is chinese name of country in which city or multicity is 
 * state_name_alpha is pinyin or english name of country.
 * in this struct,some string may be empty for the search word may be chinese pinyin or english and
 * the return result is different.
 *
*/
/*status_code[0 is ok; 1 means error ]*/

enum GuestType {
    WHOTEL = 0,
    MOBILE = 1,
    MAPARTMENT = 2,
    WEHOTEL     = 3,
}

enum LANGUAGE {
    CH = 0,
    EN = 1,
}

struct RegionRequest {
    1: string               search,
    2: cm.UserInfo             user_info,
    3: GuestType            guest,
    4: LANGUAGE             langu,
}

enum RegionType {
    RCITY = 0,
    RDISTRICT = 1,
    RSCENIC = 2,
    RMALL = 3,
}

struct RegionResult {
    1:i32       region_id,
    2:i32       region_id_v4,
    3:string    region_name,
    4:string    region_name_seo,
    5:i32       is_skip,
    6:i32           parent_id,
    7:i32           parent_id_v4,
    8:string        parent_name,
    9:string        parent_name_seo,
    10:string       composed_name,
    11:i32          hotel_num,
    12:RegionType   region_type,
    13:LANGUAGE     langu,
}

struct RegionResponseData {
    1:i32                   status_code  = -1,
    2:list<RegionResult>    region_response,
    3:i64                   search_id,
}

enum KeywordType {
    HOTEL = 0,
    TUAN = 1,
    APARTMENT = 2,
    BRAND = 3,
    DISTRICT = 4,
    MALL = 5,
    POI = 6,
    NEIGHBOR = 7,
}

struct KeywordResult {
    1: KeywordType      type,
    2: i32              keyword_id,
    3: i32              keyword_id_v4,
    4: i32              region_id,
    5: i32              region_id_v4,
    6: string           keyword_name,
    7: cm.GeoInfo       geoinfo,
    8: i32              weight,
    9: LANGUAGE         langu,
    10: i32             hot_count,
}

struct KeywordRequest {
    1: i32              region_id = -1,
    2: string           search,
    3: cm.UserInfo      user_info,
    4: GuestType             guest,
    5: LANGUAGE              langu,
}

struct KeywordResponseData  {
    1:i32                   status_code = -1,
    2:list<KeywordResult>   keyword_response,
    3:i64                   search_id,     // [注意:无符号长整数,因thrift不支持无符号,需要自己转换]
}
