# Date Created: 07/03/24
# Author: Shane Cooke
# Description: Class for parsing XML files
# Last Amended:
# Amendment Author:

import xml.etree.ElementTree as ET

# XMLParser Class
# Attempts to parse the given XML file
# Will throw error
class XMLParser:
    def __init__(self, xml_path):
        self.xml_path = xml_path

    def parse_xml(self):
        try:
            tree = ET.parse(self.xml_path)
            root = tree.getroot()
            
            parcels = []
            for entry in root.find('parcels').findall('Parcel'):
                name = entry.find('Receipient').find('Name').text

                street = entry.find('Receipient').find('Address').find('Street').text
                house = entry.find('Receipient').find('Address').find('HouseNumber').text
                postal = entry.find('Receipient').find('Address').find('PostalCode').text
                city = entry.find('Receipient').find('Address').find('City').text

                weight = float(entry.find('Weight').text)
                value = float(entry.find('Value').text)

                parcel = {
                    'Name': name,
                    'Street': street,
                    'House Number': house,
                    'Postal Code': postal,
                    'City': city,
                    'Weight': weight,
                    'Value': value
                }
                parcels.append(parcel)
                
            return parcels
        
        except FileNotFoundError:
            print('Error: File not found.')
            raise
        
        except ET.ParseError as e:
            print(f'Error Parsing XML file: {e}')
            raise