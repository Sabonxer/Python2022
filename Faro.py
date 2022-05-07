#the background.#
Rect(0,0,400,250, fill=gradiente('midnightblue', 'steelblue', inicio='superior'))
Rect(0,250, 400, 150,fill=gradiente('slateblue', 'darkslateblue', inicio='superior'))

# the rock behind the lighthouse and its reflection.#
Polygon(400,230,295,210,205,240,160,280,400,280,fill=gradiente('darkslateblue','darkblue',inicio='superior'))
Polygon(160,280,400,280,400,290,295,300, fill=gradiente('darkslateblue','darkblue', inicio='superior'),opacity=20)

# the lighthouse from the top down.#
Polygon(185,220,215,220,220,285,180,285,fill=gradiente('snow', 'darkgray',inicio='superior'))
Polygon(190,160,210,160,215,220,185,220,fill=gradiente('crimson', 'darkred',inicio='superior'))
Rect(185,150, 30,10,fill='firebrick')
Rect(190,130,20,20,fill='crimson')
Rect(195,130,10,20,fill='yellow')
Polygon(200,120,215,130,185,130,fill=gradiente('crimson','darkred', inicio='inferior'))
Rect(203,190,5,10)

# the light coming from the lighthouse.#
Circle(200,140,40,fill=gradiente('yellow','gold', 'orange',inicio='superior'), opacity=10)
Polygon(200,140,400,260,400,340, fill=gradiente('yellow', 'gold', 'orange',inicio='superior'),opacity=30)

# the rock in front of the lighthouse and its reflection.#
Polygon(145,240,235,265,270,290,120,290,fill=gradiente('darkslateblue','midnightblue',inicio='superior'))
Polygon(120,290,270,290,235,315,145,340,fill=gradiente('darkslateblue','midnightblue', inicio='superior'),opacity=30)
