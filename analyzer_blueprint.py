import os 
from pypdf import PdfReader

class DocumentAnalyzer :

    llm_model = "llama3"

    def __init__(self,file_path):
        self.file_path = file_path
        self.raw_text = ""
    
    def __str__(self):
        return f"[System] landed '{self.file_path}' targeting '{self.llm_model}' model."
    
    def read_document(self) :
        try:
            with open(self.file_path , 'r' , encoding='utf-8') as file :
                self.raw_text = file.read()
                print("Successfully , Document Read Into Memory")
                print(f"Extracted '{len(self.raw_text)}' characters.")
        
        except FileNotFoundError :
            print(f"Error Could Not find '{self.file_path}' .")

    def read_pdf(self):
        try:
            reader = PdfReader(self.file_path)
            extracted_text = " "

            num_pages = len(reader.pages)
            print(f"Extracted '{num_pages}' pages . Extracting Text ...")

            for page in reader.pages :
                self.raw_text += page.extract_text() + "\n"
                print(f"Successfull Extracted '{len(self.raw_text)}' characters .")

        except FileNotFoundError :
            print(f"Error Could Not find '{self.file_path}' .")
        except Exception as e :
            print(f'Critical Error Processing PDF : {e}')


if __name__ == "__main__":
    my_doc = DocumentAnalyzer("my_resume.pdf")
    print(my_doc)
    my_doc.read_pdf()

    print("\n -- Text Preview -- \n")
    print(my_doc.raw_text)