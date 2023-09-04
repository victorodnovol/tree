import argparse
import os
import pathlib
import stat

import colorama


class Folder:

    my_folders = []
    my_result = []

    def __init__(self, dirpath, subdirs, files):
        if not Folder.my_folders:
            Folder.my_root = self
            Folder.root_offset = len(dirpath.split('/')) - 1
        self.dirpath = dirpath
        self.subdirs = subdirs
        self.files = files
        self.level = len(dirpath.split('/')) - 1 - Folder.root_offset
        self.parent_path, self.name = os.path.split(dirpath)
        self.children = []
        Folder.my_folders.append(self)
        self.attach_to_parent()

    def attach_to_parent(self):
        """
        Прикрепляет каталог к родительскому
        """
        for fld in Folder.my_folders:
            if fld.dirpath == self.parent_path:
                fld.children.append(self)

    def _colorize(self, text, color=colorama.Fore.BLUE):
        """
        Вернуть раскрашенную строку
        """
        return color + text + colorama.Fore.RESET

    def printme(self, last=False):
        """
        Распечатать каталог
        """
        char_hline = '\u2500'
        char_vline = '\u2502'
        char_corner = '\u2514'
        char_triple = '\u251c'
        dirtab = (self.level - 1) * (
            char_vline + 4 * ' ') + char_triple + char_hline * 2 + ' '
        filetab = self.level * (char_vline +
                                4 * ' ') + char_triple + char_hline * 2 + ' '
        filetab_last = filetab.replace(char_triple, char_corner)
        if not self.level:  # Корневой элемент
            dirtab = ''
        if last:
            dirtab = dirtab.replace(char_triple, char_corner)
            filetab = filetab.replace(char_vline, ' ')
            filetab_last = filetab_last.replace(char_vline, ' ')
        print(dirtab + self._colorize(self.name))
        Folder.my_result.append(dirtab + self.name + '\n')
        for fld in self.children:
            if fld == self.children[-1] and not self.files:
                fld.printme(last=True)
            else:
                fld.printme()
        for file in self.files:
            if file == self.files[-1]:
                print(filetab_last + file)
                Folder.my_result.append(filetab_last + file + '\n')
            else:
                print(filetab + file)
                Folder.my_result.append(filetab + file + '\n')


class SysManager:

    def __init__(self):
        """
        Обработка аргументов командной строки
        """
        parser = argparse.ArgumentParser(
            description='System management program',
            usage='Run this script with parameters [-s|-c|-t] PATH. '
            'To get help use -h or --help')
        parser.add_argument('-s', '--system', help='execute system command')
        parser.add_argument('-c', '--chmod', help='check access rights')
        parser.add_argument('-t', '--tree', help='create folder tree')
        args = parser.parse_args()
        for arg, value in args._get_kwargs():
            if value:
                path_value = pathlib.Path(value)
                if not path_value.exists():
                    print('No such path available')
                    return
                func = getattr(SysManager, arg)
                func(self, path_value)

    def system(self, path):
        os.chdir(path)
        while (request := input('Shell command: ')) != 'exit':
            result = os.system(request)
            if result != 0:
                print('Wrong command, exit!')
                return
        print('The work has been completed!')

    def chmod(self, path):
        os.chdir(path)
        while (request := input('Enter the path: ')) != 'exit':
            try:
                print(oct(stat.S_IMODE(os.lstat(request).st_mode))[2:])
            except FileNotFoundError:
                print('File or directory does not exist!')
        else:
            print('The work has been completed!')

    def tree(self, path):
        os.chdir(path)
        print(f'Current path is {path}')
        while (request := input('Enter the path: ')) != 'exit':
            request = pathlib.Path(pathlib.Path.cwd() / request)
            if not request.exists():
                print('File or directory does not exist!')
            else:
                my_tree = os.walk(request, topdown=True)
                Folder.my_folders.clear()
                Folder.my_result.clear()
                for dir in my_tree:
                    Folder(*dir)
                Folder.my_root.printme()
                with open('wood_' + Folder.my_root.name, 'w') as writer:
                    writer.writelines(Folder.my_result)
        print('The work has been completed!')


if __name__ == '__main__':
    SysManager()
