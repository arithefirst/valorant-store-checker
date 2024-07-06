                     
<h1 align="center" style="font-weight: bold;">💻 Valorant Store Notifyer 💻</h1>

<p align="center">A python tool to send you the contents of your Valorant shop every time it refreshes (00:00 UTC)</p>


<p align="center">
<a href=""></a>
</p>
 
<h2 id="started">🚀 Getting started 🚀</h2>

 
 
<h3>Prerequisites</h3>

To run this project you will need
- A Linux Sever
- [Python 3.12](https://www.python.org/downloads/release/python-3120/)
 
<h3 id="cloning">Cloning</h3>

To clone this project locally run
```bash
git clone https://github.com/arithefirst/valorant-store-checker.git
```
 
<h3 id="env">Config .env variables</h2>

Use the `.env.example` as reference to create your configuration file `.env` with your Riot Games Credentials

```yaml
PASSWORD="Your Password"
USERNAME="Your Username"
DISCORD_WEBHOOK_URL="Your Discord Webhook URL"
```

**Important Note:** None of this information will ever be shared with the developers.

<h3 id="usage">Usage</h3>
To Setup this project, follow the steps below:

1) <a href=#cloning>Clone this project locally</a>
2) <a href=#env>Setup your .env file</a>
3) Run <a href="https://github.com/arithefirst/valorant-store-checker/blob/main/main.py">`main.py`</a> to check the items in your store and send them to your webhook

<h3>Automation</h3>
To Automate this project, follow the steps below:

1) Follow <a href="#usage">steps 1 and 2 in "Usage"</a>
2) Run the command `crontab -e`
3) In the text editor that opens, add `1 0 * * * python /root/{Path to Cloned Repo}/main.py >/dev/null 2>&1`
4) Replace {Path to cloned Repo} with the path to the locally cloned repository

