import xml.etree.ElementTree as ET

# Sample XML data
data = '''<person>
    <name>John Doe</name>
    <age>30</age>
    <is_student>false</is_student>
    <courses>
        <course>Math</course>
        <course>Science</course>
        <course>History</course>
    </courses>
</person>'''

# Parse XML
root = ET.fromstring(data)
print(root.find('name').text)  # Output: John Doe

# Convert back to XML (for demonstration, not practical)
xml_output = ET.tostring(root, encoding='unicode')
print(xml_output)