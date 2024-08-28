import subprocess

def pull_1():
    try:
        init = ["git", "init"]
        subprocess.run(init, check=True)
        print("Command_1:\tgit init")
    except subprocess.CalledProcessError as e:
        print(f"Error :{e}")

def pull_2():
    try:
        add = ["git", "add", "."]
        subprocess.run(add, check=True)
        print("Command_2:\tgit add .")
    except subprocess.CalledProcessError as e:
        print(f"Error :{e}")

def pull_3():
    try:
        commit = ["git", "commit", "-m", "first commit"]
        subprocess.run(commit, check=True)
        print("Command_3:\tgit commit -m 'first commit'")
    except subprocess.CalledProcessError as e:
        print(f"Error :{e}")

def pull_4():
    try:
        branch = ["git", "branch", "-M", "main"]
        subprocess.run(branch, check=True)
        print("Command_4:\tgit branch -M main")
    except subprocess.CalledProcessError as e:
        print(f"Error :{e}")

def pull_5(repo_url):
    try:
        remote = ["git", "remote", "add", "origin", repo_url]
        subprocess.run(remote, check=True)
        print(f"Command_5:\tgit remote add origin {repo_url}")
    except subprocess.CalledProcessError as e:
        print(f"Error :{e}")

def pull_6():
    try:
        push = ["git", "push", "-u", "origin", "main"]
        subprocess.run(push, check=True)
        print("Command_6:\tgit push -u origin main")
    except subprocess.CalledProcessError as e:
        print(f"Error :{e}")

def pull_all(repo_url):
    pull_1()
    pull_2()
    pull_3()
    pull_4()
    pull_5(repo_url)
    pull_6()

# Get the repository URL from user input
repo_url = input("Enter the url of your Github repository: ")

# Execute all Git commands
pull_all(repo_url)
