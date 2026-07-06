import ollama 
from analyzer_blueprint import DocumentAnalyzer

print("Starting AI Doc Pipeline....")

my_doc = DocumentAnalyzer("my_resume.pdf")
my_doc.read_pdf()

print("Sending Data To local Ai Model!!.....")

ai_prompt = f"""
You are an expert technical recruiter. Read the following resume and give me:
1. The candidate's top 3 strongest technical skills.
2. A 2-sentence summary of their best project.
Do not include any fluff or introductory text

Resume text :
{my_doc.raw_text}
"""

try :
    response = ollama.chat(model=my_doc.llm_model,messages=[
        {
            'role' : 'user' ,
            'content' : ai_prompt
        }
    ])

    print("\n" + "="*50)
    print("AI Analysis Complete :")
    print("="*50)
    print(response['message']['content'])

except Exception as e :
    print(f"\n Ai Connection Error : {e}")
    print("Make sure You Installed Ollama and ran 'ollama run llama3' in your terminal..!! ")