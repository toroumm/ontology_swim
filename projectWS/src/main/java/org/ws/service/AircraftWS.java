package org.ws.service;

import java.util.List;

import javax.jws.WebMethod;
import javax.jws.WebResult;
import javax.jws.WebService;
import javax.jws.soap.SOAPBinding;
import javax.jws.soap.SOAPBinding.ParameterStyle;
import javax.jws.soap.SOAPBinding.Style;
import javax.jws.soap.SOAPBinding.Use;
import javax.xml.bind.annotation.XmlElement;

import org.springframework.beans.factory.annotation.Autowired;
import org.ws.daos.AircraftDao;
import org.ws.data.mok.GetDataMok;
import org.ws.model.AircraftModel;


@WebService
@SOAPBinding(style=Style.DOCUMENT, use=Use.LITERAL, parameterStyle=ParameterStyle.WRAPPED)
public class AircraftWS {
	
	private GetDataMok data =  new GetDataMok();
	
	@Autowired
	AircraftDao airDao;
	
	@XmlElement
	List<AircraftModel>aircrafts;
	
	@WebMethod(operationName = "getAllAircrafts")
	@WebResult(name = "aircrafts")
	public List<AircraftModel>getAircraft(){
		return data.getListAircraftModel(10);
	}
	
	@WebMethod(operationName= "recordOneAircraft",action="recordOneAircraft") 
	@WebResult(name= "aircraft")
	public AircraftModel setAircraft(AircraftModel model){
		airDao.save(model);
		return model;
	}
}
