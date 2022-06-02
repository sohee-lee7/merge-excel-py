import tkinter as tk
from tkinter import filedialog
from merge import merge_excel

# 윈도우 창 만들기
window = tk.Tk()

# 윈도우 창 타이틀, 크기 설정
window.title("Merge Excel")
window.geometry("640x400+100+100")
window.resizable(False, False)


directory = ''
target_header = ''
regex = ''

# 폴더 선택 함수
def select_folder():
  # 폴더 선택하는 창 띄우기
  directory = filedialog.askdirectory(parent=window)

  # 선택된 폴더 이름 라벨에 보여주기
  folder_label.configure(text="선택된 폴더: " + directory)


# 폴더 선택 버튼 생성 및 눌렀을 때 selectFolder 호출
folder_btn = tk.Button(window, text="폴더 선택", command=select_folder)
folder_btn.pack()

# 선택된 폴더 보여주기 위한 텍스트라벨
folder_label = tk.Label(window, text="선택된 폴더")
folder_label.pack()

# 변경할 컬럼 헤더 이름
header_entry = tk.Entry(window)
header_entry.pack()

# 정규식
regex_entry = tk.Entry(window)
regex_entry.insert(0, '-[a-zA-Z0-9]*')
regex_entry.pack()

def merge_btn_command():
  print('merge_btn_command')
  if directory & header_entry.get() & regex_entry.get():
    merge_btn['state'] = 'normal'
    merge_excel(directory=directory, target_header=header_entry.get(), regex=regex_entry.get())
  else:
    merge_btn['state'] = 'disabled'


# 머지를 실행할 버튼
merge_btn = tk.Button(window, text="Merge", command=merge_btn_command, state='disabled')
merge_btn.pack()

window.mainloop()