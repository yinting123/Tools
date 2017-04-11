insert into ProHotelProductsPriceChange
(PromotionID,HotelID,roomtypeID,rateplanID,CouponRedemptionUpperLimit,AllowPartial,EffectiveDateFrom,EffectiveDateTo,operDate,bonusInfo)
values(%s,%s,%s,%s,%s,0,%s,%s,GETDATE(),%s)