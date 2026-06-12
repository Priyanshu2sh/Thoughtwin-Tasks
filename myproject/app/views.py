from django.shortcuts import render

# Create your views here.


# python manage.py makemigrations

# python manage.py makemigrations myapp

# pythono manage.py migrate

# python manage.py migrate myapp

# python manage.py showmigrations

# python manage.py createsuperuser

# python manage.py shell




# -----GIT COMMANDS-----

# git --version

# git config --list     (to see settings)

# git config --global --list (to see global)

# git config user.name  "Priyanshu Sharma" (to set name)

# git config user.email "abc@gmail.com"(to set emmail)

# similarly to set other values ...


# git init (initialize emoty git repo)

# git status (Check which files are tracked)

# git add <file>   (stage a file)
# git add .    (stage all files)

# git restore --staged  <file>  (Unstage a file)

# git commit -m "message" (Commit staged changes with a message)

# git commit -a -m "message" (Commit all tracked changes (skip staging))

# git log (See commit history)


# git log --oneline

# git log --stat    (To see which files changed in each commit)

# git commit (to write multi line comment)

# git commit --allow-empty -m "start_project"    (create an empty commit)

# git commit --no-edit   (use previous commit message (no editor))

# git commit --amend --no-edit   (add unstaged files to last commit)

# git commit --amend -m "Corrected message"    (to fix the last commit message)

# git reset --soft HEAD~1  (to undo the last commit and keep your changes staged)

# git stash   (Stash your changes)

# git stash push -m "message"    (Stash with a message)

# git stash list    (List all stashes)

# git stash branch <branchname>    (Create a branch from a stash)

# To stash untracked files too, use git stash -u (or --include-untracked)

# git stash show     (See what was changed in the latest stash)

# git show <commit>   (Show details of a specific commit)

# git diff    (see unstaged changes)

# git diff --staged  (see staged changes)

# git diff <commit1> <commit2>    (compare two commits)

# git log --author="Alice"   (show commits by author)

# git log --since="2 weeks ago"    (Show Recent Commits)


# git branch hello-world-images   (creates new branch)

# git branch  (list all branches)

# git checkout hello-world-images   (switch to differennt branch)

# git checkout -b eergency-branch   (creates new branch and switches to it)

# git push -u origin <branch>   (Git will set up the tracking information during the push, publish branch)

# git branch -d <branch>  (delete branch)

# git push origin --delete <branch>  (delete branch from github (remote))

# git branch -m old-name new-name  (Rename a branch)

# git revert HEAD   (Revert the latest commit)

# git revert <commit>   (Revert a specific commit)

# git revert HEAD~2   (Revert a commit further back in history)

# git revert --no-edit   (Skip commit message editor)

# git reset --soft <commit>   (Move HEAD to commit, keep changes staged)

# git reset --mixed <commit>   (Move HEAD to commit, unstage changes (default))

# git reset --hard <commit>   (Move HEAD to commit, discard all changes)

# git reset <file>   (Unstage a file)

B1
