import tkinter as tk
from tkinter import filedialog

# 윈도우 창 만들기
window = tk.Tk()

# 윈도우 창 타이틀, 크기 설정
window.title("Merge Excel")
window.geometry("640x400+100+100")
window.resizable(False, False)


# 폴더 선택 함수
def selectFolder():
  # 폴더 선택하는 창 띄우기
  dirName = filedialog.askdirectory(parent=window)
  # 선택된 폴더 이름 라벨에 보여주기
  folderLabel.configure(text="선택된 폴더: " + dirName)
  print(dirName)
  # 선택된 폴더가 있을 때만 머지버튼 활성화
  if dirName:
    mergeBtn['state'] = 'normal'
  else:
    mergeBtn['state'] = 'disabled'


# 폴더 선택 버튼 생성 및 눌렀을 때 selectFolder 호출
folderBtn = tk.Button(window, text="폴더 선택", command=selectFolder)
folderBtn.pack()

# 선택된 폴더 보여주기 위한 텍스트라벨
folderLabel = tk.Label(window, text="선택된 폴더")
folderLabel.pack()

# 머지를 실행할 버튼
mergeBtn = tk.Button(window, text="Merge", command=selectFolder, state='disabled')
mergeBtn.pack()

window.mainloop()