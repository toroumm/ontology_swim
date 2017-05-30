from cgitb import reset

from owlready import *
import json, sys, types

onto_path.append("OWL/")
onto = Ontology("http://test.org/service_euro.owl")

class Service(Thing):
    ontology = onto


class ATM_Data_Category(Service):
    ontology = onto


class ATM_Activity_Category(Service):
    ontology = onto


class ATM_Flight_Phases(Service):
    ontology = onto


class ATM_StakeHolders(Service):
    ontology = onto


class Regions(Service):
    ontology = onto

#Creating Object Properties
class hasATMDataCategory(Property):
    ontology = onto
    domain = [Service]
    range = [ATM_Data_Category]

class hasATMActivityCategory(Property):
    ontology = onto
    domain = [Service]
    range = [ATM_Activity_Category]

class hasATMFlightPhases(Property):
    ontology = onto
    domain = [Service]
    range = [ATM_Flight_Phases]

class hasATMStakeHolders(Property):
    ontology = onto
    domain = [Service]
    range = [ATM_StakeHolders]

class hasRegions(FunctionalProperty):
     ontology = onto
     # domain = [Service]
     range = [Regions]


#Creating Data Properties
class has_for_version(Property):
    ontology = onto
    domain = [Service]
    range = [str]

class has_for_versionCategory(Property):
    ontology = onto
    domain = [Service]
    range = [str]

class has_for_percentPrescribe(Property):
    ontology = onto
    domain = [Service]
    range = [str]

class has_for_implementStatus(Property):
    ontology = onto
    domain = [Service]
    range = [str]

class has_for_serviceTecnicalInterface(Property):
    ontology = onto
    domain = [Service]
    range = [str]

json_string = open("JSON/resultado.json").read()
parsed_json = json.loads(json_string)

# Creating Subclasses
regionClasses = []
flightPhaseClasses = []
dataStakeholderClasses = []
dataCategoryClasses = []
actCategoryClasses = []

for i in range(0, len(parsed_json.keys())):

    if len(parsed_json[str(i)]["atm"]["regions"]) > 0:
        for x in range(0, len(parsed_json[str(i)]["atm"]["regions"])):
            region = parsed_json[str(i)]["atm"]["regions"][x].replace(" ", "")

            if region not in regionClasses:
                newClass = types.new_class(region, (Regions,), kwds={"ontology": onto})
                regionClasses.append(newClass)

    if len(parsed_json[str(i)]["atm"]["flightPhases"]) > 0:
        for x in range(0, len(parsed_json[str(i)]["atm"]["flightPhases"])):
            flightPhase = parsed_json[str(i)]["atm"]["flightPhases"][x].replace(" ", "")

            if flightPhase not in flightPhaseClasses:
                newClass = types.new_class(flightPhase, (ATM_Flight_Phases,), kwds={"ontology": onto})
                flightPhaseClasses.append(newClass)

    if len(parsed_json[str(i)]["atm"]["dataStakeholder"]) > 0:
        for x in range(0, len(parsed_json[str(i)]["atm"]["dataStakeholder"])):
            dataStakeHolder = parsed_json[str(i)]["atm"]["dataStakeholder"][x].replace(" ", "")

            if dataStakeHolder not in dataStakeholderClasses:
                newClass = types.new_class(dataStakeHolder, (ATM_StakeHolders,), kwds={"ontology": onto})
                dataStakeholderClasses.append(newClass)

    if len(parsed_json[str(i)]["atm"]["dataCategory"]) > 0:
        for x in range(0, len(parsed_json[str(i)]["atm"]["dataCategory"])):
            dataCategory = parsed_json[str(i)]["atm"]["dataCategory"][x].replace(" ", "")

            if dataCategory not in dataCategoryClasses:
                newClass = types.new_class(dataCategory, (ATM_Data_Category,), kwds={"ontology": onto})
                dataCategoryClasses.append(newClass)

    if len(parsed_json[str(i)]["atm"]["actCategory"]) > 0:
        for x in range(0, len(parsed_json[str(i)]["atm"]["actCategory"])):
            actCategory = parsed_json[str(i)]["atm"]["actCategory"][x].replace(" ", "")

            if actCategory not in actCategoryClasses:
                newClass = types.new_class(actCategory, (ATM_Activity_Category,), kwds={"ontology": onto})
                actCategoryClasses.append(newClass)

