import pygal

radar = pygal.Radar(fill=True)
radar.title='pygal'
radar.x_labels=['智商','颜值','身材','收入','性格']
radar.add('mark',[99,90,90,80,85])

radar.render_to_file('test01.svg')
