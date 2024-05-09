from kivymd.uix.screenmanager import ScreenManager
from kivy.core.window import Window
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen
from kivymd.uix.behaviors.toggle_behavior import MDToggleButton
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.list import OneLineListItem
import re
from kivy.clock import Clock
import firebase_admin
from firebase_admin import credentials, db, auth
from kivy.storage.jsonstore import JsonStore
import hashlib



CreateAccount = '''
MDScreen:
    name: "CreateAccount"
    MDFloatLayout:
        md_bg_color:"#dae7f2"

        MDLabel:
            text: "Create Account"
            font_name: "fonts\PlayfairDisplay-Bold.ttf"
            font_size: "28sp"
            pos_hint: {"center_x": 0.5, "center_y": .91}
            halign: "center"
            theme_text_color: "Custom"
            color: "black"

        ScrollView:
            do_scroll_y: True
            do_scroll_x: False
            size_hint_y: .67
            pos_hint: {"center_x": .5, "center_y":.5}
            bar_width: 0
            GridLayout:
                size_hint_y: None
                row_default_height: 55
                height: self.minimum_height
                cols: 1
                spacing: 15, 10
                padding: 15

                MDFloatLayout:
                    size_hint: 0.79, 0.08
                    pos_hint: {"center_x": 0.5, "center_y": 0.75}

                    MDLabel:
                        text: "Name"
                        font_name: "fonts\PlayfairDisplay-Regular.ttf"
                        font_size: "14sp"
                        pos_hint: {"center_x": 0.5, "center_y": 0.9}
                        color: "#3b3e41"

                    TextInput:
                        id:name_input
                        size_hint_y: 0.75
                        pos_hint: {"center_x": 0.49, "center_y": 0.4}
                        background_color: 0, 0, 0, 0
                        cursor_color: 0, 0, 0, 1
                        cursor_width: "1sp"
                        foreground_color: "black"
                        font_size: "12sp"
                        font_name: "fonts\PlayfairDisplay-SemiBold.ttf"
                        multiline: False
                        on_text: name_error_label.text =""

                    Image:
                        source: r"pic\\asterisk (2).png"
                        pos_hint: {"center_x": 0.15, "center_y": 0.9}
                        size_hint: .2, .2

                    Image:
                        source: r"pic\\user (2).png"
                        pos_hint: {"center_x": 0.96, "center_y": 0.9}
                        size_hint: .4, .4

                    MDFloatLayout:
                        pos_hint: {"center_x": 0.5, "center_y": 0}
                        size_hint_y: 0.03
                        md_bg_color:"#3b3e41"

                MDFloatLayout:
                    size_hint: 0.79, 0.08
                    pos_hint: {"center_x": 0.5, "center_y": 0.65}

                    MDLabel:
                        text: "Email"
                        font_name:"fonts\PlayfairDisplay-Regular.ttf"
                        color: "#3b3e41"
                        font_size: "14sp"
                        pos_hint: {"center_x": 0.5, "center_y": 0.9}

                    TextInput:
                        id:email_input
                        size_hint_y: 0.75
                        pos_hint: {"center_x": 0.49, "center_y": 0.4}
                        background_color: 0, 0, 0, 0
                        cursor_color: 0, 0, 0, 1
                        cursor_width: "1sp"
                        foreground_color: "black"
                        font_name:"fonts\PlayfairDisplay-SemiBold.ttf"
                        font_size: "12sp"
                        multiline: False
                        on_text: email_error_label.text =""
                        
                    Image:
                        source:r"pic\\mail.png"
                        pos_hint: {"center_x": 0.96, "center_y": 0.9}
                        size_hint: .4, .4
                    
                    Image:
                        source: r"pic\\asterisk (2).png"
                        pos_hint: {"center_x": 0.15, "center_y": 0.9}
                        size_hint: .2, .2
                    
                    MDFloatLayout:
                        pos_hint: {"center_x": 0.5, "center_y": 0}
                        size_hint_y: 0.03
                        md_bg_color:"#3b3e41"


                MDFloatLayout:
                    size_hint: 0.79, 0.08
                    pos_hint: {"center_x": 0.5, "center_y": 0.45}

                    MDLabel:
                        text: "Password"
                        font_size: "14sp"
                        font_name: "fonts\PlayfairDisplay-Regular.ttf"
                        color: "#3b3e41"
                        pos_hint: {"center_x": 0.5, "center_y": 0.9}


                    TextInput:
                        id:password_input
                        size_hint_y: 0.75
                        pos_hint: {"center_x": 0.49, "center_y": 0.4}
                        background_color: 0, 0, 0, 0
                        cursor_color: 0, 0, 0, 1
                        cursor_width: "1sp"
                        foreground_color: "black"
                        font_name:"fonts\PlayfairDisplay-SemiBold.ttf"
                        font_size: "12sp"
                        multiline: False
                        password: True
                        on_text: password_error_label.color ="#3b3e41"

                    Image:
                        source: r"pic\\hide.png"
                        pos_hint: {"center_x": 0.96, "center_y": 0.9}
                        size_hint: 0.4, 0.4
                    Image:
                        source: r"pic\\asterisk (2).png"
                        pos_hint: {"center_x": 0.25, "center_y": 0.9}
                        size_hint: .2, .2

                    MDFloatLayout:
                        pos_hint: {"center_x": 0.5, "center_y": 0}
                        size_hint_y: 0.03
                        md_bg_color:"#3b3e41"

                MDFloatLayout:
                    size_hint: 0.79, 0.08
                    pos_hint: {"center_x": 0.5, "center_y": 0.85}

                    MDLabel:
                        text: "Age"
                        font_name:"fonts\PlayfairDisplay-Regular.ttf"
                        font_size: "14sp"
                        pos_hint: {"center_x": 0.5, "center_y": 0.9}
                        color: "#3b3e41"

                    TextInput:
                        id:age_input
                        size_hint_y: 0.75
                        pos_hint: {"center_x": 0.49, "center_y": 0.4}
                        background_color: 0, 0, 0, 0
                        cursor_color: 0, 0, 0, 1
                        cursor_width: "1sp"
                        foreground_color: "black"
                        font_size: "12sp"
                        font_name: "fonts\PlayfairDisplay-SemiBold.ttf"
                        multiline: False
                        on_text: age_error_label.text =""
   
                        
                    MDFloatLayout:
                        pos_hint: {"center_x": 0.5, "center_y": 0}
                        size_hint_y: 0.03
                        md_bg_color:"#3b3e41"


                MDFloatLayout:
                    size_hint: 0.79, 0.08
                    pos_hint: {"center_x": 0.5, "center_y": 0.55}

                    MDLabel:
                        text: "height"
                        font_name:"fonts\PlayfairDisplay-Regular.ttf"
                        color: "#3b3e41"
                        font_size: "14sp"
                        pos_hint: {"center_x": 0.5, "center_y": 0.9}

                    TextInput:
                        id:height_input
                        size_hint_y: 0.75
                        pos_hint: {"center_x": 0.49, "center_y": 0.4}
                        background_color: 0, 0, 0, 0
                        cursor_color: 0, 0, 0, 1
                        cursor_width: "1sp"
                        foreground_color: "black"
                        font_name:"fonts\PlayfairDisplay-SemiBold.ttf"
                        font_size: "13sp"
                        multiline: False
                        on_text: height_error_label.text =""

                    Image:
                        source: r"pic\\asterisk (2).png"
                        pos_hint: {"center_x": 0.18, "center_y": 0.9}
                        size_hint: .2, .2

                    MDFloatLayout:
                        pos_hint: {"center_x": 0.5, "center_y": 0}
                        size_hint_y: 0.03
                        md_bg_color:"#3b3e41"

                MDFloatLayout:
                    size_hint: 0.79, 0.08
                    pos_hint: {"center_x": 0.5, "center_y": 0.6}

                    MDLabel:
                        text: "Weight"
                        font_name:"fonts\PlayfairDisplay-Regular.ttf"
                        color: "#3b3e41"
                        font_size: "14sp"
                        pos_hint: {"center_x": 0.5, "center_y": 0.9}

                    TextInput:
                        id:weight_input
                        size_hint_y: 0.75
                        pos_hint: {"center_x": 0.49, "center_y": 0.4}
                        background_color: 0, 0, 0, 0
                        cursor_color: 0, 0, 0, 1
                        cursor_width: "1sp"
                        foreground_color: "black"
                        font_name:"fonts\PlayfairDisplay-SemiBold.ttf"
                        font_size: "13sp"
                        multiline: False
                        on_text: weight_error_label.text =""

                    Image:
                        source: r"pic\\weight.png"
                        pos_hint: {"center_x": 0.96, "center_y": 0.9}
                        size_hint: .4, .4
                    Image:
                        source: r"pic\\asterisk (2).png"
                        pos_hint: {"center_x": 0.18, "center_y": 0.9}
                        size_hint: .2, .2

                    MDFloatLayout:
                        pos_hint: {"center_x": 0.5, "center_y": 0}
                        size_hint_y: 0.03
                        md_bg_color:"#3b3e41"
            
    MDFloatLayout:        
        MDLabel:
            id: name_error_label
            text: ""
            font_name:"fonts\PlayfairDisplay-Regular.ttf"
            font_size: "11sp"
            pos_hint: {"center_x": 0.49, "center_y": 0.778}
            padding:17
            color: "#cc0000"

        MDLabel:
            id: password_error_label
            font_name:"fonts\PlayfairDisplay-Regular.ttf"
            text: "* make sure the password is 8 in length and contains capital/small letters and a number"
            font_size: "11sp"
            pos_hint: {"center_x": 0.52, "center_y": 0.32}
            padding:10
            color: "#3b3e41"

        MDLabel:
            id: weight_error_label
            text: ""
            font_name:"fonts\PlayfairDisplay-Regular.ttf"
            font_size: "11sp"
            pos_hint: {"center_x": 0.51, "center_y": 0.38}
            padding:10
            color: "#cc0000"

        MDLabel:
            id: height_error_label
            text: ""
            font_name:"fonts\PlayfairDisplay-Regular.ttf"
            font_size: "11sp"
            pos_hint: {"center_x": 0.51, "center_y": 0.46}
            padding:10
            color: "#cc0000"
            
        MDLabel:
            id: age_error_label
            text: ""
            font_name:"fonts\PlayfairDisplay-Regular.ttf"
            font_size: "11sp"
            pos_hint: {"center_x": 0.51, "center_y": 0.53}
            padding:10
            color: "#cc0000"
                    
        MDLabel:
            id: email_error_label
            font_name:"fonts\PlayfairDisplay-Regular.ttf"
            text: ""
            font_size: "11sp"
            pos_hint: {"center_x": 0.52, "center_y": 0.69}
            color:"#cc0000"

        MDLabel:
            id: check_signup_error
            font_name:"fonts\PlayfairDisplay-Regular.ttf"
            text: " "
            font_size: "11sp"
            pos_hint: {"center_x": 0.52, "center_y": 0.25}
            padding:10
            color: "#cc0000"

               
        MDRoundFlatIconButton:
            text: "Continue Create Account"
            size_hint: 0.79, 0.04
            pos_hint: {"center_x": 0.5, "center_y": 0.17}
            text_color: "white"
            line_color: "#031b31"
            md_bg_color:"#031b31"
            font_size: "20sp"
            font_name:"fonts\PlayfairDisplay-Bold.ttf"
            on_release: app.signup(name_input, email_input, password_input, age_input, weight_input,height_input)
    
       
    MDTextButton:
        text: "Already have you an Account? Login"
        font_size: "13sp"
        font_name:"fonts\PlayfairDisplay-Regular.ttf"
        pos_hint: {"center_x": 0.5, "center_y": 0.09}
        halign: "center"
        color: 120/255, 120/255, 120/255, 1
        on_release:
            root.manager.transition.direction = "right"
            root.manager.current =  "login"

'''

CreateAccount2 = '''
CreateAccountCard:
    name: "CreateAccount2"
    MDFloatLayout:
        md_bg_color:"#dae7f2"

        MDLabel:
            text: "Continue Create Account"
            font_name: "fonts\PlayfairDisplay-Bold.ttf"
            font_size: "23sp"
            pos_hint: {"center_x": 0.5, "center_y": .94}
            halign: "center"
            theme_text_color: "Custom"
            color: "black"
    
        Image:
            id:gender_image
            source:r"pic\\woman.png"
            pos_hint: {"center_x": .5, "center_y": .78}
            size_hint: .3,.3
            radius: [30, 30, 30, 30]
        
        MDFloatLayout:
            size_hint: 0.79, 0.08
            pos_hint: {"center_x": 0.5, "center_y": 0.56}

            MDLabel:
                text: "Gender"
                font_name:"fonts\PlayfairDisplay-Regular.ttf"
                color: "#3b3e41"
                font_size: "14sp"
                pos_hint: {"center_x": 0.5, "center_y": 0.85}

            MDLabel:
                id:gender_input
                size_hint_y: 0.75
                pos_hint: {"center_x": 0.5, "center_y": 0.4}
                background_color: 0, 0, 0, 0
                foreground_color: "black"
                font_name:"fonts\PlayfairDisplay-SemiBold.ttf"
                font_size: "13sp"
                on_text: gender_error_label.text =""

            MDIconButton:
                icon: "arrow-right-drop-circle"
                pos_hint: {"center_x": 0.31, "center_y": 0.85}
                user_font_size: "0.001sp"
                theme_text_color: "Custom"
                text_color: "#031b31"
                on_release: app.menuG()
                        
            MDList:
                id: gender_results
                pos_hint: {"center_x": .93, "center_y": .000001}
                font_name:"fonts\PlayfairDisplay-Regular.ttf"


            Image:
                source: r"pic\\asterisk (2).png"
                pos_hint: {"center_x": 0.23, "center_y": 0.85}
                size_hint: .2, .2

            MDFloatLayout:
                pos_hint: {"center_x": 0.5, "center_y": 0}
                size_hint_y: 0.03
                md_bg_color:"#3b3e41"


        MDFloatLayout:
            size_hint: 0.79, 0.08
            pos_hint: {"center_x": 0.5, "center_y": 0.35}

            MDLabel:
                text: "Level"
                font_name:"fonts\PlayfairDisplay-Regular.ttf"
                color: "#3b3e41"
                font_size: "14sp"
                pos_hint: {"center_x": 0.5, "center_y": 0.85}

            MDLabel:
                id:level_input
                size_hint_y: 0.75
                pos_hint: {"center_x": 0.5, "center_y": 0.4}
                background_color: 0, 0, 0, 0
                foreground_color: "black"
                font_name:"fonts\PlayfairDisplay-SemiBold.ttf"
                font_size: "13sp"
                on_text: level_error_label.text =""


            MDIconButton:
                icon: "arrow-right-drop-circle"
                pos_hint: {"center_x": 0.24, "center_y": 0.85}
                size: 0.001,.001
                theme_text_color: "Custom"
                text_color: "#031b31"
                on_release: app.menuL()
                        
            MDList:
                id: level_results
                pos_hint: {"center_x": .9, "center_y": .6}
                md_bg_color: 0, 0, 0, 0
                font_name:"fonts\PlayfairDisplay-Regular.ttf"

            Image:
                source: r"pic\\asterisk (2).png"
                pos_hint: {"center_x": 0.17, "center_y": 0.8}
                size_hint: .2, .2

            MDFloatLayout:
                pos_hint: {"center_x": 0.5, "center_y": 0}
                size_hint_y: 0.03
                md_bg_color:"#3b3e41"

        
        MDLabel:
            id: gender_error_label
            text: ""
            font_name:"fonts\PlayfairDisplay-Regular.ttf"
            font_size: "11sp"
            pos_hint: {"center_x": 0.6, "center_y": 0.54}
            padding:10
            color: "#cc0000"
                    
        MDLabel:
            id: level_error_label
            font_name:"fonts\PlayfairDisplay-Regular.ttf"
            text: ""
            font_size: "11sp"
            pos_hint: {"center_x": 0.6, "center_y": 0.33}
            color:"#cc0000"    

            
        MDRoundFlatIconButton:
            text: "Sign up   "
            size_hint: 0.79, 0.04
            pos_hint: {"center_x": 0.5, "center_y":  0.17}
            text_color: "white"
            line_color: "#031b31"
            md_bg_color:"#031b31"
            font_size: "20sp"
            font_name:"fonts\PlayfairDisplay-Bold.ttf"
            on_release: root.signup2(gender_input,level_input)
'''

