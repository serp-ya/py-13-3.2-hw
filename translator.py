import requests
import os


def make_dirs_to_file(path_to_file):
    file_dirname = os.path.dirname(path_to_file)

    if not os.path.exists(file_dirname):
        os.makedirs(file_dirname)


def read_file_by_path(path_to_file):
    with open(path_to_file) as f:
        return f.read()


def write_file_by_path(path_to_file, text_data):
    make_dirs_to_file(path_to_file)

    with open(path_to_file, 'wt', encoding='utf8') as f:
        f.write(text_data)


def translate(source_file_path, result_file_path, lang_form='en', lang_to='ru'):
    url = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
    key = 'trnsl.1.1.20170924T220958Z.c68b126185f64636.0b53609cb4b3feffdcd9b68ab27384fa1c052cce'
    lang = f'{lang_form.lower()}-{lang_to.lower()}'
    text = read_file_by_path(source_file_path)

    config = {
        'key': key,
        'lang': lang,
        'text': text,
    }

    response = requests.get(url, params=config).json()

    write_file_by_path(
        result_file_path,
        (' '.join(response.get('text', [])))
    )
