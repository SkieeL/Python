- Los enums en Python son clases que heredan de enum
- Buscar "estrategy" de Python (patrón de diseño)
- El código en Python nunca debería ser modificado pero sí extensible

--------------------------------
--------------------------------

Desarrollo de apps de escritorio

Interfaz gráfica Windows: WinForms, Windows Presentation nose cuanto
- Ent Gráfico: Windows - biblioteca: WinForms

Interfaz gráfica Linux: Hay un montón de entornos gráficos
- Ent Gráfico: Gnome - biblioteca: Gtk (escrito en C/C++) - wrapper: PyGtk (Ubuntu)
- Ent Gráfico: KDE - biblioteca: Qt (escrito en C/C++) - wrapper: PyQt/PySide (Kubuntu)
- Ent Gráfico: Xfce - biblioteca: Gtk - wrapper: PyGtk (Xubuntu)
- Ent Gráfico: LxDE - biblioteca: Gtk - wrapper: PyGtk (Lubuntu)
- Biblioteca WxWidgets - wrapper: WxPython
- Biblioteca: TCL/TK - wrapper: TkInter

Wrapper: Envoltorio que necesita Python para acceder a las funciones escritas en C/C++

Se necesita instalar módulo "TkInter" en Python -> apt-get install python-tk