Login='''
MDScreen:
    name: "login"
    MDFloatLayout:
        md_bg_color:"#dae7f2"

        Image:
            source:r"pic\logo navie.png"
            size_hint: 0.35, 0.35
            pos_hint: {"center_x": 0.5, "center_y": 0.83}

        MDLabel:
            text: "Login"
            font_size: "28sp"
            font_name:"fonts\PlayfairDisplay-Bold.ttf"
            pos_hint: {"center_x": 0.5, "center_y": 0.59}
            halign: "center"
            text_color:  "black"
           

        MDFloatLayout:
            size_hint: 0.79, 0.08
            pos_hint: {"center_x": 0.5, "center_y": 0.47}

            MDLabel:
                text: "Email"
                font_size: "14sp"
                pos_hint: {"center_x": 0.5, "center_y": 0.9}
                font_name:"fonts\PlayfairDisplay-Regular.ttf"
                color: "#3b3e41"

            TextInput:
                id:email_input
                size_hint_y: 0.75
                pos_hint: {"center_x": 0.49, "center_y": 0.4}
                background_color: 0, 0, 0, 0
                cursor_color: 0, 0, 0, 1
                cursor_width: "1sp"
                font_size: "17sp"
                foreground_color: "black"
                font_name:"fonts\PlayfairDisplay-SemiBold.ttf"
                multiline: False

            Image:
                source:r"pic\\mail.png"
                pos_hint: {"center_x": 0.96, "center_y": 0.9}
                size_hint: .4, .4

            MDFloatLayout:
                pos_hint: {"center_x": 0.5, "center_y": 0}
                size_hint_y: 0.03
                md_bg_color:"#3b3e41"         


        MDFloatLayout:
            size_hint: 0.79, 0.08
            pos_hint: {"center_x": 0.5, "center_y": 0.37}

            MDLabel:
                text: "Password"
                font_size: "14sp"
                font_name:"fonts\PlayfairDisplay-Regular.ttf"
                color: "#3b3e41"
                pos_hint: {"center_x": 0.5, "center_y": 0.9}

            TextInput:
                id:password_input
                size_hint_y: 0.75
                pos_hint: {"center_x": 0.49, "center_y": 0.4}
                background_color: 0, 0, 0, 0
                cursor_color: 0, 0, 0, 1
                cursor_width: "1sp"
                foreground_color: "black"
                font_name: "fonts\PlayfairDisplay-SemiBold.ttf"
                font_size: "17sp"
                multiline: False
                password: True

            Image:
                source: r"pic\\hide.png"
                pos_hint: {"center_x": 0.96, "center_y": 0.9}
                size_hint: 0.4, 0.4

            MDFloatLayout:
                pos_hint: {"center_x": 0.5, "center_y": 0}
                size_hint_y: 0.03
                md_bg_color:"#3b3e41"


        MDRoundFlatIconButton:
            text: "Login   "
            line_color: "#031b31"
            md_bg_color:"#031b31"
            text_color: "white"
            font_size: "20sp"
            font_name:"fonts\PlayfairDisplay-Bold.ttf"
            size_hint: 0.79, 0.04
            pos_hint: {"center_x": 0.5, "center_y": 0.17}
            on_release:
                app.login(email_input, password_input)

        MDLabel:
            id: check_login_error
            font_name:"fonts\PlayfairDisplay-Regular.ttf"
            text: " "
            font_size: "13sp"
            pos_hint: {"center_x": 0.55, "center_y": 0.3}
            padding:15
            color: "#cc0000"


    MDTextButton:
        text: "Don't have an account?  Create Account"
        font_size: "13sp"
        font_name:"fonts\PlayfairDisplay-Regular.ttf"
        pos_hint: {"center_x": 0.5, "center_y": 0.09}
        halign: "center"
        color: 120/255, 120/255, 120/255, 1
        on_release: 
            root.manager.transition.direction = "right"
            root.manager.current = "CreateAccount"

            


'''


Homepage='''

HomeCard:
    name: "homepage"
    MDFloatLayout:
        md_bg_color:"#dae7f2"

        MDLabel:
            id: name_index
            pos_hint: {"center_x": 0.56, "center_y": 0.91}
            font_size: "23sp"
            font_name:"fonts\PlayfairDisplay-BoldItalic.ttf"
            color: "black"


        MDFloatLayout:
            size_hint: .9, .09
            pos_hint: {"center_x": .5, "center_y": .82}

            MDRoundFlatIconButton:
                id: search_input
                text: "Search for workout...                      "
                font_name:"fonts\PlayfairDisplay-Regular.ttf"
                pos_hint: {"center_x": .5, "center_y": .47}
                font_size: "16sp"
                color: 0, 0, 0, 0
                line_color: rgba(241, 241, 243, 255)
                md_bg_color: rgba(241, 241, 243, 255)
                padding:20
                text_color: rgba(206, 206, 209, 255)
                on_press:
                    root.manager.transition.direction = "left"
                    root.manager.current = "search"

            Image:
                source:r"pic\\search.png"
                pos_hint: {"center_x": 0.90, "center_y": 0.55}
                size_hint: 0.5, 0.5


        MDLabel:
            text:"Popular Workout & Workouts"
            font_name:"fonts\PlayfairDisplay-BoldItalic.ttf"
            pos_hint:{"center_x":.56,"center_y": .73}
            font_size: "18sp"

        ScrollView:
            do_scroll_y: False
            do_scroll_x: True
            pos_hint: {"center_y":.56 , "center_y":.59}
            size_hint_y: 0.3
            bar_width: 0
            GridLayout:
                size_hint_x: None
                height: self.minimum_height
                width:  self.minimum_width
                rows: 1
                spacing: 10
                padding: 20,0

                BoxLayout:
                    orientation: 'vertical'
                    size_hint: None, None
                    size: "120dp", "160dp"  
                    elevation: 12 
                    canvas:
                        Color:
                            rgba: 0, 0, 0, 0  
                        RoundedRectangle:
                            size: self.size
                            pos: self.pos
                            radius: [10, 10, 10, 10]  

                    Button:
                        background_normal: 'pic\\Workout-amico.png'  
                        background_down: 'pic\\Workout-amico.png'  
                        size_hint: None, None
                        size: "120dp", "120dp"
                        on_release:
                            root.manager.transition.direction = "left"
                            root.manager.current = "Start_HBC"

                    
                    MDTextButton:
                        text: "Hammer Biceps Curls"
                        font_name:"fonts\PlayfairDisplay-Bold.ttf"
                        font_size:  "12sp"
                        pos_hint: {"center_x": 0.5, "center_y": 0.17}
                        halign: "center"
                        color: "#031b31"
                        height: self.texture_size[1]
                        on_release:
                            root.manager.transition.direction = "left"
                            root.manager.current = "Start_HBC"

                BoxLayout:
                    orientation: 'vertical'
                    size_hint: None, None
                    size: "120dp", "160dp"  
                    elevation: 10 
                    canvas:
                        Color:
                            rgba: 0, 0, 0, 0  
                        RoundedRectangle:
                            size: self.size
                            pos: self.pos
                            radius: [0, 0, 16, 16]  

                    Button:
                        background_normal: r"pic\\Biceps.png"
                        background_down: r"pic\\Biceps.png" 
                        size_hint: None, None
                        size: "140dp", "140dp"
                        on_release:
                            root.manager.transition.direction = "left"
                            root.manager.current = "workout"


                    MDTextButton:
                        text: "Workout"
                        font_name:"fonts\PlayfairDisplay-Bold.ttf"
                        font_size:  "12sp"
                        pos_hint: {"center_x": 0.5, "center_y": 0.17}
                        halign: "center"
                        color: "#031b31"
                        height: self.texture_size[1]
                        on_release:
                            root.manager.transition.direction = "left"
                            root.manager.current = "workout"

        MDLabel:
            text:"Category Program"
            font_name:"fonts\PlayfairDisplay-BoldItalic.ttf"
            pos_hint:{"center_x":.56,"center_y": .40}
            font_size: "18sp"

        ScrollView:
            do_scroll_y: False
            do_scroll_x: True
            pos_hint: {"center_x":.52 , "center_y":.25}
            size_hint_y:0.3
            bar_width:0
            GridLayout:
                size_hint_x:None
                size_hint_x: None
                height: self.minimum_height
                width:  self.minimum_width
                rows: 1
                spacing: 10
                padding: 20,0

                BoxLayout:
                    orientation: 'vertical'
                    size_hint: None, None
                    size: "120dp", "160dp"  

                    elevation: 12 

                    canvas:
                        Color:
                            rgba: 0, 0, 0, 0  
                        RoundedRectangle:
                            size: self.size
                            pos: self.pos
                            radius: [0, 0, 16, 16]  
                    Button:
                        background_normal: r"pic\\Upper2.png"
                        background_down:r"pic\\Upper2.png"
                        size_hint: None, None
                        size: "140dp", "140dp"
                        on_release:
                            root.manager.transition.direction = "left"
                            root.manager.current = "UpperBody"

                    MDTextButton:
                        text: "Upper Body"
                        font_name:"fonts\PlayfairDisplay-Bold.ttf"
                        font_size:  "12sp"
                        pos_hint: {"center_x": 0.5, "center_y": 0.17}
                        halign: "center"

                        color: "#031b31"
                        height: self.texture_size[1]
                        on_release:
                            root.manager.transition.direction = "left"
                            root.manager.current = "UpperBody"

                BoxLayout:
                    orientation: 'vertical'
                    size_hint: None, None
                    size: "120dp", "160dp"  
                    elevation: 10 

                    canvas:
                        Color:
                            rgba: 0, 0, 0, 0 
                        RoundedRectangle:
                            size: self.size
                            pos: self.pos
                            radius: [0, 0, 16, 16]  

    
                    Button:
                        background_normal: r"pic\\lower2.png"
                        background_down:r"pic\\lower2.png"
                        size_hint: None, None
                        size: "140dp", "140dp"
                        on_release:
                            root.manager.transition.direction = "left"
                            root.manager.current = "Lower Body"

                    MDTextButton:
                        text: "Lower Body"
                        font_name:"fonts\PlayfairDisplay-Bold.ttf"
                        font_size:  "12sp"
                        pos_hint: {"center_x": 0.5, "center_y": 0.17}
                        halign: "center"

                        color: "#031b31"
                        height: self.texture_size[1]
                        on_release:
                            root.manager.transition.direction = "left"
                            root.manager.current = "Lower Body"
           
        MDFloatLayout:
            canvas:
                Color:
                    rgba: 0.953, 0.957, 0.961, 1 
                RoundedRectangle:
                    pos:0.1,0.01
                    size: 450, 65
                    radius: [16, 16, 0, 0]

        MDFloatLayout:
            MDIconButton:
                icon: "magnify"
                pos_hint: {"center_x": 0.75, "center_y": 0.037}
                user_font_size: "240sp"
                theme_text_color: "Custom"
                text_color: "#031b31"
                on_release:
                    root.manager.transition.direction = "left"
                    root.manager.current = "search"

            MDIconButton:
                icon: "home"
                pos_hint: {"center_x": 0.5, "center_y": 0.037}
                user_font_size: "260sp"
                theme_text_color: "Custom"
                text_color: "#031b31"
                on_release:
                    root.manager.current = "homepage"

            MDIconButton:
                icon: "account-circle-outline"
                pos_hint: {"center_x": 0.25, "center_y":0.037}
                user_font_size: "240sp"
                theme_text_color: "Custom"
                text_color: "#031b31"
                on_release:
                    root.manager.transition.direction = "right"
                    root.manager.current = "profilepage"




'''

search='''

MDScreen:
    name: "search"
    MDFloatLayout:
        md_bg_color:"#dae7f2"

        MDLabel:
            text: "Search for workout"
            pos_hint: {"center_x": 0.66, "center_y": 0.91}
            font_size: "20sp"
            font_name:"fonts\PlayfairDisplay-BoldItalic.ttf"
            color: "black"

        MDFloatLayout:
            size_hint: .9, .09
            pos_hint: {"center_x": .5, "center_y": .82}
            md_bg_color: rgba(241, 241, 243, 255)
            font_name:"fonts\PlayfairDisplay-Regular.ttf"
            radius: [30]

            TextInput:
                id: search_input
                hint_text: "Search for workout..."
                font_name:"fonts\PlayfairDisplay-Regular.ttf"
                height: self.minimum_height
                pos_hint: {"center_x": .55, "center_y": .45}
                cursor_color: rgba(253,174,177,255)
                cursor_width: "2sp"
                font_size: "16sp"
                multiline: False
                background_color: 0, 0, 0, 0
                padding: 15
                hint_text_color: rgba(206, 206, 209, 255)
                right_icon: 'magnify'
                on_text: app.search_workout()

        MDFloatLayout:
            MDList:
                id: search_results
                pos_hint: {"center_x": .55, "center_y": .64}
                font_name:"fonts\PlayfairDisplay-Regular.ttf"

            MDFloatLayout:
                canvas:
                    Color:
                        rgba: 0.953, 0.957, 0.961, 1 
                    RoundedRectangle:
                        pos:0.1,0.01
                        size: 450, 65
                        radius: [16, 16, 0, 0]


            MDFloatLayout:
                MDIconButton:
                    icon: "magnify"
                    pos_hint: {"center_x": 0.75, "center_y": 0.037}
                    user_font_size: "240sp"
                    theme_text_color: "Custom"
                    text_color: "#031b31"
                    on_release:
                        root.manager.transition.direction = "left"
                        root.manager.current = "search"

                MDIconButton:
                    icon: "home"
                    pos_hint: {"center_x": 0.5, "center_y": 0.037}
                    user_font_size: "260sp"
                    theme_text_color: "Custom"
                    text_color: "#031b31"
                    on_release:
                        root.manager.transition.direction = "right"
                        root.manager.current = "homepage"

                MDIconButton:
                    icon: "account-circle-outline"
                    pos_hint: {"center_x": 0.25, "center_y":0.037}
                    user_font_size: "240sp"
                    theme_text_color: "Custom"
                    text_color: "#031b31"
                    on_release:
                        root.manager.transition.direction = "right"
                        root.manager.current = "profilepage"



'''

