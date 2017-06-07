from hmac import new
from re import split

import json, sys, types , csv

json_string = open("JSON/faaServices.json").read()
parsed_json = json.loads(json_string)

with open('Output/faa_services.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter='|',quotechar='|', quoting=csv.QUOTE_MINIMAL)
    # writer.writerow(['Service_Name','Version','Service_Desc','Security_Desc','Impl_Name','Impl_Desc','Service_Category','Service_Critical_Lvl','Atm_Service_Category','Messaging_Mode','LifeCicleStage','InterfaceType','ServiceProviderName'])

    writer.writerow(['Service_Name', 'Version','Service_Category','Atm_Service_Category','Messaging_Mode','LifeCicleStage','InterfaceType','ServiceProviderName'])


    for i in range(0, len(parsed_json.keys())):

        flag = 0

        serviceName = str(parsed_json[str(i)]["header"]["serviceName"][0]).replace(" ","")

        if len(parsed_json[str(i)]["header"]["serviceVersion"]) > 0:
            serviceVersion = parsed_json[str(i)]["header"]["serviceVersion"][0]
        else:
            serviceVersion = ""


        if len(parsed_json[str(i)]["header"]["serviceDescription"]) > 0:
            serviceDescription = parsed_json[str(i)]["header"]["serviceDescription"][0]
        else:
            serviceDescription = ""

        # Security
        securityDescription = parsed_json[str(i)]["security"]["securityDescription"]
        if len(securityDescription) > 0:
            securityDescription = securityDescription[0]

        #Implementation
        implementationDescrition = parsed_json[str(i)]["implementation"]["implementationDescrition"]
        if len(implementationDescrition) > 0 :
            implementationDescrition = implementationDescrition[0]

        implementationName = parsed_json[str(i)]["implementation"]["implementationName"]
        if len(implementationName) > 0:
            implementationName = implementationName[0]

        #Header
        if len(parsed_json[str(i)]["header"]["serviceCategory"]) > 0:
            serviceCategory = parsed_json[str(i)]["header"]["serviceCategory"][0]

        if len(parsed_json[str(i)]["header"]["atmServiceCategory"]) > 0:
            atmServiceCategory = parsed_json[str(i)]["header"]["atmServiceCategory"][0]

        if len(parsed_json[str(i)]["header"]["messagingMode"]) > 0:
            messagingMode = parsed_json[str(i)]["header"]["messagingMode"][0]
        else:
            messagingMode = ""

        if len(parsed_json[str(i)]["header"]["lifeCicleStage"]) > 0:
            lifeCicleStage = parsed_json[str(i)]["header"]["lifeCicleStage"][0]
        else:
            lifeCicleStage = ""

        if len(parsed_json[str(i)]["header"]["interfaceType"]) > 0:
            interfaceType = parsed_json[str(i)]["header"]["interfaceType"][0]
        else:
            interfaceType = ""

        # Provider
        if len(parsed_json[str(i)]["provider"]["serviceProviderName"]) > 0:
            serviceProviderName = parsed_json[str(i)]["provider"]["serviceProviderName"][0].split(",")[0].replace(" ","")
        else:
            serviceProviderName = ""

        if len(parsed_json[str(i)]["header"]["serviceCriticalLevel"]) > 0:
            serviceCriticalLevel = parsed_json[str(i)]["header"]["serviceCriticalLevel"][0]
        else:
            serviceCriticalLevel = ""

        if len(parsed_json[str(i)]["header"]["atmServiceCategory"]) > 0:
            atmServiceCategory = parsed_json[str(i)]["header"]["atmServiceCategory"][0].split(",")[0].replace(" ","")

        if len(parsed_json[str(i)]["header"]["serviceCategory"]) > 0:
            splited = parsed_json[str(i)]["header"]["serviceCategory"][0].split(',')

            if len(splited) == 1:
                serviceCategory = splited[0].replace(" ","")
                flag = 1
            else:
                for x in range(0,len(splited)):
                    serviceCategory = splited[x].replace(" ","")
                    writer.writerow([serviceName, serviceVersion, serviceCategory, atmServiceCategory, messagingMode,
                                     lifeCicleStage, interfaceType, serviceProviderName])
                    flag =0




        if len(parsed_json[str(i)]["header"]["atmServiceCategory"]) > 0:
            splited = parsed_json[str(i)]["header"]["atmServiceCategory"][0].split(",")
            if len(splited) == 1:
                atmServiceCategory = splited[0].replace(" ","")
                flag = 1
            else:
                for x in range(0,len(splited)):
                    atmServiceCategory = splited[x].replace(" ","")
                    writer.writerow([serviceName, serviceVersion, serviceCategory, atmServiceCategory, messagingMode,
                                     lifeCicleStage, interfaceType, serviceProviderName])
                    flag = 0

        if len(parsed_json[str(i)]["provider"]["serviceProviderName"]) > 0:
            splited = parsed_json[str(i)]["provider"]["serviceProviderName"][0].split(",")
            if len(splited) == 1:
                serviceProviderName = splited[0].replace(" ", "")
                flag = 1
            else:
                for x in range(0, len(splited)):
                    serviceProviderName = splited[x].replace(" ", "")
                    writer.writerow([serviceName, serviceVersion, serviceCategory, atmServiceCategory, messagingMode,
                                     lifeCicleStage, interfaceType, serviceProviderName])
                    flag = 0





        # print(serviceName,serviceCategory)
        # writer.writerow([serviceName,serviceVersion,serviceDescription,securityDescription,implementationName,implementationDescrition,
        #                  serviceCategory,serviceCriticalLevel,atmServiceCategory,messagingMode,lifeCicleStage,interfaceType,serviceProviderName])

        if flag == 1:
            writer.writerow([serviceName, serviceVersion,serviceCategory,atmServiceCategory,messagingMode,lifeCicleStage,interfaceType,serviceProviderName])