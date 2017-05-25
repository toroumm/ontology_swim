from hmac import new
from re import split

from owlready import *
import json, sys, types

onto_path.append("OWL/")

onto = Ontology("http://test.org/service_faa_onto.owl")


class Service(Thing):
    ontology = onto

class ServiceCategory(Service):
    ontology = onto

class ServiceCriticalLevel(Service):
    ontology = onto

class AtmServiceCategory(Service):
    ontology = onto

class MessagingMode(Service):
    ontology = onto

class LifeCicleStage(Service):
    ontology = onto

class InterfaceType(Service):
    ontology = onto

class Provider(Service):
    ontology = onto

#Creating Properties
class has_for_implementationDescrition(Property):
    ontology = onto
    domain = [Service]
    range = [str]

class has_for_implementationName(Property):
    ontology = onto
    domain = [Service]
    range = [str]

class has_for_securityDescription(Property):
    ontology = onto
    domain = [Service]
    range = [str]

json_string = open("JSON/faaServices.json").read()
parsed_json = json.loads(json_string)

serviceCategoryClasses = []
serviceCriticalLevelClasses = []
atmServiceCategoryClasses = []
messagingModeClasses = []
lifeCicleStageClasses = []
interfaceTypeClasses = []
serviceProviderNameClasses = []

for i in range(0, len(parsed_json.keys())):

    if len(parsed_json[str(i)]["header"]["serviceCategory"]) > 0:
        splited = parsed_json[str(i)]["header"]["serviceCategory"]

        if len(parsed_json[str(i)]["header"]["serviceCategory"]) == 1 :
            splited = parsed_json[str(i)]["header"]["serviceCategory"][0].split(',')

        for x in range(0, len(splited)):
            serviceCategory = splited[x].replace(" ", "")

            if serviceCategory not in serviceCategoryClasses:
                newClass = types.new_class(serviceCategory, (ServiceCategory,), kwds={"ontology": onto})
                serviceCategoryClasses.append(newClass)

    if len(parsed_json[str(i)]["header"]["serviceCriticalLevel"]) > 0:
        for x in range(0, len(parsed_json[str(i)]["header"]["serviceCriticalLevel"])):
            serviceCriticalLevel = parsed_json[str(i)]["header"]["serviceCriticalLevel"][x].replace(" ", "")

            if serviceCriticalLevel not in serviceCriticalLevelClasses:
                newClass = types.new_class(serviceCriticalLevel, (ServiceCriticalLevel,), kwds={"ontology": onto})
                serviceCriticalLevelClasses.append(newClass)

    if len(parsed_json[str(i)]["header"]["atmServiceCategory"]) > 0:

        splited = len(parsed_json[str(i)]["header"]["atmServiceCategory"])

        if len(parsed_json[str(i)]["header"]["atmServiceCategory"]) == 1:
            splited = parsed_json[str(i)]["header"]["atmServiceCategory"][0].split(',')

        for x in range(0,len(splited)):
            atmServiceCategory = splited[x]
            atmServiceCategory=atmServiceCategory.replace(" ", "")

            if atmServiceCategory not in atmServiceCategoryClasses:
                newClass = types.new_class(atmServiceCategory, (AtmServiceCategory,), kwds={"ontology": onto})
                atmServiceCategoryClasses.append(newClass)

    if len(parsed_json[str(i)]["header"]["messagingMode"]) > 0:
        for x in range(0, len(parsed_json[str(i)]["header"]["messagingMode"])):
            messagingMode = parsed_json[str(i)]["header"]["messagingMode"][x].replace(" ", "")

            if messagingMode not in messagingModeClasses:
                newClass = types.new_class(messagingMode, (MessagingMode,), kwds={"ontology": onto})
                # messagingModeList.append(messagingMode)
                messagingModeClasses.append(newClass)


    if len(parsed_json[str(i)]["header"]["lifeCicleStage"]) > 0:
        for x in range(0, len(parsed_json[str(i)]["header"]["lifeCicleStage"])):
            lifeCicleStage = parsed_json[str(i)]["header"]["lifeCicleStage"][x].replace(" ", "")

            if lifeCicleStage not in lifeCicleStageClasses:
                newClass = types.new_class(lifeCicleStage, (LifeCicleStage,), kwds={"ontology": onto})
                lifeCicleStageClasses.append(newClass)

    if len(parsed_json[str(i)]["header"]["interfaceType"]) > 0:
        for x in range(0, len(parsed_json[str(i)]["header"]["interfaceType"])):
            interfaceType = parsed_json[str(i)]["header"]["interfaceType"][x].replace(" ", "")

            if interfaceType not in interfaceTypeClasses:
                newClass = types.new_class(interfaceType, (InterfaceType,), kwds={"ontology": onto})
                interfaceTypeClasses.append(newClass)

    if len(parsed_json[str(i)]["provider"]["serviceProviderName"]) > 0:

        splited = parsed_json[str(i)]["provider"]["serviceProviderName"]

        if len(parsed_json[str(i)]["provider"]["serviceProviderName"]) == 1:
            splited = parsed_json[str(i)]["provider"]["serviceProviderName"][0].split(',')

        for x in range(0, len(splited)):
            serviceProviderName = splited[x].replace(" ", "")

            if lifeCicleStage not in serviceProviderNameClasses:
                newClass = types.new_class(serviceProviderName, (Provider,), kwds={"ontology": onto})
                serviceProviderNameClasses.append(newClass)


