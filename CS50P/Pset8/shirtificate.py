from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font("helvetica", "B", 48)
        self.cell(0, 60, "CS50 Shirtificate", align="C")
        self.image("shirtificate.png", 10, 70, 190)

def main():
    name = input("Name: ")
    shirt(name)

def shirt(name):
    pdf = PDF()
    pdf.add_page()
    pdf.set_font("helvetica", "", 24)
    pdf.set_text_color(255, 255, 255)

    pdf.set_xy(0, 140)
    pdf.cell(210, 10, f"{name} took CS50", align="C")

    pdf.output("shirtificate1.pdf")

if __name__ == "__main__":
    main()

