from plays import Plays
import PySimpleGUI as sg


plays = Plays((['Bryan Reynolds']), ['Pirates'])
scoring_plays = plays.get_plays()
layout = [
    [sg.Text(plays.players)],
    [sg.Listbox(values =scoring_plays, size=(50,50), key = '-Plays-')],
    [sg.Button('Refresh')]]
window = sg.Window("Scoring Plays",layout,margins=(100,100))
while True: 
    event,values = window.read()
    if event == sg.WIN_CLOSED:
        break
# sg.Window(title="Scoring Plays",layout = [[sg.Text('Scoring Plays')],[sg.Button('Refresh')]], margins =(200,100)).read()

window.close()