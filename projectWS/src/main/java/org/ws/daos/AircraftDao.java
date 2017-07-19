package org.ws.daos;

import java.util.Collections;
import java.util.List;

import javax.persistence.EntityManager;
import javax.persistence.PersistenceContext;
import javax.transaction.Transactional;

import org.springframework.stereotype.Repository;
import org.ws.model.AircraftModel;

@Repository
@Transactional
public class AircraftDao {

	@PersistenceContext
	EntityManager manager;

	private String className = "AircraftModel";


	private List<AircraftModel> executeQuery(String query){

		try {
			return manager.createQuery(query,AircraftModel.class).getResultList();
		} catch (Exception e) {
			return Collections.<AircraftModel>emptyList();
		}

	}

	public List<AircraftModel> getAll(){

		return executeQuery("select x from  "+className+" x");
	}

	public List<AircraftModel>getFilterOneParameter(String columnName, String parameter){

		return executeQuery("select x from "+className+" x where x."+columnName+"  =  '"+parameter+"'");
	}

	public Boolean save(AircraftModel model){

		try {
			manager.persist(model);
			return true;
		} catch (Exception e) {
			return false;
		}
	}

}
