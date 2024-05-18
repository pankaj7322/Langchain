with open("C:\\Users\\panka\\Documents\\langchain\\mbox-short.txt") as f:
    state_of_the_union = f.read()


from langchain_text_splitters import CharacterTextSplitter

text_splitter = CharacterTextSplitter(
    separator="\n\n",
    chunk_size=1000,
    # chunk_overlap=200,
    # length_function=len,
    # is_separator_regex=False,
)
texts = text_splitter.create_documents([state_of_the_union])
# print(texts)
# print(texts[0])
# print(texts[0].page_content)
print(len(texts[1].page_content))

chunks = [len(i.page_content) for i in texts]
print(chunks)

print(sum(chunks))