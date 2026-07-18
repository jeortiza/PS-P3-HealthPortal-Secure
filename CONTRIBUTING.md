# Guía de Contribución — PS-P3 HealthPortal Secure

## Regla fundamental

> **TODOS los integrantes del grupo DEBEN abrir su propio Pull Request cada semana.**
> Si no hay PR tuyo → no tienes entrega → no tienes nota esa semana.

---

## Regla especial: datos de pacientes

> **NUNCA subas datos reales de pacientes.** Usa siempre datos ficticios generados con la biblioteca Faker.
> Cualquier commit con datos personales reales será rechazado inmediatamente y reportado como incumplimiento ético.

---

## Estructura de tu entrega semanal

```
semana-XX/
└── TU_APELLIDO_NOMBRE/
    ├── avance_sXX.md        ← Descripción de tu aporte
    ├── codigo/              ← Tu código
    └── evidencia/           ← Capturas / tests
```

---

## Flujo para hacer tu PR semanal

```bash
git clone https://github.com/TU_USUARIO/PS-P3-HealthPortal-Secure.git
cd PS-P3-HealthPortal-Secure
git remote add upstream https://github.com/[LIDER]/PS-P3-HealthPortal-Secure.git

# Antes de trabajar cada semana:
git fetch upstream && git merge upstream/main && git push origin main

# Trabaja, luego:
git add semana-XX/APELLIDO_NOMBRE/
git commit -m "feat(sXX): [aporte] - APELLIDO NOMBRE"
git push origin main
# Abre PR en GitHub
```

---

## Lo que NO se permite

- Datos reales de pacientes (diagnósticos, nombres, DNI)
- Credenciales reales de sistemas de salud
- Archivos `.env` con datos de producción
- Push directo a `main`

---

*DD281 Programación Segura — Universidad Autónoma del Perú — 2026-1*