workout='''
MDScreen:
    name: "workout"
    MDFloatLayout:
        md_bg_color:"#dae7f2"

        MDLabel:
            text: "    Workout"
            font_name:"fonts\PlayfairDisplay-BlackItalic.ttf"
            font_size: "31sp"
            pos_hint: {"center_x": .65, "center_y": .83}
            color: "#031b31"

        ScrollView:
            do_scroll_y: True
            do_scroll_x: False
            size_hint_y: .60
            pos_hint: {"center_x": .5, "center_y": .46}
            bar_width: 0
            md_bg_color:"#dce8f3"

            GridLayout:
                size_hint_y: None
                row_default_height: 60
                height: self.minimum_height
                cols: 1
                spacing: 15, 30
                padding: 15, 30
                md_bg_color:"#dce8f3"

                MDFloatLayout:      

                    MDRoundFlatIconButton:
                        text: "                   Push up                           "
                        text_color: "white"
                        line_color: "#031b31"
                        md_bg_color:"#031b31"
                        pos_hint: {"center_x": .5, "center_y": .1}
                        font_size: "18sp"
                        padding: 17
                        font_name:"fonts\PlayfairDisplay-ExtraBold.ttf"
                        on_release:
                            root.manager.transition.direction = "left"
                            root.manager.current = "Start_Pu"
                
                    MDIconButton:
                        icon: "play-circle-outline"
                        pos_hint: {"center_x": .93, "center_y": .1}
                        user_font_size: "23sp"
                        theme_text_color: "Custom"
                        text_color:"white"
                        on_release:
                            root.manager.transition.direction = "left"
                            root.manager.current = "Start_Pu"
                    

                MDFloatLayout:              
                    MDRoundFlatIconButton:
                        text: "       Hammer Bicceps Curls        "
                        text_color: "white"
                        line_color: "#031b31"
                        md_bg_color:"#031b31"
                        pos_hint: {"center_x": .5, "center_y": .1}
                        font_size: "18sp"
                        padding: 17
                        font_name:"fonts\PlayfairDisplay-ExtraBold.ttf"
                        
                        on_release:
                            root.manager.transition.direction = "left"
                            root.manager.current = "Start_HBC"

                    MDIconButton:
                        icon: "play-circle-outline"
                        pos_hint: {"center_x": .93, "center_y": .1}
                        user_font_size: "23sp"
                        theme_text_color: "Custom"
                        text_color:"white"
                        on_release:
                            root.manager.transition.direction = "left"
                            root.manager.current = "Start_HBC"

                
                MDFloatLayout:              
                    MDRoundFlatIconButton:
                        text: "         Baebell Bicceps Curl          "
                        text_color: "white"
                        line_color: "#031b31"
                        md_bg_color:"#031b31"
                        pos_hint: {"center_x": .5, "center_y": .1}
                        font_size: "18sp"
                        padding: 17
                        font_name:"fonts\PlayfairDisplay-ExtraBold.ttf"
                        
                        on_release:
                            root.manager.transition.direction = "left"
                            root.manager.current = "Start_BBC"

                    MDIconButton:
                        icon: "play-circle-outline"
                        pos_hint: {"center_x": .93, "center_y": .1}
                        user_font_size: "23sp"
                        theme_text_color: "Custom"
                        text_color:"white"
                        on_release:
                            root.manager.transition.direction = "left"
                            root.manager.current = "Start_BBC"


                MDFloatLayout:              
                    MDRoundFlatIconButton:
                        text: "                          Squat                         "
                        text_color: "white"
                        line_color: "#031b31"
                        md_bg_color:"#031b31"
                        pos_hint: {"center_x": .5, "center_y": .1}
                        font_size: "18sp"
                        padding: 17
                        font_name:"fonts\PlayfairDisplay-ExtraBold.ttf"
                        
                        on_release:
                            root.manager.transition.direction = "left"
                            root.manager.current = "Start_Sq"

                    MDIconButton:
                        icon: "play-circle-outline"
                        pos_hint: {"center_x": .93, "center_y": .1}
                        user_font_size: "23sp"
                        theme_text_color: "Custom"
                        text_color:"white"
                        on_release:
                            root.manager.transition.direction = "left"
                            root.manager.current = "Start_Sq"

                            
                FloatLayout:
                    canvas:
                        Color:
                        RoundedRectangle:
                            source:r"pic\\1.jpeg"
                            pos: 20,460
                            size: 50, 50
                            radius: [30, 30, 30, 30]

                FloatLayout:
                    canvas:
                        Color:
                        RoundedRectangle:
                            source:r"pic\\Workout-amico.png"
                            pos: 20,374
                            size: 50,50
                            radius: [30, 30, 30, 30]
                FloatLayout:
                    canvas:
                        Color:
                        RoundedRectangle:
                            source: r"pic\\pus.jpeg"
                            pos: 20,640
                            size: 50,50
                            radius: [30, 30, 30, 30]
                FloatLayout:
                    canvas:
                        Color:
                        RoundedRectangle:
                            source:r"pic\\hummer.jpeg"
                            pos: 19,550
                            size: 50, 50
                            radius: [30, 30, 30, 30]
                
    MDFloatLayout:
        canvas:
            Color:
                rgba: 0.953, 0.957, 0.961, 1 
            RoundedRectangle:
                pos:0.1,0.01
                size: 450, 65
                radius: [16, 16, 0, 0]

    MDFloatLayout:
        MDIconButton:
            icon: "magnify"
            pos_hint: {"center_x": 0.75, "center_y": 0.037}
            user_font_size: "240sp"
            theme_text_color: "Custom"
            text_color: "#031b31"
            on_release:
                root.manager.transition.direction = "left"
                root.manager.current = "search"

        MDIconButton:
            icon: "home"
            pos_hint: {"center_x": 0.5, "center_y": 0.037}
            user_font_size: "260sp"
            theme_text_color: "Custom"
            text_color: "#031b31"
            on_release:
                root.manager.transition.direction = "right"
                root.manager.current = "homepage"

        MDIconButton:
            icon: "account-circle-outline"
            pos_hint: {"center_x": 0.25, "center_y":0.037}
            user_font_size: "240sp"
            theme_text_color: "Custom"
            text_color: "#031b31"
            on_release:
                root.manager.transition.direction = "right"
                root.manager.current = "profilepage"


'''
UpperBody='''
MDScreen:
    name: "UpperBody"
    MDFloatLayout:
        md_bg_color:"#dae7f2"

        MDLabel:
            text: "  Upper Body Program"
            font_name:"fonts\PlayfairDisplay-BlackItalic.ttf"
            font_size: "25sp"
            pos_hint: {"center_x": .54, "center_y": .87}
            text_color:"#031b31"

        ScrollView:
            do_scroll_y: True
            do_scroll_x: False
            size_hint_y: .70
            pos_hint: {"center_x": .5, "center_y": .43}
            bar_width: 0

            GridLayout:
                size_hint_y: None
                row_default_height: 90
                height: self.minimum_height
                cols: 1
                spacing: 15, 14
                padding: 15, 4

                MDFloatLayout:      

                    MDLabel:
                        text: "Day 1's Workout"
                        font_size: "14sp"
                        pos_hint: {"center_x": 0.5, "center_y": 0.8}
                        font_name: "fonts\PlayfairDisplay-Regular.ttf"
                        color: "#3b3e41"

                    MDLabel:
                        text: "2 Workouts | 45 Mins"
                        font_size: "14sp"
                        pos_hint: {"center_x": 1, "center_y": 0.8}
                        font_name: "fonts\PlayfairDisplay-Regular.ttf"
                        color: "#3b3e41"

                    MDRoundFlatIconButton:
                        text: "                   Push up                           "
                        text_color: "white"
                        line_color: "#031b31"
                        md_bg_color:"#031b31"
                        pos_hint: {"center_x": .5, "center_y": .1}
                        font_size: "18sp"
                        padding: 17
                        font_name:"fonts\PlayfairDisplay-ExtraBold.ttf"
                        on_release:
                            root.manager.transition.direction = "left"
                            root.manager.current = "UB_Start_Pu"

                    MDIconButton:
                        icon: "play-circle-outline"
                        pos_hint: {"center_x": .93, "center_y": .1}
                        user_font_size: "23sp"
                        theme_text_color: "Custom"
                        text_color:"white"
                        on_release:
                            root.manager.transition.direction = "left"
                            root.manager.current = "UB_Start_Pu"

                MDFloatLayout:              
                    MDRoundFlatIconButton:
                        text: "       Hammer Bicceps Curls        "
                        text_color: "white"
                        line_color: "#031b31"
                        md_bg_color:"#031b31"
                        pos_hint: {"center_x": .5, "center_y": .3}
                        font_size: "18sp"
                        padding: 17
                        font_name:"fonts\PlayfairDisplay-ExtraBold.ttf"

                        on_release:
                            root.manager.transition.direction = "left"
                            root.manager.current = "UB_Start_HBC"

                    MDIconButton:
                        icon: "play-circle-outline"
                        pos_hint: {"center_x": .93, "center_y": .29}
                        user_font_size: "23sp"
                        theme_text_color: "Custom"
                        text_color:"white"
                        on_release:
                            root.manager.transition.direction = "left"
                            root.manager.current = "UB_Start_HBC"

                MDFloatLayout:     
                    MDSeparator:
                        size_hint_x: .96
                        pos_hint: {'center_x': .5, 'center_y': .8}
                        width: 4.
                        color: "#75777a"
                    
                MDFloatLayout:
                    MDLabel:
                        text: "Day 2's Workout"
                        font_size: "14sp"
                        pos_hint: {"center_x": 0.5, "center_y": 1.6}
                        font_name:"fonts\PlayfairDisplay-Regular.ttf"
                        color: "#3b3e41"

                    MDLabel:
                        text: "2 Workouts | 35 Mins"
                        font_size: "14sp"
                        pos_hint: {"center_x": 1, "center_y":1.6}
                        font_name: "fonts\PlayfairDisplay-Regular.ttf"
                        color: "#3b3e41"
                
                MDFloatLayout:              
                    MDRoundFlatIconButton:
                        text: "         Baebell Bicceps Curl          "
                        text_color: "white"
                        line_color: "#031b31"
                        md_bg_color:"#031b31"
                        pos_hint: {"center_x": .5, "center_y": 2}
                        font_size: "18sp"
                        padding: 17
                        font_name:"fonts\PlayfairDisplay-ExtraBold.ttf"
                        
                        on_release:
                            root.manager.transition.direction = "left"
                            root.manager.current = "UB_Start_BBC"

                    MDIconButton:
                        icon: "play-circle-outline"
                        pos_hint: {"center_x": .93, "center_y": 2}
                        user_font_size: "23sp"
                        theme_text_color: "Custom"
                        text_color:"white"
                        on_release:
                            root.manager.transition.direction = "left"
                            root.manager.current = "UB_Start_BBC"

                MDFloatLayout:   
                    MDRoundFlatIconButton:
                        text: "                   Push up                           "
                        text_color: "white"
                        line_color: "#031b31"
                        md_bg_color:"#031b31"
                        pos_hint: {"center_x": .5, "center_y": 2.2}
                        font_size: "18sp"
                        padding: 17
                        font_name:"fonts\PlayfairDisplay-ExtraBold.ttf"
                        on_release:
                            root.manager.transition.direction = "left"
                            root.manager.current = "UB_Start_Pu"
                    
                    MDIconButton:
                        icon: "play-circle-outline"
                        pos_hint: {"center_x": .93, "center_y": 2.2}
                        user_font_size: "23sp"
                        theme_text_color: "Custom"
                        text_color:"white"
                        on_release:
                            root.manager.transition.direction = "left"
                            root.manager.current = "UB_Start_Pu"


                MDFloatLayout:     
                    MDSeparator:
                        size_hint_x: .96
                        pos_hint: {'center_x': .5, 'center_y': 2.7}
                        width: 4.
                        color: "#75777a"
                
                FloatLayout:
                    canvas:
                        Color:
                        RoundedRectangle:
                            source:r"pic\\pus.jpeg"
                            pos: 20,1235
                            size: 50, 50
                            radius: [30, 30, 30, 30]

                FloatLayout:
                    canvas:
                        Color:
                        RoundedRectangle:
                            source: r"pic\\1.jpeg"
                            pos: 22,990
                            size: 50, 50
                            radius: [30, 30, 30, 30]
                FloatLayout:
                    canvas:
                        Color:
                        RoundedRectangle:
                            source:r"pic\\pus.jpeg"
                            pos: 20,905
                            size: 50, 50
                            radius: [30, 30, 30, 30]
                FloatLayout:
                    canvas:
                        Color:
                        RoundedRectangle:
                            source: r"pic\\hummer.jpeg"
                            pos:20,1150
                            size: 50, 50
                            radius: [30, 30, 30, 30]

                FloatLayout:
                    MDLabel:
                        text: "Day 3 Rest Day"
                        font_size: "14sp"
                        pos_hint: {"center_x": 0.5, "center_y":8.2}
                        font_name:"fonts\PlayfairDisplay-Regular.ttf"
                        color: "#3b3e41"

                    Image:
                        source:r"pic\\sleep.png"
                        pos_hint: {"center_x": 0.9, "center_y":8.2}
                        size_hint: .4, .4
                        color: "#3b3e41"

                MDFloatLayout:     
                   
                
    MDFloatLayout:
        canvas:
            Color:
                rgba: 0.953, 0.957, 0.961, 1 
            RoundedRectangle:
                pos:0.1,0.01
                size: 450, 65
                radius: [16, 16, 0, 0]

    MDFloatLayout:
        MDIconButton:
            icon: "magnify"
            pos_hint: {"center_x": 0.75, "center_y": 0.037}
            user_font_size: "240sp"
            theme_text_color: "Custom"
            text_color: "#031b31"
            on_release:
                root.manager.transition.direction = "left"
                root.manager.current = "search"

        MDIconButton:
            icon: "home"
            pos_hint: {"center_x": 0.5, "center_y": 0.037}
            user_font_size: "260sp"
            theme_text_color: "Custom"
            text_color: "#031b31"
            on_release:
                root.manager.transition.direction = "right"
                root.manager.current = "homepage"

        MDIconButton:
            icon: "account-circle-outline"
            pos_hint: {"center_x": 0.25, "center_y":0.037}
            user_font_size: "240sp"
            theme_text_color: "Custom"
            text_color: "#031b31"
            on_release:
                root.manager.transition.direction = "right"
                root.manager.current = "profilepage"

'''

UB_Start_HBC = '''
MDScreen:
    name: "UB_Start_HBC"
    MDFloatLayout:
        md_bg_color:"#dae7f2"

        MyToggleButton:
            id: info_button
            text: "Info"
            text_color: "white"
            font_size: "12sp"
            font_name: "fonts\RamusBold-ZVPq8.ttf"
            group: "x"
            pos_hint: {"center_x": .39, "center_y": .64}
            on_release: app.show_info_description_HBC(self.state)
            md_bg_color:"#04213b"
                
        MyToggleButton:
            id: levels_button
            text: "Levels"
            text_color: "white"
            font_size: "12sp"
            font_name:"fonts\RamusBold-ZVPq8.ttf"
            group: "x"
            on_release: app.show_levels_description(self.state)
            pos_hint: {"center_x": .60, "center_y": .64}
            md_bg_color:"#04213b"
                

        MDIconButton:
            icon: "arrow-left"
            pos_hint: {"center_x": 0.06, "center_y":.94}
            user_font_size: "64sp"
            theme_text_color: "Custom"
            text_color:"#031b31"
            on_release:
                root.manager.transition.direction = "right"
                root.manager.current = "UpperBody"

        MDFloatLayout:
            MDLabel:
                text: "Hammer Biceps Curls"
                theme_text_color: "Custom"
                text_color: "black"
                size_hint: .9, .1
                pos_hint: {"center_x": .5, "center_y":.72}
                font_size: "29sp"
                font_name:"fonts\RamusBold-ZVPq8.ttf"
                    
        MDFloatLayout:
            MDCard:
                orientation: "vertical"
                padding: 0, 0, 0 , "36dp"
                size_hint: .9, .45
                pos_hint: {"center_x": .5, "center_y": .38}
                md_bg_color:"#031b31"
                        

                MDLabel:
                    id: description_label_HBC
                    text: "The Hammer bicep curl workout targets the biceps and forearms. This exercise involves holding the dumbbells in the palms facing each other and curling them simultaneously. This movement strengthens the biceps muscles for a more comprehensive arm workout. It improves grip strength and wrist stability."
                    size_hint: .9, .45
                    pos_hint: {"center_x": .5, "center_y": .4}
                    color: 1, 1, 1, 1
                    font_name: "fonts\RamusLight-p7vor.ttf"
                    font_size: "16sp"
                    opacity: 1 

            MDCard:
                orientation: "vertical"
                size_hint: .2, .05
                pos_hint: {"center_x": .5, "center_y": .2}
                md_bg_color:"#f5da88"

                MDLabel:
                    text: "Strength"
                    theme_text_color: "Custom"
                    text_color: "black"
                    size_hint: .8, .1
                    pos_hint: {"center_x": .5, "center_y": .5}
                    font_size: "12sp"
                    font_name:"fonts\RamusBold-ZVPq8.ttf"

            MDCard:
                orientation: "vertical"
                size_hint: .25, .05
                pos_hint: {"center_x": .75, "center_y": .2}
                md_bg_color:"#b15656"

                MDLabel:
                    text: "Resistance"
                    theme_text_color: "Custom"
                    text_color: "black"
                    size_hint: 0.8, .1
                    pos_hint: {"center_x": .5, "center_y": .5}
                    font_size: "12sp"
                    font_name:"fonts\RamusBold-ZVPq8.ttf"      

        MDFloatLayout:
            MDRoundFlatIconButton:
                text: "Start Workout"
                icon: "weight-lifter"
                icon_color:"white"
                text_color: "white"
                line_color: "#031b31"
                md_bg_color:"#031b31"
                pos_hint: {"center_x": .5, "center_y": .1}
                font_size: "15sp"
                font_name: "fonts\RamusBold-ZVPq8.ttf"
                on_release: 
                    app.start_workout_HBC()  
                    app.UB_progress()

            Image:
                source:r"pic\\Workout-amico.png"
                size_hint: .5, .5
                pos_hint: {"center_x": .5, "center_y": .87}
                allow_stretch: True
                keep_ratio: True

'''


UB_Start_BBC = '''
MDScreen:
    name: "UB_Start_BBC"
    MDFloatLayout:
        md_bg_color:"#dae7f2"

        MyToggleButton:
            id: info_button
            text: "Info"
            text_color: "white"
            font_size: "12sp"
            font_name:"fonts\RamusBold-ZVPq8.ttf"
            group: "x"
            pos_hint: {"center_x": .39, "center_y": .64}
            on_release: app.show_info_description_BBC(self.state)
            md_bg_color:"#04213b"
                
        MyToggleButton:
            id: levels_button
            text: "Levels"
            text_color: "white"
            font_size: "12sp"
            font_name: "fonts\RamusBold-ZVPq8.ttf"
            group: "x"
            on_release: app.show_levels_description(self.state)
            pos_hint: {"center_x": .60, "center_y": .64}
            md_bg_color:"#04213b"
                

        MDIconButton:
            icon: "arrow-left"
            pos_hint: {"center_x": 0.06, "center_y":.94}
            user_font_size: "64sp"
            theme_text_color: "Custom"
            text_color:"#031b31"
            on_release:
                root.manager.transition.direction = "right"
                root.manager.current = "UpperBody"

        MDFloatLayout:
            MDLabel:
                text: "Barbell Biceps Curls"
                theme_text_color: "Custom"
                text_color: "black"
                size_hint: .9, .1
                pos_hint: {"center_x": .55, "center_y":.72}
                font_size: "29sp"
                font_name:"fonts\RamusBold-ZVPq8.ttf"
                    
        MDFloatLayout:
            MDCard:
                orientation: "vertical"
                padding: 0, 0, 0 , "36dp"
                size_hint: .9, .45
                pos_hint: {"center_x": .5, "center_y": .38}
                md_bg_color:"#031b31"
                        

                MDLabel:
                    id: description_label_BBC
                    text: "The Barbell bicep curls are a classic strength-building exercise targeting the biceps muscles. Holding a barbell with an underhand grip, you curl the weight upward, focusing on contracting the biceps while keeping the elbows steady. This compound movement helps develop arm strength and size."
                    color: 1, 1, 1, 1
                    font_name: "fonts\RamusLight-p7vor.ttf"
                    padding:10
                    font_size: "16sp"
                    opacity: 1 

            MDCard:
                orientation: "vertical"
                size_hint: .2, .05
                pos_hint: {"center_x": .5, "center_y": .2}
                md_bg_color:"#f5da88"

                MDLabel:
                    text: "Strength"
                    theme_text_color: "Custom"
                    text_color: "black"
                    size_hint: .8, .1
                    pos_hint: {"center_x": .5, "center_y": .5}
                    font_size: "12sp"
                    font_name:"fonts\RamusBold-ZVPq8.ttf"

            MDCard:
                orientation: "vertical"
                size_hint: .25, .05
                pos_hint: {"center_x": .75, "center_y": .2}
                md_bg_color:"#b15656"

                MDLabel:
                    text: "Resistance"
                    theme_text_color: "Custom"
                    text_color: "black"
                    size_hint: 0.8, .1
                    pos_hint: {"center_x": .5, "center_y": .5}
                    font_size: "12sp"
                    font_name: "fonts\RamusBold-ZVPq8.ttf"      

        MDFloatLayout:
            MDRoundFlatIconButton:
                text: "Start Workout"
                icon: "weight-lifter"
                icon_color:"white"
                text_color: "white"
                line_color: "#031b31"
                md_bg_color:"#031b31"
                pos_hint: {"center_x": .5, "center_y": .1}
                font_size: "15sp"
                font_name:"fonts\RamusBold-ZVPq8.ttf"
                on_release: 
                    app.start_workout_BBC()  
                    app.UB_progress()
                    app.WK_counter()
                    app.reportData()

            Image:
                source: r"pic\\Workout-amico.png"
                size_hint: .5, .5
                pos_hint: {"center_x": .5, "center_y": .87}
                allow_stretch: True
                keep_ratio: True

'''

