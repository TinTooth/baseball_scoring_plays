import textwrap
from plays import Plays
import PySimpleGUI as sg


plays = Plays(['Bryan Reynolds','Aaron Judge'], ['Pirates'])
button_row = [[sg.Button(player) for player in plays.players]]




layout = [
    [button_row],
    [sg.Multiline(default_text=plays.plays_to_string(), size = (50,50), disabled=True, enable_events=True, key = 'Plays')],
    [sg.Button('Refresh'), sg.Button('All Players')]]
window = sg.Window("Scoring Plays",layout,margins=(100,100))
multiline = window['Plays'].widget


while True: 
    event,values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'All Players':
        window['Plays'].update(plays.plays_to_string())
    elif event == 'Refresh':
        window['Plays'].update(plays.refresh())
    else :
        window['Plays'].update(plays.filter_by_player(event))
        


window.close()