import os
import shutil

dict_extensions = {
    'audio_extensions': ('.mp3', '.m4a', '.wav', '.flac'),
    'img_extensons': ('.jpeg', 'JPG', 'HEIC', '.png', '.jpg', '.gif'),
    'video_extensions': ('.mp4', '.mkv', '.MKV', '.flv', '.mpeg'),
    'doc_extensions': ('.doc', '.pptx', '.pdf', '.txt', 'docx', 'xlsx', '.PDF', '.apk', '.html', 'xlsm'),
    'setup_extension': ('.exe', '.rar', '.zip', '.torrent', '.EXE')
}
path = input('Enter folder Path : ')


def file_sorter(folder_path, extension_type):
    file = []
    for items in os.listdir(folder_path):
        for extension in extension_type:
            if items.endswith(extension):
                file.append(items)

    return file


# print(file_sorter(path, dict_extensions['doc_extensions']))

for key, extensions in dict_extensions.items():

    new_folder = key.split('_')[0] + '-files'
    folder_path = os.path.join(path, new_folder)
    if os.path.exists(folder_path):
        for i in file_sorter(path, extensions):
            item_path = os.path.join(path, i)
            # new_item_path = os.path(folder_path)
            shutil.move(item_path, folder_path)
            print(f'{i} moved successfully to the folder {item_path}')

    else:
        os.mkdir(folder_path)
        for i in file_sorter(path, extensions):
            # item_path = os.path.join(folder_path, i)
            item_path = os.path.join(path, i)
            new_item_path = os.path.join(folder_path, i)
            shutil.move(item_path, new_item_path)
            print(f'{i} move successfully')
