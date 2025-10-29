#!/opt/homebrew/bin/python3

import os, zipfile, re, collections, shutil, sys

working_folder = '/tmp/iron'

def extract_and_move_images(cbz_file_path):
    if os.path.exists(working_folder):
        shutil.rmtree(working_folder)
    os.makedirs(working_folder)

    with zipfile.ZipFile(cbz_file_path, 'r') as zip_ref:
        temp_folder = '/tmp/extracted_temp'
        zip_ref.extractall(temp_folder)

        for root, dirs, files in os.walk(temp_folder):
            for file in files:
                file_path = os.path.join(root, file)
                if file.lower().endswith(('.jpg', '.jpeg', '.png')) or file.lower() == 'comicinfo.xml':
                    destination_path = os.path.join(working_folder, file)
                    shutil.move(file_path, destination_path)

        shutil.rmtree(temp_folder)

def is_image_file(file_path):
    image_extensions = ['.jpg', '.jpeg', '.png']
    return any(file_path.lower().endswith(ext) for ext in image_extensions)

def create_zip_files(chapter_files, manga_name):
    output_folder = os.path.join(os.getcwd(), 'chapters')
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    for chapter in chapter_files:
        zip_filename = f'{manga_name} - {chapter}.cbz'
        zip_filepath = os.path.join(output_folder, zip_filename)

        with zipfile.ZipFile(zip_filepath, 'w') as zip_file:
            for file_path in chapter_files[chapter]:
                zip_file.write(file_path, os.path.basename(file_path))
    shutil.rmtree(working_folder)

def get_chapter_files():
    chapter_files = collections.defaultdict(list)
    comic_info_path = None
    for filename in os.listdir(working_folder):
        file_path = os.path.join(working_folder, filename)

        if filename.lower() == 'comicinfo.xml':
            print(f'Skipping {filename}')
            comic_info_path = file_path
            continue

        pattern = r'c(\d{3})'
        match = re.search(pattern, filename)
        if match:
            chapter = match.group(1)
        else:
            print('No chapter number found for:', filename)
            exit()

        pattern = r'v(\d{2})'
        match = re.search(pattern, filename)
        if match:
            volume = match.group(1)
        else:
            print('No volume number found for:', filename)
            exit()
    
        chapter_files[f"v{volume} c{chapter}"].append(file_path)

    for file_paths in chapter_files.values():
        if comic_info_path:
            file_paths.append(comic_info_path)
        file_paths.sort()

    return chapter_files

def get_manga_name(chapter_files):
    if len(sys.argv) <= 2:
        for file_paths in chapter_files.values():
            for file_path in file_paths:
                if is_image_file(file_path):
                    manga_name = file_path.split('/')[-1].split(' - ')[0]
                    break
            if manga_name:
                break
        user_input = input(f'Manga name (press ENTER for "{manga_name}"): ')
        if user_input:
            manga_name = user_input
        return manga_name
    return sys.argv[2]

if __name__ == "__main__":
    cbz_file_path = sys.argv[1]
    extract_and_move_images(cbz_file_path)
    chapter_files = get_chapter_files()
    manga_name = get_manga_name(chapter_files)
    create_zip_files(chapter_files, manga_name)
