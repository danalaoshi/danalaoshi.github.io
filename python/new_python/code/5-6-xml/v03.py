import xml.etree.ElementTree as et


tree = et.parse(r'to_edit.xml')

root = tree.getroot()

for e in root.iter('Name'):
    print(e.text)


for stu in root.iter('Student'):
    name = stu.find('Name')

    if name != None:
        name.set( 'test', name.text * 2)

stu = root.find('Student')

e = et.Element('ADDer')
e.attrib = {'a':'b'}
e.text = '我加的'

stu.append(e)

tree.write('to_edit.xml')
