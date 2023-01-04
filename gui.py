import textwrap
from plays import Plays
import PySimpleGUI as sg


plays = Plays(['Bryan Reynolds','Aaron Judge'], ['Pirates'])
scoring_plays = plays.get_plays()

button_row = [[sg.Button(player) for player in plays.players]]

layout = [
    [button_row],
    [sg.Listbox(values =scoring_plays, size=(50,None), key = 'Plays')],
    [sg.Button('Refresh')]]
window = sg.Window("Scoring Plays",layout,margins=(100,100))
while True: 
    event,values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == 'Refresh':
        window['Plays'].update(plays.get_plays())

# sg.Window(title="Scoring Plays",layout = [[sg.Text('Scoring Plays')],[sg.Button('Refresh')]], margins =(200,100)).read()

window.close()