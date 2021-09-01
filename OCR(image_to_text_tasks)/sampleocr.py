import easyocr as ocr  #OCR

reader = ocr.Reader(['en'],model_storage_directory='.')

result = reader.readtext("Motivational_quotes.jpg")

for text in result:
    print(text[1])