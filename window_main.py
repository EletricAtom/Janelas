import PySimpleGUI as sg
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
   
year = [1920,1930,1940,1950,1960,1970,1980,1990,2000,2010]
unemployment_rate = [9.8,12,8,7.2,6.9,7,6.5,6.2,5.5,6.3]
  
def create_plot(year, unemployment_rate):
    plt.plot(year, unemployment_rate, color='red', marker='o')
    plt.title('Unemployment Rate Vs Year', fontsize=14)
    plt.xlabel('Year', fontsize=14)
    plt.ylabel('Unemployment Rate', fontsize=14)
    plt.grid(True)
    return plt.gcf()

layout = [[sg.Text('Line Plot')],
          [sg.Canvas(size=(500, 500), key='-CANVAS-')],
          [sg.Exit()],
          [sg.Text('Texto')]]



def draw_figure(canvas, figure):
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
    return figure_canvas_agg


window = sg.Window('Demo Application - Embedding Matplotlib In PySimpleGUI', layout, finalize=True, element_justification='center')

draw_figure(window['-CANVAS-'].TKCanvas, create_plot(year, unemployment_rate))

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break

window.close()