from bs4 import BeautifulSoup
import uuid

inner_tags = ["Food_Code", "Display_Name", "Portion_Default", "Portion_Amount", 
				"Solid_Fats", "Added_Sugars", "Calories", "Saturated_Fats"]

# Display the delimiter used for separating columns of the resulting row. The delimiter
# should not be present in the data, otherwise the ingestion into database will fail.
delimiter = ":"

# Open XML document and read the entire file into memory. This is okay bacause our files
# are small. For large files, we should probably process line-by-line.
fname = open("Food_Display_Table.xml", "r"). read()

# Create a 'soup' object. This object has intelligence to find tags etc
soup = BeautifulSoup(fname, "xml")

# Get all rows as a list.
xml_items = soup.find_all("Food_Display_Row")

# Now loop through the list and find the contents of all the inner tags and write to 
# an output file.
with open("food.csv", "w") as outfile:
	for xi in xml_items:
		row_items = [str(uuid.uuid4())]
		for itg in inner_tags:
			tag = xi.find(itg)
			row_items.append(tag.text)

		row = delimiter.join(row_items)
		outfile.write("%s\n" % row)