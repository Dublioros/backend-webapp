<h1>Backend-WebApp</h1>

<p>Este proyecto aborda el desarrollo del backend utilizando <strong>Python con FastAPI</strong> para la creación de <strong>APIs RESTful seguras</strong>. Incluye las siguientes características:</p>

<h2>Características</h2>
<ul>
    <li><strong>Autenticación y Autorización:</strong>
        <ul>
            <li>Implementación de <strong>JSON Web Tokens (JWT)</strong> para la autenticación segura de usuarios.</li>
        </ul>
    </li>
    <li><strong>Conexión a Base de Datos:</strong>
        <ul>
            <li>Integración robusta con bases de datos mediante <strong>HTTPS</strong>.</li>
        </ul>
    </li>
    <li><strong>Envío de Correos Electrónicos:</strong>
        <ul>
            <li>Funcionalidad para enviar correos electrónicos desde el servidor utilizando servicios de <strong>Gmail y Yahoo Mail (YMail)</strong>.</li>
        </ul>
    </li>
    <li><strong>Operaciones CRUD:</strong>
        <ul>
            <li>Creación, lectura, actualización y eliminación de datos a través de endpoints bien definidos.</li>
        </ul>
    </li>
    <li><strong>Gestión de Archivos:</strong>
        <ul>
            <li>Subida y gestión de archivos en la nube.</li>
        </ul>
    </li>
    <li><strong>Integración de Ubicación y Google Maps:</strong>
        <ul>
            <li>Funcionalidades para obtener ubicaciones y calcular distancias entre locales.</li>
        </ul>
    </li>
</ul>

<h2>Requisitos</h2>
<ul>
    <li>Python 3.8+</li>
    <li>FastAPI</li>
    <li>Base de datos compatible</li>
    <li>Configuración de servicios de correo (Gmail/YMail)</li>
    <li>Cuenta de Google Maps API</li>
</ul>

<h2>Instalación</h2>
<ol>
    <li>Clona el repositorio:
        <pre><code>git clone https://github.com/dublioros/backend-webapp.git
cd backend-webapp
        </code></pre>
    </li>
    <li>Crea un entorno virtual e instala las dependencias:
        <pre><code>python -m venv env
source env/bin/activate   # En Windows usa `env\Scripts\activate`
pip install -r requirements.txt
        </code></pre>
    </li>
    <li>Configura las variables de entorno para los servicios de correo y Google Maps.</li>
    <li>Ejecuta la aplicación:
        <pre><code>uvicorn main:app --reload
        </code></pre>
    </li>
</ol>

<h2>Uso</h2>
<p>Visita <a href="http://127.0.0.1:8000/docs">http://127.0.0.1:8000/docs</a> para acceder a la documentación interactiva de la API generada por Swagger.</p>

<h2>Contribuciones</h2>
<p>¡Las contribuciones son bienvenidas! Por favor, abre un issue o un pull request para mejorar este proyecto.</p>

<h2>Licencia</h2>
<p>Este proyecto está bajo la Licencia MIT. Mira el archivo <a href="LICENSE">LICENSE</a> para más detalles.</p>
