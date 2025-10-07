from git import Repo

repo = Repo(".")  # "." points to the root of the Git repo

# Current branch
print("Current branch:", repo.active_branch)

# All local branches
print("\nAll local branches:")
for branch in repo.branches:
    prefix = "*" if branch == repo.active_branch else " "
    print(f"{prefix} {branch}")

# Last 5 commits
print("\nLast 5 commits:")
for commit in repo.iter_commits(repo.active_branch, max_count=5):
    message = commit.message
    if isinstance(message, bytes):
        message = message.decode("utf-8", errors="replace")
    print(f"- {commit.hexsha[:7]} | {commit.author.name} | {message.strip()}")
