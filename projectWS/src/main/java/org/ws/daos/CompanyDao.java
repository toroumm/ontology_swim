package org.ws.daos;

import java.util.Collections;
import java.util.List;

import javax.persistence.EntityManager;
import javax.persistence.PersistenceContext;
import javax.transaction.Transactional;

import org.springframework.stereotype.Repository;
import org.ws.model.CompanyModel;

@Repository
@Transactional
public class CompanyDao {

	@PersistenceContext
	EntityManager manager;	
	
	private String className = "CompanyModel";

	private List<CompanyModel> executeQuery(String query){

		try {
			return manager.createQuery(query,CompanyModel.class).getResultList();
		} catch (Exception e) {
			return Collections.<CompanyModel>emptyList();
		}

	}

	public List<CompanyModel> getAll(){

		return executeQuery("select x from  "+className+" x");
	}

	public List<CompanyModel>getFilterOneParameter(String columnName, String parameter){

		return executeQuery("select x from "+className+" x where x."+columnName+"  =  '"+parameter+"'");
	}

	public Boolean save(CompanyModel model){

		try {
			manager.persist(model);
			return true;
		} catch (Exception e) {
			return false;
		}
	}

}
