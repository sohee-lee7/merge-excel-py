from ntpath import join
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from merge import merge_excel

# 윈도우 창 만들기
window = tk.Tk()

# 윈도우 창 타이틀, 크기 설정
window.title("Merge Excel")
window.geometry("400x200+300+300")
window.resizable(False, False)

# 폴더 선택 함수
def select_folder():
  # 폴더 선택하는 창 띄우기
  directory = filedialog.askdirectory(parent=window)

  # 선택된 폴더 이름 라벨에 보여주기
  if directory:
    folder_label.configure(text=directory)
  else:
    folder_label.configure(text="없음")


# 폴더 선택 버튼 생성 및 눌렀을 때 selectFolder 호출
folder_btn = tk.Button(window, text="폴더 선택", command=select_folder)
folder_btn.grid(row=1, column=1)

# 선택된 폴더 보여주기 위한 텍스트라벨
folder_label = tk.Label(window, text="없음")
folder_label.grid(row=1, column=2)

# 변경할 컬럼 헤더 이름
header_label = tk.Label(window, text="변경할 헤더")
header_label.grid(row=2, column=1)

header_entry = tk.Entry(window)
header_entry.grid(row=2, column=2)

# 정규식
regex_label = tk.Label(window,text= "정규식")
regex_label.grid(row=3, column=1)

regex_entry = tk.Entry(window)
regex_entry.insert(0, "-[a-zA-Z0-9]*")
regex_entry.grid(row=3,column=2)


def merge_btn_command():
  print(folder_label["text"] + ", " + header_entry.get() + ", " + regex_entry.get())

  # 선택된 폴더와 변경할 헤더 이름, 정규식 모두 값이 있을 뗴만 머지 실행
  if folder_label["text"] != "없음" and header_entry.get() and regex_entry.get():
    try:
      result_files = merge_excel(directory=folder_label["text"], target_header=header_entry.get(), regex=regex_entry.get())
      messagebox.showinfo("success", ','.join(result_files) + "파일들이 생성되었습니다.")
    except:
      messagebox.showerror("error", "merge 중에 에러가 발생했습니다.")
  else:
    messagebox.showwarning("waring", "merge를 실행할 수 없습니다.")


# 머지를 실행할 버튼
merge_btn = tk.Button(window, text="Merge", command=merge_btn_command)
merge_btn.grid(row=4, column=2)

window.mainloop()