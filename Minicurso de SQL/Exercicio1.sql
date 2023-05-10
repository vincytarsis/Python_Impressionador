--1 Crie uma consulta para retornar a tebela Funcionários (DimEployee)
select * from DimEmployee

--2 Selecione apenas as colunas: CódigoFuncionario, Nome, Sobrenome, Título, Gênero, Nome do Departamento
select 
DE.EmployeeKey, 
DE.FirstName,
DE.LastName,
DE.Title,
DE.Gender,
DE.DepartmentName
-- Dica Hashtag - CONCAT(fisrtname, ' ', lastname) as 'FullName'
from DimEmployee as DE

--3 Filtre apenas os funcionarios do Gênoro Masculino
select *-- Dica Hashtag - replace(REPLACE(Gender, 'M','Masculuino'), 'F','Femenino') as 'Genero',
from DimEmployee as DE
where DE.Gender = 'M'

--4 Filtre apenas os homens que são Gerentes Regionais (Sales Region Manager)
select * from DimEmployee DE
where DE.Gender = 'M' and
De.Title = 'Sales Region Manager'

-- 5 Filtre apenas os homens que são Gerentes Regionais (Sales Region Manager) ou Gerentes de Estado
-- (Sales State Manager)
select * from DimEmployee
where Gender = 'M' and
(Title = 'Sales Region Manager' or Title = 'Sales State Manager')

-- 6 Filtre apenas os homens que são Gerentes Regionais (Sales Region Manager) ou Gerentes de Estado
-- (Sales State Manager) que são da área do Departamento de Produção (Production)
select * from DimEmployee as DE
where DE.Gender = 'M' and
(DE.Title = 'Sales Region Manager' or DE.Title = 'Sales State Manager') and
DE.DepartmentName = 'Production'

--Filtre apenas os homens que são Gerentes Regionais (“Sales Region Manager”) ou Gerentes de Estado
--(“Sales State Manager”) que são da área do Departamento de Produção (“Production”) ou do departamento
--de Marketing
select * from DimEmployee DE
where DE.Gender = 'M' and
(DE.Title = 'Sales Region Manager' or DE.Title = 'Sales State Manager') and
(DE.DepartmentName = 'Production' or DE.DepartmentName = 'Marketing')
