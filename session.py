from langchain_google_genai import GoogleGenerativeAI 


api_key = 'AIzaSyB51arrkUeiodRIF_fHG-rscDn0l3CnPVk'
llm = GoogleGenerativeAI(model = 'gemini-pro', google_api_key = api_key)

print(llm.invoke(
    "List of top 5 Indian Cricketers"
))

