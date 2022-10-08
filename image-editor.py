import PIL
import PySimpleGUI as sg
from tkinter import *
from PIL import Image, ImageFilter, ImageOps
from io import BytesIO

sg.theme('Light Blue')

def update_image(original,blur,contrast,
				emboss,contour,
				sharpen,edge_enhance,smooth,edge,detail,
				mode,median,color,
				flipx,flipy,
				ascii,quantize,bw):
	global image
	#val = int(col)
	image = original.filter(ImageFilter.GaussianBlur(blur))
	image = image.filter(ImageFilter.UnsharpMask(contrast))
	#image = image.convert("P", palette = Image.ADAPTIVE, colors=val)

	if emboss:
		image = image.filter(ImageFilter.EMBOSS())
	if contour:
		image = image.filter(ImageFilter.CONTOUR())
	if sharpen:
		for i in range (0,2):
			image = image.filter(ImageFilter.SHARPEN())
	if edge_enhance:
		image = image.filter(ImageFilter.EDGE_ENHANCE())
	if smooth:
		for i in range (0,2):
			image = image.filter(ImageFilter.SMOOTH())
	if edge:
		image = image.filter(ImageFilter.FIND_EDGES())
	if detail:
		for i in range (0,3):
			image = image.filter(ImageFilter.DETAIL())
	if mode:
		for i in range (0,5):
			image = image.filter(ImageFilter.ModeFilter())

	if median:
		for i in range (0,2):
			image = image.filter(ImageFilter.MedianFilter())
	if color:
		layout1 =[
			[sg.Input(key = '-INPUT-'),sg.Button('submit'),sg.Button('Exit')]
		]
		window1 = sg.Window('Color Entry', layout1)
		while var1==True:
			event, values = window1.read(timeout=50)
			if event == sg.WIN_CLOSED:
				window1.close()
				var1=False
				break
			elif event == 'Exit':
				window1.close()
				var1=False
				break
			elif event == 'submit':
				col = int(values['-INPUT-'])
				window1.close()
				var1=False
				break
		window1.close()
		image = image.convert("P", palette = Image.ADAPTIVE, colors=col)

	if flipx:
		image = ImageOps.mirror(image)
	if flipy:
		image = ImageOps.flip(image)
	
	if ascii:
		kit.image_to_ascii_art(image_path,r"C:\\Users\\Asad Ansari\\Desktop\\File\\")

	if quantize:
		image = image.quantize(colors=256, method=PIL.Image.Quantize.FASTOCTREE, kmeans=100000, palette= None, dither=PIL.Image.Dither.FLOYDSTEINBERG)
	
	if bw:
		image = image.convert(mode='L')

	

	bio = BytesIO()
	image.save(bio, format = 'PNG')

	window['-IMAGE-'].update(data = bio.getvalue())

image_path = sg.popup_get_file('Open',no_window = True)

control_col = sg.Column([
	[sg.Frame('Blur',layout = [[sg.Slider(range = (0,10), orientation = 'h', key = '-BLUR-')]])],
	[sg.Frame('Contrast',layout = [[sg.Slider(range = (0,10), orientation = 'h', key = '-CONTRAST-')]])],
	[sg.Checkbox('Emboss', key = '-EMBOSS-'), sg.Checkbox('Contour', key = '-CONTOUR-')],
	[sg.Checkbox('Sharpen', key = '-SHARPEN-'), sg.Checkbox('Edge Enhance', key = '-EDGE_ENHANCE-')],
	[sg.Checkbox('Smoothen', key='-SMOOTH-'), sg.Checkbox('Edge Detect', key='-EDGE-')],
	[sg.Checkbox('Detail', key='-DETAIL-'), sg.Checkbox('Mode', key='-MODE-')],
	[sg.Checkbox('Median', key='-MEDIAN-'), sg.Checkbox('Color', key='-COLOR-')],
	[sg.Checkbox('Flip x', key = '-FLIPX-'), sg.Checkbox('Flip y', key = '-FLIPY-')],
	[sg.Checkbox('ASCII', key='-ASCII-'), sg.Checkbox('Quantize', key='-QUANTIZE-')],
	[sg.Checkbox('Mono', key='-BW-')],
	[sg.Button('Save image', key = '-SAVE-')],])


image_col = sg.Column([[sg.Image(image_path, key = '-IMAGE-')]])
layout = [
	[control_col,image_col]
	]

original = Image.open(image_path)
window = sg.Window('Image Editor', layout, resizable=True, finalize=True)

while True:
	event, values = window.read(timeout = 50)
	if event == sg.WIN_CLOSED:
		break

	update_image(
		original, 
		values['-BLUR-'],
		values['-CONTRAST-'],
		values['-EMBOSS-'], 
		values['-CONTOUR-'],
		values['-SHARPEN-'],
		values['-EDGE_ENHANCE-'],
		values['-SMOOTH-'],
		values['-EDGE-'],
		values['-DETAIL-'],
		values['-MODE-'],
		values['-MEDIAN-'],
		values['-COLOR-'],
		values['-FLIPX-'],
		values['-FLIPY-'],
		values['-ASCII-'],
		values['-QUANTIZE-'],
		values['-BW-'],
	)

	if event == '-SAVE-':
		save_path = sg.popup_get_file('Save',save_as = True, no_window = True) + '.png'
		image.save(save_path,'PNG')
		
window.close()