package org.ws.daos;

import java.util.Collections;
import java.util.List;

import javax.persistence.EntityManager;
import javax.persistence.PersistenceContext;
import javax.transaction.Transactional;

import org.springframework.stereotype.Repository;
import org.ws.model.ManufacturerModel;

@Repository
@Transactional
public class ManufacturerDao {

	
	@PersistenceContext
	private EntityManager manager;
	
	private String className = "ManufacturerModel";
	
	private List<ManufacturerModel> executeQuery(String query){

		try {
			return manager.createQuery(query,ManufacturerModel.class).getResultList();
		} catch (Exception e) {
			return Collections.<ManufacturerModel>emptyList();
		}

	}

	public List<ManufacturerModel> getAll(){

		return executeQuery("select x from  "+className+" x");
	}

	public List<ManufacturerModel>getFilterOneParameter(String columnName, String parameter){

		return executeQuery("select x from "+className+" x where x."+columnName+"  =  '"+parameter+"'");
	}

	public Boolean save(ManufacturerModel model){

		try {
			manager.persist(model);
			return true;
		} catch (Exception e) {
			return false;
		}
	}
}
