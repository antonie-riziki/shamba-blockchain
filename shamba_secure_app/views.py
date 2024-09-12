from django.shortcuts import render
from web3 import Web3
import requests


api_key = 'm3dJf2Waus5ilDaKsDZVYVtjAPl6XFTLvyiG5B93UYzk0eb5VC97SQ'

# Replace 'infura_url' with your actual Infura URL
infura_url = "https://mainnet.infura.io/v3/7f7b280ecacf409da9cdc5ab74def507"

# Initialize a Web3 instance using HTTPProvider
token = Web3(Web3.HTTPProvider(infura_url))

print(token)


# Create your views here.
def home(request):
    return render(request, 'index.html')


def user_dashboard(request):
    account = token.eth.account.create('!ROTD2014fhd!')

    # privateKey = account.key.hex()
    # address = account.address

    context = {
        'privateKey': account.key.hex(),
        'address':  account.address,
    }

    return render(request, 'user-dashboard.html', context)


def real_estate_dash(request):
    return render(request, 'real-estate-dash.html')