from os import system

class  GitPush:
    def __init__(self, message:str, branch:str) -> None:
        self.message = message
        self.branch = branch
        self.SSH = 'git@github.com:Aliton666/DjangoTemplates_2.git'

    def git_init(self):
        system(f'git init')
        system(f'git remote add origin{self.SSH}')

    def git_push(self):
        system(f'git add .')
        system(f'git commit -m "{self.message}"')
        system(f'git checkout -b {self.branch}')
        system(f'git push -u origin {self.branch}')

if __name__ == '__main__':
    message = input('Напигите свои изменения:/n')
    brach = 'Ali'

    git = GitPush('first commit', 'main')
    git.git_init()
    git.git_push()

    