# Creating Instances
for i in range(0, len(parsed_json.keys())):

    # header
    percentPrescribe = parsed_json[str(i)]["header"]["percentPrescribe"]
    nameService = parsed_json[str(i)]["header"]["nameService"].replace(" ", "")

    newService = Service(nameService)

    if "version" in parsed_json[str(i)]["header"]:
        version = parsed_json[str(i)]["header"]["version"]

    implementStatus = str(parsed_json[str(i)]["header"]["implementStatus"])
    versionCategory = str(parsed_json[str(i)]["header"]["versionCategory"])

    # ATM
    region = region = parsed_json[str(i)]["atm"]["regions"]
    if len(region) > 0:
        for x in range(0, len(region)):
            for y in range(0,len(regionClasses)):
                if str(regionClasses[y]) == region[x]:
                    newService.is_a.append(restriction("hasRegions", SOME, regionClasses[y]))
                    break

    flightPhase = parsed_json[str(i)]["atm"]["flightPhases"]
    if len(flightPhase) > 0:
        for x in range(0, len(flightPhase)):
            for y in range(0,len(flightPhaseClasses)):
                if str(flightPhaseClasses[y]) == flightPhase[x]:
                    newService.is_a.append(restriction("hasATMFlightPhases",SOME ,flightPhaseClasses[y]))
                    # newService.is_a.append(flightPhaseClasses[y])
                    break

    dataStakeHolder = parsed_json[str(i)]["atm"]["dataStakeholder"]
    if len(dataStakeHolder) > 0:
        for x in range(0, len(dataStakeHolder)):
            for y in range(0,len(dataStakeholderClasses)):
                if str(dataStakeholderClasses[y]) == dataStakeHolder[x]:
                    newService.is_a.append(restriction("hasATMStakeHolders",SOME,dataStakeholderClasses[y] ))
                    # newService.is_a.append(dataStakeholderClasses[y])
                    break

    dataCategory = parsed_json[str(i)]["atm"]["dataCategory"]
    if len(dataCategory) > 0:
        for x in range(0, len(dataCategory)):
            for y in range(0,len(dataCategoryClasses)):
                if str(dataCategoryClasses[y]) == dataCategory[x]:
                    newService.is_a.append(restriction("hasATMDataCategory",SOME,dataCategoryClasses[y]))
                    # newService.is_a.append(dataCategoryClasses[y])
                    break

    actCategory = parsed_json[str(i)]["atm"]["actCategory"]
    if len(actCategory) > 0:
        for x in range(0, len(actCategory)):
            for y in range(0,len(actCategoryClasses)):
                if str(actCategoryClasses[y]) == actCategory[x].replace(" ",""):
                    newService.is_a.append(restriction("hasATMActivityCategory",SOME,actCategoryClasses[y]))
                    # newService.is_a.append(actCategoryClasses[y])
                    break


    # RegistrationProcess
    if not parsed_json[str(i)]["registrationProcess"]["serviceTecnicalInterface"]:
        serviceTecnicalInterface = "No description"
    else:
        serviceTecnicalInterface = parsed_json[str(i)]["registrationProcess"]["serviceTecnicalInterface"][0]

    serviceDescription = parsed_json[str(i)]["registrationProcess"]["serviceDescription"]
    if len(serviceDescription) == 0:
        serviceDescription = "No Description"
    else:
        serviceDescription = serviceDescription[0]


    ANNOTATIONS[newService].add_annotation("comment", serviceDescription)

    newService.has_for_version = [version]
    newService.has_for_percentPrescribe = [percentPrescribe]
    newService.has_for_implementStatus = [implementStatus]
    newService.has_for_versionCategory = [versionCategory]
    newService.has_for_serviceTecnicalInterface = [serviceTecnicalInterface]


onto.save()
onto.sync_reasoner()

# print(to_owl(onto))

