--Junte as tabelas FactExchangeRate e DimCurrency
--Mantenha apenas as colunas:
--ExchangeRateKey, CurrencyKey, DateKey
--AverageRate, CurrencyName

select 
FE.ExchangeRateKey,
FE.CurrencyKey,
CONVERT(varchar(10), FE.DateKey, 103) as DataKey ,
FE.AverageRate,
DC.CurrencyName,
CONCAT(CONVERT(varchar(10), FE.DateKey, 103), DC.CurrencyKey) as DateCurrencyKey
from FactExchangeRate as FE
left join DimCurrency as DC on DC.CurrencyKey = FE.CurrencyKey