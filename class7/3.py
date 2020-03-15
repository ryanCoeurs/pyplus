"""
3. xmltodict: single vs multiple elements

3a. Open the following two XML files: show_security_zones.xml and show_security_zones_single_trust.xml. Use a generic function that accepts an argument "filename" to open and read a file. Inside this function, use xmltodict to parse the contents of the file. Your function should return the xmltodict data structure. Using this function, create two variables to store the xmltodict data structure from the two files.


3b. Compare the Python "type" of the elements at ['zones-information']['zones-security']. What is the difference between the two data types? Why?


3c. Optional - create a second function that uses xmltodict to read and parse a filename that you pass in. This function should support a "force_list" argument that is passed to xmltodict.parse(). Reminder, the force_list argument of xmltodict takes a dictionary where the dictionary key-name is the XML element that is required to be a list. For example:

force_list={"zones-security": True}

Use this new function to parse the "show_security_zones_single_trust.xml". Verify the Python data type is now a list for the ['zones-information']['zones-security'] element.

"""
import xmltodict
from pprint import pprint

def process_xml(filename):
    with open(filename) as file:
        dict = xmltodict.parse(file.read())
        return dict


def process_xml_force_list(filename):
    with open(filename) as file:
        dict = xmltodict.parse(file.read(), force_list=True)
        return dict

print("3a")
print("")
show_security_zones = process_xml("show_security_zones.xml")
show_security_zones_single_trust = process_xml("show_security_zones_single_trust.xml")
pprint(show_security_zones)
pprint(show_security_zones_single_trust)

print("")
print("3b")
print("")
print(type(show_security_zones['zones-information']['zones-security']))
print(type(show_security_zones_single_trust['zones-information']['zones-security']))
print("By default xmltodict only creates a list when there are multiple elements")

print("")
print("3c")
print("")

show_security_zones = process_xml_force_list("show_security_zones.xml")
show_security_zones_single_trust = process_xml_force_list("show_security_zones_single_trust.xml")

print(type(show_security_zones['zones-information'][0]['zones-security']))
print(type(show_security_zones_single_trust['zones-information'][0]['zones-security']))
