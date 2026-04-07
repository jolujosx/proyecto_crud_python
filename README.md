[![Deploy to Render](https://render.com)](https://proyecto-crud-python.onrender.com)
# Proyecto_crud_python# 🛠️ Sistema de Gestión de Proyectos de Ingeniería (CRUD)

Este es un sistema **CRUD (Create, Read, Update, Delete)** profesional desarrollado para la gestión de tareas técnicas y proyectos. El objetivo de este repositorio es demostrar habilidades en arquitectura de software, persistencia de datos y desarrollo web moderno bajo un entorno de nube profesional.

---

## 🚀 Tecnologías Utilizadas

*   **Backend:** Python 3.10+ con el micro-framework **Flask**.
*   **Base de Datos:** **SQLite 3** para persistencia de datos local y eficiente.
*   **Frontend:** **HTML5** y **Bootstrap 5** para una interfaz responsiva y profesional.
*   **Entorno de Desarrollo:** **GitHub Codespaces** (Cloud IDE).
*   **Control de Versiones:** **Git** con flujo de trabajo basado en commits descriptivos.

---

## 🏗️ Arquitectura del Proyecto

El proyecto sigue una estructura organizada para facilitar la escalabilidad:

```text
├── app.py              # Lógica principal del servidor y rutas del CRUD
├── database.db         # Archivo de base de datos relacional (generado automáticamente)
├── templates/          # Directorio de vistas (Frontend)
│   └── index.html      # Interfaz de usuario dinámica con Jinja2
└── README.md           # Documentación técnica del proyecto
