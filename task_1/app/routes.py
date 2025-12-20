from flask import jsonify
from app import app

@app.route('/')
def index():
    return """
    <h1>Добро пожаловать в Flask-сервис!</h1>
    <p>Этот сервис демонстрирует обработку пользовательского ввода через URL.</p>
    <ul>
        <li>Персональное приветствие: <a href="/hello/Пользователь">/hello/Пользователь</a></li>
        <li>Вычисление квадрата: <a href="/square/5">/square/5</a></li>
    </ul>
    """

@app.route('/hello/<name>')
def hello(name):
    return f"""
    <h2>Здравствуйте, {name}!</h2>
    <p><strong>Пояснение:</strong> Вы передали имя "{name}" в URL-пути.</p>
    <p>Сервис распознал его и сформировал персональное приветствие.</p>
    <a href="/">← Назад</a>
    """

@app.route('/square/<int:number>')
def square(number):
    result = number ** 2
    return f"""
    <h2>Вычисление квадрата</h2>
    <p><strong>Введённое число:</strong> {number}</p>
    <p><strong>Операция:</strong> возведение в квадрат</p>
    <p><strong>Результат:</strong> {number}² = {result}</p>
    <a href="/">← Назад</a>
    """