UB_Start_Pu = '''
MDScreen:
    name: "UB_Start_Pu"
    MDFloatLayout:
        md_bg_color:"#dae7f2"
        
        MyToggleButton:
            id: info_button
            text: "Info"
            text_color: "white"
            font_size: "12sp"
            font_name:"fonts\RamusBold-ZVPq8.ttf"
            group: "x"
            pos_hint: {"center_x": .39, "center_y": .64}
            on_release: app.show_info_description_Pu(self.state)
            md_bg_color:"#04213b"
                
        MyToggleButton:
            id: levels_button
            text: "Levels"
            text_color: "white"
            font_size: "12sp"
            font_name:"fonts\RamusBold-ZVPq8.ttf"
            group: "x"
            on_release: app.show_levels_description(self.state)
            pos_hint: {"center_x": .60, "center_y": .64}
            md_bg_color:"#04213b"
                

        MDIconButton:
            icon: "arrow-left"
            pos_hint: {"center_x": 0.06, "center_y":.94}
            user_font_size: "64sp"
            theme_text_color: "Custom"
            text_color:"#031b31"
            on_release:
                root.manager.transition.direction = "right"
                root.manager.current = "UpperBody"

        MDFloatLayout:
            MDLabel:
                text: "             Push Up     "
                theme_text_color: "Custom"
                text_color: "black"
                size_hint: .9, .1
                pos_hint: {"center_x": .55, "center_y":.72}
                font_size: "29sp"
                font_name:"fonts\RamusBold-ZVPq8.ttf"
                    
        MDFloatLayout:
            MDCard:
                orientation: "vertical"
                padding: 0, 0, 0 , "36dp"
                size_hint: .9, .45
                pos_hint: {"center_x": .5, "center_y": .38}
                md_bg_color:"#031b31"
                        

                MDLabel:
                    id: description_label_PU
                    text: "Push-ups are a fundamental exercise that strengthens the chest, shoulders, and triceps. Starting in a plank position with hands shoulder-width apart, lower your body until your chest nearly touches the ground, then push back up to the starting position. Push-ups require no equipment."
                    size_hint: .9, .45
                    pos_hint: {"center_x": .5, "center_y": .4}
                    color: 1, 1, 1, 1
                    font_name:"fonts\RamusLight-p7vor.ttf"
                    font_size: "16sp"
                    opacity: 1 

            MDCard:
                orientation: "vertical"
                size_hint: .2, .05
                pos_hint: {"center_x": .5, "center_y": .2}
                md_bg_color:"#f5da88"

                MDLabel:
                    text: "Strength"
                    theme_text_color: "Custom"
                    text_color: "black"
                    size_hint: .8, .1
                    pos_hint: {"center_x": .5, "center_y": .5}
                    font_size: "12sp"
                    font_name:"fonts\RamusBold-ZVPq8.ttf"

            MDCard:
                orientation: "vertical"
                size_hint: .25, .05
                pos_hint: {"center_x": .75, "center_y": .2}
                md_bg_color:"#5aa184"

                MDLabel:
                    text: "Stability"
                    theme_text_color: "Custom"
                    text_color: "black"
                    size_hint: 0.8, .1
                    pos_hint: {"center_x": .5, "center_y": .5}
                    font_size: "12sp"
                    padding:10
                    font_name: "fonts\RamusBold-ZVPq8.ttf"      

        MDFloatLayout:
            MDRoundFlatIconButton:
                text: "Start Workout"
                icon: "weight-lifter"
                icon_color:"white"
                text_color: "white"
                line_color: "#031b31"
                md_bg_color:"#031b31"
                pos_hint: {"center_x": .5, "center_y": .1}
                font_size: "15sp"
                font_name:"fonts\RamusBold-ZVPq8.ttf"
                on_release: 
                    app.start_workout_PU()
                    app.UB_progress()
                    app.WK_counter()
                    app.reportData()

            Image:
                source: r"pic\\Workout-amico.png"
                size_hint: .5, .5
                pos_hint: {"center_x": .5, "center_y": .87}
                allow_stretch: True
                keep_ratio: True

'''

LowerBody='''
MDScreen:
    name: "Lower Body"
    MDFloatLayout:
        md_bg_color:"#dae7f2"

        MDLabel:
            text: "   Lower Body Program"
            font_name:"fonts\PlayfairDisplay-BlackItalic.ttf"
            font_size: "25sp"
            pos_hint: {"center_x": .54, "center_y": .87}
            text_color:"#031b31"

        ScrollView:
            do_scroll_y: True
            do_scroll_x: False
            size_hint_y: .60
            pos_hint: {"center_x": .5, "center_y": .5}
            bar_width: 0

            GridLayout:
                size_hint_y: None
                row_default_height: 90
                height: self.minimum_height
                cols: 1
                spacing: 15, 10
                padding: 15, 10

                MDFloatLayout:           
                    MDLabel:
                        text: "Day 1's Workout"
                        font_size: "14sp"
                        pos_hint: {"center_x": 0.5, "center_y": 0.8}
                        font_name:"fonts\PlayfairDisplay-Regular.ttf"
                        color: "#3b3e41"

                    MDLabel:
                        text: "2 Workouts | 45 Mins"
                        font_size: "14sp"
                        pos_hint: {"center_x": 1, "center_y": 0.8}
                        font_name:"fonts\PlayfairDisplay-Regular.ttf"
                        color: "#3b3e41"

                    MDRoundFlatIconButton:
                        text: "                   Push up                           "
                        text_color: "white"
                        line_color: "#031b31"
                        md_bg_color:"#031b31"
                        pos_hint: {"center_x": .5, "center_y": .1}
                        font_size: "18sp"
                        padding: 17
                        font_name:"fonts\PlayfairDisplay-ExtraBold.ttf"
                        on_release:
                            root.manager.transition.direction = "left"
                            root.manager.current = "LB_Start_Pu"

                    MDIconButton:
                        icon: "play-circle-outline"
                        pos_hint: {"center_x": .93, "center_y": .1}
                        user_font_size: "23sp"
                        theme_text_color: "Custom"
                        text_color:"white"
                        on_release:
                            root.manager.transition.direction = "left"
                            root.manager.current = "LB_Start_Pu"
                MDFloatLayout:  

                    MDRoundFlatIconButton:
                        text: "                      Squat                              "
                        text_color: "white"
                        line_color: "#031b31"
                        md_bg_color:"#031b31"
                        pos_hint: {"center_x": .5, "center_y": .3}
                        font_size: "18sp"
                        padding: 17
                        font_name:"fonts\PlayfairDisplay-ExtraBold.ttf"
                        
                        on_release:
                            root.manager.transition.direction = "left"
                            root.manager.current = "LB_Start_Sq"

                    MDIconButton:
                        icon: "play-circle-outline"
                        pos_hint: {"center_x": .93, "center_y": .3}
                        user_font_size: "23sp"
                        theme_text_color: "Custom"
                        text_color:"white"
                        on_release:
                            root.manager.transition.direction = "left"
                            root.manager.current = "LB_Start_Sq"

                MDFloatLayout:     
                    MDSeparator:
                        size_hint_x: .96
                        pos_hint: {'center_x': .5, 'center_y': .8}
                        width: 4.
                        color: "#75777a"


                MDFloatLayout:
                    MDLabel:
                        text: "Day 2's Workout"
                        font_size: "14sp"
                        pos_hint: {"center_x": 0.5, "center_y": 1.6}
                        font_name: "fonts\PlayfairDisplay-Regular.ttf"
                        color: "#3b3e41"

                    MDLabel:
                        text: "2 Workouts | 45 Mins"
                        font_size: "14sp"
                        pos_hint: {"center_x": 1, "center_y":1.6}
                        font_name: "fonts\PlayfairDisplay-Regular.ttf"
                        color: "#3b3e41"
                
                MDFloatLayout:   
                    MDRoundFlatIconButton:
                        text: "                   Push up                           "
                        text_color: "white"
                        line_color: "#031b31"
                        md_bg_color:"#031b31"
                        pos_hint: {"center_x": .5, "center_y": 2}
                        font_size: "18sp"
                        padding: 17
                        font_name:"fonts\PlayfairDisplay-ExtraBold.ttf"
                        on_release:
                            root.manager.transition.direction = "left"
                            root.manager.current = "LB_Start_Pu"
                    
                    MDIconButton:
                        icon: "play-circle-outline"
                        pos_hint: {"center_x": .93, "center_y": 2}
                        user_font_size: "23sp"
                        theme_text_color: "Custom"
                        text_color:"white"
                        on_release:
                            root.manager.transition.direction = "left"
                            root.manager.current = "LB_Start_Pu"

                MDFloatLayout:  
                    MDRoundFlatIconButton:
                        text: "                      Squat                              "
                        text_color: "white"
                        line_color: "#031b31"
                        md_bg_color:"#031b31"
                        pos_hint: {"center_x": .5, "center_y": 2.21}
                        font_size: "18sp"
                        padding: 17
                        font_name:"fonts\PlayfairDisplay-ExtraBold.ttf"
                        
                        on_release:
                            root.manager.transition.direction = "left"
                            root.manager.current = "LB_Start_Sq"

                    MDIconButton:
                        icon: "play-circle-outline"
                        pos_hint: {"center_x": .93, "center_y": 2.21}
                        user_font_size: "23sp"
                        theme_text_color: "Custom"
                        text_color:"white"
                        on_release:
                            root.manager.transition.direction = "left"
                            root.manager.current = "LB_Start_Sq"


                MDFloatLayout:     
                    MDSeparator:
                        size_hint_x: .96
                        pos_hint: {'center_x': .5, 'center_y': 2.7}
                        width: 4.
                        color: "#75777a"
                
                FloatLayout:
                    canvas:
                        Color:
                        RoundedRectangle:
                            source: r"pic\\pus.jpeg"
                            pos: 20,1195
                            size: 50, 50
                            radius: [30, 30, 30, 30]

                FloatLayout:
                    canvas:
                        Color:
                        RoundedRectangle:
                            source: r"pic\\Workout-amico.png"
                            pos: 22,965
                            size: 55, 55
                            radius: [30, 30, 30, 30]
                FloatLayout:
                    canvas:
                        Color:
                        RoundedRectangle:
                            source:r"pic\\pus.jpeg"
                            pos: 20,885
                            size: 50, 50
                            radius: [30, 30, 30, 30]
                FloatLayout:
                    canvas:
                        Color:
                        RoundedRectangle:
                            source:r"pic\\Workout-amico.png"
                            pos:22,1113
                            size: 55, 55
                            radius: [30, 30, 30, 30]


                FloatLayout:
                    MDLabel:
                        text: "Day 3 Rest Day"
                        font_size: "14sp"
                        pos_hint: {"center_x": 0.5, "center_y":8}
                        font_name: "fonts\PlayfairDisplay-Regular.ttf"
                        color: "#3b3e41"

                    Image:
                        source:r"pic\\sleep.png"
                        pos_hint: {"center_x": 0.9, "center_y":8}
                        size_hint: .4, .4
                        color: "#3b3e41"

                MDFloatLayout:     
                    MDSeparator:
                        size_hint_x: .96
                        pos_hint: {'center_x': .5, 'center_y':8.5}
                        width: 4.
                        color: "#75777a"         
                
    MDFloatLayout:
        canvas:
            Color:
                rgba: 0.953, 0.957, 0.961, 1 
            RoundedRectangle:
                pos:0.1,0.01
                size: 450, 65
                radius: [16, 16, 0, 0]

    MDFloatLayout:
        MDIconButton:
            icon: "magnify"
            pos_hint: {"center_x": 0.75, "center_y": 0.037}
            user_font_size: "240sp"
            theme_text_color: "Custom"
            text_color: "#031b31"
            on_release:
                root.manager.transition.direction = "left"
                root.manager.current = "search"

        MDIconButton:
            icon: "home"
            pos_hint: {"center_x": 0.5, "center_y": 0.037}
            user_font_size: "260sp"
            theme_text_color: "Custom"
            text_color: "#031b31"
            on_release:
                root.manager.transition.direction = "right"
                root.manager.current = "homepage"

        MDIconButton:
            icon: "account-circle-outline"
            pos_hint: {"center_x": 0.25, "center_y":0.037}
            user_font_size: "240sp"
            theme_text_color: "Custom"
            text_color: "#031b31"
            on_release:
                root.manager.transition.direction = "right"
                root.manager.current = "profilepage"

                    
'''

