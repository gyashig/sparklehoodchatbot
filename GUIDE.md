## Hosting guide
### Flask only.

[culled from here](https://medium.com/techfront/step-by-step-visual-guide-on-deploying-a-flask-application-on-aws-ec2-8e3e8b82c4f7)

- Install gunicorn and add to your project requirements.
- Select the Ubuntu Server.
- Click on Review and Launch.
- set http tcp 80 under security groups and ssh tcp 22 to access from anywhere and add custom tcp for streamlit
- run `sudo apt-get update`
- run `sudo apt-get install python3-venv`
- clone project
- cd to the /etc/systemd/system folder
- create a <project>.service file
- Edit the following and add to the file

```
[Unit]
Description=Gunicorn instance for a simple hello world app
After=network.target
[Service]
User=ubuntu
Group=www-data
WorkingDirectory=/home/ubuntu/helloworld
ExecStart=/home/ubuntu/helloworld/venv/bin/gunicorn -b localhost:8000 app:app
Restart=always
[Install]
WantedBy=multi-user.target
```

- run `sudo systemctl daemon-reload`
- run `sudo systemctl start <project>`
- run `sudo systemctl enable <project>`

## Install nginx

- run `sudo apt-get install nginx`
- run `sudo systemctl start nginx`
- run `sudo systemctl enable nginx`

### Edit the default sites-available file

- run `sudo nano /etc/nginx/sites-available/default`
- Add this to the file below the comments

```
upstream <project> {
    server 127.0.0.1:8000;
}
```

- Clear the location/ block and add `proxy_pass http://<project>;`

```
location / {
    proxy_pass http://<project>;
}

```

- run `sudo systemctl restart nginx`


# For streamlit

- run `streamlit run frontend.py`
- To have it running after you exit the terminal, carry out the following steps:
    - run  `sudo apt-get install tmux`
    - run `tmux new -s StreamSession`
    - then run `streamlit run frontend.py`