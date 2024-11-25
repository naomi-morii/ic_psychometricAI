import matplotlib.pyplot as plt
import pandas as pd
import json
from math import pi
import sys

def cria_radar(data, context, categories, N, angles):
    df = pd.DataFrame(data, index=[context])

    # Valores
    values = df.loc[context].values.flatten().tolist()
    values += values[:1] 

    ax = plt.subplot(111, polar=True)
    plt.xticks(angles[:-1], categories, color='grey', size=8)
    
    ax.set_rlabel_position(23)
    plt.yticks([1, 2, 3, 4, 5], ["1", "2", "3", "4", "5"], color="grey", size=7)
    plt.ylim(0, 5)

    ax.plot(angles, values, linewidth=1, linestyle='solid')
    ax.fill(angles, values, 'b', alpha=0.1)

    plt.title('teste' + context[23:])

    #plt.show()
    plt.savefig(f'{context}.png', bbox_inches='tight')  
    plt.close()

def overlapping_chart(all_data, categories, N, angles):

    fig, ax = plt.subplots(figsize=(6,6), subplot_kw=dict(polar=True))
    plt.xticks(angles[:-1], categories, color='grey', size=8)

    ax.set_rlabel_position(0)
    plt.yticks([1, 2, 3, 4, 5], ["1", "2", "3", "4", "5"], color="grey", size=7)
    plt.ylim(0, 5)

    colors = ['r','b', 'g', 'y'] 
    for i, (context, data) in enumerate(all_data.items()):
        data = {k: v for k, v in data.items() if k != 'invalid response'}

        values = list(data.values())
        values += values[:1] 

        ax.plot(angles, values, linewidth=1, linestyle='solid', label=context, color=colors[i % len(colors)])
        ax.fill(angles, values, color=colors[i % len(colors)], alpha=0.1)

    #plt.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1))

    plt.savefig(f'overlapping_radar_chart.png', bbox_inches='tight')
    plt.show() 
    plt.close() 


with open(sys.argv[1], 'r') as f:
    all_data = json.load(f)

categories = ['Extraversion', 'Agreeableness', 'Conscientiousness', 'Neuroticism  ', 'Openness to Experience']  # Nomes completos das dimensões
N = len(categories)
# Ângulos
angles = [n / float(N) * 2 * pi for n in range(N)]
angles += angles[:1]

for context, data in all_data.items():
    data = {k: v for k, v in data.items() if k != 'invalid response'}
    cria_radar(data, context, categories, N, angles)

overlapping_chart(all_data, categories, N, angles)
