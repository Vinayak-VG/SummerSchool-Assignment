# SummerSchool-Assignment
GitHub Repo for students to fork and create a pull request for the assignment of Summer School

Use the Discussions Tab on the repo to post your doubts, we'll try our best to resolve them at the earliest!!

---

Link to notebook: [![Open All Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Vinayak-VG/SummerSchool-Assignment)

Link to Session Recording: [Recording Link](https://drive.google.com/file/d/1C2WUfQL3x06Kpl-xOgTb0x3srq-c8kxU/view?usp=sharing)

### How to create a submission

First, [fork the repository](https://docs.github.com/en/github/getting-started-with-github/fork-a-repo) in GitHub! :fork_and_knife:
<a href="https://docs.github.com/en/github/getting-started-with-github/fork-a-repo">
<div style="text-align:center"><img src="https://docs.github.com/assets/images/help/repository/fork_button.jpg" alt="fork button" width="500"/></div>
</a>

Your fork will have its own location, which we will call `PATH_TO_YOUR_FORK`.<br>
Next, [clone the forked repository](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository) and create a branch for your folder(`git branch my_folder`), which here we will call <my_folder>:
```bash
git clone $PATH_TO_YOUR_FORK
cd SummerSchool-Assignment
git checkout -b my_folder
```

### Submitting

Once you are happy with the submission, submit them for review.
First, commit and push your changes:
```bash
git add .
git commit -m "Added my_folder roll number"
git push --set-upstream origin my_folder
```
Finally, [submit a pull request](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request).
The last `git push` command prints a URL that can be copied into a browser to initiate such a pull request.
Alternatively, you can do so from the GitHub website.
<a href="https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request">
<div style="text-align:center"><img src="https://docs.github.com/assets/images/help/pull_requests/pull-request-start-review-button.png" alt="pull request button" width="500"/></div>
</a>

## Note
Please create a folder named  `Name_Rollno` in which you have all the contents of whatever submission you wanna make and then make a pull request


