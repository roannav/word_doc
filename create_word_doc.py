from docx import Document
from docx.shared import Inches

doc = Document()
doc.add_heading('The Late Show with Stephen Colbert')

'''
YouTube channel: https://www.youtube.com/channel/UCMtFAi84ehTSYSE9XoHefig
8.7 Million Subscribers

owned by CBS Viacom Paramount Plus

The Late Late Show with James

The Late Show with Stephen Colbert is the premier late night talk show on CBS, airing at 11:35pm EST, streaming online via Paramount+, and delivered to the International Space Station on a USB drive taped to a weather balloon. Every night, viewers can expect: Comedy, humor, funny moments, witty interviews, celebrities, famous people, movie stars, bits, humorous celebrities doing bits, funny celebs, big group photos of every star from Hollywood, even the reclusive ones, plus also jokes.
'''

doc.add_picture('img/The_Late_Show_with_Stephen_Colbert.png', width=Inches(3))
doc.save('The_Late_Show_with_Stephen_Colbert.docx')
