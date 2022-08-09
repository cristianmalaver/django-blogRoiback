# django-blogRoiback
 Blog for agregated post like a blog
 
 Para desplegar el aplicativo en tu servidro local.

1. como descargarlo: puedes hacer una copia a tu git local o puedes descargar la carpeta en .zip y descomprimirla
2. como instalar en tu localhost: dependiendo de tu SO deberas abrir la consola y buscar la ruta donde descargaste el proyecto, una vez echo esto ejecutas los siguientes comandos ejemplo para windows: 
Recuerda que debes estar en la ruta del proyecto y parado en la carpeta que se llama blog, Por ejemplo : "C:\Users\userpc\Desktop\django-blogRoiback y Recuerda tener instalado Python en tu PC

crear entorno virtual: py -m venv venv
Activar entorno virtual: .\venv\Scripts\activate
Instalar django: pip install django
instalar dependencias: pip install pillow

Aca debes entrar a la carpeta blog para ejecutar el manage.py 
Por ejemplo : "C:\Users\userpc\Desktop\django-blogRoiback\blog"

ejecutar migraciones: py manage.py makemigrations
migrar la BD de sqlite: py manage.py migrate
iniciar servidor en django : py manage.py runserver

3. ahora deberas abrir tu navegador y buscar la ruta de localhost que pone tu consola 

Como funciona el BLOG

1. Como registrarte y logearte: debes crear un usuario en el front llamado Crear usuario, lo puedes hacer cuando abres el index del proyecto y le das donde dice "no tienes una cuenta aun? Resgistrate aqui!."  una vez creado el usuario, el te redirecciona al login donde ingresaras con tu username y tu password
3. Completar tu perfil: En el constado de arriba veras un circulo sin una imagen, da click sobre esta y te llevara a tu perfil de post publicados(no debes tener nada si eres un usario nuevo) y despues da click en donde dice actualizar perfil para agregar tu foto de perfil y completar tu perfil de usuario, anexando pagina web, foto, telefono,
4.Como mirar los post: para mirar los blog escritos por otra persona estos se filtraran por orden de llegada y haciendo click en el perfil que los escribio podras ver todos los post de este usuario
5. Como crear un Post: arriba veras un + da click aqui y agrega un titulo del post una descripciòn y una imagen (las imagenes se guardaran x defecto en uana carpeta dentro del aplicativo) da click en crear post y asi podras anexar los post que necesites.

Por ultimo la base de datos del proyecto se realizo en SQLite la cual no posee usuario ni contraseña. por ende no debes hacer nada en settings.py (la base de datos lleva x defecto unos post escritos de prueba y unas imagenes)

Espero sea de su agrado y muchas gracias (se que no es el mejor codigo pero es un efuerzo que realice por una semana GRACIAS x su ATENCION) Señores RoiBACK
