package org.ws.controller;



import javax.xml.ws.Endpoint;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.ws.daos.AircraftDao;
import org.ws.service.AircraftWS;

@Controller
public class HomeController {
	
	@Autowired
	AircraftDao dao;

	@RequestMapping(value="/")
	public String index(){
		
		AircraftWS aircraftWS =  new AircraftWS();
		
		String urlData = "http://localhost:8080/projectWS/aircraftData";
		
		Endpoint e = Endpoint.create(aircraftWS);
		
		//Endpoint.publish(urlData, aircraftWS);
		
		e.publish(urlData);
		return "home";
	}
}
