[![Run Tests](https://github.com/lindavos-dot/CD/actions/workflows/run-tests.yml/badge.svg)](https://github.com/lindavos-dot/CD/actions/workflows/run-tests.yml)


## Continuous Deployment Pipeline with GitHub Actions and Digital Ocean

### Components
My solution uses the following components:

- **GitHub Actions:** An automation tool provided by GitHub that helps to test, build and deploy my code from GitHub repositories to my Droplet on Digital Ocean.
- **Digital Ocean Droplet:** A virtual private server (VPS) hosted by Digital Ocean, or what Digital Ocean calls a droplet. 
- **SSH:** Instead of a password-access to the Digital Ocean Droplet.

### Problems Encountered
During the implementation of the CD-part pipeline, I encountered the following problems:

1. **SSH Authentication:** Initially, I was afraid that creating an SSH key would block access to the droplet. For example, I couldn't find the directory where the keys were stored. So, I created a new droplet to experiment with creating SSH keys. I created and removed SSH keys locally and created droplets with direct SSH key login. As I became more familiar with it, I realized that it's silly to think that access would be blocked. Logging in would actually become much easier. The last step was converting logging in by password to an SSH key. By searching the droplet, I found that there was a default .ssh/ directory where I put the public key. However, After i wrote Deloy in .yml file Github Actions couldn't log in to the droplet. It turned out that I had forgotten to include the text of the private key in github secrets...

2. **appleboy:** I thought that this would allow me to log in and in my script i would say something like: scp -r main.py root@<ip>:/home/farm. Of course, that would be a great solution! (...ehh) After properly setting up the SSH key in the deployment part, a Winc teacher indicated that I still needed to find a way to transfer the files from the repo to the server. I thought, it's strange that he says that. There must be another solution other than my first idea. And that turned out to be true. Using appleboy/scp-action for copying files is a way more straightforward solution, as it is specifically designed for file transfers. I think that this solution is much more robust and has actually prevented me from running into an error in this part.

3. **.yml file: script:** What am I going to put in my script? I thought the script would be an extensive text similar to the contents of the .yml file. At some point, I understood the difference between appleboy/scp-action and appleboy/ssh-action. During a Winc practice, I manually transferred a file to the server and performed a restart by typing commands. With appleboy/scp-action, I transferred the files. What else do I needs to be done? Exactly, the same of course! Github Actions needs to go to the directory and give a restart command. AND IT WORKS!! :) I was very happy!! Since it worked, I thought, let it be just like this. It's only two commands. Because you can see at once what is in the .yml file, I think it is unnecessary to create a special sh file. It doesn't outweigh a lot of scroll work and so that layout makes it more disorganized for me. 