#Importarmos la libreria de selenium - Web Driver

#agregar los datos de excel
import pandas as pd
import random
#Para agregar temporizador
import time 


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

#Agregamos la ruta del webdriver
driver = webdriver.Chrome(executable_path =r"C:\Users\daine\OneDrive\Escritorio\newscraddm\chromedriver-win32\chromedriver.exe")

#Agregamos el link que queremos abrir
driver.get("https://multiplataforma.co")
time.sleep(5) #Agregamos 10s 

##PARA INGRESAR EL CORREO
#Creamos la variable para llamar a la ruta del NAME
usuario = driver.find_element_by_name("username")
for i in "Ingreso corre o usuario":
	usuario.send_keys(i)
	time.sleep(1+random.random())
#Creamos un time para que espere la carga Kgv1228

##PARA INGRESAR LA CLAVE
clave = driver.find_element_by_name("password")
for i in "La clave del correo o usuario":
	clave.send_keys(i)
	time.sleep(1+random.random())
#Creamos un time para que espere la carga Colombia2020


time.sleep(2) #Le damos dos segundos antes de iniciar sesión
clave.send_keys(Keys.ENTER) #Presionar enter desde el campo contraseña
time.sleep(5)



# Cambia el foco a la nueva pestaña de registro
driver.switch_to.window(driver.window_handles[1])

# INGRESAMOS A LA RUTA DE REGISTRO
driver.get('https://multiplataforma.co/lines/add-new')


#VAMOS A CREAR USUARIOS EN ESA PLATAFORMMA
# Número de cuentas que deseas crear
numero_de_cuentas = 20

# Bucle para crear cuentas
for i in range(numero_de_cuentas):
    while True:
        try:
            # Genera el correo electrónico utilizando un contador
            correo = f'plex-tr9015{i + 1}0kv@kgvpro.co'

            # Completa el formulario de registro
            driver.find_element_by_id('id_email').send_keys(correo)
    
            # Completa otros campos según sea necesario
            driver.find_element_by_id('id_password').send_keys('Plexpremium*0++')
    
    
            # Selecciona una opción en un combo box (posición 3)
            combobox = driver.find_element_by_id('id_plan')
            combobox.click()
            combobox.find_elements_by_tag_name('option')[3].click()
    
            # Envía el formulario de registro
            driver.find_element_by_id('create_line_button').click()

            # Espera 60 segundos para que la página cargue
            tiempo_maximo_espera = 60
            tiempo_inicial = time.time()
            while (time.time() - tiempo_inicial) < tiempo_maximo_espera:
                if "registro_exitoso" in driver.current_url:
                    print(f'Cuenta {i + 1} registrada con éxito')
                    df = df.append({'Correo': correo, 'Clave': 'Plexpremium*0++', 'Tipo de Paquete': 'Segundo Elemento'}, ignore_index=True)
                    break
                elif "error" in driver.current_url:
                    print(f'Error al registrar la cuenta {i + 1}')
                    break
                time.sleep(5)

            # Volver al formulario de registro para el siguiente registro
            driver.get('https://multiplataforma.co/lines/add-new')
            break
        except Exception as e:
            print(f'Error en el registro {i + 1}: {str(e)}')

# Exporta los correos electrónicos a un archivo de texto
correos = df['Correo'].tolist()
with open('correos.txt', 'w') as file:
    for correo in correos:
        file.write(correo + '\n')

# Cierra el navegador cuando hayas terminado
driver.quit()




