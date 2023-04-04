import git

from commitmsg.generator import CommitMessageGenerator


def main():
    generator = CommitMessageGenerator()
    repo = git.Repo()
    git_branch = repo.active_branch.name
    git_branch = "" if git_branch == "master" else f"{git_branch}: "
    diff = repo.git.diff(repo.head.commit.tree)
    type, message = generator(diff)
    print("Generated commit message:\n\n")
    print(f"{type}: {git_branch}{message}")
    print("\n\n")