LB_Start_Sq = '''
MDScreen:
    name: "LB_Start_Sq"
    MDFloatLayout:
        md_bg_color:"#dae7f2"

        MyToggleButton:
            id: info_button
            text: "Info"
            text_color: "white"
            font_size: "12sp"
            font_name:"fonts\RamusBold-ZVPq8.ttf"
            group: "x"
            pos_hint: {"center_x": .39, "center_y": .64}
            on_release: app.show_info_description_Sq(self.state)
            md_bg_color:"#04213b"
                
        MyToggleButton:
            id: levels_button
            text: "Levels"
            text_color: "white"
            font_size: "12sp"
            font_name: "fonts\RamusBold-ZVPq8.ttf"
            group: "x"
            on_release: app.show_levels_description(self.state)
            pos_hint: {"center_x": .60, "center_y": .64}
            md_bg_color:"#04213b"
                

        MDIconButton:
            icon: "arrow-left"
            pos_hint: {"center_x": 0.06, "center_y":.94}
            user_font_size: "64sp"
            theme_text_color: "Custom"
            text_color:"#031b31"
            on_release:
                root.manager.transition.direction = "right"
                root.manager.current = "Lower Body"

        MDFloatLayout:
            MDLabel:
                text: "             Squat     "
                theme_text_color: "Custom"
                text_color: "black"
                size_hint: .9, .1
                pos_hint: {"center_x": .55, "center_y":.72}
                font_size: "29sp"
                font_name: "fonts\RamusBold-ZVPq8.ttf"
                    
        MDFloatLayout:
            MDCard:
                orientation: "vertical"
                padding: 0, 0, 0 , "36dp"
                size_hint: .9, .45
                pos_hint: {"center_x": .5, "center_y": .38}
                md_bg_color:"#031b31"
                        

                MDLabel:
                    id: description_label_SQ
                    text: "A squat workout targets the lower body, strengthening muscles. By bending the knees and lowering the hips, then returning to standing, it builds functional strength, enhances balance, and improves mobility"
                    size_hint: .9, .45
                    pos_hint: {"center_x": .5, "center_y": .4}
                    color: 1, 1, 1, 1
                    font_name: "fonts\RamusLight-p7vor.ttf"
                    font_size: "16sp"
                    opacity: 1 

            MDCard:
                orientation: "vertical"
                size_hint: .2, .05
                pos_hint: {"center_x": .5, "center_y": .2}
                md_bg_color:"#f5da88"

                MDLabel:
                    text: "Strength"
                    theme_text_color: "Custom"
                    text_color: "black"
                    size_hint: .8, .1
                    pos_hint: {"center_x": .5, "center_y": .5}
                    font_size: "12sp"
                    font_name:"fonts\RamusBold-ZVPq8.ttf"

            MDCard:
                orientation: "vertical"
                size_hint: .25, .05
                pos_hint: {"center_x": .75, "center_y": .2}
                md_bg_color:"#b15656"

                MDLabel:
                    text: "Resistance"
                    theme_text_color: "Custom"
                    text_color: "black"
                    size_hint: 0.8, .1
                    pos_hint: {"center_x": .5, "center_y": .5}
                    font_size: "12sp"
                    font_name:"fonts\RamusBold-ZVPq8.ttf"      

        MDFloatLayout:
            MDRoundFlatIconButton:
                text: "Start Workout"
                icon: "weight-lifter"
                icon_color:"white"
                text_color: "white"
                line_color: "#031b31"
                md_bg_color:"#031b31"
                pos_hint: {"center_x": .5, "center_y": .1}
                font_size: "15sp"
                font_name:"fonts\RamusBold-ZVPq8.ttf"
                on_release: 
                    app.start_workout_SQ()
                    app.WK_counter()
                    app.reportData()

            Image:
                source: r"pic\\Workout-amico.png"
                size_hint: .5, .5
                pos_hint: {"center_x": .5, "center_y": .87}
                allow_stretch: True
                keep_ratio: True

'''
LB_Start_Pu = '''
MDScreen:
    name: "LB_Start_Pu"
    MDFloatLayout:
        md_bg_color:"#dae7f2"

        MyToggleButton:
            id: info_button
            text: "Info"
            text_color: "white"
            font_size: "12sp"
            font_name:"fonts\RamusBold-ZVPq8.ttf"
            group: "x"
            pos_hint: {"center_x": .39, "center_y": .64}
            on_release: app.show_info_description_Pu(self.state)
            md_bg_color:"#04213b"
                
        MyToggleButton:
            id: levels_button
            text: "Levels"
            text_color: "white"
            font_size: "12sp"
            font_name:"fonts\RamusBold-ZVPq8.ttf"
            group: "x"
            on_release: app.show_levels_description(self.state)
            pos_hint: {"center_x": .60, "center_y": .64}
            md_bg_color:"#04213b"
                

        MDIconButton:
            icon: "arrow-left"
            pos_hint: {"center_x": 0.06, "center_y":.94}
            user_font_size: "64sp"
            theme_text_color: "Custom"
            text_color:"#031b31"
            on_release:
                root.manager.transition.direction = "right"
                root.manager.current = "Lower Body"

        MDFloatLayout:
            MDLabel:
                text: "             Push Up     "
                theme_text_color: "Custom"
                text_color: "black"
                size_hint: .9, .1
                pos_hint: {"center_x": .55, "center_y":.72}
                font_size: "29sp"
                font_name:"fonts\RamusBold-ZVPq8.ttf"
                    
        MDFloatLayout:
            MDCard:
                orientation: "vertical"
                padding: 0, 0, 0 , "36dp"
                size_hint: .9, .45
                pos_hint: {"center_x": .5, "center_y": .38}
                md_bg_color:"#031b31"
                        

                MDLabel:
                    id: description_label_PU
                    text: "Push-ups are a fundamental exercise that strengthens the chest, shoulders, and triceps. Starting in a plank position with hands shoulder-width apart, lower your body until your chest nearly touches the ground, then push back up to the starting position. Push-ups require no equipment."
                    size_hint: .9, .45
                    pos_hint: {"center_x": .5, "center_y": .4}
                    color: 1, 1, 1, 1
                    font_name:"fonts\RamusLight-p7vor.ttf"
                    font_size: "16sp"
                    opacity: 1 

            MDCard:
                orientation: "vertical"
                size_hint: .2, .05
                pos_hint: {"center_x": .5, "center_y": .2}
                md_bg_color:"#f5da88"

                MDLabel:
                    text: "Strength"
                    theme_text_color: "Custom"
                    text_color: "black"
                    size_hint: .8, .1
                    pos_hint: {"center_x": .5, "center_y": .5}
                    font_size: "12sp"
                    font_name:"fonts\RamusBold-ZVPq8.ttf"

            MDCard:
                orientation: "vertical"
                size_hint: .25, .05
                pos_hint: {"center_x": .75, "center_y": .2}
                md_bg_color:"#5aa184"

                MDLabel:
                    text: "Stability"
                    theme_text_color: "Custom"
                    text_color: "black"
                    size_hint: 0.8, .1
                    pos_hint: {"center_x": .5, "center_y": .5}
                    font_size: "12sp"
                    padding:10
                    font_name: "fonts\RamusBold-ZVPq8.ttf"      

        MDFloatLayout:
            MDRoundFlatIconButton:
                text: "Start Workout"
                icon: "weight-lifter"
                icon_color:"white"
                text_color: "white"
                line_color: "#031b31"
                md_bg_color:"#031b31"
                pos_hint: {"center_x": .5, "center_y": .1}
                font_size: "15sp"
                font_name:"fonts\RamusBold-ZVPq8.ttf"
                on_release: 
                    app.start_workout_PU()
                    app.WK_counter()
                    app.reportData()


            Image:
                source: r"pic\\Workout-amico.png"
                size_hint: .5, .5
                pos_hint: {"center_x": .5, "center_y": .87}
                allow_stretch: True
                keep_ratio: True

'''
profilepage='''

ProfileCard:
    name: "profilepage"
    MDFloatLayout:
        md_bg_color:"#dae7f2"

        ProfileCard:
            size_hint_y: .65
            pos_hint: {"center_y": .8}
            elevation: 1
            md_bg_color: 1, 1, 1, 1
            radius: [0, 0, 20, 20]

            MDFloatLayout:
                canvas:
                    Color:
                        rgba: 0.0078, 0.1059, 0.1882, 1	  
                    RoundedRectangle:
                        pos:0.1,65
                        size: 450, 500
                        radius: [10, 10, 30, 30]

            # Username
            MDLabel:
                text: "My Profile"
                font_name:"fonts\PlayfairDisplay-BoldItalic.ttf"
                font_size: "20sp"
                pos_hint: {"center_x": .5, "center_y": .70}
                halign: "center"
                color: "white"

            Image:
                id:profileImage
                source:r"pic\\woman.png"
                pos_hint: {"center_x": .5, "center_y": .50}
                size_hint: .3,.3
                radius: [30, 30, 30, 30]


            MDLabel:
                id: name_index
                text: "Sara"
                font_name: "fonts\PlayfairDisplay-BoldItalic.ttf"
                color: "#eeeeee"
                font_size: "23sp"
                pos_hint: {"center_x": .48, "center_y": .31}
                halign: "center"

            MDLabel:  
                id:leve_index
                text: "level"
                font_name:"fonts\PlayfairDisplay-Regular.ttf"
                color: "#eeeeee"
                font_size: "14sp"
                pos_hint: {"center_x": .48, "center_y": .245}
                halign: "center"

            MDFloatLayout:
                canvas:
                    Color:
                        rgba: 0.9333, 0.9333, 0.9333, 1 
                    RoundedRectangle:
                        pos:50,40
                        size: 350, 70
                        radius: [15, 15, 15, 15]


            MDGridLayout:
                rows: 2
                cols: 3
                size_hint: .76, .1
                pos_hint: {"center_x": .5, "center_y": .14}

                MDLabel:
                    text: "Height"
                    font_name: "fonts\PlayfairDisplay-ExtraBold.ttf"
                    font_size: "14sp"
                    color: "#042645"
                    halign: "center"

                MDLabel:
                    text: "Weight"
                    font_name:"fonts\PlayfairDisplay-ExtraBold.ttf"
                    font_size: "14sp"
                    color: "#042645"
                    halign: "center"

                MDLabel:
                    text: "Age"
                    font_name:"fonts\PlayfairDisplay-ExtraBold.ttf"
                    font_size: "14sp"
                    color: "#042645"
                    halign: "center"
                    

                MDLabel:
                    id:height_index
                    text: "160 cm"
                    font_size: "12sp"
                    halign: "center"
                    font_name:"fonts\PlayfairDisplay-SemiBold.ttf"
                    color: "#3b3e41"

                MDLabel:
                    id:weight_index
                    text: "52 kg"
                    font_name:"fonts\PlayfairDisplay-SemiBold.ttf"
                    font_size: "12sp"
                    halign: "center"
                    color: "#3b3e41"

                MDLabel:
                    id:age_index
                    text: "24"
                    font_name: "fonts\PlayfairDisplay-SemiBold.ttf"
                    font_size: "12sp"
                    halign: "center"
                    color: "#3b3e41"

        MDLabel:
            text: "Account"
            font_name:"fonts\PlayfairDisplay-BoldItalic.ttf"
            font_size: "25sp"
            pos_hint: {"center_x": .54, "center_y": .45}
            color:"#031b31"

        ScrollView:
            do_scroll_y: True
            do_scroll_x: False
            size_hint_y: .80
            pos_hint: {"center_x": .5, "center_y": 0}
            bar_width: 0
            GridLayout:
                size_hint_y: None
                row_default_height: 60
                height: self.minimum_height
                cols: 1
                spacing: 15, 10
                padding: 15

                MDFloatLayout:
                    MDIconButton:
                        icon: "play-circle-outline"
                        pos_hint: {"center_x": .9, "center_y": .59}
                        user_font_size: "20sp"
                        theme_text_color: "Custom"
                        color: "#042645"
                        on_release:
                            root.manager.transition.direction = "left"
                            root.manager.current = "EditProfile"


                    MDLabel:
                        text: "Edit personal information"
                        font_name:"fonts\PlayfairDisplay-Medium.ttf"
                        font_size: "17sp"
                        pos_hint: {"center_x": .55, "center_y": .6}
                        color: "#042645"



                MDFloatLayout:
                    MDIconButton:
                        icon: "play-circle-outline"
                        pos_hint: {"center_x": .9, "center_y": .55}
                        user_font_size: "20sp"
                        theme_text_color: "Custom"
                        text_color: "#042645"
                        on_release:
                            root.manager.transition.direction = "left"
                            root.manager.current = "report"


                    MDLabel:
                        text: "Reports"
                        font_name:"fonts\PlayfairDisplay-Medium.ttf"
                        font_size: "17sp"
                        pos_hint: {"center_x": .55, "center_y": .55}
                        color: "#042645"

        # Logout Button
        MDRoundFlatIconButton:
            text: "Logout   "   
            line_color: "#031b31"
            md_bg_color:"#031b31"
            text_color: "white"
            font_size: "20sp"
            font_name:"fonts\PlayfairDisplay-Bold.ttf"
            size_hint: 0.79, 0.03
            pos_hint: {"center_x": 0.5, "center_y": 0.18}
            on_release:
                root.manager.transition.direction = "right"
                root.manager.current = "login"
              
                
    MDFloatLayout:
        canvas:
            Color:
                rgba: 0.953, 0.957, 0.961, 1 
            RoundedRectangle:
                pos:0.1,0.01
                size: 450, 65
                radius: [16, 16, 0, 0]

    MDFloatLayout:
        MDIconButton:
            icon: "magnify"
            pos_hint: {"center_x": 0.75, "center_y": 0.037}
            user_font_size: "240sp"
            theme_text_color: "Custom"
            text_color: "#031b31"
            on_release:
                root.manager.transition.direction = "left"
                root.manager.current = "search"

        MDIconButton:
            icon: "home"
            pos_hint: {"center_x": 0.5, "center_y": 0.037}
            user_font_size: "260sp"
            theme_text_color: "Custom"
            text_color: "#031b31"
            on_release:
                root.manager.transition.direction = "left"
                root.manager.current = "homepage"

        MDIconButton:
            icon: "account-circle-outline"
            pos_hint: {"center_x": 0.25, "center_y":0.037}
            user_font_size: "240sp"
            theme_text_color: "Custom"
            text_color: "#031b31"
            on_release:
                root.manager.transition.direction = "right"
                root.manager.current = "profilepage"



'''

EditProfile='''
EditeProfileCard:
    name: "EditProfile"
    MDFloatLayout:
        md_bg_color:"#dae7f2"

        MDLabel:
            text: "Personal information"
            font_name:"fonts\PlayfairDisplay-Bold.ttf"
            font_size: "28sp"
            pos_hint: {"center_x": 0.5, "center_y": 0.88}
            halign: "center"
            theme_text_color: "Custom"
            color: "black"

        MDIconButton:
            icon: "arrow-left"
            pos_hint: {"center_x": 0.06, "center_y":.94}
            user_font_size: "64sp"
            theme_text_color: "Custom"
            text_color:"#031b31"
            on_release:
                root.manager.transition.direction = "right"
                root.manager.current = "profilepage"

        ScrollView:
            do_scroll_y: True
            do_scroll_x: False
            size_hint_y: 1.6
            pos_hint: {"center_x": .5, "center_y":0}
            bar_width: 0
            GridLayout:
                size_hint_y: None
                row_default_height: 60
                height: self.minimum_height
                cols: 1
                spacing: 15, 10
                padding: 15

                MDFloatLayout:
                    size_hint: 0.79, 0.08
                    pos_hint: {"center_x": 0.5, "center_y": 0.75}

                    MDLabel:
                        text: "Name"
                        font_name:"fonts\PlayfairDisplay-Regular.ttf"
                        font_size: "14sp"
                        pos_hint: {"center_x": 0.5, "center_y": 0.9}
                        color: "#3b3e41"

                    TextInput:
                        id: name_index
                        text:str(name_index)
                        size_hint_y: 0.75
                        pos_hint: {"center_x": 0.49, "center_y": 0.4}
                        background_color: 0, 0, 0, 0
                        cursor_color: 0, 0, 0, 1
                        cursor_width: "1sp"
                        foreground_color: "black"
                        font_size: "17sp"
                        font_name:"fonts\PlayfairDisplay-SemiBold.ttf"
                        multiline: False
                        on_text: name_error_label.text =""
                        
                    MDLabel:
                        id: name_error_label
                        text: ""
                        font_name:"fonts\PlayfairDisplay-Regular.ttf"
                        font_size: "11sp"
                        pos_hint: {"center_x": 0.5, "center_y":1.5}
                        padding:17
                        color: "#cc0000"

                    Image:
                        source:r"pic\\user (2).png"
                        pos_hint: {"center_x": 0.96, "center_y": 0.9}
                        size_hint: .4, .4

                    MDFloatLayout:
                        pos_hint: {"center_x": 0.5, "center_y": 0}
                        size_hint_y: 0.03
                        md_bg_color:"#3b3e41"


                MDFloatLayout:
                    size_hint: 0.79, 0.08
                    pos_hint: {"center_x": 0.5, "center_y": 0.75}

                    MDLabel:
                        text: "Age"
                        font_name:"fonts\PlayfairDisplay-Regular.ttf"
                        font_size: "14sp"
                        pos_hint: {"center_x": 0.5, "center_y": 0.9}
                        color: "#3b3e41"

                    TextInput:
                        id:age_index
                        size_hint_y: 0.75
                        pos_hint: {"center_x": 0.49, "center_y": 0.4}
                        background_color: 0, 0, 0, 0
                        cursor_color: 0, 0, 0, 1
                        cursor_width: "1sp"
                        foreground_color: "black"
                        font_size: "17sp"
                        font_name:"fonts\PlayfairDisplay-SemiBold.ttf"
                        multiline: False
                        on_text: age_error_label.text =""

                    MDFloatLayout:
                        pos_hint: {"center_x": 0.5, "center_y": 0}
                        size_hint_y: 0.03
                        md_bg_color:"#3b3e41"

                MDFloatLayout:
                    size_hint: 0.79, 0.08
                    pos_hint: {"center_x": 0.5, "center_y": 0.55}

                    MDLabel:
                        text: "Weight"
                        font_name: "fonts\PlayfairDisplay-Regular.ttf"
                        color: "#3b3e41"
                        font_size: "14sp"
                        pos_hint: {"center_x": 0.5, "center_y": 0.9}

                    TextInput:
                        id:weight_index
                        size_hint_y: 0.75
                        pos_hint: {"center_x": 0.49, "center_y": 0.4}
                        background_color: 0, 0, 0, 0
                        cursor_color: 0, 0, 0, 1
                        cursor_width: "1sp"
                        foreground_color: "black"
                        font_name:"fonts\PlayfairDisplay-SemiBold.ttf"
                        font_size: "17sp"
                        multiline: False
                        on_text: weight_error_label.text =""

                    Image:
                        source:r"pic\\weight.png"
                        pos_hint: {"center_x": 0.96, "center_y": 0.9}
                        size_hint: .4, .4

                    MDFloatLayout:
                        pos_hint: {"center_x": 0.5, "center_y": 0}
                        size_hint_y: 0.03
                        md_bg_color:"#3b3e41"

                MDFloatLayout:
                    size_hint: 0.79, 0.08
                    pos_hint: {"center_x": 0.5, "center_y": 0.65}

                    MDLabel:
                        text: "Gender"
                        font_name:"fonts\PlayfairDisplay-Regular.ttf"
                        color: "#3b3e41"
                        font_size: "14sp"
                        pos_hint: {"center_x": 0.5, "center_y": 0.8}

                    MDLabel:
                        id:gender_index
                        text:str(gender_index)
                        size_hint_y: 0.75
                        pos_hint: {"center_x": 0.5, "center_y": 0.4}
                        background_color: 0, 0, 0, 0
                        foreground_color: "black"
                        font_name:"fonts\PlayfairDisplay-SemiBold.ttf"
                        font_size: "13sp"
                        on_text: gender_error_label.text =""

                    MDIconButton:
                        icon: "arrow-right-drop-circle"
                        pos_hint: {"center_x": 0.25, "center_y": 0.8}
                        user_font_size: "0.001sp"
                        theme_text_color: "Custom"
                        text_color: "#031b31"
                        on_release: root.menuG()
                        
                    MDList:
                        id: gender_results
                        pos_hint: {"center_x": .93, "center_y": .000001}
                        font_name:"fonts\PlayfairDisplay-Regular.ttf"

                    MDFloatLayout:
                        pos_hint: {"center_x": 0.5, "center_y": 0}
                        size_hint_y: 0.03
                        md_bg_color:"#3b3e41"

                MDFloatLayout:
                    size_hint: 0.79, 0.08
                    pos_hint: {"center_x": 0.5, "center_y": 0.55}

                    MDLabel:
                        text: "Level"
                        font_name:"fonts\PlayfairDisplay-Regular.ttf"
                        color: "#3b3e41"
                        font_size: "14sp"
                        pos_hint: {"center_x": 0.5, "center_y": 0.8}

                    
                    MDLabel:
                        id:level_index
                        text:str(level_index)
                        size_hint_y: 0.75
                        pos_hint: {"center_x": 0.5, "center_y": 0.4}
                        background_color: 0, 0, 0, 0
                        foreground_color: "black"
                        font_name:"fonts\PlayfairDisplay-SemiBold.ttf"
                        font_size: "13sp"
                        on_text: level_error_label.text =""


                    MDIconButton:
                        icon: "arrow-right-drop-circle"
                        pos_hint: {"center_x": 0.2, "center_y": 0.82}
                        size: 0.001,.001
                        theme_text_color: "Custom"
                        text_color: "#031b31"
                        on_release: root.menuL()
                                
                    MDList:
                        id: level_results
                        pos_hint: {"center_x": .9, "center_y": .6}
                        font_name:"fonts\PlayfairDisplay-Regular.ttf"

                    MDFloatLayout:
                        pos_hint: {"center_x": 0.5, "center_y": 0}
                        size_hint_y: 0.03
                        md_bg_color:"#3b3e41"
    MDFloatLayout:  
        MDLabel:
            id: weight_error_label
            text: ""
            font_name:"fonts\PlayfairDisplay-Regular.ttf"
            font_size: "11sp"
            pos_hint: {"center_x": 0.51, "center_y": 0.57 }
            padding:10
            color: "#cc0000"

        MDLabel:
            id: age_error_label
            text: ""
            font_name:"fonts\PlayfairDisplay-Regular.ttf"
            font_size: "11sp"
            pos_hint: {"center_x": 0.51, "center_y": 0.64}
            padding:10
            color: "#cc0000"

        MDLabel:
            id: gender_error_label
            text: ""
            font_name:"fonts\PlayfairDisplay-Regular.ttf"
            font_size: "11sp"
            pos_hint: {"center_x": 0.6, "center_y": 0.47}
            padding:10
            color: "#cc0000"
                        
        MDLabel:
            id: level_error_label
            font_name:"fonts\PlayfairDisplay-Regular.ttf"
            text: ""
            font_size: "11sp"
            pos_hint: {"center_x": 0.6, "center_y": 0.39}
            color:"#cc0000"   
                        



        MDRoundFlatIconButton:
            text: "Update changes   "
            size_hint: 0.79, 0.04
            icon: "account-check"
            icon_color:"white"
            pos_hint: {"center_x": 0.5, "center_y": 0.18}
            text_color: "white"
            line_color: "#031b31"
            md_bg_color:"#031b31"
            font_size: "20sp"
            font_name:"fonts\PlayfairDisplay-Bold.ttf"
            on_release: root.edit_profile_user(name_index, age_index, weight_index, gender_index, level_index)

    MDFloatLayout
        MDLabel:
            id: name_error_label
            text: ""
            font_name:"fonts\PlayfairDisplay-Regular.ttf"
            font_size: "11sp"
            pos_hint: {"center_x": 0.52, "center_y": 0.73}
            padding:17
            color: "#cc0000"

'''

