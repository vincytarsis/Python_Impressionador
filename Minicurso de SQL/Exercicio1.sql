--1 Crie uma consulta para retornar a tebela Funcion�rios (DimEployee)
select * from DimEmployee

--2 Selecione apenas as colunas: C�digoFuncionario, Nome, Sobrenome, T�tulo, G�nero, Nome do Departamento
select 
DE.EmployeeKey, 
DE.FirstName,
DE.LastName,
DE.Title,
DE.Gender,
DE.DepartmentName
from DimEmployee as DE

--3 Filtre apenas os funcionarios do G�noro Masculino
select * from DimEmployee as DE
where DE.Gender = 'M'

--4 Filtre apenas os homens que s�o Gerentes Regionais (Sales Region Manager)
select * from DimEmployee DE
where DE.Gender = 'M' and
De.Title = 'Sales Region Manager'

-- 5 Filtre apenas os homens que s�o Gerentes Regionais (Sales Region Manager) ou Gerentes de Estado
-- (Sales State Manager)
select * from DimEmployee
where Gender = 'M' and
(Title = 'Sales Region Manager' or Title = 'Sales State Manager')

-- 6 Filtre apenas os homens que s�o Gerentes Regionais (Sales Region Manager) ou Gerentes de Estado
-- (Sales State Manager) que s�o da �rea do Departamento de Produ��o (Production)
select * from DimEmployee as DE
where DE.Gender = 'M' and
(DE.Title = 'Sales Region Manager' or DE.Title = 'Sales State Manager') and
DE.DepartmentName = 'Production'