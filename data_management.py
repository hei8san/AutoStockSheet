import gspread as gc
from datetime import date



class DataManger:
    def __init__(self, data: dict) -> None:
        self.data = data
        self.dict_gid = {"NVDA": 228254102, "TPR": 1833218885, "MSFT": 168617616, "QQQ": 600061735, "^GSPC": 36600606, "GS": 821506004, "GOOG": 2116979974, "AMZN": 1678571736, "LLY": 1757361579 }
        # dict_gid is {'Name of Sheet': 'ID of sheet'}
        # ID of sheet is the last part of URL of sheet 
    def to_spreadsheet(self, ticker):
        client = gc.service_account(filename='./sheet-yfinance-per-graph-cca9c444edb4.json')
        wb_1 = client.open('WB1')
        sheet = wb_1.get_worksheet_by_id(self.dict_gid[ticker])
        # dd/mm/YY
        next_row = len(sheet.get_all_values()) + 1
        today = date.today()
        d1 = today.strftime("%Y/%m/%d")
        sheet.update_cell(next_row,1, d1)
        try:
            # stock_price
            stock_price = self.data['stock_price']
            sheet.update_cell(next_row,2, stock_price)
            # per
            per = self.data['per']
            sheet.update_cell(next_row,3, per)
            # eps
            eps = self.data['eps']
            sheet.update_cell(next_row,4, eps)
        except:
            print("Error occurs")
            
        
        
        
        
        
        

