import translator
import os


def get_dir_abs_path(dir_name=''):
    main_path = os.path.dirname(__file__)
    main_abs_path = os.path.abspath(main_path)

    return os.path.join(main_abs_path, dir_name)


def make_path_to_file(filename, filedir=get_dir_abs_path()):
    return os.path.join(filedir, filename)


def get_dir_file_names(dir_path):
    return os.listdir(dir_path)


def check_file_type(filetype, filename):
    return filename.strip().endswith(filetype)


def filter_txt_files_in_list(file_names_list):
    filter_txt_files_helper = lambda filename: check_file_type('.txt', filename)
    filtered_file_names = filter(filter_txt_files_helper, file_names_list)

    return list(filtered_file_names)


def core():
    current_dir_path = get_dir_abs_path()
    current_dir_files_list = get_dir_file_names(current_dir_path)
    articles = filter_txt_files_in_list(current_dir_files_list)

    for article in articles:
        lang = article.split('.')[0]
        source_path = make_path_to_file(article)
        result_path = make_path_to_file(article, get_dir_abs_path('translation'))

        translator.translate(source_path, result_path, lang)


if __name__ == '__main__':
    core()
