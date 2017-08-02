package org.ws.model;

import java.util.List;

import javax.persistence.CascadeType;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.ManyToMany;
import javax.xml.bind.annotation.XmlElement;

public class AirportModel {
	
	@Id @GeneratedValue(strategy = GenerationType.AUTO)
	private int id;
	
	@XmlElement(required=false)
	private String name;
	
	@XmlElement(required=false)
	@ManyToMany(cascade=CascadeType.ALL, mappedBy="fromTo")
	private List<AircraftModel>aircraftsOut;
	
	@XmlElement(required=false)
	@ManyToMany(cascade=CascadeType.ALL,mappedBy="goingTo")
	private List<AircraftModel>aircraftsIn;

	public int getId() {
		return id;
	}

	public void setId(int id) {
		this.id = id;
	}

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}

	public List<AircraftModel> getAircraftsOut() {
		return aircraftsOut;
	}

	public void setAircraftsOut(List<AircraftModel> aircraftsOut) {
		this.aircraftsOut = aircraftsOut;
	}

	public List<AircraftModel> getAircraftsIn() {
		return aircraftsIn;
	}

	public void setAircrafstIn(List<AircraftModel> aircraftIn) {
		this.aircraftsIn = aircraftIn;
	}
	
	public void addAircraftOut(AircraftModel model){
		this.aircraftsOut.add(model);
	}

	public void addAircraftIn(AircraftModel model){
		this.aircraftsIn.add(model);
	}

	
}
