from app import app

if __name__ == '__main__':
    print("Запуск Flask-сервиса")
    print("Маршруты:")
    print("   - GET /calc?a=...&b=...&op=...")
    print("   - GET /status")
    print("\nПоддерживаемые операции: +, -, *, /")
    print("Пример: http://127.0.0.1:5000/calc?a=10&b=2&op=*")
    app.run(debug=True)