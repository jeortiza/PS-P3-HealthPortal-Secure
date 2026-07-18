# PS-P3 — UQ·HealthShield | Secure Health Portal with End-to-End PHI Encryption

### DD281 Programación Segura · Universidad Autónoma del Perú · 2026-1 · UQ AI SOLUTION COMPANY SAC

[![Django CI/CD Pipeline](https://github.com/RubenCarty/PS-P3-HealthPortal-Secure/actions/workflows/ci.yml/badge.svg)](https://github.com/RubenCarty/PS-P3-HealthPortal-Secure/actions/workflows/ci.yml)
[![Grupo](https://img.shields.io/badge/Grupo-G3-blue?style=for-the-badge)]()
[![Stack](https://img.shields.io/badge/Stack-Python%20%7C%20Django%205%20%7C%20Azure-orange?style=for-the-badge)]()
[![Journal](https://img.shields.io/badge/Target-J.Biomedical_Informatics_Q1-red?style=for-the-badge)]()
[![Demo](https://img.shields.io/badge/Demo-health.uqaisolutions.com.pe-green?style=for-the-badge)]()

---

## 🏆 Los 5 Títulos Scopus Q1 del Curso DD281-2026-1

> Todos los grupos del curso publican su investigación en journals Scopus Q1 al término del ciclo.
> El docente es coautor y guía el proceso de publicación.

| Grupo  | Proyecto            | Título Scopus Q1 Optimizado                                                                                                                                                                    | Journal Target                                    |   Q    |
| :----: | ------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------- | :----: |
|   G1   | UQ·SecureID         | "Zero-Trust Behavioral Authentication: A Machine Learning-Enhanced Identity Verification Framework with Anomaly Detection for Continuous User Authentication in Cloud-Native Web Applications" | Computers & Security — Elsevier                   |   Q1   |
|   G2   | UQ·FinSecure        | "SecureFinAPI: A Hybrid Machine Learning and Rule-Based Fraud Detection System for RESTful Banking APIs Compliant with OWASP API Security Top 10"                                              | J. Information Security & Applications — Elsevier |   Q1   |
| **G3** | **UQ·HealthShield** | **"PrivacyShield: An End-to-End Encrypted Electronic Health Record System with Attribute-Based Access Control for HIPAA and Ley N°29733 Compliance"**                                          | **J. Biomedical Informatics — Elsevier**          | **Q1** |
|   G4   | UQ·CivicVote        | "CryptoVote: A Blockchain-Enhanced Electronic Voting Protocol with Zero-Knowledge Proof Verification for Tamper-Resistant and Privacy-Preserving Democratic Processes"                         | Future Generation Computer Systems — Elsevier     |   Q1   |
|   G5   | UQ·AuditAI          | "AutoPenTest-AI: An Artificial Intelligence-Driven Automated Web Penetration Testing Framework with Natural Language Vulnerability Reporting Based on OWASP Top 10"                            | IEEE Access — IEEE                                |   Q1   |

---

## 📄 Tu Proyecto: G3 — UQ·HealthShield

### Título Scopus Q1 Optimizado

> **"PrivacyShield: An End-to-End Encrypted Electronic Health Record System with Attribute-Based Access Control for HIPAA and Ley N°29733 Compliance"**
>
> 🎯 **Journal:** Journal of Biomedical Informatics — Elsevier — **Q1** — Impact Factor: 4.5
> 🔗 **Verificar cuartil:** https://www.scimagojr.com/journalsearch.php?q=Journal+of+Biomedical+Informatics

---

### ❗ Problema que Resuelve

Los sistemas de salud digitales enfrentan la peor combinación posible: **datos ultra-sensibles + seguridad deficiente**. Según el Informe de Brechas de Salud 2023 (IBM):

- El sector salud tuvo el **costo promedio de brecha más alto**: $10.9 millones USD por incidente
- El **60% de hospitales peruanos** no cumple criterios mínimos de protección de datos (INEI 2023)
- Los datos médicos se venden en mercado negro por **$250–$1,000 USD** por expediente (vs. $1-5 USD para datos de tarjeta)

Los problemas técnicos que resuelve UQ·HealthShield:

1. **Datos clínicos en texto plano en BD**: diagnósticos, medicamentos y notas accesibles a cualquiera con acceso a la BD
2. **Control de acceso genérico**: médicos pueden ver historias de pacientes que no les corresponden
3. **Sin consentimiento digital**: no hay mecanismo para que el paciente controle quién accede a sus datos
4. **No cumple Ley N°29733**: falta registro de accesos y protección de datos sensibles

**UQ·HealthShield** resuelve esto con:

- Cifrado AES-256-GCM de todos los campos PHI (Protected Health Information) en la base de datos
- Control de acceso ABAC (Attribute-Based): solo el médico tratante accede a su paciente
- Consentimiento digital registrado y auditable
- Audit trail inmutable de cada acceso a una historia clínica

---

### 🎯 Objetivo del Proyecto

**Objetivo General:**
Desarrollar e implementar un portal de salud digital que garantice la confidencialidad, integridad y disponibilidad de los datos médicos mediante cifrado AES-256-GCM end-to-end y control de acceso basado en atributos (ABAC), cumpliendo con HIPAA y la Ley N°29733 del Perú.

**Objetivos Específicos:**

1. Implementar cifrado transparente de PHI con AES-256-GCM en modelos Django (EncryptedField)
2. Diseñar el esquema ABAC para 5 roles: paciente / médico / enfermero / admin / auditor
3. Construir el módulo de consentimiento informado digital con firma criptográfica
4. Crear el audit trail con registro inmutable de cada acceso a datos sensibles
5. Demostrar cumplimiento con los 18 controles PHI de HIPAA y el Art. 9 de la Ley N°29733
6. Desplegar en Azure App Services bajo `health.uqaisolutions.com.pe`

---

## 📅 Plan de Desarrollo por Semanas (8 Semanas)

### Visión general

```
S1 → Diseño + Setup Django 5
S2 → Auth médico con 2FA obligatorio
S3 → Cifrado AES-256-GCM de PHI
S4 ★ EP: Exposición 60%
S5 → ABAC granular + consentimiento digital
S6 → Azure Deploy + Key Vault para claves
S7 → Audit trail + compliance HIPAA/Ley 29733
S8 ★ EF: Presentación Final 100%
```

---

### SEMANA 1 — Setup Django 5 + Clasificación de Datos Sensibles

**Objetivo:** Diseñar el sistema antes de codificar, clasificando qué datos deben cifrarse.

**Tareas del equipo:**

- [ ] Hacer fork del repositorio: `https://github.com/RubenCarty/PS-P3-HealthPortal-Secure`
- [ ] Configurar Django 5.0.7 + django-axes + django-csp
- [ ] Clasificar datos del portal en 3 niveles: Público / Confidencial / Altamente Confidencial
- [ ] Los datos Altamente Confidenciales son PHI: diagnóstico, medicamentos, notas clínicas, DNI, teléfono
- [ ] Diseñar el esquema de base de datos (no cifrar lo que no necesita cifrarse — para filtros)
- [ ] Análisis STRIDE del portal de salud
- [ ] Documentar Privacy Impact Assessment en `docs/semana-01/pia.md`

**Branch a crear:**

```bash
git checkout -b feature/S1-ApellidoNombre-setup-clasificacion-datos
```

---

### SEMANA 2 — Autenticación Médica con 2FA Obligatorio

**Objetivo:** Solo personal autorizado con doble factor accede al sistema.

**Tareas del equipo:**

- [ ] Implementar login Django con rate limiting (django-axes: max 5 intentos)
- [ ] Implementar TOTP obligatorio para rol médico y admin (pyotp + QR code)
- [ ] Implementar TOTP opcional para enfermeros y pacientes
- [ ] Sesiones con timeout de 30 minutos de inactividad
- [ ] Django-CSP: Content Security Policy estricta
- [ ] Cabeceras de seguridad: HSTS, X-Frame-Options, X-Content-Type-Options
- [ ] Templates de login diferenciados por rol

**Branch a crear:**

```bash
git checkout -b feature/S2-ApellidoNombre-auth-2fa-medico
```

---

### SEMANA 3 — Cifrado AES-256-GCM de PHI (Innovación Principal)

**Objetivo:** Todos los campos sensibles cifrados automáticamente — incluso si alguien accede a la BD, no ve nada.

**Tareas del equipo:**

- [ ] Implementar `apps/patients/encryption.py`:
  - `PHIEncryption._get_key()`: PBKDF2HMAC con SHA-256, 480,000 iteraciones
  - `PHIEncryption.encrypt()`: AES-256-GCM con nonce aleatorio de 12 bytes
  - `PHIEncryption.decrypt()`: con manejo de excepción → "[DATO NO DISPONIBLE]"
- [ ] Implementar `EncryptedField` descriptor para uso transparente en modelos
- [ ] Aplicar en modelo `Patient`: `dni`, `telefono`, `fecha_nacimiento`
- [ ] Aplicar en modelo `MedicalRecord`: `diagnostico`, `medicamentos`, `notas`
- [ ] Verificar: `SELECT diagnostico FROM medical_records` en BD → debe mostrar texto cifrado base64
- [ ] Tests: cifrado → descifrado correcto, dato alterado → excepción capturada

**Branch a crear:**

```bash
git checkout -b feature/S3-ApellidoNombre-cifrado-phi-aes256
```

---

### SEMANA 4 ★ — EP: EVALUACIÓN PARCIAL (60% del proyecto)

**Entregables OBLIGATORIOS:**

1. **Pull Request** con avances S1–S4 integrados en `main`
2. **Demo en vivo** (15 minutos):
   - Login médico con 2FA (mostrar QR + código TOTP)
   - Acceder a historia clínica de paciente
   - Abrir la BD directamente → mostrar datos cifrados (base64 ilegible)
   - Intentar acceder con usuario sin 2FA (debe ser bloqueado)
   - Mostrar django-axes bloqueando después de 5 intentos fallidos
3. **Tests corriendo** en CI/CD (badge verde)

**Branch a crear:**

```bash
git checkout -b release/EP-S4-NombreGrupo
```

**Rúbrica EP (100 puntos):**
| Criterio | Puntos |
|---|:---:|
| Cifrado AES-256-GCM verificable en BD | 35 |
| 2FA funcional con TOTP | 25 |
| Cabeceras de seguridad HTTP | 15 |
| Django-axes bloqueando brute force | 10 |
| Tests (cobertura ≥ 60%) | 15 |

---

### SEMANA 5 — ABAC Granular + Consentimiento Digital

**Objetivo:** Solo el médico responsable puede ver a su paciente. El paciente controla quién accede.

**Tareas del equipo:**

- [ ] Implementar ABAC: `MedicalAccess` tabla con `doctor_id`, `patient_id`, `granted_at`, `expires_at`
- [ ] Decorador `@requires_patient_consent(patient_id)` para rutas de historia clínica
- [ ] Módulo de consentimiento: paciente puede otorgar/revocar acceso a un médico
- [ ] `ConsentRecord` con hash de integridad (SHA-256 del consentimiento + timestamp)
- [ ] Endpoint para que el paciente vea todos sus accesos activos
- [ ] Admin puede ver el audit de consentimientos

**Branch a crear:**

```bash
git checkout -b feature/S5-ApellidoNombre-abac-consentimiento
```

---

### SEMANA 6 — Azure Deploy + Key Vault para Claves de Cifrado

**Objetivo:** App en `health.uqaisolutions.com.pe` con claves de cifrado en Azure Key Vault (no en código).

**Tareas del equipo:**

- [ ] Crear Azure App Service (Python 3.11, Django, westus3)
- [ ] Clave maestra de cifrado PHI → Azure Key Vault (NUNCA en .env ni en código)
- [ ] Configurar Azure SQL Database
- [ ] Configurar Django `ALLOWED_HOSTS`, `CSRF_TRUSTED_ORIGINS`, `SECURE_SSL_REDIRECT = True`
- [ ] CI/CD: tests → Bandit → Safety → pytest-django → deploy
- [ ] Verificar HSTS activo en producción

**Branch a crear:**

```bash
git checkout -b feature/S6-ApellidoNombre-azure-keyvault-deploy
```

---

### SEMANA 7 — Audit Trail + Compliance HIPAA / Ley N°29733

**Objetivo:** Documentar y demostrar compliance con regulaciones de salud.

**Tareas del equipo:**

- [ ] Implementar `AuditLog` inmutable: cada acceso a PHI registra quién/cuándo/qué/desde dónde
- [ ] Log inmutable: los registros de audit no pueden editarse ni borrarse (sin UPDATE/DELETE en tabla)
- [ ] Completar `docs/compliance/hipaa_checklist.md` con los 18 controles PHI
- [ ] Completar `docs/compliance/ley29733_checklist.md` con Art. 9 y 16
- [ ] Reporte de compliance autogenerado: `/admin/compliance-report`
- [ ] Solicitar escaneo a G5 (AuditAI) y documentar remediaciones

**Branch a crear:**

```bash
git checkout -b feature/S7-ApellidoNombre-audit-trail-compliance
```

---

### SEMANA 8 ★ — EF: EVALUACIÓN FINAL (Proyecto 100%)

**Entregables OBLIGATORIOS:**

1. **Pull Request final** fusionado en `main`
2. **Demo completa** (20 minutos) en `health.uqaisolutions.com.pe`
3. **Paper draft** — Abstract + Methodology completos

**Rúbrica EF (100 puntos):**
| Criterio | Puntos |
|---|:---:|
| Portal completo desplegado en Azure | 25 |
| Cifrado AES-256-GCM end-to-end verificado | 25 |
| ABAC + consentimiento digital | 20 |
| Compliance HIPAA + Ley 29733 documentado | 15 |
| Borrador paper Scopus Q1 | 10 |
| Presentación y defensa técnica | 5 |

---

## 🔧 Flujo de Trabajo GitHub (Obligatorio)

### 1. Fork del repositorio

```
GitHub → https://github.com/RubenCarty/PS-P3-HealthPortal-Secure → Fork
```

### 2. Configurar tu fork

```bash
git clone https://github.com/TU-USUARIO/PS-P3-HealthPortal-Secure.git
cd PS-P3-HealthPortal-Secure
git remote add upstream https://github.com/RubenCarty/PS-P3-HealthPortal-Secure.git
git fetch upstream
```

### 3. Sincronizar y crear branch semanal

```bash
git checkout main && git pull upstream main && git push origin main
git checkout -b feature/S3-MamaniAna-cifrado-aes256-phi
```

### 4. Commit + Push + PR

```bash
git add apps/patients/encryption.py apps/patients/models.py
git commit -m "feat(S3): implement AES-256-GCM transparent field encryption for PHI"
git push origin feature/S3-MamaniAna-cifrado-aes256-phi
# → PR hacia RubenCarty/PS-P3-HealthPortal-Secure:main
```

---

## 📚 Repositorios de Referencia

### Django y Seguridad Web

| Repositorio                                                                      | Qué aprender                                                       |
| -------------------------------------------------------------------------------- | ------------------------------------------------------------------ |
| [django/django](https://github.com/django/django)                                | Documentación oficial Django — Security middleware, CSRF, sessions |
| [jazzband/django-axes](https://github.com/jazzband/django-axes)                  | Rate limiting y bloqueo de brute force en Django                   |
| [mozilla/django-csp](https://github.com/mozilla/django-csp)                      | Content Security Policy para Django                                |
| [ottoyiu/django-cors-headers](https://github.com/adamchainz/django-cors-headers) | CORS seguro en Django APIs                                         |

### Cifrado y Criptografía Python

| Repositorio                                               | Qué aprender                                            |
| --------------------------------------------------------- | ------------------------------------------------------- |
| [pyca/cryptography](https://github.com/pyca/cryptography) | Librería oficial — AES-GCM, RSA, PBKDF2 con ejemplos    |
| [fernet/fernet-spec](https://github.com/fernet/spec)      | Especificación de cifrado simétrico (alternativa a GCM) |

### Health y HIPAA

| Repositorio                                                 | Qué aprender                                                      |
| ----------------------------------------------------------- | ----------------------------------------------------------------- |
| [hapifhir/hapi-fhir](https://github.com/hapifhir/hapi-fhir) | Estándar FHIR para interoperabilidad de datos de salud            |
| [openemr/openemr](https://github.com/openemr/openemr)       | Sistema EHR open source más completo — arquitectura de referencia |
| [topics/hipaa](https://github.com/topics/hipaa)             | Proyectos relacionados con compliance HIPAA                       |

### Audit Trail y Logging

| Repositorio                                                             | Qué aprender                               |
| ----------------------------------------------------------------------- | ------------------------------------------ |
| [jazzband/django-auditlog](https://github.com/jazzband/django-auditlog) | Audit trail automático para modelos Django |

---

## 🏗️ Estructura Completa del Proyecto

```
PS-P3-HealthPortal-Secure/
│
├── 📄 README.md
├── 📄 CONTRIBUTING.md
├── 📄 requirements.txt
├── 📄 .env.example
├── 📄 manage.py
│
├── 📁 .github/
│   ├── PULL_REQUEST_TEMPLATE.md
│   └── workflows/
│       ├── ci.yml
│       └── azure-deploy.yml
│
├── 📁 healthportal/                     ← Configuración Django
│   ├── settings/
│   │   ├── base.py
│   │   ├── development.py
│   │   └── production.py                ← Azure + Key Vault
│   └── urls.py
│
├── 📁 apps/
│   ├── 📁 accounts/                     ← Auth + 2FA
│   │   ├── models.py                    ← User con rol + totp_secret
│   │   ├── views.py                     ← Login + TOTP verify
│   │   └── forms.py
│   │
│   ├── 📁 patients/                     ← Pacientes + PHI cifrado
│   │   ├── encryption.py                ← PHIEncryption + EncryptedField (S3)
│   │   ├── models.py                    ← Patient con EncryptedField
│   │   ├── views.py
│   │   └── forms.py
│   │
│   ├── 📁 records/                      ← Historias clínicas
│   │   ├── models.py                    ← MedicalRecord con PHI cifrado
│   │   └── views.py                     ← ABAC checks
│   │
│   ├── 📁 consent/                      ← Consentimiento digital (S5)
│   │   ├── models.py                    ← ConsentRecord
│   │   └── views.py
│   │
│   └── 📁 audit/                        ← Audit trail (S7)
│       ├── models.py                    ← AuditLog inmutable
│       └── views.py                     ← Reporte de compliance
│
├── 📁 templates/
│   ├── base.html
│   ├── accounts/login.html
│   ├── patients/detail.html
│   └── audit/report.html
│
├── 📁 database/
│   └── schema.sql
│
├── 📁 docs/
│   ├── semana-01/pia.md                 ← Privacy Impact Assessment
│   ├── semana-01/stride_analysis.md
│   ├── semana-03/encryption_design.md
│   ├── compliance/hipaa_checklist.md
│   ├── compliance/ley29733_checklist.md
│   └── semana-08/EF_paper_draft.md
│
└── 📁 tests/
    ├── test_encryption.py               ← Tests cifrado/descifrado
    ├── test_abac.py                     ← Tests acceso por rol/atributo
    └── test_audit.py                    ← Tests inmutabilidad audit log
```

---

## ⚡ Inicio Rápido (Local)

```bash
git clone https://github.com/TU-USUARIO/PS-P3-HealthPortal-Secure.git
cd PS-P3-HealthPortal-Secure
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env

python manage.py migrate
python manage.py createsuperuser
python manage.py runserver 8003
# → http://localhost:8003

pytest tests/ -v
python manage.py check --deploy  # Chequeo de seguridad Django
```

> **AVISO:** Los datos de pacientes en este proyecto son FICTICIOS (generados con Faker).
> Nunca incluir datos reales de pacientes en commits.

---

## 👥 Integrantes del Grupo G3

|  #  | Nombre      | GitHub                                 | Rol Técnico                   |
| :-: | ----------- | -------------------------------------- | ----------------------------- |
|  1  | [Completar] | [@usuario](https://github.com/usuario) | Líder / Auth 2FA              |
|  2  | [Completar] | [@usuario](https://github.com/usuario) | Cifrado AES-256-GCM + Modelos |
|  3  | [Completar] | [@usuario](https://github.com/usuario) | ABAC + Consentimiento         |
|  4  | [Completar] | [@usuario](https://github.com/usuario) | Audit Trail + Compliance      |
|  5  | [Completar] | [@usuario](https://github.com/usuario) | Azure Deploy + CI/CD          |

---

## 👨‍🏫 Contacto Docente

- **Docente:** Mg. Ruben Quispe Llacctarimay — [@RubenCarty](https://github.com/RubenCarty)
- **Repo del curso:** [DD281-Programacion-Segura-2026-1](https://github.com/RubenCarty/DD281-Programacion-Segura-2026-1)
- **Demo G3:** [health.uqaisolutions.com.pe](https://health.uqaisolutions.com.pe)

---

_Universidad Autónoma del Perú — DD281 Programación Segura — 2026-1_
_UQ AI SOLUTION COMPANY SAC — Ciclo VIII — Ingeniería de Sistemas_
