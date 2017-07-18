package org.ws.data.mok;

import java.util.ArrayList;
import java.util.List;

import org.ws.model.*;




public class GetDataMok {
	
	private String airportNames[] = {"A","B","C"};
	private String companyNames[]= {"CA","CB","CC"};
	private String manufacturerNames[]= {"MA","MB","MC"};
	private String icaoNumber[]= {"I1","I2","I3","I4","I5"};
	
	
	public String[] getAirportNames() {
		return airportNames;
	}

	public void setAirportNames(String[] airportNames) {
		this.airportNames = airportNames;
	}

	public String[] getCompanyNames() {
		return companyNames;
	}

	public void setCompanyNames(String[] companyNames) {
		this.companyNames = companyNames;
	}

	public String[] getManufacturerNames() {
		return manufacturerNames;
	}

	public void setManufacturerNames(String[] manufacturerNames) {
		this.manufacturerNames = manufacturerNames;
	}

	public AirportModel getAirportModelIn(String name, AircraftModel craft){
		
		AirportModel model = new AirportModel();
		
		model.addAircraftIn(craft);
		
		model.setName(name);
		
		return model;
	}
	
	public AirportModel getAirportModelOut(String name, AircraftModel craft){
		
		AirportModel model = new AirportModel();
		
		model.addAircraftOut(craft);
		
		model.setName(name);
		
		return model;
	}
	
	public ManufacturerModel getManufacturerModel(String name, AircraftModel craft){
		
		ManufacturerModel model = new ManufacturerModel();
		
		model.setName(name);
		
		model.AddAircraft(craft);
		
		return model;
	}
	
	public CompanyModel getCompanyModel(String name, AircraftModel craft){
		
		CompanyModel model =  new CompanyModel();
		
		model.addAircraft(craft);
		
		model.setName(name);
		
		return model;
	}
	
	public AircraftModel getAircraftModel(String name){
		
		AircraftModel model =  new AircraftModel();

		return model;
	}
	
	public List<AircraftModel>getListAircraftModel(int quant){
		
		List<AircraftModel>aircrafts = new ArrayList<AircraftModel>();
		 
		for(int i = 0; i < quant; i++){
			
			AircraftModel model = new AircraftModel();
			
			model.setCompany(getCompanyModel(companyNames[(int)(i%companyNames.length)], model));
			model.setFromto(getAirportModelOut(airportNames[(int)(i%airportNames.length)], model));
			model.setGoingTo(getAirportModelIn(airportNames[(int)((i+1)%airportNames.length)], model));
			model.setIcao(icaoNumber[(int) (i%icaoNumber.length)]);
			
			model.setManufacturer(getManufacturerModel(manufacturerNames[(int)(i%manufacturerNames.length)], model));
			
			model.setSpeed((float)Math.random());
			
			aircrafts.add(model);
		}
		return aircrafts;
	}

}
