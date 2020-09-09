import matplotlib.pyplot as plt
import numpy as np
import time

def plot_ocean(username, scores, working_directory, url):
    labels = [ "Açıklık",
    "Sorumluluk",
    "Dışadönüklük",
    "Uyumluluk",
    "Nevrotiklik"]
    num_vars = len(labels)
    angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
    scores += scores[:1]
    angles += angles[:1]
    labels += labels[:1]

    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
    ax.plot(angles, scores, color='#1aaf6c', linewidth=1)
    ax.fill(angles, scores, color='#1aaf6c', alpha=0.25)
    ax.set_theta_offset(np.pi / 2)
    ax.set_theta_direction(-1)
    ax.set_thetagrids(np.degrees(angles), labels)
    for label, angle in zip(ax.get_xticklabels(), angles):
      if angle in (0, np.pi):
        label.set_horizontalalignment('center')
      elif 0 < angle < np.pi:
        label.set_horizontalalignment('left')
      else:
        label.set_horizontalalignment('right')
    ax.set_ylim(0, 4)
    plt.yticks(range(0,5))
    ax.set_rlabel_position(180 / num_vars)
    ax.tick_params(colors='#222222')
    ax.tick_params(axis='y', labelsize=8)
    ax.grid(color='#AAAAAA')
    ax.spines['polar'].set_color('#222222')
    ax.set_facecolor('#FAFAFA')

    ax.set_title(f'{username} Twitter Kişilik Analizi', y=1.08)
    
    plt.text(0.95,-0.1, url, horizontalalignment='center',verticalalignment='center', transform=ax.transAxes)

    now = int(time.time())
    plt.savefig(f'{working_directory}/web/images/{username}-ocean-{now}', bbox_inches='tight')
    return f'{working_directory}/web/images/{username}-ocean-{now}.png'