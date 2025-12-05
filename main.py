import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import pyperclip
import re
from collections import defaultdict


class BufferParserApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Парсер буфера обмена")
        self.root.geometry("800x600")
        
        # Создание интерфейса
        self.create_widgets()
    
    def create_widgets(self):
        # Кнопка "Вставить из буфера"
        self.btn_paste = tk.Button(
            self.root,
            text="Вставить из буфера",
            command=self.parse_buffer,
            font=("Arial", 12),
            padx=10,
            pady=5
        )
        self.btn_paste.pack(pady=10)
        
        # Фрейм для меток с количеством строк
        info_frame = tk.Frame(self.root)
        info_frame.pack(pady=5, padx=10, fill=tk.X)
        
        # Метка "Количество строк"
        self.label_count = tk.Label(
            info_frame,
            text="Количество строк: 0",
            font=("Arial", 12)
        )
        self.label_count.pack(side=tk.LEFT)
        
        # Метка "Итого строк"
        self.label_total = tk.Label(
            info_frame,
            text="Выведено строк: 0",
            font=("Arial", 12)
        )
        self.label_total.pack(side=tk.RIGHT)
        
        # Текстовое поле с прокруткой
        self.text_output = scrolledtext.ScrolledText(
            self.root,
            wrap=tk.WORD,
            font=("Courier", 14),
            width=80,
            height=25
        )
        self.text_output.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)
    
    def parse_buffer(self):
        try:
            # Получаем текст из буфера обмена
            clipboard_text = pyperclip.paste()
            
            # Проверяем, что в буфере находится текст
            if not clipboard_text or not isinstance(clipboard_text, str):
                messagebox.showwarning("Предупреждение", "В буфере обмена нет текста!")
                return
            
            # Разбиваем на строки
            lines = clipboard_text.strip().split('\n')
            lines = [line.strip() for line in lines if line.strip()]
            
            # Обновляем количество строк
            self.label_count.config(text=f"Количество строк: {len(lines)}")
            
            # Парсим пути
            parsed_paths = []
            for line in lines:
                # Удаляем кавычки
                line = line.replace('"', '').replace("'", '')
                
                # Извлекаем путь
                path = line.strip()
                
                # Разбиваем путь на части
                path_parts = [part for part in path.replace('\\', '/').split('/') if part]
                
                if len(path_parts) >= 2:
                    # Берем предпоследнюю и последнюю папку
                    second_last_folder = path_parts[-2]
                    last_folder = path_parts[-1]
                    parsed_paths.append((second_last_folder, last_folder))
                elif len(path_parts) == 1:
                    # Если только одна папка, используем её и для предпоследней, и для последней
                    parsed_paths.append((path_parts[0], path_parts[0]))
            
            # Группируем по предпоследней папке
            grouped = defaultdict(list)
            for second_last, last in parsed_paths:
                grouped[second_last].append(last)
            
            # Сортируем группы по предпоследней папке, а внутри группы - по последней папке
            sorted_groups = sorted(grouped.items())
            for key in sorted_groups:
                grouped[key[0]] = sorted(key[1])
            
            # Формируем вывод с группировкой
            output_lines = []
            sorted_group_keys = sorted(grouped.keys())
            
            for i, second_last_folder in enumerate(sorted_group_keys):
                # Название группы (предпоследняя папка)
                output_lines.append(second_last_folder)
                
                # Список последних папок с табуляцией
                for last_folder in sorted(grouped[second_last_folder]):
                    output_lines.append(f"\t{last_folder}")
                
                # Пустая строка между группами (кроме последней)
                if i < len(sorted_group_keys) - 1:
                    output_lines.append("")
            
            # Выводим в текстовое поле
            self.text_output.delete(1.0, tk.END)
            self.text_output.insert(1.0, '\n'.join(output_lines))
            
            # Подсчитываем количество выведенных последних папок (без учета групп и пустых строк)
            total_last_folders = sum(len(folders) for folders in grouped.values())
            
            # Обновляем итоговое количество строк
            self.label_total.config(text=f"Выведено строк: {total_last_folders}")
            
        except Exception as e:
            messagebox.showerror("Ошибка", f"Произошла ошибка: {str(e)}")


def main():
    root = tk.Tk()
    app = BufferParserApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()

