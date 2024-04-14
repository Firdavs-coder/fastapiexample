# Auto Deployment

## I just learnt how to auto deploy with Github and SSH. So, I want to share with you the steps

1. Deploy the project on github

2. Go to the your server and generate ssh key:
   - `ssh-keygen -t key_name -C "<your_email@example.com>"`
   - Press enter
   - `cat /root/.ssh/key_name` (SSH_PRIVATE_KEY)
   - `cat /root/.ssh/key_name.pub` (SSH_key)
   - `cat /root/.ssh/key_name.pub » authorize_keys`

3. Go to Github/Settings/SSH and GPG Keys and click 'New SSH key' button and add your SSH_key

4. Go to your project on github and go to settings of your repository. There, you browse '`Secrets and variables/Actions`' and click '`New Repository button`' and add these:
   - `SERVER_IP` which is your server ip address
   - `SERVER_USERNAME` which is  your server username. Mostly, it is named `root`
   - `SSH_PORT` which is your server port. Mostly, it is `22`
   - `SSH_PRIVATE_KEY` which is ssh private key that you generate above

5. On your project, create .github/workflows folder and inside it, create deploy.yml file.

6. Inside, the deploy.yml file, paste this:

```shell
name: Somehow Name :)

on:
  push:
    branches:
      - main

jobs:
  deploy:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v2

      - name: SSH into server and deploy
        uses: appleboy/ssh-action@master
        with:
          host: ${{ secrets.SERVER_IP }}
          username: ${{ secrets.SERVER_USERNAME }}
          key: ${{ secrets.SSH_PRIVATE_KEY }}
          port: ${{ secrets.SSH_PORT }}
          script: |
            cd path_to_your_project_on_server
            git pull origin main
            pip install -r requirements.txt
```

7. Copy your repository ssh. For example, `git@github.com:YOUR-USERNAME/project.git`. It would be on Code button and clone your project on the server with that ssh.

8. If you use docker, just run these commands:
   - `docker build -t name_for_image .`
   - `docker run --name name_for_container -p 80:80 -d -v $(pwd):/app name_for_image`

or not, just add these line at deploy.yml after the installation of requirements.txt

- `systemctl restart service_name`

P.S: It is basic sample to auto deployment. I wrote this post because I use this post to copy the commands while deployment :)
