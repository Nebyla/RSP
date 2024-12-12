import socket
import tkinter as tk

class FinalClientApp:
    def __init__(self, master, server_address, port):
        self.master = master
        self.master.title("Последние сообщения")
        self.text_box = tk.Text(master, width=50, height=10)
        self.text_box.pack()
        
        self.server_address = server_address
        self.port = port
        
        self.update_messages()
    
    def update_messages(self):
        try:
            with socket.create_connection((self.server_address, self.port)) as sock:
                messages = sock.recv(1024).decode()
                self.text_box.delete(1.0, tk.END)
                self.text_box.insert(tk.END, messages)
        except ConnectionError:
            self.text_box.insert(tk.END, "Ошибка подключения.")
        
        self.master.after(10000, self.update_messages)

if __name__ == "__main__":
    root = tk.Tk()
    app = FinalClientApp(root, 'localhost', 12345)  # Укажите фиксированный порт TCP-сервера
    root.mainloop()