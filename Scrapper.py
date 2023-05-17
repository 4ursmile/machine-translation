import string
from pygoogletranslation import Translator
src = 'en'
des = 'vi'
data_name = 'data.txt'
wf = open(data_name, 'w')
translator = Translator()
def clean_data(path, remove_pattern = 'Ngày'):
    with open(path, 'r', encoding='utf-8') as f:
        lines = filter(None, (line.rstrip() for line in f))
        for line in lines:
            line = line.strip()
            if line.startswith(remove_pattern):
                continue
            else:
                s_sentence = str(line);
                print(s_sentence)
                d_sentence = translator.translate(s_sentence, src=src, dest=des).text
                combine = s_sentence+'/t'+d_sentence + '/n'
                wf.write(combine)
if __name__ == '__main__':
    clean_data('data_raw.txt')

