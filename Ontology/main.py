from owlready import *
import json,sys,types

onto_path.append("OWL/")

onto = Ontology("http://test.org/service_onto.owl")

class Service(Thing):
    ontology = onto

class has_for_service(Property):
    ontology = onto
    domain = [Service]
    range = [str]

class ATM_Data_Category(Service):
    pass

class ATM_Data_Category(Service):
    pass

class ATM_Activity_Category(Service):
    ontology = onto

class ATM_Flight_Phases(Service):
    ontology = onto

class ATM_StakeHolders(Service):
    ontology = onto

class Regions(Service):
    pass

json_string = open("JSON/euro_services.json").read()
parsed_json = json.loads(json_string)


#Creating Subclasses
regionsList = []
flightPhasesList = []
dataStakeholderList = []
dataCategoryList = []
actCategoryList = []

for i in range(0,len(parsed_json.keys())):

    if len(parsed_json[str(i)]["atm"]["regions"]) > 0:

        for x in range(0,len(parsed_json[str(i)]["atm"]["regions"])):

            region = parsed_json[str(i)]["atm"]["regions"][x]
            region=region.replace(" ", "")

            if region not in regionsList:
                regionsList.append(region)


    if len(parsed_json[str(i)]["atm"]["flightPhases"]) > 0:

        for x in range(0,len(parsed_json[str(i)]["atm"]["flightPhases"])):

            flightPhase = parsed_json[str(i)]["atm"]["flightPhases"][x]
            flightPhase=flightPhase.replace(" ", "")

            if flightPhase not in flightPhasesList:
                flightPhasesList.append(flightPhase)


    if len(parsed_json[str(i)]["atm"]["dataStakeholder"]) > 0:

        for x in range(0,len(parsed_json[str(i)]["atm"]["dataStakeholder"])):

            dataStakeHolder = parsed_json[str(i)]["atm"]["dataStakeholder"][x]
            dataStakeHolder=dataStakeHolder.replace(" ", "")

            if dataStakeHolder not in dataStakeholderList:
                dataStakeholderList.append(dataStakeHolder)


    if len(parsed_json[str(i)]["atm"]["dataCategory"]) > 0:

        for x in range(0,len(parsed_json[str(i)]["atm"]["dataCategory"])):

            dataCategory = parsed_json[str(i)]["atm"]["dataCategory"][x]
            dataCategory=dataCategory.replace(" ", "")

            if dataCategory not in dataCategoryList:
                dataCategoryList.append(dataCategory)


    if len(parsed_json[str(i)]["atm"]["actCategory"]) > 0:

        for x in range(0,len(parsed_json[str(i)]["atm"]["actCategory"])):

            actCategory = parsed_json[str(i)]["atm"]["actCategory"][x]
            actCategory=actCategory.replace(" ", "")

            if actCategory not in actCategoryList:
                actCategoryList.append(actCategory)


regionClasses = []
flightPhaseClasses = []
dataStakeholderClasses = []
dataCategoryClasses = []
actCategoryClasses = []

for i in range(0,len(regionsList)):
    newClass = types.new_class(regionsList[i], (Regions,), kwds={"ontology": onto})
    regionClasses.append(newClass)

for i in range(0,len(flightPhasesList)):
    newClass = types.new_class(flightPhasesList[i], (ATM_Flight_Phases,), kwds={"ontology": onto})
    flightPhaseClasses.append(newClass)

for i in range(0,len(dataStakeholderList)):
    newClass = types.new_class(dataStakeholderList[i], (ATM_StakeHolders,), kwds={"ontology": onto})
    dataStakeholderClasses.append(newClass)

for i in range(0, len(dataCategoryList)):
    newClass = types.new_class(dataCategoryList[i], (ATM_Data_Category,), kwds={"ontology": onto})
    dataCategoryClasses.append(newClass)

for i in range(0, len(actCategoryList)):
    newClass = types.new_class(actCategoryList[i], (ATM_Activity_Category,), kwds={"ontology": onto})
    actCategoryClasses.append(newClass)

