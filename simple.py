from uspto.peds.client import UsptoPatentExaminationDataSystemClient
# import json as JS
# from json import loads

# from dicttoxml import dicttoxml

# import xml.etree.ElementTree as ET



client = UsptoPatentExaminationDataSystemClient()

expression = 'firstNamedApplicant:(nasa)'
result     = client.search(expression)

# xml = dicttoxml(loads(result))

# print(xml)

print(result)