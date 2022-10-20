# Print a list of games with Indian servers

A simple python script which queries BattleMetrics server (thanks for the API folks <3). And creates a list of games with verifyable Indian servers.

## How to run

- Install Python (depending on your os it might vary, google it)
- Install requests via `pip install requests`
- Go to [battlemetrics](https://www.battlemetrics.com/account/register), register and create an access token
- Paste the access token in value TOKEN in the script. It will look something like ```TOKEN = 'asdhajkshdkahsdkjahsd...'```
- Run the script via `python bm.py`

## TODO

- Add more APIs?
- Integrate it to a webservice