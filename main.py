from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.button import MDRoundFlatButton, MDFillRoundFlatButton, MDFlatButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.dialog import MDDialog
from kivymd.uix.scrollview import MDScrollView
from kivymd.uix.label import MDLabel
from kivy.core.window import Window


Window.size = (350, 600)

class CalculadoraApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"  
        self.theme_cls.primary_palette = "DeepPurple"
        
        # Lista para almacenar las operaciones del historial
        self.historial = []
        self.dialogo_historial = None
        
        # Layout Principal (Vertical)
        layout_principal = MDBoxLayout(orientation='vertical', padding=15, spacing=10)
        
        # Pantalla de visualización (Input de texto)
        self.pantalla = MDTextField(
            text="0",
            halign="right",
            font_size="36sp",
            readonly=True,
            mode="fill",
            fill_color_normal=(0.15, 0.15, 0.15, 1)
        )
        layout_principal.add_widget(self.pantalla)
        
        # Cuadrícula para los botones (4 columnas)
        cuadricula = MDGridLayout(cols=4, spacing=10, size_hint_y=0.8)
        
        # Reemplazamos el espacio vacío final por 'H' de Historial
        botones = [
            'C', '%', '/', 'del',
            '7', '8', '9', '*',
            '4', '5', '6', '-',
            '1', '2', '3', '+',
            '0', '.', '=', 'H'
        ]
        
        # Creación y agregación de botones a la cuadrícula
        for texto in botones:
            # Si es un operador o botón especial, le damos un color llamativo
            if texto in ['/', '*', '-', '+', '=', 'C', '%', 'del', 'H']:
                btn = MDFillRoundFlatButton(
                    text=texto,
                    font_size="20sp",
                    size_hint=(1, 1),
                    on_press=self.al_presionar_boton
                )
            else:
                # Botones numéricos normales
                btn = MDRoundFlatButton(
                    text=texto,
                    font_size="20sp",
                    size_hint=(1, 1),
                    on_press=self.al_presionar_boton
                )
            cuadricula.add_widget(btn)
            
        layout_principal.add_widget(cuadricula)
        return layout_principal

    def al_presionar_boton(self, instancia):
        texto_actual = self.pantalla.text
        texto_boton = instancia.text
        
        if texto_boton == 'C':
            self.pantalla.text = '0'
            
        elif texto_boton == 'del':
            if len(texto_actual) > 1:
                self.pantalla.text = texto_actual[:-1]
            else:
                self.pantalla.text = '0'
                
        elif texto_boton == 'H':
            # Llamamos a la función que muestra el historial
            self.mostrar_historial()
                
        elif texto_boton == '=':
            try:
                # Reemplazamos el símbolo de porcentaje por /100 para que python lo entienda
                expresion = texto_actual.replace('%', '/100')
                resultado = str(eval(expresion))
                
                if resultado.endswith('.0'):
                    resultado = resultado[:-2]
                
                # Guardamos la operación en el historial ANTES de cambiar la pantalla
                operacion_completa = f"{texto_actual} = {resultado}"
                self.historial.append(operacion_completa)
                    
                self.pantalla.text = resultado

            except ZeroDivisionError:
                self.pantalla.text = "Error: Div / 0"
            except Exception:
                self.pantalla.text = "Error"
                
        else:
            if texto_actual == '0' or "Error" in texto_actual:
                if texto_boton in ['/', '*', '-', '+', '%', '.']:
                    self.pantalla.text = "0" + texto_boton
                else:
                    self.pantalla.text = texto_boton
            else:
                self.pantalla.text += texto_boton

    def mostrar_historial(self):
        # Si el historial está vacío, mostramos un mensaje amigable
        if not self.historial:
            texto_historial = "No hay operaciones registradas todavía."
        else:
            # Unimos los elementos del historial con saltos de línea (del más nuevo al más viejo)
            texto_historial = "\n".join(reversed(self.historial))

        # Crear un contenedor con scroll por si el historial es muy largo
        scroll = MDScrollView(size_hint_y=None, height=200)
        contenido = MDLabel(
            text=texto_historial,
            theme_text_color="Secondary",
            font_style="Body1",
            size_hint_y=None,
            adaptive_height=True
        )
        scroll.add_widget(contenido)

        # Construimos y abrimos el diálogo flotante
        self.dialogo_historial = MDDialog(
            title="Historial de Operaciones",
            type="custom",
            content_cls=scroll,
            buttons=[
                MDFlatButton(
                    text="Borrar Todo",
                    theme_text_color="Custom",
                    text_color=self.theme_cls.primary_color,
                    on_release=self.borrar_historial
                ),
                MDFlatButton(
                    text="Cerrar",
                    theme_text_color="Custom",
                    text_color=self.theme_cls.primary_color,
                    on_release=lambda x: self.dialogo_historial.dismiss()
                ),
            ],
        )
        self.dialogo_historial.open()

    def borrar_historial(self, instancia):
        # Limpia la lista y cierra el diálogo
        self.historial.clear()
        if self.dialogo_historial:
            self.dialogo_historial.dismiss()

if __name__ == '__main__':
    CalculadoraApp().run()
