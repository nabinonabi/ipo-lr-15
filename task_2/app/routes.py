from flask import request, jsonify
from app import app

@app.route('/calc')
def calc():
    a = request.args.get('a')
    b = request.args.get('b')
    op = request.args.get('op')

    
    if a is None or b is None or op is None:
        return jsonify({
            "error": "Отсутствуют параметры",
            "пояснение": "Требуются параметры: a (число), b (число), op (операция: +, -, *, /)",
            "пример": "/calc?a=5&b=3&op=+"
        }), 400

    try:
        a = float(a)
        b = float(b)
    except ValueError:
        return jsonify({
            "error": "Некорректный ввод",
            "пояснение": "Параметры a и b должны быть числами",
            "получено": {"a": a, "b": b}
        }), 400

    if op == '+':
        result = a + b
        desc = "сложение"
    elif op == '-':
        result = a - b
        desc = "вычитание"
    elif op == '*':
        result = a * b
        desc = "умножение"
    elif op == '/':
        if b == 0:
            return jsonify({
                "error": "Деление на ноль",
                "пояснение": "Параметр b не может быть равен нулю при делении"
            }), 400
        result = a / b
        desc = "деление"
    else:
        return jsonify({
            "error": "Неподдерживаемая операция",
            "пояснение": "Поддерживаются только: +, -, *, /",
            "получено": op
        }), 400

    
    return jsonify({
        "ввод": {"a": a, "b": b, "операция": op},
        "операция_описание": desc,
        "результат": result,
        "пояснение": f"Результат {desc} чисел {a} и {b} равен {result}"
    })

@app.route('/status')
def status():
    return jsonify({
        "status": "running",
        "service": "Flask App",
        "пояснение": "Сервис работает корректно и готов обрабатывать запросы."
    })