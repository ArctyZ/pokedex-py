import sys
import requests
from PyQt5.QtWidgets import QApplication,QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QGridLayout
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QFont, QFontDatabase, QPixmap, QImage


class Pokedex(QWidget):
    def __init__(self):
        super().__init__()
        self.title_label = QLabel("Pokédex", self)
        self.pokemon_input = QLineEdit(self)
        self.search_button = QPushButton("Search",self)
        self.order_label = QLabel(f"Order:", self)
        self.pokemon_order_label = QLabel("Pokemon's order", self)
        self.name_label = QLabel("Name:", self)
        self.pokemon_name_label = QLabel("Pokemon's name", self)
        self.form_label = QLabel("Form:", self)
        self.pokemon_form_label = QLabel("Pokemon's form", self)
        self.type_label = QLabel("Type:", self)
        self.pokemon_type_label = QLabel("Pokemon's type", self)
        self.height_label = QLabel("Height:", self)
        self.pokemon_height_label = QLabel("pokemon's height", self)
        self.weight_label = QLabel("Weight:", self)
        self.pokemon_weight_label = QLabel("pokemon's Weight", self)
        self.pokemon_description_label = QLabel("pokemon's Description", self)
        self.sound_button = QPushButton("Sounds", self)
        self.image_sprite = QLabel(self)
        self.footer_label = QLabel(self)

        # test image
        image_data = QImage()
        image_data.loadFromData(requests.get('https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/132.png').content)
        self.image_sprite.setPixmap(QPixmap(image_data).scaled(QSize(250,250)))
        self.image_sprite.setScaledContents(True)

        # setting hyperlink
        template = "<span>{0}<a href={1}>{2}</a></span>"
        self.footer_label.setText(template.format("Visit my ", "https://github.com/ArctyZ", "Github"))
        self.footer_label.setOpenExternalLinks(True)


        self.initUI()

    def initUI(self):
        self.setWindowTitle("Pokedex")

        # Layout
        vbox = QVBoxLayout()
        vbox.addWidget(self.title_label)

        search_box = QHBoxLayout()
        search_box.addWidget(self.pokemon_input)
        search_box.addWidget(self.search_button)
        vbox.addLayout(search_box)
        self.setLayout(vbox)

        stat_box = QGridLayout()
        stat_box.addWidget(self.order_label, 0, 0)
        stat_box.addWidget(self.pokemon_order_label, 0, 1)
        stat_box.addWidget(self.name_label, 1, 0)
        stat_box.addWidget(self.pokemon_name_label, 1, 1)
        stat_box.addWidget(self.form_label, 2,0)
        stat_box.addWidget(self.pokemon_form_label, 2,1)
        stat_box.addWidget(self.type_label, 3,0)
        stat_box.addWidget(self.pokemon_type_label, 3,1)
        stat_box.addWidget(self.height_label, 4,0)
        stat_box.addWidget(self.pokemon_height_label, 4,1)
        stat_box.addWidget(self.weight_label, 5,0)
        stat_box.addWidget(self.pokemon_weight_label, 5,1)
        stat_box.addWidget(self.pokemon_description_label, 6,0,0,2)

        mid_section_box = QHBoxLayout()
        mid_section_box.addLayout(stat_box)

        mid_right_section_box = QVBoxLayout()
        mid_right_section_box.addWidget(self.image_sprite)
        mid_right_section_box.addWidget(self.sound_button)
        mid_section_box.addLayout(mid_right_section_box)

        vbox.addLayout(mid_section_box)
        vbox.addWidget(self.footer_label)

        self.title_label.setAlignment(Qt.AlignCenter)
        self.footer_label.setAlignment(Qt.AlignCenter)

        # font setting
        font_id = QFontDatabase.addApplicationFont("fonts/PixelifySans-VariableFont_wght.ttf")
        font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
        my_font = QFont(font_family, 20)
        self.setFont(my_font)

        # styling

        self.title_label.setObjectName("title_label")
        self.image_sprite.setObjectName("image_sprite")
        self.footer_label.setObjectName("footer_label")
        self.setStyleSheet("""
            QLabel#title_label{
                font-size: 50px;
                font-weight: bold;
                color:hsl(58, 83%, 64%);
            }

            QLabel#image_sprite{
                height: 40px;
            
            }
            
            QLabel#footer_label{
                font-size: 15px;
            }


        """)


    def search_click(self):
        pass

    def display_data(self, data):
        pass

    def play_sound(self):
        pass

    def display_error(self, message):
        pass






if __name__ == "__main__":
    app =QApplication(sys.argv)
    pokedex = Pokedex()
    pokedex.show()
    sys.exit(app.exec_())