# AD Application

Una aplicación de ejemplo con documentación automática usando PyMdocs y MkDocs.

## 📋 Características

- ✅ Estructura lista para producción
- ✅ Documentación automática con MkDocs y Material Theme
- ✅ mkdocstrings para generar API docs desde docstrings
- ✅ GitHub Actions workflow para deployment automático
- ✅ Configuración completa con pyproject.toml

## 🚀 Inicio rápido

### 1. Clonar e instalar

```bash
git clone https://github.com/IMateos92/AD.git
cd AD

# Crear entorno virtual
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

# Instalar dependencias de desarrollo
pip install -r requirements.txt
```

### 2. Ver la documentación localmente

```bash
mkdocs serve
```

Abre http://localhost:8000 en tu navegador.

### 3. Construir la documentación

```bash
mkdocs build
```

## 📁 Estructura del proyecto

```
AD/
├── docs/                 # Documentación en Markdown
│   ├── index.md
│   ├── installation.md
│   ├── usage.md
│   ├── api.md
│   └── contributing.md
├── src/                  # Código fuente
│   ├── __init__.py
│   └── example.py
├── tests/                # Tests unitarios
│   ├── __init__.py
│   └── test_example.py
├── .github/
│   └── workflows/
│       └── docs.yml      # CI/CD para GitHub Pages
├── mkdocs.yml            # Configuración de MkDocs
├── pyproject.toml        # Configuración del proyecto
├── requirements.txt      # Dependencias
├── pytest.ini            # Configuración de pytest
└── README.md
```

## 📚 Documentación

La documentación completa está disponible en [docs/](docs/).

- [Guía de instalación](docs/installation.md)
- [Cómo usar](docs/usage.md)
- [API Reference](docs/api.md)
- [Contribuir](docs/contributing.md)

## 🛠️ Desarrollo

### Instalar en modo editable

```bash
pip install -e .
```

### Instalar herramientas de desarrollo

```bash
pip install -e ".[dev]"
```

### Ejecutar tests

```bash
pytest
```

## 📖 Ver documentación

```bash
mkdocs serve
```

## 🤝 Contribuciones

¡Las contribuciones son bienvenidas! Consulta [docs/contributing.md](docs/contributing.md) para más detalles.

## 📄 Licencia

Este proyecto está bajo licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más detalles.
