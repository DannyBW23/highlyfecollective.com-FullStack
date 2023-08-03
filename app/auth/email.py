
import requests
def send_mail(to_address ,text):
	url = 'https://api.mailgun.net/v3/{}/messages'.format('highlyfecollective.com')
	auth = ('api', '88d3d636fe020ca0b81cd506dc52635a-4e034d9e-6046f5a2')
	data = {
        'from': 'Highlyfe Collective LLC <mailgun@{}>'.format('highlyfecollective.com'),
        'to': to_address,
        'subject': 'Reset Password',
        'html': text
    }

	response = requests.post(url, auth=auth, data=data)
	response.raise_for_status()


