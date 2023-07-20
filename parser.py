import requests

req = requests.get('https://api.battlemetrics.com/servers/17389558')
task = req.json()
data = task.get('data')
count = data.get('attributes')
name = count.get('name')
players = count.get('players')
maxPlayers = count.get('maxPlayers')
status = count.get('status')
print(f'{name}: {players}/{maxPlayers}.\n {status}')