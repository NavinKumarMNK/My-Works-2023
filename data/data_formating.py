import pandas as pd

corpus_tamil_path = './data/corpus_tamil.txt'
corpus_english_path = './data/corpus_english.txt'

glossary_tamil_path = './data/glossary_tamil.txt'
glossary_english_path = './data/glossary_english.txt'

def read_text_file(file_path):
    with open(file_path, 'r') as file:
        lines = [line.strip() for line in file.readlines()]
    return lines

corpus_tamil_lines = read_text_file(corpus_tamil_path)
corpus_english_lines = read_text_file(corpus_english_path)
glossary_tamil_lines = read_text_file(glossary_tamil_path)
glossary_english_lines = read_text_file(glossary_english_path)

corpus = pd.DataFrame({'Tamil': corpus_tamil_lines, 'English': corpus_english_lines})
glossary = pd.DataFrame({'Tamil': glossary_tamil_lines, 'English': glossary_english_lines})

dataset = pd.concat([corpus, glossary], axis=0)
dataset.to_csv('./data/dataset.csv', index=False)