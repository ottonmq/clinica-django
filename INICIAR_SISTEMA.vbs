Set WshShell = CreateObject("WScript.Shell")

WshShell.Run "cmd.exe /c cd /d C:\Users\ASUS\desktop\program\Django && python manage.py runserver", 0, vbFalse
