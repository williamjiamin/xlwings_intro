import xlwings as xlwings

def SayHello():
	wb = xw.Book.caller()
	wb.sheet["Sheet1"].range("E10").value = "Hello, I  am William"