#Creating Instances
for i in range(0,len(parsed_json.keys())):

    regionsList = []
    flightPhasesList = []
    dataStakeholderList = []
    dataCategoryList = []
    actCategoryList = []

    #header
    percentPrescribe = parsed_json[str(i)]["header"]["percentPrescribe"]
    nameService = parsed_json[str(i)]["header"]["nameService"].replace(" ", "")
    # version = parsed_json[str(i)]["header"]["version"]
    implementStatus = parsed_json[str(i)]["header"]["implementStatus"]
    versionCategory = parsed_json[str(i)]["header"]["versionCategory"]

    # ATM
    if len(parsed_json[str(i)]["atm"]["regions"]) > 0:
        for x in range(0, len(parsed_json[str(i)]["atm"]["regions"])):
            region = parsed_json[str(i)]["atm"]["regions"][x].replace(" ", "")
            regionsList.append(region)

    if len(parsed_json[str(i)]["atm"]["flightPhases"]) > 0:
        for x in range(0, len(parsed_json[str(i)]["atm"]["flightPhases"])):
            flightPhase = parsed_json[str(i)]["atm"]["flightPhases"][x].replace(" ", "")
            flightPhasesList.append(flightPhase)

    if len(parsed_json[str(i)]["atm"]["dataStakeholder"]) > 0:
        for x in range(0, len(parsed_json[str(i)]["atm"]["dataStakeholder"])):
            dataStakeHolder = parsed_json[str(i)]["atm"]["dataStakeholder"][x].replace(" ", "")
            dataStakeholderList.append(dataStakeHolder)

    if len(parsed_json[str(i)]["atm"]["dataCategory"]) > 0:
        for x in range(0, len(parsed_json[str(i)]["atm"]["dataCategory"])):
            dataCategory = parsed_json[str(i)]["atm"]["dataCategory"][x].replace(" ", "")
            dataCategoryList.append(dataCategory)

    if len(parsed_json[str(i)]["atm"]["actCategory"]) > 0:
        for x in range(0, len(parsed_json[str(i)]["atm"]["actCategory"])):
            actCategory = parsed_json[str(i)]["atm"]["actCategory"][x].replace(" ", "")
            actCategoryList.append(actCategory)

    # flightPhases
    # dataStakeholder
    # dataCategory
    # actCategory

    # RegistrationProcess
    serviceTecnicalInterface = parsed_json[str(i)]["registrationProcess"]["serviceTecnicalInterface"]
    serviceDescription = str(parsed_json[str(i)]["registrationProcess"]["serviceDescription"])

    newService = Service(nameService)

    for y in range(0,len(regionsList)):
        for x in range(0,len(regionClasses)):
            if str(regionClasses[x]) == (regionsList[y]):
                newService.is_a.append(regionClasses[x])

    for y in range(0, len(flightPhasesList)):
        for x in range(0, len(flightPhaseClasses)):
            if str(flightPhaseClasses[x]) == (flightPhasesList[y]):
                newService.is_a.append(flightPhaseClasses[x])

    for y in range(0, len(dataStakeholderList)):
        for x in range(0, len(dataStakeholderClasses)):
            if str(dataStakeholderClasses[x]) == (dataStakeholderList[y]):
                newService.is_a.append(dataStakeholderClasses[x])

    for y in range(0, len(dataCategoryList)):
        for x in range(0, len(dataCategoryClasses)):
            if str(dataCategoryClasses[x]) == (dataCategoryList[y]):
                newService.is_a.append(dataCategoryClasses[x])

    for y in range(0, len(actCategoryList)):
        for x in range(0, len(dataCategoryClasses)):
            if str(actCategoryClasses[x]) == (actCategoryList[y]):
                newService.is_a.append(actCategoryClasses[x])



    if len(serviceDescription) == 0:
        serviceDescription = "None"

    ANNOTATIONS[newService].add_annotation("comment",serviceDescription)


#
#     # test_service.has_for_service = ['Filipe Santiago de Queiroz'+str(x)]

onto.save()
# print(to_owl(onto))

