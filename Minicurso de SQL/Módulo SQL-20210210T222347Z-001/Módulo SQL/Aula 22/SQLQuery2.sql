-- Quantos produtos vedemos na empresa?
select COUNT(*) from DimProduct

--Qual o valod o produto mais caro?
select MAX(UnitPrice) from DimProduct

-- Qual a média dos preços dos produtos?
select ROUND(AVG(UnitPrice),2)
from DimProduct

-- Quantas marcas temos na empresa?
select
count(distinct(BrandName))
from DimProduct
