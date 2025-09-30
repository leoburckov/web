from http.server import HTTPServer, BaseHTTPRequestHandler


class SimpleHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        """Обрабатывает GET-запросы и возвращает соответствующие страницы"""
        try:
            # Определяем какая страница запрашивается
            if self.path == '/':
                filepath = 'pages/index.html'
            elif self.path == '/catalog':
                filepath = 'pages/catalog.html'
            elif self.path == '/category':
                filepath = 'pages/category.html'
            elif self.path == '/contacts':
                filepath = 'pages/contacts.html'
            else:
                # Для любых других путей возвращаем контакты
                filepath = 'pages/contacts.html'

            # Читаем HTML-файл
            with open(filepath, 'r', encoding='utf-8') as file:
                html_content = file.read()

            # Отправляем ответ
            self.send_response(200)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.end_headers()
            self.wfile.write(html_content.encode('utf-8'))

        except FileNotFoundError:
            self.send_error(404, "File not found")

    def log_message(self, format, *args):
        print(f"GET {self.path}")


def run_server():
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, SimpleHandler)

    print("🚀 Сервер запущен на http://localhost:8000")
    print("📄 Доступные страницы:")
    print("   / - Главная")
    print("   /catalog - Каталог")
    print("   /category - Категория")
    print("   /contacts - Контакты")
    print("   /any-other-path - Контакты")
    print("⏹️  Для остановки: Ctrl+C")

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n🛑 Сервер остановлен")
        httpd.shutdown()


if __name__ == '__main__':
    run_server()