report = '''
MDScreen:
    name: "report"
    MDFloatLayout:
        md_bg_color:"#dae7f2"

        MDLabel:
            text: "Reports"
            font_name:"fonts\PlayfairDisplay-Bold.ttf"
            font_size: "28sp"
            pos_hint: {"center_x": 0.5, "center_y": 0.94}
            halign: "center"
            theme_text_color: "Custom"
            color: "black"

        MDIconButton:
            icon: "arrow-left"
            pos_hint: {"center_x": 0.06, "center_y":.94}
            user_font_size: "64sp"
            theme_text_color: "Custom"
            text_color:"#031b31"
            on_release:
                root.manager.transition.direction = "right"
                root.manager.current = "profilepage"

        MDIconButton:
            icon: "menu"
            pos_hint: {"center_x": .87, "center_y": .94}
            user_font_size: "20sp"
            theme_text_color: "Custom"
            text_color:"#031b31"

        MDFloatLayout:
            canvas:
                Color:
                    rgba: 0.0078, 0.1059, 0.1882, 1	  
                RoundedRectangle:
                    pos:0.1,0
                    size: 450, 390
                    radius: [30, 30, 10, 10]

            MDLabel:
                text: "Plan Progress"
                text_color:"#031b31"
                font_name:"fonts\PlayfairDisplay-BlackItalic.ttf"
                font_size: "24sp"
                pos_hint: {"center_x": 0.7, "center_y": 0.51}
           
            MDFloatLayout:
                MDLabel:
                    text: "Upper body plan"
                    color:1,1,1
                    font_name:"fonts\PlayfairDisplay-Bold.ttf"
                    font_size: "22sp"
                    pos_hint: {"center_x": 0.55, "center_y": 0.43}
            MDFloatLayout:
                MDLabel:
                    color:"white"
                    text: "4 Workouts | 3 Days "
                    pos_hint: {"center_x": .65, "center_y": 0.375}
                    font_name:"fonts\PlayfairDisplay-Bold.ttf"
                    font_size: "12sp"  


            MDLabel:
                text: "   Total Progress"
                pos_hint: {"center_x": 0.78, "center_y": 0.22}
                color:"white"
                font_name:"fonts\\PlayfairDisplay-SemiBold.ttf"
                font_size: "16sp"  

            MDLabel:
                id: progress_label
                text: "{}%".format(app.UB_total_progress)  
                pos_hint: {"center_x": 0.91, "center_y": 0.16}
                color:"white"
                font_name:"fonts\PlayfairDisplay-Bold.ttf"
                font_size: "30sp"

            Image:
                id:prograssbar
                source:r"pic\\0.png"
                size_hint: .88, .88
                pos_hint: {"center_x": .5, "center_y": .17}
                allow_stretch: True
                keep_ratio: True


    MDFloatLayout:
        MDLabel:
            text: "Workouts"
            font_size: "16sp"
            pos_hint: {"center_x": 0.7, "center_y": 0.8}
            color:"#031b31"
            font_name:"fonts\PlayfairDisplay-BoldItalic.ttf"

        MDIcon:
            icon: "run-fast"
            color:"#031b31"
            width: "24dp"
            pos_hint: {"center_x": 0.15, "center_y": 0.8}

        MDLabel:
            id: wk_count
            text: "0"
            color:"#031b31"
            font_name:"fonts\PlayfairDisplay-BoldItalic.ttf"
            font_size: "16sp"
            pos_hint: {"center_x":1.3, "center_y": 0.8}

    MDFloatLayout:
        MDLabel:
            text: "Calories"
            font_size: "16sp"
            pos_hint: {"center_x": 0.7, "center_y": 0.75}
            color:"#031b31"
            font_name:"fonts\PlayfairDisplay-BoldItalic.ttf"

        MDIcon:
            icon: "fire"
            color:"#031b31"
            width: "24dp"
            pos_hint: {"center_x": 0.15, "center_y": 0.75}

        MDLabel:
            id:total_cal
            text: "0"
            color:"#031b31"
            font_name:"fonts\PlayfairDisplay-BoldItalic.ttf"
            font_size: "16sp"
            pos_hint: {"center_x":1.3, "center_y": 0.75}

    MDFloatLayout:
        MDLabel:
            text: "Time"
            font_size: "16sp"
            pos_hint: {"center_x": 0.7, "center_y": 0.7}
            color:"#031b31"
            font_name:"fonts\PlayfairDisplay-BoldItalic.ttf"

        MDIcon:
            icon: "clock-outline"
            color:"#031b31"
            width: "24dp"
            pos_hint: {"center_x": 0.15, "center_y": 0.7}

        MDLabel:
            id:wk_time
            text: "0"
            font_name:"fonts\PlayfairDisplay-BoldItalic.ttf"
            font_size: "16sp"
            pos_hint: {"center_x":1.3, "center_y": 0.7}

    MDFloatLayout:
        MDLabel:
            text: "Right reps"
            font_size: "16sp"
            pos_hint: {"center_x": 0.7, "center_y": 0.65}
            color:"#031b31"
            font_name:"fonts\PlayfairDisplay-BoldItalic.ttf"

        MDIcon:
            icon: "checkbox-outline"
            color:"#031b31"
            width: "24dp"
            pos_hint: {"center_x": 0.15, "center_y": 0.65}

        MDLabel:
            id:total_reps
            text: "0"
            font_name:"fonts\PlayfairDisplay-BoldItalic.ttf"
            font_size: "16sp"
            pos_hint: {"center_x":1.3, "center_y": 0.65}


    MDFloatLayout:
        MDLabel:
            text: "Wrong reps"
            font_size: "16sp"
            pos_hint: {"center_x": 0.7, "center_y": 0.6}
            color:"#031b31"
            font_name:"fonts\PlayfairDisplay-BoldItalic.ttf"

        MDIcon:
            icon: "alpha-x-box-outline"
            color:"#031b31"
            width: "24dp"
            pos_hint: {"center_x": 0.15, "center_y": 0.60}

        MDLabel:
            id:total_Wreps
            text: "0"
            font_name:"fonts\PlayfairDisplay-BoldItalic.ttf"
            font_size: "16sp"
            pos_hint: {"center_x":1.3, "center_y": 0.6}

            
'''

Start_HBC = '''
MDScreen:
    name: "Start_HBC"
    MDFloatLayout:
        md_bg_color:"#dae7f2"

        MyToggleButton:
            id: info_button
            text: "Info"
            text_color: "white"
            font_size: "12sp"
            font_name: "fonts\RamusBold-ZVPq8.ttf"
            group: "x"
            pos_hint: {"center_x": .39, "center_y": .64}
            on_release: app.show_info_description_HBC(self.state)
            md_bg_color:"#04213b"
                
        MyToggleButton:
            id: levels_button
            text: "Levels"
            text_color: "white"
            font_size: "12sp"
            font_name:"fonts\RamusBold-ZVPq8.ttf"
            group: "x"
            on_release: app.show_levels_description(self.state)
            pos_hint: {"center_x": .60, "center_y": .64}
            md_bg_color:"#04213b"
                

        MDIconButton:
            icon: "arrow-left"
            pos_hint: {"center_x": 0.06, "center_y":.94}
            user_font_size: "64sp"
            theme_text_color: "Custom"
            text_color:"#031b31"
            on_release:
                root.manager.transition.direction = "right"
                root.manager.current = "workout"

        MDFloatLayout:
            MDLabel:
                text: "Hammer Biceps Curls"
                theme_text_color: "Custom"
                text_color: "black"
                size_hint: .9, .1
                pos_hint: {"center_x": .5, "center_y":.72}
                font_size: "29sp"
                font_name:"fonts\RamusBold-ZVPq8.ttf"
                    
        MDFloatLayout:
            MDCard:
                orientation: "vertical"
                padding: 0, 0, 0 , "36dp"
                size_hint: .9, .45
                pos_hint: {"center_x": .5, "center_y": .38}
                md_bg_color:"#031b31"
                        

                MDLabel:
                    id: description_label_HBC
                    text: "The Hammer bicep curl workout targets the biceps and forearms. This exercise involves holding the dumbbells in the palms facing each other and curling them simultaneously. This movement strengthens the biceps muscles for a more comprehensive arm workout. It improves grip strength and wrist stability."
                    size_hint: .9, .45
                    pos_hint: {"center_x": .5, "center_y": .4}
                    color: 1, 1, 1, 1
                    font_name: "fonts\RamusLight-p7vor.ttf"
                    font_size: "16sp"
                    opacity: 1 

            MDCard:
                orientation: "vertical"
                size_hint: .2, .05
                pos_hint: {"center_x": .5, "center_y": .2}
                md_bg_color:"#f5da88"

                MDLabel:
                    text: "Strength"
                    theme_text_color: "Custom"
                    text_color: "black"
                    size_hint: .8, .1
                    pos_hint: {"center_x": .5, "center_y": .5}
                    font_size: "12sp"
                    font_name:"fonts\RamusBold-ZVPq8.ttf"

            MDCard:
                orientation: "vertical"
                size_hint: .25, .05
                pos_hint: {"center_x": .75, "center_y": .2}
                md_bg_color:"#b15656"

                MDLabel:
                    text: "Resistance"
                    theme_text_color: "Custom"
                    text_color: "black"
                    size_hint: 0.8, .1
                    pos_hint: {"center_x": .5, "center_y": .5}
                    font_size: "12sp"
                    font_name:"fonts\RamusBold-ZVPq8.ttf"      

        MDFloatLayout:
            MDRoundFlatIconButton:
                text: "Start Workout"
                icon: "weight-lifter"
                icon_color:"white"
                text_color: "white"
                line_color: "#031b31"
                md_bg_color:"#031b31"
                pos_hint: {"center_x": .5, "center_y": .1}
                font_size: "15sp"
                font_name: "fonts\RamusBold-ZVPq8.ttf"
                on_release: 
                    app.start_workout_HBC()  
                    app.WK_counter()
                    app.reportData()


            Image:
                source:r"pic\\Workout-amico.png"
                size_hint: .5, .5
                pos_hint: {"center_x": .5, "center_y": .87}
                allow_stretch: True
                keep_ratio: True

'''


Start_BBC = '''
MDScreen:
    name: "Start_BBC"
    MDFloatLayout:
        md_bg_color:"#dae7f2"

        MyToggleButton:
            id: info_button
            text: "Info"
            text_color: "white"
            font_size: "12sp"
            font_name:"fonts\RamusBold-ZVPq8.ttf"
            group: "x"
            pos_hint: {"center_x": .39, "center_y": .64}
            on_release: app.show_info_description_BBC(self.state)
            md_bg_color:"#04213b"
                
        MyToggleButton:
            id: levels_button
            text: "Levels"
            text_color: "white"
            font_size: "12sp"
            font_name: "fonts\RamusBold-ZVPq8.ttf"
            group: "x"
            on_release: app.show_levels_description(self.state)
            pos_hint: {"center_x": .60, "center_y": .64}
            md_bg_color:"#04213b"
                

        MDIconButton:
            icon: "arrow-left"
            pos_hint: {"center_x": 0.06, "center_y":.94}
            user_font_size: "64sp"
            theme_text_color: "Custom"
            text_color:"#031b31"
            on_release:
                root.manager.transition.direction = "right"
                root.manager.current = "workout"

        MDFloatLayout:
            MDLabel:
                text: "Barbell Biceps Curls"
                theme_text_color: "Custom"
                text_color: "black"
                size_hint: .9, .1
                pos_hint: {"center_x": .55, "center_y":.72}
                font_size: "29sp"
                font_name:"fonts\RamusBold-ZVPq8.ttf"
                    
        MDFloatLayout:
            MDCard:
                orientation: "vertical"
                padding: 0, 0, 0 , "36dp"
                size_hint: .9, .45
                pos_hint: {"center_x": .5, "center_y": .38}
                md_bg_color:"#031b31"
                        

                MDLabel:
                    id: description_label_BBC
                    text: "The Barbell bicep curls are a classic strength-building exercise targeting the biceps muscles. Holding a barbell with an underhand grip, you curl the weight upward, focusing on contracting the biceps while keeping the elbows steady. This compound movement helps develop arm strength and size."
                    color: 1, 1, 1, 1
                    font_name: "fonts\RamusLight-p7vor.ttf"
                    padding:10
                    font_size: "16sp"
                    opacity: 1 

            MDCard:
                orientation: "vertical"
                size_hint: .2, .05
                pos_hint: {"center_x": .5, "center_y": .2}
                md_bg_color:"#f5da88"

                MDLabel:
                    text: "Strength"
                    theme_text_color: "Custom"
                    text_color: "black"
                    size_hint: .8, .1
                    pos_hint: {"center_x": .5, "center_y": .5}
                    font_size: "12sp"
                    font_name:"fonts\RamusBold-ZVPq8.ttf"

            MDCard:
                orientation: "vertical"
                size_hint: .25, .05
                pos_hint: {"center_x": .75, "center_y": .2}
                md_bg_color:"#b15656"

                MDLabel:
                    text: "Resistance"
                    theme_text_color: "Custom"
                    text_color: "black"
                    size_hint: 0.8, .1
                    pos_hint: {"center_x": .5, "center_y": .5}
                    font_size: "12sp"
                    font_name: "fonts\RamusBold-ZVPq8.ttf"      

        MDFloatLayout:
            MDRoundFlatIconButton:
                text: "Start Workout"
                icon: "weight-lifter"
                icon_color:"white"
                text_color: "white"
                line_color: "#031b31"
                md_bg_color:"#031b31"
                pos_hint: {"center_x": .5, "center_y": .1}
                font_size: "15sp"
                font_name:"fonts\RamusBold-ZVPq8.ttf"
                on_release: 
                    app.start_workout_BBC() 
                    app.WK_counter() 
                    app.reportData()


            Image:
                source: r"pic\\Workout-amico.png"
                size_hint: .5, .5
                pos_hint: {"center_x": .5, "center_y": .87}
                allow_stretch: True
                keep_ratio: True

'''

Start_Sq = '''
MDScreen:
    name: "Start_Sq"
    MDFloatLayout:
        md_bg_color:"#dae7f2"

        MyToggleButton:
            id: info_button
            text: "Info"
            text_color: "white"
            font_size: "12sp"
            font_name:"fonts\RamusBold-ZVPq8.ttf"
            group: "x"
            pos_hint: {"center_x": .39, "center_y": .64}
            on_release: app.show_info_description_Sq(self.state)
            md_bg_color:"#04213b"
                
        MyToggleButton:
            id: levels_button
            text: "Levels"
            text_color: "white"
            font_size: "12sp"
            font_name: "fonts\RamusBold-ZVPq8.ttf"
            group: "x"
            on_release: app.show_levels_description(self.state)
            pos_hint: {"center_x": .60, "center_y": .64}
            md_bg_color:"#04213b"
                

        MDIconButton:
            icon: "arrow-left"
            pos_hint: {"center_x": 0.06, "center_y":.94}
            user_font_size: "64sp"
            theme_text_color: "Custom"
            text_color:"#031b31"
            on_release:
                root.manager.transition.direction = "right"
                root.manager.current = "workout"

        MDFloatLayout:
            MDLabel:
                text: "             Squat     "
                theme_text_color: "Custom"
                text_color: "black"
                size_hint: .9, .1
                pos_hint: {"center_x": .55, "center_y":.72}
                font_size: "29sp"
                font_name: "fonts\RamusBold-ZVPq8.ttf"
                    
        MDFloatLayout:
            MDCard:
                orientation: "vertical"
                padding: 0, 0, 0 , "36dp"
                size_hint: .9, .45
                pos_hint: {"center_x": .5, "center_y": .38}
                md_bg_color:"#031b31"
                        

                MDLabel:
                    id: description_label_SQ
                    text: "A squat workout targets the lower body, strengthening muscles. By bending the knees and lowering the hips, then returning to standing, it builds functional strength, enhances balance, and improves mobility"
                    size_hint: .9, .45
                    pos_hint: {"center_x": .5, "center_y": .4}
                    color: 1, 1, 1, 1
                    font_name: "fonts\RamusLight-p7vor.ttf"
                    font_size: "16sp"
                    opacity: 1 

            MDCard:
                orientation: "vertical"
                size_hint: .2, .05
                pos_hint: {"center_x": .5, "center_y": .2}
                md_bg_color:"#f5da88"

                MDLabel:
                    text: "Strength"
                    theme_text_color: "Custom"
                    text_color: "black"
                    size_hint: .8, .1
                    pos_hint: {"center_x": .5, "center_y": .5}
                    font_size: "12sp"
                    font_name:"fonts\RamusBold-ZVPq8.ttf"

            MDCard:
                orientation: "vertical"
                size_hint: .25, .05
                pos_hint: {"center_x": .75, "center_y": .2}
                md_bg_color:"#b15656"

                MDLabel:
                    text: "Resistance"
                    theme_text_color: "Custom"
                    text_color: "black"
                    size_hint: 0.8, .1
                    pos_hint: {"center_x": .5, "center_y": .5}
                    font_size: "12sp"
                    font_name:"fonts\RamusBold-ZVPq8.ttf"      

        MDFloatLayout:
            MDRoundFlatIconButton:
                text: "Start Workout"
                icon: "weight-lifter"
                icon_color:"white"
                text_color: "white"
                line_color: "#031b31"
                md_bg_color:"#031b31"
                pos_hint: {"center_x": .5, "center_y": .1}
                font_size: "15sp"
                font_name:"fonts\RamusBold-ZVPq8.ttf"
                on_release: 
                    app.start_workout_SQ()
                    app.WK_counter()
                    app.reportData()
            Image:
                source: r"pic\\Workout-amico.png"
                size_hint: .5, .5
                pos_hint: {"center_x": .5, "center_y": .87}
                allow_stretch: True
                keep_ratio: True

'''