for i in range(0, len(parsed_json.keys())):

    serviceName = str(parsed_json[str(i)]["header"]["serviceName"][0]).replace(" ","")
    newService = Service(serviceName)

    #Implementation
    implementationDescrition = parsed_json[str(i)]["implementation"]["implementationDescrition"]
    if len(implementationDescrition) > 0 :
        implementationDescrition = implementationDescrition[0]

    newService.has_for_implementationDescrition = [implementationDescrition]

    implementationName = parsed_json[str(i)]["implementation"]["implementationName"]
    if len(implementationName) > 0:
        implementationName = implementationName[0]

    newService.has_for_implementationName = [implementationName]

    #Header
    serviceCategory = parsed_json[str(i)]["header"]["serviceCategory"]
    if len(serviceCategory) > 0:
        if len(serviceCategory) == 1:
            serviceCategory = serviceCategory[0].split(',')

        for x in range(0,len(serviceCategory)):
            for y in range(0,len(serviceCategoryClasses)):
                if str(serviceCategoryClasses[y]) == serviceCategory[x]:
                    newService.is_a.append(serviceCategoryClasses[y])
                    break

    serviceCriticalLevel = parsed_json[str(i)]["header"]["serviceCriticalLevel"]
    if len(serviceCriticalLevel) > 0:
        for x in range(0,len(serviceCriticalLevel)):
            for y in range(0,len(serviceCriticalLevelClasses)):
                if str(serviceCriticalLevelClasses[y]) == serviceCriticalLevel[x]:
                    newService.is_a.append(serviceCriticalLevelClasses[y])
                    break

    atmServiceCategory = parsed_json[str(i)]["header"]["atmServiceCategory"]
    if len(atmServiceCategory) > 0:
        if len(atmServiceCategory) == 1:
            atmServiceCategory = atmServiceCategory[0].split(',')

        for x in range(0,len(atmServiceCategory)):
            for y in range(0,len(atmServiceCategoryClasses)):
                if str(atmServiceCategoryClasses[y]) == atmServiceCategory[x]:
                    newService.is_a.append(atmServiceCategoryClasses[y])
                    break

    messagingMode = parsed_json[str(i)]["header"]["messagingMode"]
    if len(messagingMode) > 0:
        for x in range(0,len(messagingMode)):
            for y in range(0,len(messagingModeClasses)):
                if str(messagingModeClasses[y]) == messagingMode[x]:
                    newService.is_a.append(messagingModeClasses[y])
                    break

    lifeCicleStage = parsed_json[str(i)]["header"]["lifeCicleStage"]
    if len(lifeCicleStage) > 0:
        for x in range(0, len(lifeCicleStage)):
            for y in range(0, len(lifeCicleStageClasses)):
                if str(lifeCicleStageClasses[y]) == lifeCicleStage[x]:
                    newService.is_a.append(lifeCicleStageClasses[y])
                    break

    serviceVersion = parsed_json[str(i)]["header"]["serviceVersion"]

    interfaceType = parsed_json[str(i)]["header"]["interfaceType"]
    if len(interfaceType) > 0:
        for x in range(0, len(interfaceType)):
            for y in range(0, len(interfaceTypeClasses)):
                if str(interfaceTypeClasses[y]) == interfaceType[x]:
                    newService.is_a.append(interfaceTypeClasses[y])
                    break

    serviceDescription = parsed_json[str(i)]["header"]["serviceDescription"]
    if len(serviceDescription) > 0:
        serviceDescription = parsed_json[str(i)]["header"]["serviceDescription"][0]

    ANNOTATIONS[newService].add_annotation("comment", str(serviceDescription))

    #Security
    securityDescription = parsed_json[str(i)]["security"]["securityDescription"]
    if len(securityDescription) > 0:
        securityDescription = securityDescription[0]

    newService.has_for_securityDescription = [securityDescription]

    #Provider
    serviceProviderName = parsed_json[str(i)]["provider"]["serviceProviderName"]
    if len(serviceProviderName) > 0:
        if len(serviceProviderName) == 1:
            serviceProviderName = serviceProviderName[0].split(',')

        for x in range(0, len(serviceProviderName)):
            for y in range(0, len(serviceProviderNameClasses)):
                if str(serviceProviderNameClasses[y]) == serviceProviderName[x]:
                    newService.is_a.append(serviceProviderNameClasses[y])
                    break


onto.save()