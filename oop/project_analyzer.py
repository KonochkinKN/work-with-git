import os


class ProjectAnalyzer(object):
    git_dir = '.git'

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(ProjectAnalyzer, cls).__new__(cls)
        return cls.instance

    def check_git_repository(self):
        """
        Простая проверка на принадлежность в гит-репозиторию
        :return: Признак принадлежности
        """
        files = os.listdir('.')
        if self.git_dir in files and\
                os.path.isdir(self.git_dir):
            return True
        # files = os.listdir('..')
        # if self.git_dir in files and\
        #         os.path.isdir('../' + self.git_dir):
        #     return True
        return False

    def __show_branch(self, files, files_dir, shift):
        for f in files:
            path = os.path.join(files_dir, f)
            if os.path.isdir(path):
                print("\t"*shift + f'|__ {f}')
                new_files = os.listdir(path)
                self.__show_branch(new_files, path, shift+1)
            elif os.path.isfile(path):
                print("\t"*shift + f'|__ {f}')

    def show_project_tree(self):
        files = os.listdir('.')
        files.remove(self.git_dir)
        self.__show_branch(files, '.', shift=0)


if __name__ == '__main__':
    pa = ProjectAnalyzer()
    print(pa.check_git_repository())
    pa.show_project_tree()

