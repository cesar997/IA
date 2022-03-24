#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-

utiles = ['zacapuntas', 'borrador', 'lapiz', 'lapicera', 'calculadora', 'cuadernos']

print("\n\tEsta es la lista original: ")
print(utiles)

utiles.insert(0, 'regla')
utiles.insert(5, 'resistol')

print("\n\tEsta es la lista con los nuevos elementos: ")
print(utiles)