Start_Pu = '''
MDScreen:
    name: "Start_Pu"
    MDFloatLayout:
        md_bg_color:"#dae7f2"

        MyToggleButton:
            id: info_button
            text: "Info"
            text_color: "white"
            font_size: "12sp"
            font_name:"fonts\RamusBold-ZVPq8.ttf"
            group: "x"
            pos_hint: {"center_x": .39, "center_y": .64}
            on_release: app.show_info_description_Pu(self.state)
            md_bg_color:"#04213b"
                
        MyToggleButton:
            id: levels_button
            text: "Levels"
            text_color: "white"
            font_size: "12sp"
            font_name:"fonts\RamusBold-ZVPq8.ttf"
            group: "x"
            on_release: app.show_levels_description(self.state)
            pos_hint: {"center_x": .60, "center_y": .64}
            md_bg_color:"#04213b"
                

        MDIconButton:
            icon: "arrow-left"
            pos_hint: {"center_x": 0.06, "center_y":.94}
            user_font_size: "64sp"
            theme_text_color: "Custom"
            text_color:"#031b31"
            on_release:
                root.manager.transition.direction = "right"
                root.manager.current = "workout"

        MDFloatLayout:
            MDLabel:
                text: "             Push Up     "
                theme_text_color: "Custom"
                text_color: "black"
                size_hint: .9, .1
                pos_hint: {"center_x": .55, "center_y":.72}
                font_size: "29sp"
                font_name:"fonts\RamusBold-ZVPq8.ttf"
                    
        MDFloatLayout:
            MDCard:
                orientation: "vertical"
                padding: 0, 0, 0 , "36dp"
                size_hint: .9, .45
                pos_hint: {"center_x": .5, "center_y": .38}
                md_bg_color:"#031b31"
                        

                MDLabel:
                    id: description_label_PU
                    text: "Push-ups are a fundamental exercise that strengthens the chest, shoulders, and triceps. Starting in a plank position with hands shoulder-width apart, lower your body until your chest nearly touches the ground, then push back up to the starting position. Push-ups require no equipment."
                    size_hint: .9, .45
                    pos_hint: {"center_x": .5, "center_y": .4}
                    color: 1, 1, 1, 1
                    font_name:"fonts\RamusLight-p7vor.ttf"
                    font_size: "16sp"
                    opacity: 1 

            MDCard:
                orientation: "vertical"
                size_hint: .2, .05
                pos_hint: {"center_x": .5, "center_y": .2}
                md_bg_color:"#f5da88"

                MDLabel:
                    text: "Strength"
                    theme_text_color: "Custom"
                    text_color: "black"
                    size_hint: .8, .1
                    pos_hint: {"center_x": .5, "center_y": .5}
                    font_size: "12sp"
                    font_name:"fonts\RamusBold-ZVPq8.ttf"

            MDCard:
                orientation: "vertical"
                size_hint: .25, .05
                pos_hint: {"center_x": .75, "center_y": .2}
                md_bg_color:"#5aa184"

                MDLabel:
                    text: "Stability"
                    theme_text_color: "Custom"
                    text_color: "black"
                    size_hint: 0.8, .1
                    pos_hint: {"center_x": .5, "center_y": .5}
                    font_size: "12sp"
                    padding:10
                    font_name: "fonts\RamusBold-ZVPq8.ttf"      

        MDFloatLayout:
            MDRoundFlatIconButton:
                text: "Start Workout"
                icon: "weight-lifter"
                icon_color:"white"
                text_color: "white"
                line_color: "#031b31"
                md_bg_color:"#031b31"
                pos_hint: {"center_x": .5, "center_y": .1}
                font_size: "15sp"
                font_name:"fonts\RamusBold-ZVPq8.ttf"
                on_release: 
                    app.start_workout_PU()
                    app.WK_counter()
                    app.reportData()

            Image:
                source: r"pic\\Workout-amico.png"
                size_hint: .5, .5
                pos_hint: {"center_x": .5, "center_y": .87}
                allow_stretch: True
                keep_ratio: True

'''
first_page = '''
Screen:
    name: "firstpage"
    MDFloatLayout:
        md_bg_color: "#dae7f2"

        Image:
            source: r"pic\logo navie.png"
            size_hint: 0.45, 0.45
            pos_hint: {"center_x": 0.5, "center_y": 0.7}

        MDLabel:
            text: "Welcome to Fitness Tracker"
            font_name: "fonts\\RamusBold-ZVPq8.ttf"
            pos_hint: {"center_x": 0.5, "center_y": 0.18}
            halign: "center"
            theme_text_color: "Custom"
            font_name:"fonts\PlayfairDisplay-Italic.ttf"
            text_color: "#031b31"

        MDRoundFlatButton:
            text: "                    Sign up                    "
            text_color: "white"
            line_color: "#031b31"
            md_bg_color:"#031b31"
            pos_hint: {"center_x": .5, "center_y": .34}
            font_size: "19sp"
            font_name:"fonts\PlayfairDisplay-SemiBold.ttf"
            padding:10
            on_release:
                root.manager.transition.direction = "left"
                root.manager.current =  "CreateAccount"

        MDRoundFlatButton:
            text: "                      Login                      "
            text_color: "white"
            line_color: "#031b31"
            md_bg_color:"#031b31"
            pos_hint: {"center_x": .5, "center_y": .25}
            font_size: "19sp"
            font_name:"fonts\PlayfairDisplay-SemiBold.ttf"
            padding:10
            on_release:
                root.manager.transition.direction = "left"
                root.manager.current =  "login"
'''


class ProfileCard(Screen):
    def on_enter(self):
        store = JsonStore('data.json')
        user_uid = store.get('user_id')['value']
        print(user_uid)
        Clock.schedule_once(lambda dt: self.update_labels(user_uid), 0.1)

    def update_labels(self, user_uid):

        user_data = db.reference('user').child(user_uid).get()
        print("Cront user Fond")

        if user_data:
            self.ids.height_index.text = user_data.get('height', '')
            self.ids.weight_index.text = user_data.get('weight', '')
            self.ids.age_index.text = user_data.get('age', '')
            self.ids.name_index.text = user_data.get('name', '')
            self.ids.leve_index.text=user_data.get('level', '')


        screen_manager = self.manager
        if user_data.get('gender', '') == "Male":
            profilepage = screen_manager.get_screen("profilepage")
            profilepage.ids.profileImage.source = "pic\\man.png" 
        elif user_data.get('gender', '') == "Female":
            profilepage = screen_manager.get_screen("profilepage")
            profilepage.ids.profileImage.source = "pic\\woman.png" 



class HomeCard(Screen):
    def on_enter(self):
        store = JsonStore('data.json')
        user_uid = store.get('user_id')['value']
        print(user_uid)
        Clock.schedule_once(lambda dt: self.update_labels(user_uid), 0.1)

    def update_labels(self, user_uid):
        user_data = db.reference('user').child(user_uid).get()
        print("Cront user Fond")

        if user_data:
            self.ids.name_index.text = "Hello, " + user_data.get('name', '')


class EditeProfileCard(Screen):

    def on_enter(self):
        store = JsonStore('data.json')
        user_uid = store.get('user_id')['value']
        Clock.schedule_once(lambda dt: self.update_labels(user_uid), 0.1)

    def update_labels(self, user_uid):
        user_data = db.reference('user').child(user_uid).get()

        if user_data:
            self.ids.weight_index.text = user_data.get('weight', '')
            self.ids.age_index.text = user_data.get('age', '')
            self.ids.name_index.text = user_data.get('name', '')
            self.ids.level_index.text = user_data.get('level', '')
            self.ids.gender_index.text = user_data.get('gender', '')

    def edit_profile_user(self, name_index, age_index, weight_index, gender_index, level_index):
        name = name_index.text
        age = age_index.text
        weight = weight_index.text
        gender = gender_index.text
        level = level_index.text
        if all([
        self.username_check(name),  self.weight_check(weight),  self.age_check(age), 
        self.gender_check(gender), self.level_check(level)]):
            
            try:
                store = JsonStore('data.json')
                user_uid = store.get('user_id')['value']
                db_ref = db.reference('user')
                db_ref.child(user_uid).update({
                    'name': name,
                    'age': age,
                    'weight': weight,
                    'gender': gender,
                    'level': level
                })
                MDApp.get_running_app().root.current = 'profilepage'
                
            except ValueError as e:
                    print('Error signing up:', str(e))


    def username_check(self, username):
        username_pattern = r"^\w{1,10}$"
        if not re.match(username_pattern, username):
            self.ids.name_error_label.text = "* The username should be between 1 and 10 characters"
            username = ""
            return False
        else:
            self.ids.name_error_label.text = ""
            return True

    def email_check(self, email):
        email_pattern = r"^[a-zA-Z0-9_.+-]+@(?:gmail\.com|yahoo\.com|hotmail\.com)$"
        if not re.match(email_pattern, email):
            self.ids.email_error_label.text = "* Invalid email format" 
            email = ""  
            return False
        else:
            self.ids.email_error_label.text= ""
            return True
        
    def weight_check(self, weight):
        if not re.match(r"^\d+$", weight):
            self.ids.weight_error_label.text = "* invalid input, make sure to input a number in weight"
            weight = ""
            return False
        else:
            self.ids.weight_error_label.text = ""
            return True


    def age_check(self, age):
        if not re.match(r"^(|\d+)$", age):
            self.ids.age_error_label.text = "* Invalid input. Please input a number for age."
            age = "" 
            return False   
        else:
            age = ""
            return True 
        
    def gender_check(self,gender):
        if  gender == "" :
            self.ids.gender_error_label.text = "* Invalid input. Please choose a gender."
            gender = ""  
            return False              
        else:
            self.ids.gender_error_label.text = ""  
            return True 
        
    def level_check(self,level):
        if  level == "" :
            self.ids.level_error_label.text = "* Invalid input. Please choose a level."
            level = ""  
            return False              
        else:
            self.ids.level_error_label.text = ""  
            return True 
        
    def menuG(self):
        self.ids.gender_results.bind(on_touch_down=lambda instance, 
                           touch: self.ids.gender_results.clear_widgets() if not self.ids.gender_results.collide_point(*touch.pos) else None)
        items_G = ['Male', 'Female']
        for Gender in items_G:
            list_item = OneLineListItem(text=Gender)
            list_item.bind(on_release=lambda instance: self.selected_gender(instance, self.ids.gender_results))
            self.ids.gender_results.add_widget(list_item)

    def selected_gender(self, instance, gender_results):

        screen_manager = self.manager
        selected_gender_ = instance.text
        if selected_gender_ == "Male":
            self.ids.gender_index.text = "Male"
            profilepage = screen_manager.get_screen("profilepage")
            profilepage.ids.profileImage.source = "pic\\man.png" 
        elif selected_gender_ == "Female":
            self.ids.gender_index.text = "Female"
            profilepage = screen_manager.get_screen("profilepage")
            profilepage.ids.profileImage.source = "pic\\woman.png" 
        gender_results.clear_widgets()

    def menuL(self):
        self.ids.level_results.bind(on_touch_down=lambda instance, 
                           touch: self.ids.level_results.clear_widgets() if not self.ids.level_results.collide_point(*touch.pos) else None)
        items_L =['Beginner','Intermediate','Advanced']
        for level in items_L:
            list_item = OneLineListItem(text=level)
            list_item.bind(on_release=lambda instance: self.selected_level(instance, self.ids.level_results))
            self.ids.level_results.add_widget(list_item)
            
    def selected_level(self, instance, level_results):
        selected_level_ = instance.text
        if selected_level_ == "Beginner":
            self.ids.level_index.text = "Beginner"
        elif selected_level_ == "Intermediate":
            self.ids.level_index.text = "Intermediate"
        elif selected_level_ == "Advanced":
            self.ids.level_index.text = "Advanced"
        level_results.clear_widgets()


class MyToggleButton(MDRectangleFlatButton, MDToggleButton):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.font_color_down = "white"
        self.font_color_normal = "white"
        self.background_down ="#7e8c9a"
        self.background_normal="#04213b"
        self.line_color="#04213b"
        self.md_bg_color="#34393c"

