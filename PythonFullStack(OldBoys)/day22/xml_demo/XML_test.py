# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author:     Ran_hj
# Datetime:   2022-08-15 9:44
# className:  XML_test.py

# 调用xml_test文件

import xml.etree.ElementTree as ET

tree = ET.parse("xml_test")
root = tree.getroot()
print(root.tag)

# 遍历xml文档
for child in root:
    print(child.tag, child.attrib)
    for i in child:
        print(i.tag, i.text)

# 只遍历year 节点
for node in root.iter('year'):
    print(node.tag, node.text)
# ---------------------------------------

import xml.etree.ElementTree as ET

tree = ET.parse("xml_test")
root = tree.getroot()

# 修改
for node in root.iter('year'):
    new_year = int(node.text) + 1
    node.text = str(new_year)
    node.set("updated", "yes")

tree.write("xml_test")

# 删除node
for country in root.findall('country'):
    rank = int(country.find('rank').text)
    if rank > 50:
        root.remove(country)

tree.write('output.xml')