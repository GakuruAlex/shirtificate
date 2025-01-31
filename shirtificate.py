from fpdf import FPDF
from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.image("./shirtificate.png", 10, 70, 190)
        self.set_font(family="Times",  size=48, style='B')
        self.cell(0, 57, "CS50 Shirtificate", align="C")
        self.ln(20)

    def shirt(self, name: str):
        pdf = PDF()
        pdf.add_page(orientation="portrait", format="a4")
        pdf.set_font(family = "Times", size = 30, style='B')
        pdf.set_text_color(255,255,255)
        pdf.cell(0, 213, f"{name} took CS50", align="C")
        pdf.output("shirtificate.pdf")

def main():
    pdf = PDF()
    pdf.shirt(input("Name: "))

if __name__ == "__main__":
    main()