# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author:     Ran_hj
# Datetime:   2022-08-15 10:00
# className:  newXML.py
# 新建XML
import xml.etree.ElementTree as ET

new_xml = ET.Element("namelist")
name = ET.SubElement(new_xml, "name", attrib={"enrolled": "yes"})
age = ET.SubElement(name, "age", attrib={"checked": "no"})
sex = ET.SubElement(name, "sex")
age.text = '33'
# sex.text = '男'
name2 = ET.SubElement(new_xml, "name", attrib={"enrolled": "no"})
age = ET.SubElement(name2, "age")
age.text = '19'
# sex.text = '女'

et = ET.ElementTree(new_xml)  # 生成文档对象
et.write("test.xml", encoding="utf-8", xml_declaration=True)

ET.dump(new_xml)  # 打印生成的格式
