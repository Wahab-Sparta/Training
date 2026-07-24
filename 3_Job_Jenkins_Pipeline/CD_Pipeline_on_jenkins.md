# 3 Job CI/CD Pipeline on Jenkins

We want to be able to make a change on our dev branch, push the changes to GitHub and automatically have our changes tested, merged with main branch (if tests were successful), and uploaded to a running EC2 instances to instantly see the changes go live.

## What do we need?

* Git repo of the TicTacToe app
* EC2 Instance running the TicTacToe app
* Security group attached to EC2 instance allowing SSH traffic from the Jenkins worker node
* Setup SSH key pair on GitHub
* Setup webhook on GitHub
* Setup the Pipeline to run the 3 Jobs on Jenkins

## Diagram of Pipeline
![alt text](<Images/Jenkins CICD Pipeline.png>)

This diagram illustrates how our pipeline will work:
* As you can see the developer will do a `git push` (on the dev branch) which will trigger a webhook on GitHub that Jenkins is listening for. 

* Jenkins will then use an Agent Node to carry out the 3 Jobs assigned to it.
* In Job 1:  
    1.  It will use the provided GitHub SSH key to get the repo.
    2.  Tests will be carried out to assure the app still works as intended.
    3.  If all the tests are successful, Job 2 will be triggered.
* In Job 2:  
    1.  Using the provided GitHub SSH key, it will merge the dev branch into the main branch.
    2.  Then it will trigger Job 3.
* In Job 3: 
    1.  Using the provided GitHub SSH key and AWS SSH key, it will copy or sync the new app code with the app code running on an EC2 instance.
    2.  Next it will restart the app.

## Benefits
There are several benefits of having an automated pipeline like this:
* The entire SDLC is automated, from compiling code to testing to deployment.
* Much faster delivery to live. In this case, the whole sequence from pushing to GitHub and seeing it live on the instance took around 1 minute.
* No human error during testing or updating the live app.
* Reduced risk; since every build follows the exact same steps.
* Code is automatically tested and validated.

## GitHub SSH Key

To create a GitHub SSH Key, please refer to [this documentation](../SSH_with_GitHub/Create_SSH_key_for_GitHub.md)

## GitHub Webhook

To create a Webhook on GitHub:

