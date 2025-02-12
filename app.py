from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route('/')
def index():
    # Запрос к API для получения случайной цитаты
    response = requests.get('https://zenquotes.io/api/random')
    quote_data = response.json()[0]  # Получаем первую цитату из ответа
    quote = quote_data['q']
    author = quote_data['a']

    return render_template('index.html', quote=quote, author=author)


if __name__ == '__main__':
    app.run(debug=True)
