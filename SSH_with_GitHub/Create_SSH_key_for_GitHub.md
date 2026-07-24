# Creating an SSH key pair for GitHub

### Using Git Bash, Create the Key Pair
1. CD into your .ssh directory
2. Create the keypair using this command:
```
ssh-keygen -t ed25519 -a 100 -C "firstname@techxxx-pc-or-laptop"
```
3. Enter a name for your key e.g. "techXXX-firstname-github-key".
4. You can enter a passphrase if you wish for extra security, or leave it empty.
5. Your key should now be created.   

You will have two new files in your .ssh folder with the name you entered in step 3. The public key will have a .pub extension, outlining that is the public key.


### Adding private SSH key to your ssh-agent
You now need to add your private key to your ssh-agent, so it can be used for authentication.

1. Run the command:
```
eval `ssh-agent -s`
```
2. Now you can add your private key:
```
ssh-add <name of key>
```
Make sure it is the private key you have added, not the public one.   
The public key has a file extension ".pub".

### Adding public key to GitHub account

1. Log into your GitHub account on the GitHub website.
2. Go to Settings and click on SSH and GPG keys.
3. Click "New SSH key".
4. Add a name for your public key
5. Make sure the Key type is Authentication Key
6. Open a git bash terminal and type:
```
cat ~/.ssh/<name of key>
```
⚠️Disclaimer: This is assuming you have stored your ssh key in ~/.ssh  

7. Copy what the terminal output and paste it into the Key box in GitHub.  
8. Click "Add SSH key"

### Check it works
To check we have successfully connected to GitHub using ssh we can use the following command:
```
ssh -T git@github.com
```

It should output "Hi user! You've successfully authenticated, but GitHub does not provide shell access."