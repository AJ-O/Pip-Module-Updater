import os
import json

from selenium import webdriver

def getData():

    var = os.popen('pip3 list --format=json').read()
    varjson = json.loads(var)

    valdict = {}

    for v in varjson:

        valdict[v['name']] = v['version']

    #print(valdict.keys())
    #print(valdict.values())
    return valdict

def moduleCheck():

    data = getData()
    newVersions = []
    olderVersions = []
    moduleNames = []
    elements = []
    moduleInfo = []

    baseUrl = "https://pypi.org/project/"
    driver = webdriver.Firefox('./')
    modulesNotFound = []

    for mname in data.keys():

        try:

            driver.get(baseUrl + mname)
            nameTag = driver.find_element_by_class_name('package-header__name')
            elements.append(nameTag.text)

        except:

            print(mname + " is mostly discontinued!")
            modulesNotFound.append(mname)

    driver.quit()

    for i in range(len(modulesNotFound)):

        del data[modulesNotFound[i]]

    i = 0

    for mname in data.keys():

        temp = elements[i].split(' ')

        #print('system m: {0} system v: {1} installed version: {2}'.format(mname, data[mname], temp[1]) )

        if temp[1] != data[mname]:

            newVersions.append(temp[1])
            olderVersions.append(data[mname])
            moduleNames.append(mname)

        i += 1

    moduleInfo.append(moduleNames)
    moduleInfo.append(olderVersions)
    moduleInfo.append(newVersions)

    return moduleInfo
