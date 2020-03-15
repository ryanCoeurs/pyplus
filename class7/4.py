"""
4. Use lxml to find() elements in an XML tree

4a. Use the find() method to retrieve the first "zones-security" element. Print out the tag of this element and of all its children elements. Your output should be similar to the following:

Find tag of the first zones-security element
--------------------
zones-security

Find tag of all child elements of the first zones-security element
--------------------
zones-security-zonename
zones-security-send-reset
zones-security-policy-configurable
zones-security-interfaces-bound
zones-security-interfaces


4b. Use the find() method to find the first "zones-security-zonename". Print out the zone name for that element (the "text" of that element).


4c. Use the findall() method to find all occurrences of "zones-security". For each of these security zones, print out the security zone name ("zones-security-zonename", the text of that element).

"""

from lxml import etree

with open("show_security_zones.xml") as file:
    security_zones_tree = etree.fromstring(file.read())


print("4a")
print("")
print("""
Find tag of the first zones-security element
--------------------
zones-security

Find tag of all child elements of the first zones-security element
--------------------
""")

for child in security_zones_tree.find('zones-security'):
    print(child.tag)

print("")
print("4b")
print("")
print(security_zones_tree.find('.//zones-security-zonename').text)


print("")
print("4c")
print("")
for child in security_zones_tree.findall('.//zones-security-zonename'):
    print(child.text)
