import os
import json

from selenium import webdriver

#get the current pip modules and save it to a dictionary
def getData():

    var = os.popen('pip3 list --format=json').read()
    varjson = json.loads(var)

    valdict = {}

    for v in varjson:

        valdict[v['name']] = v['version']

    #print(valdict.keys())
    #print(valdict.values())
    return valdict

#Using selenium to extract the latest pip modules as the user has
def moduleCheck():

    data = getData()
    newVersions = []#store the new versions of the modules
    olderVersions = []#store the older versions for comparision
    moduleNames = []#store the pip modules
    elements = []#storing the elements extracted via selenium
    moduleInfo = []#store olderVersions, newVersions, moduleNames as n*3 matrix

    baseUrl = "https://pypi.org/project/"
    driver = webdriver.Firefox('./')
    modulesNotFound = []#to remove those modules that don't exist or support is removed

    for mname in data.keys():

        try:

            driver.get(baseUrl + mname)
            nameTag = driver.find_element_by_class_name('package-header__name')#this element contains the module name and latest version
            elements.append(nameTag.text)

        except:

            print(mname + " is mostly discontinued!")
            modulesNotFound.append(mname)

    driver.quit()

    #remove the modules that are discontinued
    for i in range(len(modulesNotFound)):

        del data[modulesNotFound[i]]

    i = 0#to iterate through element list which contain the html tags

    for mname in data.keys():

        temp = elements[i].split(' ')#split the tag as the first part contains the module name, second contains the version

        #print('system m: {0} system v: {1} installed version: {2}'.format(mname, data[mname], temp[1]) )

        if temp[1] != data[mname]:#if the versions vary only then continue

            newVersions.append(temp[1])
            olderVersions.append(data[mname])
            moduleNames.append(mname)

        i += 1

    moduleInfo.append(moduleNames)
    moduleInfo.append(olderVersions)
    moduleInfo.append(newVersions)

    return moduleInfo
