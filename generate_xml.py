import xml.etree.ElementTree as ET
import pandas as pd

df = pd.read_parquet("./retaildbt/feeds/wrestlingshoes.parquet")

root = ET.Element("products")

for _, row in df.iterrows():
    item = ET.SubElement(root, "item")
    for col in df.columns:
        ET.SubElement(item, col).text = str(row[col])

tree = ET.ElementTree(root)
tree.write("products.xml", encoding="utf-8", xml_declaration=True)
