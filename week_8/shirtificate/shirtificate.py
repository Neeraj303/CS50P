from fpdf import FPDF, TextMode

class PDF(FPDF):

    def __init__(self, name):
        super().__init__()
        self.name = name

    def header(self):
        # Below to ensure the coorindates of the pdf
        #self.set_line_width(0.5)
        #self.set_draw_color(r=255, g=128, b=0)
        #self.line(x1=105, y1=0, x2=105, y2=297)
        self.set_font("Times", "BI", 44)
        self.cell(0,50, f"CS50 Shirtificate", align="C", center=True, new_x="LMARGIN", new_y="TOP")
        self.image("shirtificate.png", x=10, y=60, w=190, h=197)

    def footer(self):
        self.set_y(-170)
        self.set_font("Times", "BI", 28)
        self.set_text_color(255,255,255)
        self.cell(0,0, f"{self.name} took CS50", align="C")



def main():
    name = input("Name: ")
    pdf = PDF(name)
    pdf.output("shirtificate.pdf")

if __name__ == "__main__":
    main()