class FitnessApp(MDApp):
    UB_total_progress = 0 
    WK_total_progress = 0 

    def build(self):
        screen_manager = ScreenManager()
        screen_manager.add_widget(Builder.load_string(first_page))
        screen_manager.add_widget(Builder.load_string(CreateAccount))
        screen_manager.add_widget(Builder.load_string(CreateAccount2))
        screen_manager.add_widget( Builder.load_string(Login))
        screen_manager.add_widget(Builder.load_string(Homepage))
        screen_manager.add_widget(Builder.load_string(workout))
        screen_manager.add_widget( Builder.load_string(UpperBody))
        screen_manager.add_widget(Builder.load_string(UB_Start_HBC))
        screen_manager.add_widget(Builder.load_string(UB_Start_BBC))
        screen_manager.add_widget(Builder.load_string(UB_Start_Pu))
        screen_manager.add_widget(Builder.load_string(LowerBody))
        screen_manager.add_widget(Builder.load_string(LB_Start_Sq))
        screen_manager.add_widget(Builder.load_string(LB_Start_Pu))
        screen_manager.add_widget(Builder.load_string(profilepage))
        screen_manager.add_widget(Builder.load_string(EditProfile))
        screen_manager.add_widget(Builder.load_string(report))
        screen_manager.add_widget(Builder.load_string(Start_HBC))
        screen_manager.add_widget(Builder.load_string(Start_BBC))
        screen_manager.add_widget(Builder.load_string(Start_Sq))
        screen_manager.add_widget(Builder.load_string(Start_Pu))
        screen_manager.add_widget(Builder.load_string(search))

        Window.size = (300,550)
        return  screen_manager

    def reportData(self):
        import Realtime.BBC.RealtimeBBC as RealtimeBBC 
        import Realtime.HBC.RealtimeHBC as RealtimeHBC
        import Realtime.Pushup.RealtimePushUp as RealtimePushUp 
        import Realtime.Squat.RealtimeSquat as RealtimeSquat  

        BBCreps =RealtimeBBC.total_reps
        BBCwreps = RealtimeBBC.total_Wreps
        BBCTime =RealtimeBBC.total_time
        BBC_cal =RealtimeBBC.total_cal

        HBCreps = RealtimeHBC.total_reps
        HBCwreps = RealtimeHBC.total_Wreps
        HBCTime =RealtimeHBC.total_time
        HBC_cal =RealtimeHBC.total_cal

        PUreps = RealtimePushUp.total_reps
        Puwreps = RealtimePushUp.total_Wreps
        PUTime =RealtimePushUp.total_time
        PU_cal =RealtimePushUp.total_cal      

        SQreps = RealtimeSquat.total_reps
        SQwreps = RealtimeSquat.total_Wreps
        SQTime =RealtimeSquat.total_time
        SQ_cal =RealtimeSquat.total_cal 


        Tcal=HBC_cal+BBC_cal+PU_cal+SQ_cal
        formatted_cal = "{:.2f}".format(Tcal)
        Treps=BBCreps+HBCreps+PUreps+SQreps
        Twreps =BBCwreps+HBCwreps+Puwreps+SQwreps
        Ttime =BBCTime+HBCTime+PUTime+SQTime
        Ttime_min =Ttime/60
        formatted_time = "{:.2f}".format(Ttime_min)

        report_screen = self.root.get_screen("report")
        report_screen.ids.wk_time.text = str(formatted_time)
        report_screen.ids.total_reps.text = str(Treps)
        report_screen.ids.total_Wreps.text = str(Twreps)
        report_screen.ids.total_cal.text = str(formatted_cal)


    def WK_counter(self):
        self.WK_total_progress += 1
        self.root.get_screen("report").ids.wk_count.text = str(self.WK_total_progress)

    def UB_progress(self):
        self.UB_total_progress += 25
        if self.UB_total_progress > 100:
            self.UB_total_progress = 100  
        if self.UB_total_progress ==  25:
            self.root.get_screen("report").ids.prograssbar.source= "pic\\25.png"
        elif self.UB_total_progress ==  50:
            self.root.get_screen("report").ids.prograssbar.source= "pic\\50.png"
        elif self.UB_total_progress ==  75:
            self.root.get_screen("report").ids.prograssbar.source= "pic\\75.png"
        elif self.UB_total_progress ==  100:
            self.root.get_screen("report").ids.prograssbar.source= "pic\\100.png"

        self.root.get_screen("report").ids.progress_label.text = "{}%".format(self.UB_total_progress)


    def show_info_description_HBC(self, state):
        start_hbc_screen = self.root.get_screen("Start_HBC")
        description_label = start_hbc_screen.ids.description_label_HBC
        UB_start_hbc_screen = self.root.get_screen("UB_Start_HBC")
        description_label2 = UB_start_hbc_screen.ids.description_label_HBC
        des_text="The Hammer bicep curl workout targets the biceps and forearms. This exercise involves holding the dumbbells in the palms facing each other and curling them simultaneously. This movement strengthens the biceps muscles for a more comprehensive arm workout. It improves grip strength and wrist stability."
        if state == "down":
            description_label.opacity = 1
            description_label2.opacity = 1
            description_label.text = des_text
            description_label2.text =des_text
        else:
            description_label.opacity = 0
            description_label2.opacity = 0

    def show_info_description_BBC(self, state):
        start_bbc_screen = self.root.get_screen("Start_BBC")
        description_label = start_bbc_screen.ids.description_label_BBC
        UB_start_bbc_screen = self.root.get_screen("UB_Start_BBC")
        description_label_UB_BBC = UB_start_bbc_screen.ids.description_label_BBC
        des_text="The Barbell bicep curls are a classic strength-building exercise targeting the biceps muscles. Holding a barbell with an underhand grip, you curl the weight upward, focusing on contracting the biceps while keeping the elbows steady. This compound movement helps develop arm strength and size."
        if state == "down":
            description_label.opacity = 1
            description_label_UB_BBC.opacity=1
            description_label.text = des_text
            description_label_UB_BBC.text = des_text
        else:
            description_label.opacity = 0
            description_label_UB_BBC.opacity=0

    def show_info_description_Sq(self, state):
        start_Sq_screen = self.root.get_screen("Start_Sq")
        description_label = start_Sq_screen.ids.description_label_SQ
        LB_start_Sq_screen = self.root.get_screen("LB_Start_Sq")
        description_label2 = LB_start_Sq_screen.ids.description_label_SQ
        des_text="A squat workout targets the lower body, strengthening muscles. By bending the knees and lowering the hips, then returning to standing, it builds functional strength, enhances balance, and improves mobility"
        if state == "down":
            description_label.opacity = 1
            description_label2.opacity=1
            description_label.text = des_text
            description_label2.text = des_text
        else:
            description_label.opacity = 0
            description_label2.opacity = 0

    def show_info_description_Pu(self, state):
        start_PU_screen = self.root.get_screen("Start_Pu")
        description_label = start_PU_screen.ids.description_label_PU
        UB_start_Pu_screen = self.root.get_screen("UB_Start_Pu")
        description_label_UB_Pu = UB_start_Pu_screen.ids.description_label_PU
        LB_start_Pu_screen = self.root.get_screen("LB_Start_Pu")
        description_label_LB_Pu = LB_start_Pu_screen.ids.description_label_PU
        des_text="Push-ups are a fundamental exercise that strengthens the chest, shoulders, and triceps. Starting in a plank position with hands shoulder-width apart, lower your body until your chest nearly touches the ground, then push back up to the starting position. Push-ups require no equipment."
        if state == "down":
            description_label.opacity = 1
            description_label_UB_Pu.opacity=1
            description_label_LB_Pu.opacity=1
            description_label.text = des_text
            description_label_UB_Pu.text = des_text
            description_label_LB_Pu.text = des_text

        else:
            description_label.opacity = 0
            description_label_UB_Pu.opacity=0
            description_label_LB_Pu.opacity=0

    def show_levels_description(self, state):
        start_Sq_screen = self.root.get_screen("Start_Sq")
        description_label_Sq = start_Sq_screen.ids.description_label_SQ

        LB_start_Sq_screen = self.root.get_screen("LB_Start_Sq")
        description_label_LB_Sq = LB_start_Sq_screen.ids.description_label_SQ

        start_hbc_screen = self.root.get_screen("Start_HBC")
        description_label_HBC = start_hbc_screen.ids.description_label_HBC

        UB_start_hbc_screen = self.root.get_screen("UB_Start_HBC")
        description_label_UB_HBC = UB_start_hbc_screen.ids.description_label_HBC

        start_Pu_screen = self.root.get_screen("Start_Pu")
        description_label_Pu = start_Pu_screen.ids.description_label_PU

        LB_start_Pu_screen = self.root.get_screen("LB_Start_Pu")
        description_label_LB_Pu = LB_start_Pu_screen.ids.description_label_PU

        UB_start_PU_screen = self.root.get_screen("UB_Start_Pu")
        description_label_UB_Pu = UB_start_PU_screen.ids.description_label_PU

        start_bbc_screen = self.root.get_screen("Start_BBC")
        description_label_BBC = start_bbc_screen.ids.description_label_BBC

        UB_start_bbc_screen = self.root.get_screen("UB_Start_BBC")
        description_label_UB_BBC = UB_start_bbc_screen.ids.description_label_BBC

        level_des="Levels \n Beginner level: 8 reps, 3 sets \n Intermediate level: 12 reps, 3 sets \n Pro level: 15 reps, 3 sets"

        if state == "down":
            description_label_Sq.opacity = 1
            description_label_LB_Sq.opacity = 1
            description_label_HBC.opacity = 1
            description_label_UB_HBC.opacity = 1
            description_label_Pu.opacity = 1
            description_label_LB_Pu.opacity = 1
            description_label_UB_Pu.opacity = 1
            description_label_BBC.opacity = 1
            description_label_UB_BBC.opacity = 1


            description_label_Sq.text = level_des
            description_label_LB_Sq.text = level_des
            description_label_HBC.text = level_des
            description_label_UB_HBC.text = level_des
            description_label_Pu.text = level_des
            description_label_LB_Pu.text = level_des
            description_label_UB_Pu.text = level_des
            description_label_BBC.text = level_des
            description_label_UB_BBC.text = level_des

        else:
            description_label_Sq.opacity = 0
            description_label_LB_Sq.opacity = 0
            description_label_HBC.opacity = 0
            description_label_UB_HBC.opacity = 0
            description_label_Pu.opacity = 0
            description_label_LB_Pu.opacity = 0
            description_label_UB_Pu.opacity = 0
            description_label_BBC.opacity = 0
            description_label_UB_BBC.opacity = 0


    def start_workout_HBC(self):
        import Realtime.HBC.RealtimeHBC as RealtimeHBC 
        store = JsonStore('data.json')
        user_uid = store.get('user_id')['value']
        user_data = db.reference('user').child(user_uid).get()
        
        if  user_data.get('level', '') == "Beginner":
            level=0
        elif  user_data.get('level', '') =="Intermediate":
            level=1
        elif  user_data.get('level', '') =="Advanced":
            level=2

        RealtimeHBC.Process_Frame(level)


    def start_workout_BBC(self):

        import Realtime.BBC.RealtimeBBC as RealtimeBBC 
        store = JsonStore('data.json')
        user_uid = store.get('user_id')['value']
        user_data = db.reference('user').child(user_uid).get()
        
        if  user_data.get('level', '') == "Beginner":
            level=0
        elif  user_data.get('level', '') =="Intermediate":
            level=1
        elif  user_data.get('level', '') =="Advanced":
            level=2
        RealtimeBBC.Process_Frame(level) 


    
    def start_workout_SQ(self):

        import Realtime.Squat.RealtimeSquat as RealtimeSquat 
        store = JsonStore('data.json')
        user_uid = store.get('user_id')['value']
        user_data = db.reference('user').child(user_uid).get()
        
        if  user_data.get('level', '') == "Beginner":
            level=0
        elif  user_data.get('level', '') =="Intermediate":
            level=1
        elif  user_data.get('level', '') =="Advanced":
            level=2
        RealtimeSquat.Process_Frame(level) 

    def start_workout_PU(self):

        import Realtime.Pushup.RealtimePushUp as RealtimePushUp 
        store = JsonStore('data.json')
        user_uid = store.get('user_id')['value']
        user_data = db.reference('user').child(user_uid).get()
        
        if  user_data.get('level', '') == "Beginner":
            level=0
        elif  user_data.get('level', '') =="Intermediate":
            level=1
        elif  user_data.get('level', '') =="Advanced":
            level=2
        RealtimePushUp.Process_Frame(level) 
       
    def first(self, *args):
        screen_manager=ScreenManager()
        screen_manager.current = "firstpage"

    def search_workout(self):
        search_screen = self.root.get_screen("search")
        search_results = search_screen.ids.search_results
        search_input= search_screen.ids.search_input
        search_results.clear_widgets()
        search_query = search_input.text.strip().lower()
        workouts = [
            "Push-up",
            "Hammer bicep curls",
            "Squats",
            "Barbell bicep curls",
        ]

        filtered_workouts = [workout for workout in workouts if search_query in workout.lower()]
        for workout in filtered_workouts:
            list_item = OneLineListItem(text=workout)
            list_item.bind(on_release=self.show_workout_details)
            search_results.add_widget(list_item)
            
    def show_workout_details(self, instance):
        selected_workout = instance.text
        if selected_workout == "Push-up":
            self.root.current = 'Start_Pu'
        elif selected_workout == "Hammer bicep curls":
            self.root.current = 'Start_HBC'
        elif selected_workout == "Squats":
            self.root.current = 'Start_Sq'
        elif selected_workout == "Barbell bicep curls":
           self.root.current = 'Start_BBC'

    def hash_password(self, password):
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        return hashed_password
    
    def login(self, email_input, password_input):
        email = email_input.text
        password = password_input.text
        check_login_error = self.root.get_screen("login").ids.check_login_error
        try:
            store = JsonStore('data.json')
            user = auth.get_user_by_email(email)
            user_data = db.reference('user').child(user.uid).get()
            if user_data and user_data.get('password') == self.hash_password(password):
                print('Login successful:', user.uid)
                store.put('user_id', value=user.uid)

                email_input.text = ""
                password_input.text = ""
                check_login_error.text = ""
                self.root.current = "homepage"
            else:
                check_login_error.text="* Invalid email or password"
        except :
            check_login_error.text="* Invalid email or password"


    def signup(self, name_input, email_input, password_input, age_input, weight_input, height_input):
        name = name_input.text
        email = email_input.text
        password = password_input.text
        age = age_input.text
        weight = weight_input.text
        height = height_input.text
        check_signup_error = self.root.get_screen("CreateAccount").ids.check_signup_error

        if all([self.username_check(name), self.email_check(email), self.password_strength(password),self.weight_check(weight)
                ,self.height_check(height),self.age_check(age)]):
            try:
                store = JsonStore('data.json')
                hashed_password = self.hash_password(password)
                user = auth.create_user(
                    email=email,
                    password=hashed_password
                )

                print('User created:', user.uid)
                store.put('user_id', value=user.uid)
                db_ref = db.reference('user')
                db_ref.child(user.uid).set({
                    'name': name,
                    'email': email,
                    'password': hashed_password,
                    'age': age,
                    'weight': weight,
                    'height': height,

                })
                print('User information saved to the database')
                
                self.root.transition.direction = "left"
                self.root.current = 'CreateAccount2'

            except:
                check_signup_error.text="* The email is used"


    def username_check(self, username):
        name_error_label_CA = self.root.get_screen("CreateAccount").ids.name_error_label
        name_input_CA=self.root.get_screen("CreateAccount").ids.name_input

        username_pattern = r"^\w{1,10}$"
        if not re.match(username_pattern, username):
            name_input_CA.text = ""
            name_error_label_CA.text = "* The username should be between 1 and 10 characters"
            return False
        else:
            name_error_label_CA.text = ""
            return True


    def email_check(self, email):
        CAscreen = self.root.get_screen("CreateAccount")
        email_input = CAscreen.ids.email_input
        email_error_label = CAscreen.ids.email_error_label  

        email_pattern = r"^[a-zA-Z0-9_.+-]+@(?:gmail\.com|yahoo\.com|hotmail\.com)$"
        if not re.match(email_pattern, email):
            email_input.text = ""  
            email_error_label.text = "* Invalid email format"
            return False
        else:
            email_error_label.text = ""
            return True

    def password_strength(self, password):
        CAscreen = self.root.get_screen("CreateAccount")        
        password_input = CAscreen.ids.password_input
        passWColor=CAscreen.ids.password_error_label

        has_capital = any(char.isupper() for char in password)
        has_small = any(char.islower() for char in password)
        has_number = any(char.isdigit() for char in password)
        is_valid_length = len(password) >= 8
        
        if all([has_capital, has_small, has_number, is_valid_length]):
            passWColor.color="#6aa84f"
            return True
        else:
            passWColor.color="red"       
            password_input.text= ""  
            return False
            
    def weight_check(self, weight):
        weight_error_label = self.root.get_screen("CreateAccount").ids.weight_error_label
        weight_input=self.root.get_screen("CreateAccount").ids.weight_input

        if not re.match(r"^\d+$", weight):
            weight_input.text = ""
            weight_error_label.text = "* invalid input, make sure to input a number in weight"
            return False
        else:
            weight_error_label.text = ""
            return True
    
    def height_check(self, height):
        height_error_label = self.root.get_screen("CreateAccount").ids.height_error_label
        height_input=self.root.get_screen("CreateAccount").ids.height_input

        if not re.match(r"^\d+$", height):
            height_input.text = ""
            height_error_label.text = "* invalid input, make sure to input a number in height"
            return False
        else:
            height_error_label.text = ""
            return True


    def age_check(self, age):
        age_error_label = self.root.get_screen("CreateAccount").ids.age_error_label
        age_input = self.root.get_screen("CreateAccount").ids.age_input
        
        if not re.match(r"^(|\d+)$", age):
            age_input.text = ""  
            age_error_label.text = "* Invalid input. Please input a number for age."
            return False   
            
        else:
            age_error_label.text = ""
            return True        
    
    def menuG(self):
        CA_screen = self.root.get_screen("CreateAccount2")
        gender_results = CA_screen.ids.gender_results

        gender_results.bind(on_touch_down=lambda instance, 
                           touch: gender_results.clear_widgets() if not gender_results.collide_point(*touch.pos) else None)
        items_G = ['Male', 'Female']
        for Gender in items_G:
            list_item = OneLineListItem(text=Gender)
            list_item.bind(on_release=lambda instance: self.selected_gender(instance, gender_results))
            gender_results.add_widget(list_item)

    def selected_gender(self, instance, gender_results):
        CA_screen = self.root.get_screen("CreateAccount2")
        gender_input = CA_screen.ids.gender_input
        gender_image = CA_screen.ids.gender_image

        selected_gender_ = instance.text
        if selected_gender_ == "Male":
            gender_input.text = "Male"
            gender_image.source = "pic\\man.png" 
        elif selected_gender_ == "Female":
            gender_input.text = "Female"
            gender_image.source = "pic\\woman.png" 
        gender_results.clear_widgets()


    def menuL(self):
        CA_screen = self.root.get_screen("CreateAccount2")
        level_results = CA_screen.ids.level_results

        level_results.bind(on_touch_down=lambda instance, 
                           touch: level_results.clear_widgets() if not level_results.collide_point(*touch.pos) else None)

        items_L =['Beginner','Intermediate','Advanced']

        for level in items_L:
            list_item = OneLineListItem(text=level)
            list_item.bind(on_release=lambda instance: self.selected_level(instance, level_results))
            level_results.add_widget(list_item)

    def selected_level(self, instance, level_results):
        CA_screen = self.root.get_screen("CreateAccount2")
        level_input = CA_screen.ids.level_input

        selected_level_ = instance.text
        if selected_level_ == "Beginner":
            level_input.text = "Beginner"
        elif selected_level_ == "Intermediate":
            level_input.text = "Intermediate"
        elif selected_level_ == "Advanced":
            level_input.text = "Advanced"

        level_results.clear_widgets()

class CreateAccountCard(Screen):
    def on_enter(self):
        store = JsonStore('data.json')
        user_uid = store.get('user_id')['value']
        Clock.schedule_once(lambda dt: self.update_labels(user_uid), 0.1)

    def update_labels(self, user_uid):
        user_data = db.reference('user').child(user_uid).get()
        print("Cront user Fond")
        if user_data:
            self.ids.level_input.text = user_data.get('level', '')
            self.ids.gender_input.text = user_data.get('gender', '')

    def signup2(self,gender_input, level_input):
        gender = gender_input.text
        level = level_input.text

        if all((self.gender_check(gender), self.level_check(level))):
            try:
                store = JsonStore('data.json')
                user_uid = store.get('user_id')['value']
                db_ref = db.reference('user')
                db_ref.child(user_uid).update({
                    'gender': gender,
                    'level': level
                })
                print('User information Update to the database')

                MDApp.get_running_app().root.current = 'homepage'
                
            except ValueError as e:
                    print('Error signing up:', str(e))

    
    def gender_check(self,gender):
        if  gender == "" :
            self.ids.gender_error_label.text = "* Invalid input. Please choose a gender."
            gender = ""  
            return False              
        else:
            self.ids.gender_error_label.text = ""  
            return True 
        
    def level_check(self,level):
        if  level == "" :
            self.ids.level_error_label.text = "* Invalid input. Please choose a level."
            level = ""  
            return False              
        else:
            self.ids.level_error_label.text = ""  
            return True 
    
if __name__ == "__main__":
    cred = credentials.Certificate("serviceAccountKey .json")
    firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://fitness-tracker-50e80-default-rtdb.firebaseio.com/'
    })
    FitnessApp().run()





