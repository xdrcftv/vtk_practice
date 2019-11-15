import os
import xml.etree.ElementTree as ET


PathXml = 'C:/INFINITT/BNCT_TEMP'

whole_files = os.listdir(PathXml)
list(whole_files)
xml_file = os.path.join(PathXml, whole_files[0])
xml_doc = ET.parse(xml_file)

root = xml_doc.getroot()

CT_image = root.find("CTImage")

CT_dir = []
CT_slide = []

for child in CT_image:
    CTD = CT_image.findtext(child.tag)
    CT_dir.append(CTD)
    CT_slide.append(dcm.dcmread(CTD))

Ref_CT = CT_slide[0]

ConstPixelDims= (int(Ref_CT.Columns), int(Ref_CT.Rows), len(CT_slide))

ConstPixelSpacing = (float(Ref_CT.PixelSpacing[1]),float(Ref_CT.PixelSpacing[0]), float(Ref_CT.SliceThickness))

