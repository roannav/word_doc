from docx import Document, text
from docx.shared import Inches

print(dir(text.run.WD_BREAK))

doc = Document()
doc.add_heading('The Late Show with Stephen Colbert')
doc.add_picture('img/The_Late_Show_with_Stephen_Colbert.png', width=Inches(3))

p = doc.add_paragraph('Go to ')
p.add_run('YouTube channel: ').bold = True
p.add_run('https://www.youtube.com/channel/UCMtFAi84ehTSYSE9XoHefig ').add_break()
p.add_run('This channel has 8.7 Million Subscribers')

doc.add_heading('About the show', level=2)
doc.add_paragraph('The Late Show with Stephen Colbert is the premier late ' +
'night talk show on CBS, airing at 11:35pm EST, streaming online via ' +
'Paramount+, and delivered to the International Space Station on a USB drive taped to a weather balloon. Every night, viewers can expect: Comedy, humor, funny moments, witty interviews, celebrities, famous people, movie stars, bits, humorous celebrities doing bits, funny celebs, big group photos of every star from Hollywood, even the reclusive ones, plus also jokes.', style='Quote')

'''
owned by CBS Viacom Paramount Plus

The Late Late Show with James

'''

doc.save('The_Late_Show_with_Stephen_Colbert.docx')
