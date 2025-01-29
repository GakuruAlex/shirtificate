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
        shirt_name.text((150, 200), font=font, text=f"{name} took CS50", fill='white')
        cs50_shirt.save('cs50_shirtificate.png')
        cs50_shirt.close()

class PDF(FPDF):
    def __init__(self):
        self.pdf = FPDF()
    

def main():
    shirtificate = Shirtificate()
    shirt = shirtificate.open_shirt("shirtificate.png")
    shirtificate.print_name_to_shirt(shirt, 'Alex Gakuru')

if __name__ =="__main__":
    main()