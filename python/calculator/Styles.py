# LINK PARA LER SOBRE OS TIPOS DE ESTILOS DE JANELAS
# https://doc.qt.io/qtforpython/tutorials/basictutorial/widgetstyling.html

# Estilos do Qt for Python

import qdarkstyle
from PySide6.QtWidgets import QApplication
from constants import PRIMARY_COLOR, DARKER_PRIMARY_COLOR, DARKEST_PRIMARY_COLOR


qss = f"""
    QPushButton[cssClass="specialButton"] {{
        color: #fff;
        background: {PRIMARY_COLOR};
        border-radius: 5px;
    }}
    QPushButton[cssClass="specialButton"]:hover {{
        color: #fff;
        background: {DARKER_PRIMARY_COLOR};
    }}
    QPushButton[cssClass="specialButton"]:pressed {{
        color: #fff;
        background: {DARKEST_PRIMARY_COLOR};
    }}
"""

def setupTheme(app: QApplication):

    # Aplica o estilo escuro do qdarkstyle
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyside6())

    # Sobrepoe o estilo padrao com um QSS personalizado
    app.setStyleSheet(app.styleSheet() + qss)