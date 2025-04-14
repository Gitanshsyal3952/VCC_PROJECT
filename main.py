import requests

def get_data(request):
    request_args = request.args

    if not request_args:
        return {"error": "Missing query parameters"}, 400

    data_type = request_args.get('type')
    query = request_args.get('query')

    if not data_type or not query:
        return {"error": "Missing 'type' or 'query'"}, 400

    if data_type == 'weather':
        # Replace this with your real API key from OpenWeatherMap
        api_key = 'bca8a8f69286338b683aa623a44abfde'
        url = f'https://api.openweathermap.org/data/2.5/weather?q={query}&appid={api_key}&units=metric'
    elif data_type == 'stock':
        # Replace this with your real API key from Alpha Vantage
        api_key = 'ZRNI3J784CAZHM75'
        url = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={query}&apikey={api_key}'
    else:
        return {"error": "Invalid type. Use 'weather' or 'stock'"}, 400

    response = requests.get(url) 