1. Go to [GitHub](https://github.com) and open your Tic Tac Toe repository.
2. Click on the Settings tab for your repo.
3. Click on Webhooks and then click "Add webhook"
4. Enter your entire Jenkins server IP (Make sure to remember the port number if needed e.g. `127.0.0.1:8080`)
5. Make sure "Just the push event" is selected as we only want the push event to trigger the webhook.
6. Click "Add webhook"

Your webhook has now been created. In the steps below regarding how to create the Jobs in the Pipeline, it will show how Jenkins will listen to the Webhook to trigger the first Job.

## Jenkins CICD Pipeline

Below will describe how to create the Jenkins Pipeline. I've also included all the different methods I found for doing certain jobs.

## Job 1 - Testing

To create Job 1 on Jenkins:
  1. Create a new item, enter a name for your item and choose "Freestyle project".
  2. Enter a description describing what your job will do.
  3. Click "Discard old builds" and set the "Max# of builds to keep" to 5.   
  (This will keep only a max of 5 builds in your build history, you can change this to a higher number if you want to keep more builds.)
  4. Click "GitHub project" and enter your App GitHub link.
  5. Under Source Code Management click "Git" and enter your SHH URL in "Repository URL". 
  6. Click "Add" under "Credentials" and choose "Jenkins".
     1. Change the "Kind" to "SSH Username with private key"
     2. Add an ID and Username for your key
     3. Under "Private Key", click "Enter directly" then click "Add".
     4. Paste your private key entirely.  
⚠️ **Make sure to include "-----BEGIN OPENSSH PRIVATE KEY-----" and "-----END OPENSSH PRIVATE KEY-----". Every single character in your key is needed.**
  1. Click on the "credentials" dropdown and choose the credentials you just created.
  2.  In "Branch Specifier" enter "*/dev"
  3.  Under "Build Triggers" select "GitHub hook trigger for GITScm polling". (This is what allows Jenkins to listen to the GitHub webhook.)
  4.  Under "Build Environment" select "Provide Node & npm bin/ folder to PATH".
      1.  Under NodeJS Installation, click on the dropdown and select NodeJS version 20.
  5.  Under Build Steps click "Add build step" and choose "Execute Shell".
  6.  In the Execute Shell block, enter these commands:
```
  cd app
  npm ci
  npm test
```
These commands allow the agent to go into your app directory, do a clean install of the app and then run all the tests.

 **COMPLETE THIS LAST STEP ONLY AFTER COMPLETING JOB 2**
  * Under "Post-build Actions" click "Add post-build action" and choose "Build other projects".
  * Choose the Job 2 project you have created and select "Trigger only if build is stable".


## Job 2 - Merging

For this job, you can copy the project from Job 1.
  1. Create a new item, enter a name for your item and choose enter your Job 1 name at the bottom to copy from it.
  2. Enter a description describing what your job will do.  
  ⚠️ **IF YOU COPIED PROJECT FROM JOB 1**  
  **Deselect "GitHub hook trigger for GITScm polling" under "Build Triggers.**   
  If you do not deselect, it will run Job 2 right after you make a push to GitHub.

There are a couple of different methods for merging your changes from dev to main.

---

### Method 1 - Git Commands
This method will use Execute Shell and only use Git commands.
  1. Change the "Branches to build" under "Source Code Management" to "*/main"  
  **IF YOU DIDN'T COPY PROJECT FROM JOB 1**
     1. Under "Build Environment" select "SSH Agent" and select your Git SSH credentials created in Job 1
     2. Click "Add build step" under "Build steps", then select "Execute Shell".
  1. In the "Execute shell" block enter the following commands:
```
  git switch main
  git merge origin/dev
  git push origin main
```
With these commands the agent will switch to the main branch, merge with the dev branch and push the merge to main.

---

### Method 2 - Pre-build merge + Git Publisher merge results
This method will use a pre-build merge and then push to git.
  1. Change the "Branches to build" under "Source Code Management" to "*/dev"

  2. Remove the Build Step left behind from 
  3. Click "Add" under "Source Code Management" and click "Merge before build". Inside the new block:
     1. Enter "origin" in "Name of repository"
     2. Enter "main" in "Branch to merge to"
     3. Enter "default" in "Merge strategy"
     4. Enter "--ff" in "Fast-forward mode"
  4. Under "Post-build Actions" click "Add post-build action" and choose "Git Publisher" Inside the new block:
     1. Select "Merge Results" (This will push the merge you did in pre-build)
     2. Click "Add Branch"
     3. Enter "main" in "Branch to push"
     4. Enter "origin" in "Target remote name"  

⚠️ **IF YOU COPIED PROJECT FROM JOB 1**
1. **Delete the "Execute Shell" block under "Build Steps"**  
   If you do not delete the "Execute Shell" block, your job may not run successfully.
2. Deselect "SSH Agent" under "Build Environment"  
   This isn't necessary, but the SSH Agent isn't used in this method.

---

### Method 3 - Only Git Publisher push
This way technically does not do a merge, but will still push your changes from the dev branch to the main branch.
  1. Change the "Branches to build" under "Source Code Management" to "*/dev"

  2. Under "Post-build Actions" click "Add post-build action" and choose "Git Publisher" Inside the new block:
     1. Select "Push Only If Build Succeeds"
     2. Click "Add Branch"
     3. Enter "main" in "Branch to push"
     4. Enter "origin" in "Target remote name"

⚠️ **IF YOU COPIED PROJECT FROM JOB 1**
1. **Delete the "Execute Shell" block under "Build Steps"**  
   If you do not delete the "Execute Shell" block, your job may not run successfully.
2. Deselect "SSH Agent" under "Build Environment"  
   This isn't necessary, but the SSH Agent isn't used in this method.  

---

⚠️ After adding **ONE** of these methods **go back to Job 1** and add the Post Build Action mentioned at the [end of Job 1](#job-1---testing).  
If you do not do this, Job 2 will **NOT** trigger.


**COMPLETE THIS LAST STEP ONLY AFTER COMPLETING JOB 3**
  * Under "Post-build Actions" click "Add post-build action" and choose "Build other projects".
  * Choose the Job 3 project you have created and select "Trigger only if build is stable".

## Job 3 - Uploading to EC2
For this job, you can copy the project from Job 1. 
  1. Create a new item, enter a name for your item and choose enter your Job 3 name at the bottom to copy from it.
  2. Enter a description describing what your job will do.
  3. Change the "Branches to build" under "Source Code Management" to "*/main"
  4. Under "Build Environment" select "SSH Agent", then click "Add" and choose "Jenkins"  
  (Here is where we will add your AWS private key for your EC2 instance)
     1. Change the "Kind" to "SSH Username with private key"
     2. Add an ID and Username for your key
     3. Under "Private Key", click "Enter directly" then click "Add".
     4. Paste your AWS private key entirely.  
     ⚠️ **Make sure to include "-----BEGIN RSA PRIVATE KEY-----" and "-----END RSA PRIVATE KEY-----". Every single character in your key is needed.**
  5. Click on the "credentials" dropdown and choose the credentials you just created.
  6. If you didn't copy the project from Job 1, click "Add build step" under "Build Steps" and choose "Execute shell"

Next we need use the Execute Shell block to update the code in the live EC2 instance with the new code from your git repo. There are two ways of doing this, one with an `scp` command and one with an `rsync` command. Code may be different depending on where you have stored your app.

---

### Method 1 - SCP (Secure Copy)
If you have stored your code in the root directory, by using `scp` you cannot directly copy into the root directory due to permissions. Instead you can either:

1. SSH in and change the permissions of the directorym, then scp the app code to the root directory, SSH in again and restart the app.
```
ssh -o StrictHostKeyChecking=no ubuntu@<ENTER EC2 PUBLIC IP> "sudo chown -R ubuntu /tech610-tic-tac-toe/app"
scp -o StrictHostKeyChecking=no -r app ubuntu@<ENTER EC2 PUBLIC IP>:/tech610-tic-tac-toe/
ssh -o StrictHostKeyChecking=no ubuntu@<ENTER EC2 PUBLIC IP><<EOT
sudo pm2 restart TTT
echo "App has restarted with the changes"
EOT
```
* `sudo chown` is used to change the owner of the app directory to ubuntu, allowing you to use `scp` into the root directory.   
* You do not need the first command if your app is not in the root directory.
* 📝NOTE: `sudo pm2 restart TTT` TTT is the name of my PM2 process, instead you can use `index.js`

### OR

2. Copy the app code into /home/ubuntu, then SSH in and use `sudo` to `cp` (copy) it to the root directory where the app folder lives.

```
scp -o StrictHostKeyChecking=no -r app ubuntu@<ENTER EC2 PUBLIC IP>:/home/ubuntu
ssh -o StrictHostKeyChecking=no ubuntu@<ENTER EC2 PUBLIC IP><<EOT
sudo cp -r app /tech610-tic-tac-toe
rm -r app
cd /tech610-tic-tac-toe/app
sudo pm2 restart TTT
echo "App has restarted with the changes"
EOT
```
* I did `rm -r app` to remove the app copied into /home/ubuntu, so there are not unnecessary files wasting space.
* `-o StricHostKeyChecking=no` is used to automatically say Yes to the prompt when SSHing into a VM for the first time. If this isn't used, your commands may not run.

---

### Method 2 - RSYNC (Remote Sync)

```
rsync -avze "ssh -o StrictHostKeyChecking=no" --rsync-path="sudo rsync" app/ ubuntu@<ENTER EC2 PUBLIC IP>:/tech610-tic-tac-toe/app/
ssh -o StrictHostKeyChecking=no ubuntu@<ENTER EC2 PUBLIC IP><<EOT
cd /tech610-tic-tac-toe/app
sudo pm2 restart TTT
echo "App has restarted with the changes"
EOT
```
* With this method, rsync will only updates any changes between the directories, instead of overwriting the entire directory.
* `rsync -avze`:
  * `-a` Copies the files recursively whilst preserving permissions and metadata.
  * `-v` Prints information about what files rsync is transferring.
  * `-z` Compresses the file data during transfer to reduce network bandwidth.
  * `-e` Allows you to specify the remote shell (e.g. SSH) to use for the connection
* `--rsync-path="sudo rsync"` This allows rsync to run as super user, allowing us to execute the command in the root directory.  

📝NOTE: Remember to check if the path to your app directory is correct, otherwise it will try to copy or sync your app to the wrong directory.

## Testing the Pipeline
You can test your pipeline works by adding a date and time on line 100 in /app/server.js
![alt text](Images/serverjs_line100.png)  
Once you push your changes, your pipeline should start running from Job 1, all the way to Job 3.

If your timestamp shows up on the app (see below), then your pipeline worked!  

It's recommended to run your pipeline multiple times to see different changes. An example is below of the app running with 2 different hardcoded timestamps.  
![alt text](Images/timestap_1640.png)
![alt text](Images/timestamp_1643.png)