#!/usr/bin/python3
import os
# Launch GTK Desktop Dialog When The Folder Reach The File Quantity
file_count: int = 6
dialog_width: int = 11
# Run Always In System Init
folder: str = os.path.abspath('Descargas/tanda_de_6_A') + '/'
# Check How Much File Are To Show Dialog
if (os.listdir(folder).__len__() == file_count):
    os.system(f'zenity --width={len("The [ {folder} ] folder has reached the {file_count} files.") * dialog_width} --info --text "The [ {folder} ] folder has reached the {file_count} files."')
elif (os.listdir(folder).__len__() < file_count):
    os.system(f'zenity --width={len("The [ {folder} ] folder has less than {file_count} files.") * dialog_width} --info --text "The [ {folder} ] folder has less than {file_count} files."')
else:
    os.system(f'zenity --width={len("The [ {folder} ] folder has {os.listdir(folder).__len__() - file_count} more.") * dialog_width} --info --text "The [ {folder} ] folder has {os.listdir(folder).__len__() - file_count} more."')