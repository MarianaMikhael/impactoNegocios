-- Inner Join do formulário em etapas --
select sist.cod_Sistema as 'ID Sistema',
		 infra.fk_Sistema_id as 'FK Infraestrutura',
		 infra.cod_Infraestrutura as 'ID Infraestrutura',
		 cont.fk_Sistema_id as 'FK Continuidade',
		 cont.cod_Continuidade as 'ID Continuidade',
		 critic.fk_Sistema_id as 'FK Criticidade',
		 critic.cod_Criticidade as 'ID Criticidade',
		 sist.sistema as 'Nome Sistema',
		 sist.ativo as 'Status',
		 critic.nivel_Criticidade as 'Nível de Criticidade'
from systems_t_sistema as sist
inner join systems_t_infraestrutura as infra on sist.cod_Sistema = infra.fk_Sistema_id
inner join systems_t_continuidade_tecnologica as cont on sist.cod_Sistema = cont.fk_Sistema_id
inner join systems_t_criticidade as critic on sist.cod_Sistema = critic.fk_Sistema_id