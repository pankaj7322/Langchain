from langchain_google_genai import GoogleGenerativeAIEmbeddings
api_key = 'AIzaSyDAn6F0H3rrvUjE_y9iNREdE6PB1C8Ueuw'
embeddings = GoogleGenerativeAIEmbeddings(model= 'models/embedding-001', google_api_key = api_key, timout = 100)
vector = embeddings.embed_query("hello world")
print(vector[:5])
print(len(vector))
"""
    each sentence represetns with a vector has 768 value
    Dimensionality 768
"""
# result = genai.embed_content(
#     model = "models/embedding-001",
#     content = "what is the meaningof life?",
#     task_type = "retrival_document",
#     title = "embedding of single string"
# )
# print(len(result['embedding']))