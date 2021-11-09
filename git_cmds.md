## Essential GIT commands

**A. Create a new repository on the command line**

1. echo "# something, for example, repo name" >> README.md
2. git init
3. git add <fname> (add file with name fname) / git add . (add everything)
4. git commit -m "first commit"
5. git branch -M main
6. git remote add origin https://<personal access token>@github.com/Tirthankar-Dutta-2016/<rep_name>.git
7. git push -u origin main


**B. Push an existing repository from the command line**

1. git remote add origin https://github.com/Tirthankar-Dutta-2016/<repo_name>.git
2. git branch -M main
3. git push -u origin main

**My Personal Access Token for GitHub:** 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
