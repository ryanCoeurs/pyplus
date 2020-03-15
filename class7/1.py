"""
1a. Using the show_security_zones.xml file, read the file contents and parse the file using etree.fromstring(). Print out the newly created XML variable and also print out the variable's type. Your output should look similar to the following: 

<Element zones-information at 0x7f3271194b48>
<class 'lxml.etree._Element'>

1b. Using your XML variable from exercise 1a, print out the entire XML tree in a readable format (ensure that the output string is a unicode string).


1c. Print out the root element tag name (this tag should have a value of "zones-information"). Print the number of child elements of the root element (you can retrieve this using the len() function).


1d. Using both direct indices and the getchildren() method, obtain the first child element and print its tag name. 


1e. Create a variable named "trust_zone". Assign this variable to be the first "zones-security" element in the XML tree. Access this newly created variable and print out the text of the "zones-security-zonename" child.


1f. Iterate through all of the child elements of the "trust_zone" variable. Print out the tag name for each child element.

"""

from lxml import etree

#security_zones_tree = ""
with open("show_security_zones.xml") as file:
    security_zones_tree = etree.fromstring(file.read())


print("1a")
print("")
print(security_zones_tree)
print(type(security_zones_tree))

print("")
print("1b")
print("")
print(etree.tostring(security_zones_tree).decode())

print("")
print("1c")
print("")
print(security_zones_tree.tag)
print(len(security_zones_tree))

print("")
print("1d")
print("")
print(security_zones_tree[0].tag)
print(security_zones_tree.getchildren()[0].tag)

print("")
print("1e")
print("")
trust_zone = security_zones_tree[0]
print(trust_zone.find('zones-security-zonename').text)

print("")
print("1f")
print("")
for child in trust_zone:
    print(child.tag)
