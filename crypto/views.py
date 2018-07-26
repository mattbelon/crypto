from django.shortcuts import render

# Create your views here.   
def home(request):
    import requests
    import json
    prices_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH,EOS,ETC,CET&tsyms=USD")
    prices = json.loads(prices_request.content)

    api_request = requests.get("https://min-api.cryptocompare.com/data/v2/news/?lang=EN")
    api = json.loads(api_request.content)
    return render(request, 'home.html',{'api':api,'prices':prices})

def prices(request):
    if request.method == 'POST':
        import requests
        import json
        query = request.POST['query']
        query = query.upper()
        crypto_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms="+query+"&tsyms=USD")
        crypto = json.loads(crypto_request.content)
        return render(request, 'prices.html',{'query':query,'crypto':crypto})

    else:
        return render(request, 'prices.html',{})