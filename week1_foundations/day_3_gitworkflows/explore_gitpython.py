from git import Repo

repo = Repo(".")
for branch in repo.branches:
    print(branch)
