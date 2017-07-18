package org.ws.daos;

import java.util.Collections;
import java.util.List;

import javax.persistence.EntityManager;
import javax.persistence.PersistenceContext;
import javax.transaction.Transactional;

import org.springframework.stereotype.Repository;
import org.ws.model.AirportModel;

@Transactional
@Repository
public class AirportDao {

	@PersistenceContext
	EntityManager manager;
	
	private String className = "AirportModel";
	
	
	private List<AirportModel> executeQuery(String query){
		
		try {
			return manager.createQuery(query,AirportModel.class).getResultList();
		} catch (Exception e) {
			return Collections.<AirportModel>emptyList();
		}
		
	}
	
	public List<AirportModel> getAll(){
		
		return executeQuery("select x from  "+className+" x");
	}
	
	public List<AirportModel>getFilterOneParameter(String columnName, String parameter){
		
		return executeQuery("select x from "+className+" x where x."+columnName+"  =  '"+parameter+"'");
	}
	
	public Boolean save(AirportModel model){
		
		try {
			manager.persist(model);
			return true;
		} catch (Exception e) {
			return false;
		}
	}
}
