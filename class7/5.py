"""
5. Dealing with Namespaces

Namespaces in XML help to differentiate between conflicting element names. 

5a. Load the show_version.xml file (originally from a Cisco NX-OS device) using the etree.fromstring() method. Note this XML document, unlike the previous documents, contains the document encoding information. Because the document encoding is at the top of the file, you will need to read the file using "rb" mode (the "b" signifies binary mode). Print out the the namespace map of this XML object. You can accomplish this by using the .nsmap attribute of your XML object.


5b. Similar to earlier exercises, use the find() method to access the text of the "proc_board_id" element (serial number). As this XML object contains namespace data, you will need to use the {*} namespace wildcard in the find() method. Your find call should look as follows:

find(".//{*}proc_board_id")

The {*} is a namespace wildcard and says to match ALL namespaces.
"""

from lxml import etree

with open("show_version.xml", "rb") as file:
    show_version = etree.fromstring(file.read())


print("5a")
print("")

print(show_version.nsmap)

print("")
print("5b")
print("")
print(show_version.find(".//{*}proc_board_id").text)
