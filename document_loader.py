from langchain_community.document_loaders.csv_loader import CSVLoader


loader = CSVLoader(file_path="D:\\New folder (2)\\archive (4)\\Churn_Modelling.csv")
data = loader.load()
# print(data)
print(type(data))
print(data[0])
print(data[0].page_content)
print(len(data))
print(data[0].page_content)
