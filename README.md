# Email Auth DNS Resolver

Este script permite resolver y verificar los registros DNS para configuraciones de autenticación de correo electrónico, como SPF, DKIM y DMARC. Es una herramienta útil para administradores de sistemas y especialistas en seguridad que necesitan analizar configuraciones de dominios.

## Características

- Consulta y verifica registros **SPF** para políticas de envío de correo.
- Consulta y verifica registros **DKIM** utilizando un selector específico.
- Consulta y verifica registros **DMARC** para políticas de autenticación de correo electrónico a nivel de dominio.
- Guarda los resultados en un archivo JSON estructurado.

## Requisitos

- Python 3.x
- Biblioteca `dnspython` (instalar con `pip install dnspython`)

## Uso

Ejecuta el script desde la línea de comandos con los argumentos correspondientes.

### Argumentos

- `-n, --name` (obligatorio): Dominio para resolver los registros DNS.
- `-o, --output` (obligatorio): Nombre del archivo de salida para guardar los resultados en formato JSON.
- `-d, --dkim-selector` (opcional): Selector DKIM personalizado.
- `-s, --server` (opcional): Servidor DNS específico para realizar las consultas.

### Ejemplo de Uso

#### Consultar un dominio y guardar los resultados en un archivo JSON:

```bash
python email_auth_dns_resolver.py -n example.com -o resultados.json
```

#### Consultar un dominio especificando un selector DKIM:

```bash
python email_auth_dns_resolver.py -n example.com -d default -o resultados.json
```

#### Consultar un dominio utilizando un servidor DNS personalizado:

```bash
python email_auth_dns_resolver.py -n example.com -s 8.8.8.8 -o resultados.json
```

### Ejemplo de Salida

El archivo JSON generado tendrá un formato similar al siguiente:

```json
{
    "Name": "example.com",
    "SpfRecord": "v=spf1 include:_spf.google.com ~all",
    "SpfEnabled": true,
    "DkimRecord": "v=DKIM1; k=rsa; p=MIIB...",
    "DkimEnabled": true,
    "DmarcRecord": "v=DMARC1; p=none; rua=mailto:dmarc@example.com",
    "DmarcEnabled": true
}
```

## Licencia

Este proyecto está bajo la licencia MIT. Consulta el archivo `LICENSE` para más detalles.

---

**Licencia MIT**

```plaintext
Copyright (c) 2024 [Tu Nombre o Compañía]

Por la presente se concede permiso, de forma gratuita, a cualquier persona que obtenga una copia de este software y los archivos de documentación asociados (el "Software"), para utilizar el Software sin restricciones, incluyendo sin limitación los derechos de usar, copiar, modificar, fusionar, publicar, distribuir, sublicenciar y/o vender copias del Software, y permitir a las personas a las que se les proporcione el Software que lo hagan, sujeto a las siguientes condiciones:

El aviso de copyright anterior y este aviso de permiso se incluirán en todas las copias o partes sustanciales del Software.

EL SOFTWARE SE PROPORCIONA "TAL CUAL", SIN GARANTÍA DE NINGÚN TIPO, EXPRESA O IMPLÍCITA, INCLUYENDO PERO NO LIMITADO A GARANTÍAS DE COMERCIABILIDAD, IDONEIDAD PARA UN PROPÓSITO PARTICULAR Y NO INFRACCIÓN. EN NINGÚN CASO LOS AUTORES O TITULARES DEL COPYRIGHT SERÁN RESPONSABLES DE NINGUNA RECLAMACIÓN, DAÑO U OTRA RESPONSABILIDAD, YA SEA EN UNA ACCIÓN DE CONTRATO, AGRAVIO O DE OTRO TIPO, QUE SURJA DE O EN CONEXIÓN CON EL SOFTWARE O EL USO U OTRO TIPO DE ACCIONES EN EL SOFTWARE.
```
