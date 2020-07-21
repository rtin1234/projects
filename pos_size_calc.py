'''
Position Size Calculator

This script automates the position size calculation formula

EXTRA: Do the same for equity pairs

EXTRA: Make it compatible as an android app

'''

from alpha_vantage.foreignexchange import ForeignExchange
import tkinter as tk

VALUE_PER_PIP = 10          # for Standard Lots

leverage = {
    'audcad': 20,
    'audchf': 20,
    'audhkd': 10,
    'audjpy': 20,
    'audnzd': 20,
    'audsgd': 20,
    'audusd': 20,
    'cadchf': 30,
    'cadhkd': 10,
    'cadjpy': 30,
    'cadsgd': 20,
    'chfhkd': 10,
    'chfjpy': 30,
    'chfzar': 20,
    'euraud': 20,
    'eurcad': 30,
    'eurchf': 30,
    'eurczk': 20,
    'eurdkk': 20,
    'eurgbp': 30,
    'eurhkd': 10,
    'eurhuf': 20,
    'eurjpy': 30,
    'eurnok': 20,
    'eurnzd': 20,
    'eurpln': 20,
    'eursek': 20,
    'eursgd': 20,
    'eurtry': 20,
    'eurusd': 30,
    'eurzar': 20,
    'gbpaud': 20,
    'gbpcad': 30,
    'gbpchf': 30,
    'gbphkd': 10,
    'gbpjpy': 30,
    'gbpnzd': 20,
    'gbppln': 20,
    'gbpsgd': 20,
    'gbpusd': 30,
    'gbpzar': 20,
    'hkdjpy': 10,
    'nzdcad': 20,
    'nzdchf': 20,
    'nzdhkd': 10,
    'nzdjpy': 20,
    'nzdsgd': 20,
    'nzdusd': 20,
    'sgdchf': 20,
    'sgdhkd': 10,
    'sgdjpy': 20,
    'tryjpy': 20,
    'usdcad': 30,
    'usdchf': 30,
    'usdcnh': 20,
    'usdczk': 20,
    'usddkk': 20,
    'usdhkd': 10,
    'usdhuf': 20,
    'usdinr': 20,
    'usdjpy': 30,
    'usdmxn': 20,
    'usdnok': 20,
    'usdpln': 20,
    'usdsar': 20,
    'usdsek': 20,
    'usdsgd': 20,
    'usdthb': 20,
    'usdtry': 20,
    'usdzar': 20,
    'zarjpy': 20
}

# Milestone 1.1: Create the script to run for forex pairs
def position_size():
    '''
    Calculates the proper position size accounting for risk
    Position Size in Lots = (account size in quote currency * rink in %) / (stop loss in pips * value per pip)
    '''
    pair = str(entry_currency_pair.get())
    acnt_size = float(entry_acc_size.get())
    quote = str(pair[-3:])
    stop_loss = float(entry_stop_loss.get())
    risk = float(entry_risk.get())/100
    accnt_size_in_quote = acnt_size * fx_quote('CHF', quote)
    pos_size = round((accnt_size_in_quote * risk) / (stop_loss * VALUE_PER_PIP), 3)

    if quote != 'jpy':
        lbl_pos_size_result['text'] = pos_size
        nom_pos_size = pos_size * 100000

    else:
        lbl_pos_size_result['text'] = pos_size/100
        nom_pos_size = pos_size/100 * 100000

    margin_req = round(nom_pos_size / leverage[pair], 2)
    lbl_margn_req_result['text'] = margin_req

# Milestone 1: Figure out how to use Alpha Vantage API
# The FREE version of Alpha Vantage only allows 5 requests per minute and a maximum of 500 requests per day.
def fx_quote(base, quote):
    API_KEY = 'NHFTFC9ZTIBUUPZO'
    fx = ForeignExchange(API_KEY)
    data = fx.get_currency_exchange_rate(from_currency='CHF', to_currency=quote)
    data = list(data)
    return float(data[0]['5. Exchange Rate'])

# Milestone 2: create a GUI so that it can run as an app and not in the terminal
window = tk.Tk()
window.title("Position Size Calculator")

# FIRST ROW
lbl_currency_pair = tk.Label(text='Currency Pair: ', bg='white', fg='black')
entry_currency_pair = tk.Entry()
lbl_currency_pair.grid(row=0, column=0, sticky="NSEW")
entry_currency_pair.grid(row=0, column=1, sticky='NSEW')


# SECOND ROW
lbl_acc_size = tk.Label(text='Account Size: (CHF)', bg='white', fg='black')
entry_acc_size = tk.Entry()
lbl_acc_size.grid(row=1, column=0, sticky="NSEW")
entry_acc_size.grid(row=1, column=1, sticky="E")

# THIRD ROW
lbl_risk = tk.Label(text="Risk (%): ", bg='white', fg='black')
entry_risk = tk.Entry()
lbl_risk.grid(row=2, column=0, sticky='NSEW')
entry_risk.grid(row=2, column=1, sticky='W')

# FOURTH ROW
lbl_stop_loss = tk.Label(text="Stop Loss (pips): ", bg='white', fg='black')
entry_stop_loss = tk.Entry()
lbl_stop_loss.grid(row=3, column=0, sticky='NSEW')
entry_stop_loss.grid(row=3, column=1, sticky='E')


# FIFTH ROW (BUTTON) #TODO Link Button
button_calc = tk.Button(text='Calculate', command=position_size)
button_calc.bind("<Return>", lambda event=None: button_calc.invoke())
button_calc.grid(row=4, column=1, sticky='NSEW')
empty = tk.Label(bg='white')
empty.grid(row=4, column=0, sticky='NSEW')

# SIXTH ROW
lbl_pos_size = tk.Label(text='Position Size (Lots): ', bg='white', fg='black')
lbl_pos_size_result = tk.Label(text='0', bg='white', fg='black') # TODO
lbl_pos_size.grid(row=5, column=0, sticky='NSEW')
lbl_pos_size_result.grid(row=5, column=1, sticky='NSEW')

# 7th row
lbl_margn_req = tk.Label(text='Margin Required (CHF): ', bg='white', fg='black')
lbl_margn_req_result = tk.Label(text='0', bg='white', fg='black') # TODO
lbl_margn_req.grid(row=6, column=0, sticky="NSEW")
lbl_margn_req_result.grid(row=6, column=1, sticky='NSEW')

window.mainloop()

# # def main():
# #     position_size()






# if __name__ == "__main__":
#     main()