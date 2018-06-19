# -*- coding: utf-8 -*-

def home():
	table = TABLE()
	colors_rows = db(db.colors.id > 0).select()
	for x in colors_rows:
		table.append(
			TR(x.color)
			)
	return dict(
		table = table,
		)
