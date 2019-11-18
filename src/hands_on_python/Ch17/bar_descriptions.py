import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

my_style = LS('#333366', base_style=LCS)
chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)
chart.title = 'Python Projects'
chart.x_labels = ['system-desigt-primer', 'awesome-python', 'public-apis']

plto_dicts = [{'value': 76050, 'label': 'Description of system-desigt-primer'},
              {'value': 75267, 'label': 'Description of awesome-python'},
              {'value': 64678, 'label': 'Description of public-apis'}]

chart.add('', plto_dicts)
chart.render_to_file('bar_descriptions.svg')
