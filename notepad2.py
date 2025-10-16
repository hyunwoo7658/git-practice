import tkinter as tk

# 기본 창 생성
window = tk.Tk()

# 창 제목 설정
window.title("메모장")

# 메뉴바 생성
menubar = tk.Menu(window)

# 파일 메뉴 생성
file_menu = tk.Menu(menubar, tearoff=0)
file_menu.add_command(label="새 파일")
file_menu.add_command(label="열기")
file_menu.add_command(label="저장")
file_menu.add_separator()
file_menu.add_command(label="끝내기", command=window.quit)

# 메뉴바에 파일 메뉴 추가
menubar.add_cascade(label="파일", menu=file_menu)

# 편집 메뉴 생성
edit_menu = tk.Menu(menubar, tearoff=0)
edit_menu.add_command(label="잘라내기")
edit_menu.add_command(label="복사하기")
edit_menu.add_command(label="붙여넣기")
menubar.add_cascade(label="편집", menu=edit_menu)

window.config(menu=menubar)

# 텍스트 입력을 위한 Text 위젯 생성
text_area = tk.Text(window)
text_area.pack(expand=True, fill='both') # 창 크기에 맞게 확장

# 창이 화면에 계속 표시되도록 이벤트 루프 실행
window.mainloop()
