import sys
import requests
from PyQt5.QtWidgets import QApplication,QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QGridLayout,QGroupBox
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QFont, QFontDatabase, QPixmap, QImage


class Pokedex(QWidget):
    def __init__(self):
        super().__init__()
        self.title_label = QLabel("Pokédex", self)
        self.pokemon_input = QLineEdit(self)
        self.search_button = QPushButton("Search",self)
        self.order_label = QLabel(self)
        self.name_label = QLabel("Name:", self)
        self.pokemon_name_label = QLabel(self)
        self.form_label = QLabel("Form:", self)
        self.pokemon_form_label = QLabel(self)
        self.type_label = QLabel("Type:", self)
        self.pokemon_type_label = QLabel(self)
        self.height_label = QLabel("Height:", self)
        self.pokemon_height_label = QLabel(self)
        self.weight_label = QLabel("Weight:", self)
        self.pokemon_weight_label = QLabel(self)
        self.pokemon_description_label = QLabel(self)
        self.sound_button = QPushButton("Sounds 🔊", self)
        self.image_sprite = QLabel(self)
        self.footer_label = QLabel(self)

        # test image
        self.image_data = QImage()
        

        # setting hyperlink
        template = "<hr><br><span>{0}<a href={1}>{2}</a></span>"
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
        self.setObjectName("body")
        self.image_sprite.setObjectName("image_sprite")
        stat_box.setObjectName("stat_box")
        self.footer_label.setObjectName("footer_label")
        self.setStyleSheet("""
            #body{
                background-color: hsl(149, 98%, 50%);
                
                
            }

            #stat_box{
                background-color: red;
            }               
            
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
                padding:10px;
            }


        """)
        
        self.search_button.clicked.connect(self.search_click)
        
    def search_click(self):
        

        try:
            pokemon_name = self.pokemon_input.text()
            url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"
            res = requests.get(url)
            res.raise_for_status()
            data = res.json()
            if data["name"] == pokemon_name:
                self.display_data(data)

        except:
            pass

    def display_data(self, data):
        self.order_label.setText(f"#{data["order"]}")
        self.pokemon_name_label.setText(data["name"])
        self.pokemon_type_label.setText(data["types"][0]["type"]["name"])
        self.pokemon_height_label.setText(f"{data["height"] / 10}m")
        self.pokemon_weight_label.setText(f"{data["weight"]}kg")
        self.display_image(data["sprites"]["front_default"])

    
    def display_image(self, url):
        self.image_data.loadFromData(requests.get(f"{url}").content)
        self.image_sprite.setPixmap(QPixmap(self.image_data).scaled(QSize(250,250)))
        self.image_sprite.setScaledContents(True)

    def play_sound(self):
        pass

    def display_error(self, message):
        pass






if __name__ == "__main__":
    app =QApplication(sys.argv)
    pokedex = Pokedex()
    pokedex.show()
    sys.exit(app.exec_())