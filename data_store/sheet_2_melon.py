
import openpyxl
from PIL import Image

book = openpyxl.load_workbook("./melon_top_xls.xlsx")
sheet = book.create_sheet()
sheet.title = "Mamamoo"
sheet2 = book.worksheets[1]

imgFile = './images/mamamoo.jpg'
img = Image.open(imgFile)
new_img = img.resize((500, 300))
new_img.save('mmm.jpg')
img2 = openpyxl.drawing.image.Image('mmm.jpg')
sheet2.add_image(img2, 'A1')

book.save("./melon_top_xls.xlsx")