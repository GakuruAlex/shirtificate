from PIL import Image, ImageDraw, ImageFont
from sys import exit
from fpdf import FPDF
class Shirtificate():
    def __init__(self):
        pass
    def open_shirt(self, cs50_shirt: str):
        try:
            cs50_shirt = Image.open(cs50_shirt)
        except FileNotFoundError:
            exit(f"{cs50_shirt} doesn't exist!")
        else:
            return cs50_shirt
    def print_name_to_shirt(self, cs50_shirt: Image, name: str):
        font = ImageFont.truetype("./OpenSans-Regular.ttf", 30)
        shirt_name = ImageDraw.Draw(cs50_shirt)
        shirt_name.text((150, 200), font=font, text=f"{name} took CS50", fill='white', align='left')
        cs50_shirt.save('cs50_shirtificate.png')
        cs50_shirt.close()

class PDF(FPDF):
    def __init__(self):
        self.pdf = FPDF(orientation='P', unit='mm', format='A4')
        self.pdf.add_page()
        self.pdf.set_font(family='Times', size= 50,style='B')
    def create_pdf(self, shirt):
        self.pdf.set_margin(20)
        self.pdf.cell( text="CS50 Shirtificate", align='C', new_x='LMARGIN', new_y='NEXT', center=True)
        self.pdf.set_y(50)
        self.pdf.image(name= shirt, h= 220, w = 170 )
        self.pdf.output('shirtificate.pdf')


def main():
    shirtificate = Shirtificate()
    shirt = shirtificate.open_shirt("shirtificate.png")
    shirtificate.print_name_to_shirt(shirt, input("Name: "))
    pdf = PDF()
    pdf.create_pdf(shirt= './cs50_shirtificate.png')


if __name__ =="__main__":
    main()