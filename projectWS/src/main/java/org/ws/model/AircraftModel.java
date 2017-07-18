package org.ws.model;

import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.ManyToOne;
import javax.persistence.OneToOne;
import javax.persistence.Table;

@Table(name ="aircraft")
@Entity
public class AircraftModel {

	@Id @GeneratedValue(strategy = GenerationType.AUTO)
	private int id;
	private String model;
	private String icao;
	private float speed;
	
	@ManyToOne
	private CompanyModel company;
	
	@ManyToOne
	private ManufacturerModel manufacturer;
	
	@OneToOne
	private AirportModel goingTo;
	
	@OneToOne
	private AirportModel fromto;
	
	public CompanyModel getCompany() {
		return company;
	}
	public void setCompany(CompanyModel company) {
		this.company = company;
	}
	public AirportModel getGoingTo() {
		return goingTo;
	}
	public void setGoingTo(AirportModel goingTo) {
		this.goingTo = goingTo;
	}
	public AirportModel getFromto() {
		return fromto;
	}
	public void setFromto(AirportModel fromto) {
		this.fromto = fromto;
	}
	public ManufacturerModel getManufacturer() {
		return manufacturer;
	}
	public void setManufacturer(ManufacturerModel manufacturer) {
		this.manufacturer = manufacturer;
	}
	public int getId() {
		return id;
	}
	public void setId(int id) {
		this.id = id;
	}
	public String getModel() {
		return model;
	}
	public void setModel(String model) {
		this.model = model;
	}
	public String getIcao() {
		return icao;
	}
	public void setIcao(String icao) {
		this.icao = icao;
	}
	public float getSpeed() {
		return speed;
	}
	public void setSpeed(float speed) {
		this.speed = speed;
	}
	@Override
	public String toString() {
		return "AircraftModel [id=" + id + ", model=" + model + ", icao=" + icao + ", speed=" + speed + "]";
	}
}