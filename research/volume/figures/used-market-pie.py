"""Render an illustrative market pie from user-selected volumes; not Cox shares."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import math,html
P=Path(__file__).resolve().parent
values=[780684,596641,19000000,18500000]
labels=['CarMax','Carvana','Other dealers','Private-party / non-dealer estimate']
colors=['#2D5873','#06A9CD','#9DB3C1','#DCE4E9']
S=2;W=1200;H=750
im=Image.new('RGB',(W*S,H*S),'white');d=ImageDraw.Draw(im)
svg=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}"><rect width="1200" height="750" fill="white"/>']
font='/System/Library/Fonts/Supplemental/Arial.ttf'
bold='/System/Library/Fonts/Supplemental/Arial Bold.ttf'
def text(x,y,t,size=20,color='#173449',heavy=False):
 f=ImageFont.truetype(bold if heavy else font,size*S)
 d.text((x*S,y*S),t,font=f,fill=color)
 svg.append(f'<text x="{x}" y="{y+size}" font-family="Arial,sans-serif" font-size="{size}" fill="{color}" font-weight="{700 if heavy else 400}">{html.escape(t)}</text>')
text(60,38,'U.S. used-car market',36,heavy=True)
text(60,94,'Illustrative annual transaction mix | approximately 38.9 million sales',20,'#526371')
cx,cy,r=310,380,220;angle=-90
for v,c in zip(values,colors):
 end=angle+360*v/sum(values)
 d.pieslice(tuple(z*S for z in (cx-r,cy-r,cx+r,cy+r)),angle,end,fill=c,outline='white',width=4)
 a,b=math.radians(angle),math.radians(end)
 x1,y1=cx+r*math.cos(a),cy+r*math.sin(a);x2,y2=cx+r*math.cos(b),cy+r*math.sin(b)
 svg.append(f'<path d="M {cx} {cy} L {x1} {y1} A {r} {r} 0 {int(end-angle>180)} 1 {x2} {y2} Z" fill="{c}" stroke="white" stroke-width="2"/>')
 angle=end
for i,(label,value,color) in enumerate(zip(labels,values,colors)):
 y=220+i*92
 d.rectangle((600*S,y*S,618*S,(y+18)*S),fill=color)
 svg.append(f'<rect x="600" y="{y}" width="18" height="18" fill="{color}"/>')
 text(640,y-4,label,22,heavy=True)
 text(640,y+30,f'{value/1e6:.2f} million vehicles | {value/sum(values):.1%}',21,'#526371')
text(60,645,'Approximation, not a Cox-published market-share breakdown.',17,'#526371',True)
text(60,680,'Company volumes: Carvana CY2025; CarMax FY ended February 2026. Other dealers (19.0m) and',15,'#677580')
text(60,704,'private-party / non-dealer (18.5m) are rounded estimates; the latter’s composition is unverified.',15,'#677580')
svg.append('</svg>')
im.save(P/'used-market-pie.png')
(P/'used-market-pie.svg').write_text('\n'.join(svg))
