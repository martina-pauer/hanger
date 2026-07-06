#!/usr/bin/python3
import asyncio
import os
from googletrans import Translator
# Translate all the Markdown in the folder and sub-folders to language
root_folder: str = '/workspaces/hanger/'
md_list: list[str] = []
lang_codes: list[str] =     [
                                'es', 'fr', 'de',
                                'ja', 'zh', 'uk',
                                'ru', 'it', 'pt'

                            ]

async def GoogleTranslation(message: str, lang_code: str):
    '''
        Use Google Translator for translate the message
        to selected language by international lang code
    '''
    async with Translator() as content:
        translation = await content.translate(message, dest = lang_code)
        return translation.text

class Documents:
    '''
        Representation of reduced content from
        a document for don't read each time need
        the content for could write it.
    '''
    def __init__(self, file_path: str, first_line: int, last_line: int):
        # Only Save Content for Data Encapsulation to protect files
        self.content: str = ''
        
        with open(os.path.abspath(file_path), 'r') as doc:
            for line in range(first_line, last_line + 1):
                self.content += doc.readline()
            doc.close()
        
        self.doc_path: str = os.path.abspath(file_path)

    def translation(self, code: str):
        '''
            Write Translation To Language code
            in file
        '''
        with open(self.doc_path, 'a') as translator:
            # Make Translation
            translated: str = self.content.replace('[EN]', f'[{code}]')
            translated: str = asyncio.run(GoogleTranslation(translated, code))
            # Add Translation To File
            translator.write(f'\n{translated}')
            translator.close()
            # Clean Memory
            del translated

if __name__ == '__main__':
    os.system(f'cd {os.path.abspath(root_folder)}')
    
    technical = Documents(f"{os.path.abspath('TECHNICAL_ROADMAP.md')}", 1, 97)

    roadmap = Documents(f"{os.path.abspath('ROADMAP.md')}", 1, 5)

    readme = Documents(f"{os.path.abspath('README.md')}", 3, 51)

    agent = Documents(f"{os.path.abspath('AGENTS.md')}", 1, 43)

    md_list: list[str] =   [technical, roadmap, readme, agent]
    # Get files in sub-folders (Only md)
    dirs: list[str] = os.listdir(f'{os.path.abspath(root_folder)}')

    def get_files(folder: str):
        '''
            Auxiliar Function For Could
            use recursivity to iterates
            over all sub folders
        '''
        # Get Files From Root (Level 1) to Last Folder With md files (Level 5)
        for file_name in dirs:
            # Level 1
            if os.path.isdir(file_name):
                # Iterative Case: is Directory
                dirs_1 = os.listdir(os.path.abspath(file_name))
                dirs.__add__(dirs_1)
                for names_1 in dirs_1:
                    # Level 2
                    if (names_1.__contains__('.md') and (not os.path.isdir(f'{os.path.abspath(f'{file_name}/{names_1}')}')) and (not md_list.__contains__(names_1))):
                        md_list.append(Documents(f'{file_name}/{names_1}', 1, 440))
                    elif os.path.isdir(f'{file_name}'):
                        if os.path.isdir(os.path.abspath(f'{file_name}/{names_1}')):
                            dirs_2 = os.listdir(os.path.abspath(f'{file_name}/{names_1}'))
                            dirs.__add__(dirs_2)
                            for names_2 in dirs_2:
                                # Level 3
                                if (names_2.__contains__('.md') and (not os.path.isdir(f'{file_name}/{names_1}/{names_2}')) and (not md_list.__contains__(names_2))):
                                    md_list.append(Documents(f'{file_name}/{names_1}/{names_2}', 1, 440))
                                elif os.path.isdir(os.path.abspath(f'{file_name}/{names_1}/{names_2}')):    
                                    dirs_3 = os.listdir(os.path.abspath(f'{file_name}/{names_1}/{names_2}'))
                                    dirs.__add__(dirs_3)
                                    for names_3 in dirs_3:
                                        # Level 4
                                        if (names_3.__contains__('.md') and (not os.path.isdir(f'{os.path.abspath(f'{file_name}/{names_1}/{names_2}/{names_3}')}')) and (not md_list.__contains__(names_3))):
                                            md_list.append(Documents(f'{os.path.abspath(f'{file_name}/{names_1}/{names_2}/{names_3}')}', 1, 440))                    
                                        elif os.path.isdir(os.path.abspath(f'{file_name}/{names_1}/{names_2}/{names_3}')):    
                                            dirs_4 = os.listdir(os.path.abspath(f'{file_name}/{names_1}/{names_2}/{names_3}'))
                                            dirs.__add__(dirs_4)
                                            for names_4 in dirs_4:
                                                # Level 5
                                                if (names_4.__contains__('.md') and (not os.path.isdir(f'{os.path.abspath(f'{file_name}/{names_1}/{names_2}/{names_3}/{names_4}')}')) and (not md_list.__contains__(names_4))):
                                                    md_list.append(Documents(f'{os.path.abspath(f'{file_name}/{names_1}/{names_2}/{names_3}/{names_4}')}', 1, 440))                    
                                                elif os.path.isdir(os.path.abspath(f'{file_name}/{names_1}/{names_2}/{names_3}/{names_4}')):    
                                                    dirs_5 = os.listdir(os.path.abspath(f'{file_name}/{names_1}/{names_2}/{names_3}/{names_4}'))
                                                    dirs.__add__(dirs_5)  
                                                    
            elif (file_name.__contains__('.md') and (not os.path.isdir(f'{os.path.abspath(file_name)}')) and (not md_list.__contains__(file_name))):
                # Only Add New Files: Base Case, is a file
                md_list.append(Documents(f'{os.path.abspath(file_name)}', 1, 440))
    # Detect All The Markdown Files Before Translate Them            
    get_files(root_folder)         
    # Add Translation for each content in respective file
    for language in lang_codes:
        for content in md_list:
            content.translation(language)