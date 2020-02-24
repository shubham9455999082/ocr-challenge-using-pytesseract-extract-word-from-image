from PyPDF2 import PdfFileReader
##def ocr_core(filename):
    ##pdf = PdfFileReader(filename)


#with open("C:\Users\Shubham\Desktop\image pdf reading\44_21.pdf", 'rb') as file:
    #pdf = PdfFileReader(file)
    ##page = pdf.getPage(5)
    ##text=page.extractText()
    ##print(text)



    #retrun text
    #print(page.extractText())
#import os.path
#path = os.path.abspath(os.path.dirname(__file__))
#print(ocr_core(os.path.join("C:\\Users\\Shubham\\Desktop\\image pdf reading\\44_21.pdf")))





import PyPDF2
import re
import glob

#your full path of directory
def ocr_core(filename):
    mypath='C:\\Users\\Shubham\\Desktop\\bijli ocr\\test_data\\test data'
    for file in glob.glob(mypath + "/*.pdf"):
         print(file)
         if file.endswith('.pdf'):
            fileReader = PyPDF2.PdfFileReader(open(file, "rb"))
            count = 0
            count = fileReader.numPages
            while count >= 0:
                count -= 1
                pageObj = fileReader.getPage(count)
                text = pageObj.extractText()
                print(text)
import os.path
#path = os.path.abspath(os.path.dirname(__file__))
print(ocr_core(os.path.join('C:\\Users\\Shubham\\Desktop\\bijli ocr\\test_data\\test data')))

