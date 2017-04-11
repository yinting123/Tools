USE PromotionDB

DECLARE @promotionid int
DECLARE @hotelid varchar(255)
DECLARE @roomtyid varchar(255)
DECLARE @rpid int 
DECLARE @coupon int
DECLARE @startDay varchar(50)
DECLARE @endDay varchar(50)

SET @promotionid = %d
set @hotelid = '%s'
set @roomtyid = '%s'
set @rpid = %d
set @coupon = %d
set @startDay = '%s'
set @endDay = '%s'


insert into dbo.ProHotelProductPriceChange
(   PromotionID,
    HotelID,
    roomtypeID,
    rateplanID,
    HotelName,
    RoomTypeName,
    RatePlanName,
    CouponRedemptionUpperLimit,
    AllowPartial,
    EffectiveDateFrom,
    EffectiveDateTo,
    Operator,
    operDate
)
values(
    @promotionid , -- PromotionID - bigint
    @hotelid , -- HotelID - varchar(50)
    @roomtyid , -- roomtypeID - varchar(50)
    @rpid , -- rateplanID - bigint
    '' , -- HotelName - varchar(100)
    '' , -- RoomTypeName - varchar(100)
    '' , -- RatePlanName - varchar(100)
    @coupon , -- CouponRedemptionUpperLimit - int
    0 , -- AllowPartial - tinyint
    @startDay, -- EffectiveDateFrom - datetime
    @endDay,-- EffectiveDateTo - datetime
    '',-- Operator - varchar(50)
    GETDATE()  -- operDate - datetime

)
