select
DS.StoreKey,
DS.StoreName,
DimGeography.RegionCountryName
from DimStore as DS
left join DimGeography on DS.GeographyKey = DimGeography.GeographyKey
