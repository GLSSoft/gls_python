from platform import node
from tracemalloc import start
from tqdm import tqdm
from wadiso import Model as activemodel

from tqdm import tqdm
import time

from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        # Logo
        self.image('C:\\Users\\adrian\\OneDrive - EOH\\Work\\ReportGenerator\\gls_fc-water-on-transparent-rgb.png', x=180,y=10, w=10, h=10)
        # Arial bold 15
        self.set_font('Arial', 'B', 16)
        # Move to the right
        #self.cell(40)
        # Title
        self.cell(0, 10, 'GLS Demo Model Report', 1, 1, 'L')
        # Line break
        self.ln(20)

    # Page footer
    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        # Arial italic 8
        self.set_font('Arial', 'I', 8)
        # Page number
        self.cell(0, 10, 'Page: ' + str(self.page_no()), 0, 0, 'C')

    def chapter_title(self, num, label):
        # Arial 12
        self.set_font('Arial', '', 12)
        # Background color
        self.set_fill_color(200, 220, 255)
        # Title
        self.cell(0, 6, 'Chapter %d : %s' % (num, label), 0, 1, 'L', 1)
        # Line break
        self.ln(4)

    def chapter_body(self, name):
        # Read text file
        with open(name, 'rb') as fh:
            txt = fh.read().decode('latin-1')
        # Times 12
        self.set_font('Arial', '', 12)
        # Output justified text
        self.multi_cell(0, 5, txt)
        # Line break
        self.ln()
        # Mention in italics
        self.set_font('', 'I')

    def print_chapter(self, num, title, name):
        self.add_page()
        self.chapter_title(num, title)
        self.chapter_body(name)
        
    def add_figurenumber(self, title):
        # Line break
        self.cell(0, 6, title, 0, 1, 'R', 1)
        self.ln(2)
           
    
def PDFReport():         
    startTime = time.time()    
       
    pdf = PDF('P', 'mm', 'A4')
    
    pdf.set_title("Model Report")
    
    pdf.set_author("GLS")
    
    pdf.print_chapter(1, 'Section 1', 'C:\\Users\\adrian\\OneDrive - EOH\\Work\\ReportGenerator\\section1.txt')
    
    pdf.image("C:\\Users\\adrian\\OneDrive - EOH\\Work\\ReportGenerator\\Figure_1.png", w = 160 )
    
    pdf.add_figurenumber("Figure 1 - A Chart")
    
    pdf.print_chapter(2, 'Section 2', 'C:\\Users\\adrian\\OneDrive - EOH\\Work\\ReportGenerator\\section2.txt')
    
    pdf.image("C:\\Users\\adrian\\OneDrive - EOH\\Work\\ReportGenerator\\Figure_2.png", w = 120 )
    
    pdf.add_figurenumber("Figure 2 - The Same Chart Again")
    
    pdf.output('C:\\Users\\adrian\\OneDrive - EOH\\Work\\ReportGenerator\\Report.pdf', 'F')    
    
    print(str(time.time() - startTime))  
    
    
if __name__ == "__main__":
    PDFReport()  