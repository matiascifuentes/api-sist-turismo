from models.datamart import HistoricoListas, HistoricoSesiones

def get_itemset_historico_listas():
	items_listas = HistoricoListas.query.order_by(HistoricoListas.id_lista).all()
	itemset = []

	if(items_listas):
		last_id = items_listas[0].id_lista
		aux_list = []
		for item in items_listas:
			actual_id = item.id_lista
			if(actual_id == last_id):
				aux_list.append(item.id_servicio)
			else:
				itemset.append(tuple(aux_list))
				aux_list = []
			last_id = actual_id
	return itemset

def get_itemset_historico_sesiones(id_usuario, max_results):
	items_sesiones = HistoricoSesiones.query.filter_by(id_usuario=id_usuario).order_by(HistoricoSesiones.id_sesion).limit(max_results).all()
	itemset = []

	if(items_sesiones):
		last_id = items_sesiones[0].id_sesion
		aux_list = []
		for item in items_sesiones:
			actual_id = item.id_sesion
			if(actual_id == last_id):
				aux_list.append(item.id_servicio)
			else:
				itemset.append(tuple(aux_list))
				aux_list = []
			last_id = actual_id
	return itemset 
