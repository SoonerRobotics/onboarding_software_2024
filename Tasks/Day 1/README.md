# Software Onboarding 2024 | Day 1

Welcome to Day 1 of the Sooner Competitive Robotics software onboarding! Today we are going to focus a few smaller tasks to get you warmed up and familiar with the tools we use. By the end of today, you should have a very basic understanding of Git and Python! It is important to note that if you have never programmed before you will have to do some additional learning on your own time. We will provide resources to help you along the way, but it is up to you to put in the effort to learn and grow as a software member.

## Table of Contents

1. [Git](#git)
2. [Python](#python)
3. [Pong](#pong)
4. [Snake](#snake)
5. [Additional Resources](#additional-resources)

## Git

Git is a version control system that we use to manage our codebase. It allows us to track changes to our code and collaborate with other team members effectively. If you have not already installed Git, please refer back to the [Getting Started](/README.md) section for instructions on how to do so.

To cover the basics of Git, we will be working through the [Learn Git Branching](https://learngitbranching.js.org/) tutorial. If you are reading this on your own, please take some time to work through the tutorial and familiarize yourself with the basic commands and concepts of Git. If you are reading this with the team, we will work through the tutorial together and answer any questions you may have. We will mainly be focusing on levels 1 and 2 (Introduction to Git Commits and Branching in Git) today.

There are four commands it does not cover that are important to know:
- `git status` - This command shows the status of the working directory and the staging area. It lets you see which changes have been staged, which haven't, and which files aren't being tracked by Git.
- `git fetch` - This command downloads commits, files, and refs from a remote repository into your local repo. It will not merge the changes into your local branch.
- `git pull` - This command fetches changes from a remote repository and merges them into your local branch.
- `git push` - This command sends the committed changes to the remote repository.

### Pull Requests and Github

So, if git does all of this magic on my computer why do I need to know about Github? Well, Github allows us to host our codebase on the internet so other developers can access it. It also provides us a way to visually review changes and collaborate on code. At the end of onboarding, we will be using its *pull request* feature which allows you to *pull* your changes into a different branch. Typically, we prevent developers from pushing into the "main" branch and instead require pull requests. This allows us to review the changes and ensure that the *main* branch always remains stable.

### Cloning the Repository

If you haven't already, create a Github account and send me your username so I can add you to the organization. Next, clone the repository by running the following command in your terminal:

```bash
git clone https://github.com/SoonerRobotics/onboarding_software_2024
```

If you have any issues with this step, please reach out to me or any of the other team members for help.

### Creating a Branch

Create a new branch by running the following command in your terminal:

```bash
git checkout -b <branch-name>
```

For the purposes of onboarding, your branch name should be `onboarding/<your-name>`. In practice, we have various branch naming standards we try to follow on all of our repositories (but is not always the case).

## Tasks

### Pong

Okay, so you may be wondering "Well Dylan, isn't Pong a bit of a stretch to start with?" and to that I say yes it definitely is. We will not be implementing any of the programs over the next few days from scratch, but rather we will be fixing various issues and learning how to work with an existing codebase. This will give you a good idea of what it is like to navigate through someone else's code and provide some additional problem solving skills. We try to keep our codebases well documented and easy to read, but as the lead software developer for the last two years I can assure you that is not always the case.
<!-- TODO: INSERT PICTURE OF REALLY BAD CODE HERE -->