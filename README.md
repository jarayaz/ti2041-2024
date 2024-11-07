# ti2041-2024
# GestiónAPP - Sistema de Gestión de Productos

Sistema web desarrollado con Django para la gestión de productos, permitiendo el registro, consulta, edición y eliminación de productos con sus respectivas características.

## Características Principales

- Autenticación de usuarios
- Gestión de productos (CRUD)
- Asignación de características a productos
- Control de acceso basado en roles (Admin y Operario)
- Interfaz responsiva y amigable
- Validación de formularios
- Mensajes de retroalimentación

## Roles y Permisos

- **ADMIN_PRODUCTS**:
  - Acceso completo al CRUD de productos
  - Puede acceder al panel de administración
  - Puede editar y eliminar productos

- **OPERARIOS**:
  - Puede registrar nuevos productos
  - Puede consultar productos
  - No puede editar ni eliminar productos

## Requisitos Previos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)
- Virtualenv (opcional pero recomendado)

## Instalación

1. Clonar el repositorio:
```bash
git clone <url-del-repositorio>
cd gestionAPP
```

2. Crear y activar entorno virtual (opcional pero recomendado):
```bash
python -m venv venv
# En Windows:
venv\Scripts\activate
# En Linux/Mac:
source venv/bin/activate
```

3. Instalar dependencias:
```bash
pip install -r requirements.txt
```

4. Realizar migraciones:
```bash
python manage.py makemigrations
python manage.py migrate
```

5. Crear superusuario:
```bash
python manage.py createsuperuser
```

6. Crear grupos y permisos iniciales:
```bash
python manage.py shell
```
```python
from django.contrib.auth.models import Group
Group.objects.create(name='ADMIN_PRODUCTS')
Group.objects.create(name='OPERARIOS')
exit()
```

## Ejecución

1. Iniciar el servidor de desarrollo:
```bash
python manage.py runserver
```

2. Acceder a la aplicación:
- Abrir navegador web y visitar: `http://127.0.0.1:8000`
- Para acceder al panel de administración: `http://127.0.0.1:8000/admin`
- Credenciales admin password: inacap2024 este perfil puede hacer todo
- Credenciales usuario1 password:yosoyel123 este perfil solo puede ver la pantalla consultas.

## Estructura del Proyecto

```
gestionAPP/
├── gestionAPP/          # Configuración principal del proyecto
│   ├── settings.py      # Configuraciones de Django
│   ├── urls.py          # URLs principales
│   └── wsgi.py          # Configuración WSGI
├── productos/           # Aplicación de productos
│   ├── migrations/      # Migraciones de la base de datos
│   ├── templates/       # Plantillas HTML
│   ├── forms.py         # Formularios
│   ├── models.py        # Modelos de datos
│   ├── urls.py          # URLs de la aplicación
│   └── views.py         # Vistas y lógica de negocio
├── static/              # Archivos estáticos (CSS, JS, etc.)
├── manage.py            # Script de gestión de Django
└── requirements.txt     # Dependencias del proyecto
```

## Modelos de Datos

### Producto
- código (único)
- nombre
- precio
- marca (FK)
- categoría (FK)
- características (M2M)
- fecha_ingreso
- fecha_modificacion

### Marca
- nombre

### Categoría
- nombre

### Característica
- nombre

### ProductoCaracteristica
- producto (FK)
- característica (FK)
- valor

## Funcionalidades Implementadas

1. **Gestión de Productos**
   - Registro de nuevos productos
   - Consulta de productos existentes
   - Edición de productos (solo admin)
   - Eliminación de productos (solo admin)

2. **Características de Productos**
   - Asignación múltiple de características
   - Valores personalizados por característica

3. **Seguridad**
   - Autenticación de usuarios
   - Control de acceso basado en roles
   - Protección CSRF
   - Validación de formularios

4. **Interfaz de Usuario**
   - Diseño responsivo
   - Mensajes de retroalimentación
   - Validación en tiempo real
   - Tablas de consulta ordenadas

## Consideraciones Técnicas

- Base de datos: SQLite (por defecto)
- Framework CSS: Estilos propios
- Zona horaria: America/Santiago
- Idioma: Español

## Autor

JAIR ARAYA 

