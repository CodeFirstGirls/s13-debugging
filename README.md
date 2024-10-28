# MathsForDevs
You are joining a team of developers for a mathematical software company who have just realised 
that the test file is failing and there is a bug caused somewhere in the 
code, but don’t know where or what commit caused the change.

Your team plan to use git bisect to work out which commit caused the code to fail and then work to fix it.

## Needed Context
- Your team knows that the first code commit was good (tests all passing) 
- Your team knows that the last code commit was bad (tests failing)

## Process Reminder
- `git bisect start`
- Use git bisect to mark an initial good and bad commit using the commit hash
  - You can find all commit hashes by running the command `git log` in the cloned repository
- At each step, run the given commit to see if the tests fail or pass
  - And then mark that commit as either good or bad
- You will eventually find what commit caused the tests to fail
- You can then identify what caused the error and fix it

For the official guided documentation on git bisect visit [here](https://git-scm.com/docs/git-bisect)


#### 📖 Scenario for Session 13 📖
