
import openpyxl
import csv
import pyexcelerate
import pdfplumber

def csv_to_excel(fn, coding="utf-8"):
    with open(fn, encoding=coding) as fr:
        rows = csv.reader(fr)
        data = [r for r in rows]
    wb = pyexcelerate.Workbook()
    wb.new_sheet(fn.split("/")[0], data=data)
    wb.save(fn.replace("csv", 'xlsx'))


def xlsx_to_csv(fn):
    ''' change xlsx or xls file to csv depends on openpyxl '''
    wb = openpyxl.load_workbook(filename=fn, read_only=True)
    sheet_name = wb.get_sheet_names()
    # print(sheet_name)  # 查看 excel 共有几张表
    sheet = wb[sheet_name[0]]  # 选择操作 excel 文件的第一张表
    with open('result.csv', 'w', newline='', encoding='utf-8') as fw:
        ww = csv.writer(fw)
        for r in sheet.rows:
            row = [i.value for i in r]
            ww.writerow(row)

def pdf_to_txt(fn):
    with pdfplumber.open(fn) as pdf:
        for page in pdf.pages:
            txtdata = page.extract_text()
            with open('result.txt', 'w', encoding='utf-8') as fw:
                fw.write(txtdata)

def main(fil, method = 0):
    fn = fil
    if method == 0:
        csv_to_excel(fn)
    elif method == 1:
        xlsx_to_csv(fn)
    elif method == 2:
        pdf_to_txt(fn)

if __name__ == '__main__':
    main()