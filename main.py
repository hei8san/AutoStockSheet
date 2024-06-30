import yfinance as yf
import base64
from data_management import DataManger


def retrieve_data(ticker) -> dict:
    stock = yf.Ticker(ticker)
    data = stock.info
    per = data['trailingPE']
    eps = data['trailingEps']
    stock_price = data['currentPrice']
    result = {"ticker": ticker, "per": per, "eps": eps, "stock_price": stock_price}
    return result




def hello_pubsub(event, context):
    """Triggered from a message on a Cloud Pub/Sub topic.
    Args:
         event (dict): Event payload.
         context (google.cloud.functions.Context): Metadata for the event.
    """
    try:
        if 'data' in event:
            pubsub_message = base64.b64decode(event['data']).decode('utf-8')
            # Further processing...
        else:
            print("Error: No data key present in the event.")
    except KeyError as e:
        print(f"KeyError: {str(e)} - Check the structure of the event object.")
    except base64.binascii.Error as e:
        print(f"Base64 Decode Error: {str(e)} - Check if the data is correctly base64 encoded.")
    except UnicodeDecodeError as e:
        print(f"Unicode Decode Error: {str(e)} - The decoded data might not be in UTF-8 format.")
    
    lst_stocks = ["NVDA"]
    # lst_stocks corresponds to the key of dict_gid in the DataManger class.  
        try:
            dict_data = retrieve_data(stock)
            obj_dataManagement = DataManger(dict_data)
            obj_dataManagement.to_spreadsheet(stock)
        except Exception as e:
            print(f"Error updating spreadsheet for {stock}: {e}")
