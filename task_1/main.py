from app import app

if __name__ == '__main__':
    print("Запуск Flask-сервиса")
    print("Доступные маршруты:")
    print("   - GET /")
    print("   - GET /hello/<name>")
    print("   - GET /square/<number>")
    print("\nОткройте: http://127.0.0.1:5000")
    app.run(debug=True)