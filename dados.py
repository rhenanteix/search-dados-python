import PyPDF2
import pandas as pd

pdf = open('teste.pdf', 'rb')
reader = PyPDF2.PdfFileReader(pdf)
pagina = reader.getPage(0)

text=(pagina.extractText())
text=text.split(",")
text

# creating a list of keywords to search for in the pdf file
search_keywords=['Banco', 'Apelante', 'processo', 'apelante', 'apelado', 'comarca', 'cidade', 'tribunal']

# to search for the keywords in the extracted text and then locate sentences with keywords
for sentence in text:
            lst = []
            for word in search_keywords:
                if word in sentence: 
                    lst.append(word)
            print('{0} key word(s) in sentence: {1}'.format(len(lst), ', '.join(lst)))
            print(sentence + "\n")

            dados = pd.DataFrame(lst)
            dados.to_json('dadosExportados.json')
