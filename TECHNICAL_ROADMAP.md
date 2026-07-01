# Technical Roadmap

This roadmap converts the current product notes in `ROADMAP.md` into implementable engineering work for `hanger_app`. It focuses on the next backend, security, operations, and documentation milestones.

## 1. Controlled User Onboarding

Goal: only register users who pass a selection process.

Implementation scope:

- [x] Add an application workflow with states: `submitted`, `screening`, `interview`, `accepted`, `rejected`, and `invited`.
- [x] Store application answers, reviewer notes, decision timestamps, and reviewer user IDs.
- [x] Replace open registration with invite-only registration tied to accepted applications.
- [x] Add admin routes and CLI commands to review, accept, reject, and invite applicants.
  CLI commands and protected admin application routes are implemented.
- [x] Add audit events for every application state change.
  Accept, reject, invite, interview scheduling, interview completion, and note creation are audited at the service layer.

Acceptance criteria:

- [x] A non-invited user cannot create an account.
- [x] Accepted applicants receive a single-use invitation.
- [x] Tests cover duplicate applications, rejected applications, expired invites, and admin-only decisions.

## 2. Per-Installation Requirements

Goal: support different eligibility rules and operating limits for each deployed server.

Implementation scope:

- [x] Introduce an `installation_settings` table for onboarding rules, eligibility criteria, limits, and branding.
- [x] Move server-specific values out of source code into environment variables or database-backed settings.
- [x] Validate required production settings during application startup.
- [x] Add an admin UI or CLI for reading and updating safe settings.
  CLI support is implemented with `settings-list`, `settings-get`, and `settings-set`.
- [~] Document required configuration in `README.md` and deployment examples.
  `README.md` and contributor commands are updated; richer deployment examples remain pending.

Acceptance criteria:

- [x] Each deployment can define its own eligibility rules without code changes.
- [x] Missing production configuration fails fast with a clear error.
- [x] Tests verify default settings, overrides, and invalid configuration.

## 3. Interview and Research Pipeline

Goal: manage interviews with possible future users and convert research into actionable product signals.

Implementation scope:

- [x] Add applicant interview scheduling fields: contact method, preferred times, assigned interviewer, and status.
- [x] Add interview notes with structured categories: motivation, fit, risks, and follow-up actions.
- [x] Add privacy controls so only admins or assigned interviewers can read interview notes.
- [x] Add aggregate exports for research metrics without exposing sensitive notes.

Acceptance criteria:

- [x] Interview notes are access-controlled and audited.
- [x] Admins can list applicants by interview status.
- [x] Research exports exclude private free-text notes by default.

## 4. Funding and Operations Readiness

Goal: prepare the project for external funding, sponsorship, or structured collaboration.

Implementation scope:

- [ ] Add operational metrics: registered users, active users, applications by status, invitation conversion, and message/job health.
- [ ] Add health dashboards or CLI reports using the existing `/health/live` and `/health/ready` foundations.
- [ ] Improve logging around authentication, onboarding, background jobs, and upload access decisions.
- [ ] Add data retention policies for applications, interview notes, and recovery tokens.
- [ ] Add backup and restore documentation for SQLite deployments.

Acceptance criteria:

- [ ] Maintainers can generate a funding-ready usage report without direct database inspection.
- [ ] Sensitive user data is excluded from public or sponsor-facing exports.
- [ ] Backup and restore steps are documented and tested against a local database.

## Cross-Cutting Engineering Priorities

- Security: preserve invite token single-use semantics, role-based access control, audit logs, and upload authorization.
- Testing: keep coverage above the CI threshold and add route/service tests for every onboarding decision path.
- Migrations: add schema changes only through numbered files in `src/hanger_app/migrations/`; never rewrite applied migrations.
- Documentation: update `AGENTS.md`, `README.md`, and deployment notes whenever commands, configuration, or workflows change.
- Observability: prefer structured logs and explicit health checks over silent failures.

## Suggested Implementation Order

1. [x] Add application and invitation schema.
2. [x] Implement repository and service layer for application decisions.
3. [x] Add admin CLI commands and protected admin routes.
4. [x] Disable open registration when invite-only mode is enabled.
5. [x] Add installation settings and production validation.
6. [x] Add interview notes and access controls.
7. [ ] Add reporting commands and sanitized exports.
8. [~] Document deployment, backup, restore, and operational workflows.
# Hoja de ruta técnica

Esta hoja de ruta convierte las notas del producto actual en `ROADMAP.md` en trabajo de ingeniería implementable para `hanger_app`. Se centra en los próximos hitos de backend, seguridad, operaciones y documentación.

## 1. Incorporación de usuarios controlada

Objetivo: registrar únicamente usuarios que pasen un proceso de selección.

Alcance de implementación:

- [x] Agregue un flujo de trabajo de aplicación con estados: "enviado", "detección", "entrevista", "aceptado", "rechazado" e "invitado".
- [x] Almacenar respuestas de aplicaciones, notas de revisores, marcas de tiempo de decisiones e ID de usuarios de revisores.
- [x] Reemplazar el registro abierto con un registro solo por invitación vinculado a las solicitudes aceptadas.
- [x] Agregue rutas de administración y comandos CLI para revisar, aceptar, rechazar e invitar a los solicitantes.
  Se implementan comandos CLI y rutas de aplicaciones de administración protegidas.
- [x] Agregar eventos de auditoría para cada cambio de estado de la aplicación.
  Aceptar, rechazar, invitar, programar entrevistas, completar entrevistas y crear notas se auditan en la capa de servicio.

Criterios de aceptación:

- [x] Un usuario no invitado no puede crear una cuenta.
- [x] Los solicitantes aceptados reciben una invitación de un solo uso.
- [x] Las pruebas cubren solicitudes duplicadas, solicitudes rechazadas, invitaciones vencidas y decisiones exclusivas del administrador.

## 2. Requisitos por instalación

Objetivo: admitir diferentes reglas de elegibilidad y límites operativos para cada servidor implementado.

Alcance de implementación:

- [x] Introducir una tabla `installation_settings` para reglas de incorporación, criterios de elegibilidad, límites y marca.
- [x] Mover valores específicos del servidor fuera del código fuente a variables de entorno o configuraciones respaldadas por bases de datos.
- [x] Validar la configuración de producción requerida durante el inicio de la aplicación.
- [x] Agregue una interfaz de usuario o CLI de administrador para leer y actualizar configuraciones seguras.
  La compatibilidad con CLI se implementa con `settings-list`, `settings-get` y `settings-set`.
- [~] Documentar la configuración requerida en `README.md` y ejemplos de implementación.
  `README.md` y los comandos del colaborador se actualizan; quedan pendientes ejemplos de implementación más completos.

Criterios de aceptación:

- [x] Cada implementación puede definir sus propias reglas de elegibilidad sin cambios de código.
- [x] La configuración de producción faltante falla rápidamente con un error claro.
- [x] Las pruebas verifican la configuración predeterminada, las anulaciones y la configuración no válida.

## 3. Entrevistas y proceso de investigación

Objetivo: gestionar entrevistas con posibles futuros usuarios y convertir la investigación en señales de producto procesables.

Alcance de implementación:

- [x] Agregar campos de programación de entrevistas para solicitantes: método de contacto, horarios preferidos, entrevistador asignado y estado.
- [x] Agregar notas de entrevista con categorías estructuradas: motivación, ajuste, riesgos y acciones de seguimiento.
- [x] Agregue controles de privacidad para que solo los administradores o los entrevistadores asignados puedan leer las notas de la entrevista.
- [x] Agregar exportaciones agregadas para métricas de investigación sin exponer notas confidenciales.

Criterios de aceptación:

- [x] Las notas de las entrevistas tienen acceso controlado y auditadas.
- [x] Los administradores pueden enumerar a los solicitantes por estado de la entrevista.
- [x] Las exportaciones de investigación excluyen las notas privadas de texto libre de forma predeterminada.

## 4. Preparación para la financiación y las operaciones

Objetivo: preparar el proyecto para financiación externa, patrocinio o colaboración estructurada.

Alcance de implementación:

- [] Agregar métricas operativas: usuarios registrados, usuarios activos, solicitudes por estado, conversión de invitaciones y estado del mensaje/trabajo.
- [] Agregue paneles de control de estado o informes CLI utilizando las bases `/health/live` y `/health/ready` existentes.
- [] Mejorar el registro en torno a la autenticación, la incorporación, los trabajos en segundo plano y las decisiones de acceso a las cargas.
- [] Agregar políticas de retención de datos para aplicaciones, notas de entrevistas y tokens de recuperación.
- [] Agregar documentación de copia de seguridad y restauración para implementaciones de SQLite.

Criterios de aceptación:

- [] Los mantenedores pueden generar un informe de uso listo para financiar sin inspección directa de la base de datos.
- [ ] Los datos confidenciales de los usuarios están excluidos de las exportaciones públicas o de patrocinadores.
- [] Los pasos de copia de seguridad y restauración están documentados y probados en una base de datos local.

## Prioridades transversales de ingeniería

- Seguridad: conserva la semántica de un solo uso del token de invitación, el control de acceso basado en roles, los registros de auditoría y la autorización de carga.
- Pruebas: mantenga la cobertura por encima del umbral de CI y agregue pruebas de ruta/servicio para cada ruta de decisión de incorporación.
- Migraciones: agregue cambios de esquema solo a través de archivos numerados en `src/hanger_app/migrations/`; nunca reescriba las migraciones aplicadas.
- Documentación: actualice `AGENTS.md`, `README.md` y las notas de implementación cada vez que cambien los comandos, la configuración o los flujos de trabajo.
- Observabilidad: prefiera registros estructurados y controles de estado explícitos a fallas silenciosas.

## Orden de implementación sugerida

1. [x] Agregar esquema de solicitud e invitación.
2. [x] Implementar repositorio y capa de servicio para decisiones de aplicaciones.
3. [x] Agregue comandos CLI de administración y rutas de administración protegidas.
4. [x] Deshabilite el registro abierto cuando el modo solo por invitación esté habilitado.
5. [x] Agregar configuración de instalación y validación de producción.
6. [x] Agregue notas de entrevistas y controles de acceso.
7. [] Agregue comandos de informes y exportaciones desinfectadas.
8. [~] Implementación de documentos, copia de seguridad, restauración y flujos de trabajo operativos.
# Hoja de ruta técnica

Esta hoja de ruta convierte las notas del producto actual en `ROADMAP.md` en trabajo de ingeniería implementable para `hanger_app`. Se centra en los próximos hitos de backend, seguridad, operaciones y documentación.

## 1. Incorporación de usuarios controlada

Objetivo: registrar únicamente usuarios que pasen un proceso de selección.

Alcance de implementación:

- [x] Agregue un flujo de trabajo de aplicación con estados: "enviado", "detección", "entrevista", "aceptado", "rechazado" e "invitado".
- [x] Almacenar respuestas de aplicaciones, notas de revisores, marcas de tiempo de decisiones e ID de usuarios de revisores.
- [x] Reemplazar el registro abierto con un registro solo por invitación vinculado a las solicitudes aceptadas.
- [x] Agregue rutas de administración y comandos CLI para revisar, aceptar, rechazar e invitar a los solicitantes.
  Se implementan comandos CLI y rutas de aplicaciones de administración protegidas.
- [x] Agregar eventos de auditoría para cada cambio de estado de la aplicación.
  Aceptar, rechazar, invitar, programar entrevistas, completar entrevistas y crear notas se auditan en la capa de servicio.

Criterios de aceptación:

- [x] Un usuario no invitado no puede crear una cuenta.
- [x] Los solicitantes aceptados reciben una invitación de un solo uso.
- [x] Las pruebas cubren solicitudes duplicadas, solicitudes rechazadas, invitaciones vencidas y decisiones exclusivas del administrador.

## 2. Requisitos por instalación

Objetivo: admitir diferentes reglas de elegibilidad y límites operativos para cada servidor implementado.

Alcance de implementación:

- [x] Introducir una tabla `installation_settings` para reglas de incorporación, criterios de elegibilidad, límites y marca.
- [x] Mover valores específicos del servidor fuera del código fuente a variables de entorno o configuraciones respaldadas por bases de datos.
- [x] Validar la configuración de producción requerida durante el inicio de la aplicación.
- [x] Agregue una interfaz de usuario o CLI de administrador para leer y actualizar configuraciones seguras.
  La compatibilidad con CLI se implementa con `settings-list`, `settings-get` y `settings-set`.
- [~] Documentar la configuración requerida en `README.md` y ejemplos de implementación.
  `README.md` y los comandos del colaborador se actualizan; quedan pendientes ejemplos de implementación más completos.

Criterios de aceptación:

- [x] Cada implementación puede definir sus propias reglas de elegibilidad sin cambios de código.
- [x] La configuración de producción faltante falla rápidamente con un error claro.
- [x] Las pruebas verifican la configuración predeterminada, las anulaciones y la configuración no válida.

## 3. Entrevistas y proceso de investigación

Objetivo: gestionar entrevistas con posibles futuros usuarios y convertir la investigación en señales de producto procesables.

Alcance de implementación:

- [x] Agregar campos de programación de entrevistas para solicitantes: método de contacto, horarios preferidos, entrevistador asignado y estado.
- [x] Agregar notas de entrevista con categorías estructuradas: motivación, ajuste, riesgos y acciones de seguimiento.
- [x] Agregue controles de privacidad para que solo los administradores o los entrevistadores asignados puedan leer las notas de la entrevista.
- [x] Agregar exportaciones agregadas para métricas de investigación sin exponer notas confidenciales.

Criterios de aceptación:

- [x] Las notas de las entrevistas tienen acceso controlado y auditadas.
- [x] Los administradores pueden enumerar a los solicitantes por estado de la entrevista.
- [x] Las exportaciones de investigación excluyen las notas privadas de texto libre de forma predeterminada.

## 4. Preparación para la financiación y las operaciones

Objetivo: preparar el proyecto para financiación externa, patrocinio o colaboración estructurada.

Alcance de implementación:

- [] Agregar métricas operativas: usuarios registrados, usuarios activos, solicitudes por estado, conversión de invitaciones y estado del mensaje/trabajo.
- [] Agregue paneles de control de estado o informes CLI utilizando las bases `/health/live` y `/health/ready` existentes.
- [] Mejorar el registro en torno a la autenticación, la incorporación, los trabajos en segundo plano y las decisiones de acceso a las cargas.
- [] Agregar políticas de retención de datos para aplicaciones, notas de entrevistas y tokens de recuperación.
- [] Agregar documentación de copia de seguridad y restauración para implementaciones de SQLite.

Criterios de aceptación:

- [] Los mantenedores pueden generar un informe de uso listo para financiar sin inspección directa de la base de datos.
- [ ] Los datos confidenciales de los usuarios están excluidos de las exportaciones públicas o de patrocinadores.
- [] Los pasos de copia de seguridad y restauración están documentados y probados en una base de datos local.

## Prioridades transversales de ingeniería

- Seguridad: conserva la semántica de un solo uso del token de invitación, el control de acceso basado en roles, los registros de auditoría y la autorización de carga.
- Pruebas: mantenga la cobertura por encima del umbral de CI y agregue pruebas de ruta/servicio para cada ruta de decisión de incorporación.
- Migraciones: agregue cambios de esquema solo a través de archivos numerados en `src/hanger_app/migrations/`; nunca reescriba las migraciones aplicadas.
- Documentación: actualice `AGENTS.md`, `README.md` y las notas de implementación cada vez que cambien los comandos, la configuración o los flujos de trabajo.
- Observabilidad: prefiera registros estructurados y controles de estado explícitos a fallas silenciosas.

## Orden de implementación sugerida

1. [x] Agregar esquema de solicitud e invitación.
2. [x] Implementar repositorio y capa de servicio para decisiones de aplicaciones.
3. [x] Agregue comandos CLI de administración y rutas de administración protegidas.
4. [x] Deshabilite el registro abierto cuando el modo solo por invitación esté habilitado.
5. [x] Agregar configuración de instalación y validación de producción.
6. [x] Agregue notas de entrevistas y controles de acceso.
7. [] Agregue comandos de informes y exportaciones desinfectadas.
8. [~] Implementación de documentos, copia de seguridad, restauración y flujos de trabajo operativos.
# Feuille de route technique

Cette feuille de route convertit les notes de produit actuelles dans « ROADMAP.md » en travaux d'ingénierie implémentables pour « hanger_app ». Il se concentre sur les prochaines étapes du backend, de la sécurité, des opérations et de la documentation.

## 1. Intégration contrôlée des utilisateurs

Objectif : enregistrer uniquement les utilisateurs qui réussissent un processus de sélection.

Portée de mise en œuvre :

- [x] Ajoutez un workflow de candidature avec les états : "soumis", "sélection", "entretien", "accepté", "rejeté" et "invité".
- [x] Stockez les réponses de l'application, les notes des réviseurs, les horodatages des décisions et les identifiants des utilisateurs des réviseurs.
- [x] Remplacer l'inscription ouverte par une inscription sur invitation uniquement liée aux candidatures acceptées.
- [x] Ajoutez des routes d'administration et des commandes CLI pour examiner, accepter, rejeter et inviter les candidats.
  Les commandes CLI et les routes d'application d'administration protégées sont implémentées.
- [x] Ajoutez des événements d'audit pour chaque changement d'état de l'application.
  L'acceptation, le rejet, l'invitation, la planification des entretiens, la réalisation des entretiens et la création de notes sont audités au niveau de la couche de service.

Critères d'acceptation :

- [x] Un utilisateur non invité ne peut pas créer de compte.
- [x] Les candidats acceptés reçoivent une invitation à usage unique.
- [x] Les tests couvrent les candidatures en double, les candidatures rejetées, les invitations expirées et les décisions réservées aux administrateurs.

## 2. Exigences par installation

Objectif : prendre en charge différentes règles d'éligibilité et limites de fonctionnement pour chaque serveur déployé.

Portée de mise en œuvre :

- [x] Introduire un tableau `installation_settings` pour les règles d'intégration, les critères d'éligibilité, les limites et la marque.
- [x] Déplacez les valeurs spécifiques au serveur du code source vers des variables d'environnement ou des paramètres sauvegardés dans la base de données.
- [x] Validez les paramètres de production requis lors du démarrage de l'application.
- [x] Ajoutez une interface utilisateur ou une CLI d'administration pour lire et mettre à jour les paramètres sécurisés.
  La prise en charge de la CLI est implémentée avec `settings-list`, `settings-get` et `settings-set`.
- [~] Documentez la configuration requise dans `README.md` et les exemples de déploiement.
  `README.md` et les commandes des contributeurs sont mis à jour ; des exemples de déploiement plus riches restent en attente.

Critères d'acceptation :

- [x] Chaque déploiement peut définir ses propres règles d'éligibilité sans changement de code.
- [x] La configuration de production manquante échoue rapidement avec une erreur claire.
- [x] Les tests vérifient les paramètres par défaut, les remplacements et la configuration invalide.

## 3. Pipeline d'entretiens et de recherche

Objectif : gérer les entretiens avec de futurs utilisateurs potentiels et convertir la recherche en signaux produits exploitables.

Portée de mise en œuvre :

- [x] Ajoutez des champs de planification des entretiens avec les candidats : méthode de contact, heures préférées, intervieweur désigné et statut.
- [x] Ajoutez des notes d'entretien avec des catégories structurées : motivation, adéquation, risques et actions de suivi.
- [x] Ajoutez des contrôles de confidentialité afin que seuls les administrateurs ou les enquêteurs désignés puissent lire les notes d'entretien.
- [x] Ajoutez des exportations globales pour les métriques de recherche sans exposer les notes sensibles.

Critères d'acceptation :

- [x] Les notes d'entretien sont contrôlées et auditées.
- [x] Les administrateurs peuvent répertorier les candidats par statut d'entretien.
- [x] Les exportations de recherche excluent par défaut les notes privées en texte libre.

## 4. Préparation au financement et aux opérations

Objectif : préparer le projet à un financement externe, un sponsoring ou une collaboration structurée.

Portée de mise en œuvre :

- [ ] Ajoutez des métriques opérationnelles : utilisateurs enregistrés, utilisateurs actifs, candidatures par statut, conversion d'invitation et santé des messages/tâches.
- [ ] Ajoutez des tableaux de bord d'intégrité ou des rapports CLI en utilisant les fondations existantes `/health/live` et `/health/ready`.
- [ ] Améliorez la journalisation autour de l'authentification, de l'intégration, des tâches en arrière-plan et des décisions d'accès au téléchargement.
- [ ] Ajoutez des politiques de conservation des données pour les applications, les notes d'entretien et les jetons de récupération.
- [ ] Ajouter une documentation de sauvegarde et de restauration pour les déploiements SQLite.

Critères d'acceptation :

- [ ] Les responsables peuvent générer un rapport d'utilisation prêt à être financé sans inspection directe de la base de données.
- [ ] Les données utilisateur sensibles sont exclues des exportations publiques ou destinées aux sponsors.
- [ ] Les étapes de sauvegarde et de restauration sont documentées et testées par rapport à une base de données locale.

## Priorités d'ingénierie transversales

- Sécurité : préservez la sémantique à usage unique du jeton d'invitation, le contrôle d'accès basé sur les rôles, les journaux d'audit et l'autorisation de téléchargement.
- Tests : maintenez la couverture au-dessus du seuil CI et ajoutez des tests d'itinéraire/service pour chaque chemin de décision d'intégration.
- Migrations : ajoutez des modifications de schéma uniquement via des fichiers numérotés dans `src/hanger_app/migrations/` ; ne réécrivez jamais les migrations appliquées.
- Documentation : mettez à jour `AGENTS.md`, `README.md` et les notes de déploiement chaque fois que les commandes, la configuration ou les flux de travail changent.
- Observabilité : préférez les journaux structurés et les contrôles de santé explicites aux échecs silencieux.

## Ordre de mise en œuvre suggéré

1. [x] Ajoutez un schéma d'application et d'invitation.
2. [x] Implémenter le référentiel et la couche de service pour les décisions d'application.
3. [x] Ajoutez des commandes CLI d'administration et des routes d'administration protégées.
4. [x] Désactivez l'inscription ouverte lorsque le mode sur invitation uniquement est activé.
5. [x] Ajoutez les paramètres d'installation et la validation de la production.
6. [x] Ajoutez des notes d'entretien et des contrôles d'accès.
7. [ ] Ajoutez des commandes de reporting et des exportations nettoyées.
8. [~] Documentez les workflows de déploiement, de sauvegarde, de restauration et opérationnels.
# Feuille de route technique

Cette feuille de route convertit les notes de produit actuelles dans « ROADMAP.md » en travaux d'ingénierie implémentables pour « hanger_app ». Il se concentre sur les prochaines étapes du backend, de la sécurité, des opérations et de la documentation.

## 1. Intégration contrôlée des utilisateurs

Objectif : enregistrer uniquement les utilisateurs qui réussissent un processus de sélection.

Portée de mise en œuvre :

- [x] Ajoutez un workflow de candidature avec les états : "soumis", "sélection", "entretien", "accepté", "rejeté" et "invité".
- [x] Stockez les réponses de l'application, les notes des réviseurs, les horodatages des décisions et les identifiants des utilisateurs des réviseurs.
- [x] Remplacer l'inscription ouverte par une inscription sur invitation uniquement liée aux candidatures acceptées.
- [x] Ajoutez des routes d'administration et des commandes CLI pour examiner, accepter, rejeter et inviter les candidats.
  Les commandes CLI et les routes d'application d'administration protégées sont implémentées.
- [x] Ajoutez des événements d'audit pour chaque changement d'état de l'application.
  L'acceptation, le rejet, l'invitation, la planification des entretiens, la réalisation des entretiens et la création de notes sont audités au niveau de la couche de service.

Critères d'acceptation :

- [x] Un utilisateur non invité ne peut pas créer de compte.
- [x] Les candidats acceptés reçoivent une invitation à usage unique.
- [x] Les tests couvrent les candidatures en double, les candidatures rejetées, les invitations expirées et les décisions réservées aux administrateurs.

## 2. Exigences par installation

Objectif : prendre en charge différentes règles d'éligibilité et limites de fonctionnement pour chaque serveur déployé.

Portée de mise en œuvre :

- [x] Introduire un tableau `installation_settings` pour les règles d'intégration, les critères d'éligibilité, les limites et la marque.
- [x] Déplacez les valeurs spécifiques au serveur du code source vers des variables d'environnement ou des paramètres sauvegardés dans la base de données.
- [x] Validez les paramètres de production requis lors du démarrage de l'application.
- [x] Ajoutez une interface utilisateur ou une CLI d'administration pour lire et mettre à jour les paramètres sécurisés.
  La prise en charge de la CLI est implémentée avec `settings-list`, `settings-get` et `settings-set`.
- [~] Documentez la configuration requise dans `README.md` et les exemples de déploiement.
  `README.md` et les commandes des contributeurs sont mis à jour ; des exemples de déploiement plus riches restent en attente.

Critères d'acceptation :

- [x] Chaque déploiement peut définir ses propres règles d'éligibilité sans changement de code.
- [x] La configuration de production manquante échoue rapidement avec une erreur claire.
- [x] Les tests vérifient les paramètres par défaut, les remplacements et la configuration invalide.

## 3. Pipeline d'entretiens et de recherche

Objectif : gérer les entretiens avec de futurs utilisateurs potentiels et convertir la recherche en signaux produits exploitables.

Portée de mise en œuvre :

- [x] Ajoutez des champs de planification des entretiens avec les candidats : méthode de contact, heures préférées, intervieweur désigné et statut.
- [x] Ajoutez des notes d'entretien avec des catégories structurées : motivation, adéquation, risques et actions de suivi.
- [x] Ajoutez des contrôles de confidentialité afin que seuls les administrateurs ou les enquêteurs désignés puissent lire les notes d'entretien.
- [x] Ajoutez des exportations globales pour les métriques de recherche sans exposer les notes sensibles.

Critères d'acceptation :

- [x] Les notes d'entretien sont contrôlées et auditées.
- [x] Les administrateurs peuvent répertorier les candidats par statut d'entretien.
- [x] Les exportations de recherche excluent par défaut les notes privées en texte libre.

## 4. Préparation au financement et aux opérations

Objectif : préparer le projet à un financement externe, un sponsoring ou une collaboration structurée.

Portée de mise en œuvre :

- [ ] Ajoutez des métriques opérationnelles : utilisateurs enregistrés, utilisateurs actifs, candidatures par statut, conversion d'invitation et santé des messages/tâches.
- [ ] Ajoutez des tableaux de bord d'intégrité ou des rapports CLI en utilisant les fondations existantes `/health/live` et `/health/ready`.
- [ ] Améliorez la journalisation autour de l'authentification, de l'intégration, des tâches en arrière-plan et des décisions d'accès au téléchargement.
- [ ] Ajoutez des politiques de conservation des données pour les applications, les notes d'entretien et les jetons de récupération.
- [ ] Ajouter une documentation de sauvegarde et de restauration pour les déploiements SQLite.

Critères d'acceptation :

- [ ] Les responsables peuvent générer un rapport d'utilisation prêt à être financé sans inspection directe de la base de données.
- [ ] Les données utilisateur sensibles sont exclues des exportations publiques ou destinées aux sponsors.
- [ ] Les étapes de sauvegarde et de restauration sont documentées et testées par rapport à une base de données locale.

## Priorités d'ingénierie transversales

- Sécurité : préservez la sémantique à usage unique du jeton d'invitation, le contrôle d'accès basé sur les rôles, les journaux d'audit et l'autorisation de téléchargement.
- Tests : maintenez la couverture au-dessus du seuil CI et ajoutez des tests d'itinéraire/service pour chaque chemin de décision d'intégration.
- Migrations : ajoutez des modifications de schéma uniquement via des fichiers numérotés dans `src/hanger_app/migrations/` ; ne réécrivez jamais les migrations appliquées.
- Documentation : mettez à jour `AGENTS.md`, `README.md` et les notes de déploiement chaque fois que les commandes, la configuration ou les flux de travail changent.
- Observabilité : préférez les journaux structurés et les contrôles de santé explicites aux échecs silencieux.

## Ordre de mise en œuvre suggéré

1. [x] Ajoutez un schéma d'application et d'invitation.
2. [x] Implémenter le référentiel et la couche de service pour les décisions d'application.
3. [x] Ajoutez des commandes CLI d'administration et des routes d'administration protégées.
4. [x] Désactivez l'inscription ouverte lorsque le mode sur invitation uniquement est activé.
5. [x] Ajoutez les paramètres d'installation et la validation de la production.
6. [x] Ajoutez des notes d'entretien et des contrôles d'accès.
7. [ ] Ajoutez des commandes de reporting et des exportations nettoyées.
8. [~] Documentez les workflows de déploiement, de sauvegarde, de restauration et opérationnels.
# Technische Roadmap

Diese Roadmap wandelt die aktuellen Produkthinweise in „ROADMAP.md“ in umsetzbare Engineering-Arbeiten für „hanger_app“ um. Der Schwerpunkt liegt auf den nächsten Backend-, Sicherheits-, Betriebs- und Dokumentationsmeilensteinen.

## 1. Kontrolliertes Benutzer-Onboarding

Ziel: Nur Benutzer registrieren, die einen Auswahlprozess bestehen.

Umsetzungsumfang:

- [x] Fügen Sie einen Bewerbungsworkflow mit den Status „eingereicht“, „Überprüfung“, „Interview“, „akzeptiert“, „abgelehnt“ und „eingeladen“ hinzu.
- [x] Speichern Sie Bewerbungsantworten, Prüfernotizen, Entscheidungszeitstempel und Prüfer-Benutzer-IDs.
- [x] Ersetzen Sie die offene Registrierung durch eine Registrierung nur auf Einladung, die an angenommene Bewerbungen gebunden ist.
- [x] Fügen Sie Admin-Routen und CLI-Befehle hinzu, um Bewerber zu prüfen, anzunehmen, abzulehnen und einzuladen.
  CLI-Befehle und geschützte Admin-Anwendungsrouten sind implementiert.
- [x] Fügen Sie Prüfereignisse für jede Änderung des Anwendungsstatus hinzu.
  Annehmen, Ablehnen, Einladen, Interviewplanung, Interviewabschluss und Notizenerstellung werden auf der Serviceebene geprüft.

Akzeptanzkriterien:

- [x] Ein nicht eingeladener Benutzer kann kein Konto erstellen.
- [x] Akzeptierte Bewerber erhalten eine einmalige Einladung.
- [x] Tests umfassen doppelte Bewerbungen, abgelehnte Bewerbungen, abgelaufene Einladungen und Entscheidungen, die nur dem Administrator vorbehalten sind.

## 2. Anforderungen pro Installation

Ziel: Unterstützung verschiedener Berechtigungsregeln und Betriebsgrenzen für jeden bereitgestellten Server.

Umsetzungsumfang:

- [x] Führen Sie eine „installation_settings“-Tabelle für Onboarding-Regeln, Berechtigungskriterien, Beschränkungen und Branding ein.
- [x] Verschieben Sie serverspezifische Werte aus dem Quellcode in Umgebungsvariablen oder datenbankgestützte Einstellungen.
- [x] Validieren Sie die erforderlichen Produktionseinstellungen während des Anwendungsstarts.
- [x] Fügen Sie eine Admin-Benutzeroberfläche oder CLI zum Lesen und Aktualisieren sicherer Einstellungen hinzu.
  CLI-Unterstützung wird mit „settings-list“, „settings-get“ und „settings-set“ implementiert.
- [~] Dokumentieren Sie die erforderliche Konfiguration in „README.md“ und Bereitstellungsbeispiele.
  „README.md“ und Contributor-Befehle werden aktualisiert; Ausführlichere Bereitstellungsbeispiele stehen noch aus.

Akzeptanzkriterien:

- [x] Jede Bereitstellung kann ohne Codeänderungen ihre eigenen Berechtigungsregeln definieren.
- [x] Fehlende Produktionskonfiguration schlägt schnell mit einem eindeutigen Fehler fehl.
– [x] Tests überprüfen Standardeinstellungen, Überschreibungen und ungültige Konfigurationen.

## 3. Interview- und Forschungspipeline

Ziel: Interviews mit möglichen zukünftigen Nutzern verwalten und Recherchen in umsetzbare Produktsignale umwandeln.

Umsetzungsumfang:

- [x] Fügen Sie Felder für die Planung von Bewerberinterviews hinzu: Kontaktmethode, bevorzugte Zeiten, zugewiesener Interviewer und Status.
- [x] Fügen Sie Interviewnotizen mit strukturierten Kategorien hinzu: Motivation, Eignung, Risiken und Folgemaßnahmen.
- [x] Fügen Sie Datenschutzkontrollen hinzu, damit nur Administratoren oder zugewiesene Interviewer Interviewnotizen lesen können.
- [x] Fügen Sie aggregierte Exporte für Forschungsmetriken hinzu, ohne vertrauliche Notizen preiszugeben.

Akzeptanzkriterien:

- [x] Interviewnotizen sind zugriffskontrolliert und geprüft.
- [x] Administratoren können Bewerber nach Interviewstatus auflisten.
- [x] Forschungsexporte schließen private Freitextnotizen standardmäßig aus.

## 4. Finanzierung und Betriebsbereitschaft

Ziel: Das Projekt auf externe Finanzierung, Sponsoring oder strukturierte Zusammenarbeit vorbereiten.

Umsetzungsumfang:

- [ ] Betriebsmetriken hinzufügen: registrierte Benutzer, aktive Benutzer, Bewerbungen nach Status, Einladungsumwandlung und Nachrichten-/Jobstatus.
- [ ] Fügen Sie Gesundheits-Dashboards oder CLI-Berichte mithilfe der vorhandenen Grundlagen „/health/live“ und „/health/ready“ hinzu.
- [ ] Verbessern Sie die Protokollierung rund um Authentifizierung, Onboarding, Hintergrundjobs und Upload-Zugriffsentscheidungen.
- [ ] Fügen Sie Datenaufbewahrungsrichtlinien für Bewerbungen, Interviewnotizen und Wiederherstellungstokens hinzu.
- [ ] Sicherungs- und Wiederherstellungsdokumentation für SQLite-Bereitstellungen hinzufügen.

Akzeptanzkriterien:

- [ ] Betreuer können ohne direkte Datenbankprüfung einen finanzierungsbereiten Nutzungsbericht erstellen.
- [ ] Sensible Benutzerdaten sind von öffentlichen oder Sponsor-bezogenen Exporten ausgeschlossen.
- [ ] Sicherungs- und Wiederherstellungsschritte werden dokumentiert und anhand einer lokalen Datenbank getestet.

## Übergreifende technische Prioritäten

- Sicherheit: Bewahrt die Einmalsemantik des Einladungstokens, die rollenbasierte Zugriffskontrolle, Prüfprotokolle und die Upload-Autorisierung.
- Tests: Halten Sie die Abdeckung über dem CI-Schwellenwert und fügen Sie Routen-/Diensttests für jeden Onboarding-Entscheidungspfad hinzu.
- Migrationen: Schemaänderungen nur über nummerierte Dateien in „src/hanger_app/migrations/“ hinzufügen; Schreiben Sie angewandte Migrationen niemals neu.
- Dokumentation: Aktualisieren Sie „AGENTS.md“, „README.md“ und Bereitstellungshinweise, wenn sich Befehle, Konfiguration oder Arbeitsabläufe ändern.
- Beobachtbarkeit: Bevorzugen Sie strukturierte Protokolle und explizite Zustandsprüfungen gegenüber stillen Fehlern.

## Vorgeschlagene Implementierungsreihenfolge

1. [x] Anwendungs- und Einladungsschema hinzufügen.
2. [x] Implementieren Sie die Repository- und Serviceschicht für Anwendungsentscheidungen.
3. [x] Admin-CLI-Befehle und geschützte Admin-Routen hinzufügen.
4. [x] Deaktivieren Sie die offene Registrierung, wenn der Nur-Einladungs-Modus aktiviert ist.
5. [x] Installationseinstellungen und Produktionsvalidierung hinzufügen.
6. [x] Fügen Sie Interviewnotizen und Zugriffskontrollen hinzu.
7. [] Fügen Sie Berichtsbefehle und bereinigte Exporte hinzu.
8. [~] Dokumentbereitstellung, Sicherung, Wiederherstellung und betriebliche Arbeitsabläufe.
# Technische Roadmap

Diese Roadmap wandelt die aktuellen Produkthinweise in „ROADMAP.md“ in umsetzbare Engineering-Arbeiten für „hanger_app“ um. Der Schwerpunkt liegt auf den nächsten Backend-, Sicherheits-, Betriebs- und Dokumentationsmeilensteinen.

## 1. Kontrolliertes Benutzer-Onboarding

Ziel: Nur Benutzer registrieren, die einen Auswahlprozess bestehen.

Umsetzungsumfang:

- [x] Fügen Sie einen Bewerbungsworkflow mit den Status „eingereicht“, „Überprüfung“, „Interview“, „akzeptiert“, „abgelehnt“ und „eingeladen“ hinzu.
- [x] Speichern Sie Bewerbungsantworten, Prüfernotizen, Entscheidungszeitstempel und Prüfer-Benutzer-IDs.
- [x] Ersetzen Sie die offene Registrierung durch eine Registrierung nur auf Einladung, die an angenommene Bewerbungen gebunden ist.
- [x] Fügen Sie Admin-Routen und CLI-Befehle hinzu, um Bewerber zu prüfen, anzunehmen, abzulehnen und einzuladen.
  CLI-Befehle und geschützte Admin-Anwendungsrouten sind implementiert.
- [x] Fügen Sie Prüfereignisse für jede Änderung des Anwendungsstatus hinzu.
  Annehmen, Ablehnen, Einladen, Interviewplanung, Interviewabschluss und Notizenerstellung werden auf der Serviceebene geprüft.

Akzeptanzkriterien:

- [x] Ein nicht eingeladener Benutzer kann kein Konto erstellen.
- [x] Akzeptierte Bewerber erhalten eine einmalige Einladung.
- [x] Tests umfassen doppelte Bewerbungen, abgelehnte Bewerbungen, abgelaufene Einladungen und Entscheidungen, die nur dem Administrator vorbehalten sind.

## 2. Anforderungen pro Installation

Ziel: Unterstützung verschiedener Berechtigungsregeln und Betriebsgrenzen für jeden bereitgestellten Server.

Umsetzungsumfang:

- [x] Führen Sie eine „installation_settings“-Tabelle für Onboarding-Regeln, Berechtigungskriterien, Beschränkungen und Branding ein.
- [x] Verschieben Sie serverspezifische Werte aus dem Quellcode in Umgebungsvariablen oder datenbankgestützte Einstellungen.
- [x] Validieren Sie die erforderlichen Produktionseinstellungen während des Anwendungsstarts.
- [x] Fügen Sie eine Admin-Benutzeroberfläche oder CLI zum Lesen und Aktualisieren sicherer Einstellungen hinzu.
  CLI-Unterstützung wird mit „settings-list“, „settings-get“ und „settings-set“ implementiert.
- [~] Dokumentieren Sie die erforderliche Konfiguration in „README.md“ und Bereitstellungsbeispiele.
  „README.md“ und Contributor-Befehle werden aktualisiert; Ausführlichere Bereitstellungsbeispiele stehen noch aus.

Akzeptanzkriterien:

- [x] Jede Bereitstellung kann ohne Codeänderungen ihre eigenen Berechtigungsregeln definieren.
- [x] Fehlende Produktionskonfiguration schlägt schnell mit einem eindeutigen Fehler fehl.
– [x] Tests überprüfen Standardeinstellungen, Überschreibungen und ungültige Konfigurationen.

## 3. Interview- und Forschungspipeline

Ziel: Interviews mit möglichen zukünftigen Nutzern verwalten und Recherchen in umsetzbare Produktsignale umwandeln.

Umsetzungsumfang:

- [x] Fügen Sie Felder für die Planung von Bewerberinterviews hinzu: Kontaktmethode, bevorzugte Zeiten, zugewiesener Interviewer und Status.
- [x] Fügen Sie Interviewnotizen mit strukturierten Kategorien hinzu: Motivation, Eignung, Risiken und Folgemaßnahmen.
- [x] Fügen Sie Datenschutzkontrollen hinzu, damit nur Administratoren oder zugewiesene Interviewer Interviewnotizen lesen können.
- [x] Fügen Sie aggregierte Exporte für Forschungsmetriken hinzu, ohne vertrauliche Notizen preiszugeben.

Akzeptanzkriterien:

- [x] Interviewnotizen sind zugriffskontrolliert und geprüft.
- [x] Administratoren können Bewerber nach Interviewstatus auflisten.
- [x] Forschungsexporte schließen private Freitextnotizen standardmäßig aus.

## 4. Finanzierung und Betriebsbereitschaft

Ziel: Das Projekt auf externe Finanzierung, Sponsoring oder strukturierte Zusammenarbeit vorbereiten.

Umsetzungsumfang:

- [ ] Betriebsmetriken hinzufügen: registrierte Benutzer, aktive Benutzer, Bewerbungen nach Status, Einladungsumwandlung und Nachrichten-/Jobstatus.
- [ ] Fügen Sie Gesundheits-Dashboards oder CLI-Berichte mithilfe der vorhandenen Grundlagen „/health/live“ und „/health/ready“ hinzu.
- [ ] Verbessern Sie die Protokollierung rund um Authentifizierung, Onboarding, Hintergrundjobs und Upload-Zugriffsentscheidungen.
- [ ] Fügen Sie Datenaufbewahrungsrichtlinien für Bewerbungen, Interviewnotizen und Wiederherstellungstokens hinzu.
- [ ] Sicherungs- und Wiederherstellungsdokumentation für SQLite-Bereitstellungen hinzufügen.

Akzeptanzkriterien:

- [ ] Betreuer können ohne direkte Datenbankprüfung einen finanzierungsbereiten Nutzungsbericht erstellen.
- [ ] Sensible Benutzerdaten sind von öffentlichen oder Sponsor-bezogenen Exporten ausgeschlossen.
- [ ] Sicherungs- und Wiederherstellungsschritte werden dokumentiert und anhand einer lokalen Datenbank getestet.

## Übergreifende technische Prioritäten

- Sicherheit: Bewahrt die Einmalsemantik des Einladungstokens, die rollenbasierte Zugriffskontrolle, Prüfprotokolle und die Upload-Autorisierung.
- Tests: Halten Sie die Abdeckung über dem CI-Schwellenwert und fügen Sie Routen-/Diensttests für jeden Onboarding-Entscheidungspfad hinzu.
- Migrationen: Schemaänderungen nur über nummerierte Dateien in „src/hanger_app/migrations/“ hinzufügen; Schreiben Sie angewandte Migrationen niemals neu.
- Dokumentation: Aktualisieren Sie „AGENTS.md“, „README.md“ und Bereitstellungshinweise, wenn sich Befehle, Konfiguration oder Arbeitsabläufe ändern.
- Beobachtbarkeit: Bevorzugen Sie strukturierte Protokolle und explizite Zustandsprüfungen gegenüber stillen Fehlern.

## Vorgeschlagene Implementierungsreihenfolge

1. [x] Anwendungs- und Einladungsschema hinzufügen.
2. [x] Implementieren Sie die Repository- und Serviceschicht für Anwendungsentscheidungen.
3. [x] Admin-CLI-Befehle und geschützte Admin-Routen hinzufügen.
4. [x] Deaktivieren Sie die offene Registrierung, wenn der Nur-Einladungs-Modus aktiviert ist.
5. [x] Installationseinstellungen und Produktionsvalidierung hinzufügen.
6. [x] Fügen Sie Interviewnotizen und Zugriffskontrollen hinzu.
7. [] Fügen Sie Berichtsbefehle und bereinigte Exporte hinzu.
8. [~] Dokumentbereitstellung, Sicherung, Wiederherstellung und betriebliche Arbeitsabläufe.
# 技術ロードマップ

このロードマップは、`ROADMAP.md` 内の現在の製品ノートを `hanger_app` の実装可能なエンジニアリング作業に変換します。次のバックエンド、セキュリティ、運用、ドキュメントのマイルストーンに焦点を当てています。

## 1. 制御されたユーザーのオンボーディング

目標: 選考プロセスを通過したユーザーのみを登録します。

実装範囲:

- [x] 状態を含むアプリケーション ワークフローを追加します: `submitted`、`screening`、`interview`、`accepted`、`rejected`、および `invited`。
- [x] アプリケーションの回答、レビュー担当者のメモ、決定タイムスタンプ、およびレビュー担当者のユーザー ID を保存します。
- [x] オープン登録を、承認されたアプリケーションに関連付けられた招待専用登録に置き換えます。
- [x] 申請者を確認、承認、拒否、招待するための管理ルートと CLI コマンドを追加します。
  CLI コマンドと保護された管理アプリケーション ルートが実装されています。
- [x] アプリケーションの状態変化ごとに監査イベントを追加します。
  承諾、拒否、招待、面接のスケジュール設定、面接の完了、メモの作成はサービス層で監査されます。

受け入れ基準:

- [x] 招待されていないユーザーはアカウントを作成できません。
- [x] 承認された応募者は、1 回限りの招待状を受け取ります。
- [x] テストでは、重複した申請、拒否された申請、期限切れの招待、および管理者のみの決定が対象になります。

## 2. インストールごとの要件

目標: 導入されたサーバーごとに異なる資格ルールと動作制限をサポートします。

実装範囲:

- [x] オンボーディング ルール、資格基準、制限、およびブランド化のための「installation_settings」テーブルを導入します。
- [x] サーバー固有の値をソース コードから環境変数またはデータベースに基づく設定に移動します。
- [x] アプリケーションの起動時に必要な運用設定を検証します。
- [x] 安全な設定を読み取り、更新するための管理 UI または CLI を追加します。
  CLI サポートは、`settings-list`、`settings-get`、および `settings-set` で実装されます。
- [~] `README.md` に必要な設定と展開例を文書化します。
  「README.md」と寄稿者のコマンドが更新されました。より豊富な導入例は保留中です。

受け入れ基準:

- [x] 各展開では、コードを変更せずに独自の適格性ルールを定義できます。
- [x] 実稼働構成が欠落していると、明らかなエラーが発生してすぐに失敗します。
- [x] テストでは、デフォルト設定、オーバーライド、および無効な構成を検証します。

## 3. インタビューと調査パイプライン

目標: 将来のユーザーとなる可能性のあるユーザーとのインタビューを管理し、調査結果を実用的な製品シグナルに変換します。

実装範囲:

- [x] 応募者の面接スケジュール フィールドを追加します: 連絡方法、希望時間、割り当てられた面接官、およびステータス。
- [x] 構造化されたカテゴリ (モチベーション、適合性、リスク、フォローアップ アクション) を含むインタビューメモを追加します。
- [x] 管理者または割り当てられた面接官のみが面接メモを読めるようにプライバシー制御を追加します。
- [x] 機密メモを公開せずに調査指標の集計エクスポートを追加します。

受け入れ基準:

- [x] インタビューメモはアクセス制御され、監査されます。
- [x] 管理者は、面接ステータスごとに応募者をリストできます。
- [x] リサーチのエクスポートでは、デフォルトでプライベートな自由記述メモが除外されます。

## 4. 資金調達と運営の準備

目標: 外部からの資金提供、スポンサーシップ、または構造化されたコラボレーションのためにプロジェクトを準備します。

実装範囲:

- [ ] 運用メトリクスを追加します: 登録ユーザー、アクティブ ユーザー、ステータス別のアプリケーション、招待の変換、メッセージ/ジョブの健全性。
- [ ] 既存の `/health/live` および `/health/ready` 基盤を使用して、ヘルス ダッシュボードまたは CLI レポートを追加します。
- [ ] 認証、オンボーディング、バックグラウンド ジョブ、およびアップロード アクセスの決定に関するログを改善します。
- [ ] アプリケーション、インタビューメモ、リカバリトークンのデータ保持ポリシーを追加します。
- [ ] SQLite デプロイメントのバックアップと復元に関するドキュメントを追加します。

受け入れ基準:

- [ ] メンテナンス者は、データベースを直接検査することなく、資金調達の準備ができた使用状況レポートを生成できます。
- [ ] 機密性の高いユーザー データは、公開エクスポートまたはスポンサー向けエクスポートから除外されます。
- [ ] バックアップと復元の手順が文書化され、ローカル データベースに対してテストされます。

## 横断的なエンジニアリングの優先事項

- セキュリティ: 招待トークンの使い捨てセマンティクス、ロールベースのアクセス制御、監査ログ、およびアップロード承認を保持します。
- テスト: カバレッジを CI しきい値以上に保ち、すべてのオンボーディング決定パスにルート/サービス テストを追加します。
- 移行: `src/hanger_app/migrations/` 内の番号付きファイルを通じてのみスキーマ変更を追加します。適用された移行を決して書き換えないでください。
- ドキュメント: コマンド、構成、またはワークフローが変更されるたびに、「AGENTS.md」、「README.md」、および展開ノートを更新します。
- 可観測性: サイレント障害よりも構造化されたログと明示的なヘルスチェックを好みます。

## 推奨される実装順序

1. [x] アプリケーションと招待スキーマを追加します。
2. [x] アプリケーションの決定のためにリポジトリとサービス層を実装します。
3. [x] 管理 CLI コマンドと保護された管理ルートを追加します。
4. [x] 招待専用モードが有効な場合、オープン登録を無効にします。
5. [x] インストール設定と運用検証を追加します。
6. [x] インタビューメモとアクセス制御を追加します。
7. [ ] レポート コマンドとサニタイズされたエクスポートを追加します。
8. [~] 導入、バックアップ、復元、運用ワークフローを文書化します。
# 技術ロードマップ

このロードマップは、`ROADMAP.md` 内の現在の製品ノートを `hanger_app` の実装可能なエンジニアリング作業に変換します。次のバックエンド、セキュリティ、運用、ドキュメントのマイルストーンに焦点を当てています。

## 1. 制御されたユーザーのオンボーディング

目標: 選考プロセスを通過したユーザーのみを登録します。

実装範囲:

- [x] 状態を含むアプリケーション ワークフローを追加します: `submitted`、`screening`、`interview`、`accepted`、`rejected`、および `invited`。
- [x] アプリケーションの回答、レビュー担当者のメモ、決定タイムスタンプ、およびレビュー担当者のユーザー ID を保存します。
- [x] オープン登録を、承認されたアプリケーションに関連付けられた招待専用登録に置き換えます。
- [x] 申請者を確認、承認、拒否、招待するための管理ルートと CLI コマンドを追加します。
  CLI コマンドと保護された管理アプリケーション ルートが実装されています。
- [x] アプリケーションの状態変化ごとに監査イベントを追加します。
  承諾、拒否、招待、面接のスケジュール設定、面接の完了、メモの作成はサービス層で監査されます。

受け入れ基準:

- [x] 招待されていないユーザーはアカウントを作成できません。
- [x] 承認された応募者は、1 回限りの招待状を受け取ります。
- [x] テストでは、重複した申請、拒否された申請、期限切れの招待、および管理者のみの決定が対象になります。

## 2. インストールごとの要件

目標: 導入されたサーバーごとに異なる資格ルールと動作制限をサポートします。

実装範囲:

- [x] オンボーディング ルール、資格基準、制限、およびブランド化のための「installation_settings」テーブルを導入します。
- [x] サーバー固有の値をソース コードから環境変数またはデータベースに基づく設定に移動します。
- [x] アプリケーションの起動時に必要な運用設定を検証します。
- [x] 安全な設定を読み取り、更新するための管理 UI または CLI を追加します。
  CLI サポートは、`settings-list`、`settings-get`、および `settings-set` で実装されます。
- [~] `README.md` に必要な設定と展開例を文書化します。
  「README.md」と寄稿者のコマンドが更新されました。より豊富な導入例は保留中です。

受け入れ基準:

- [x] 各展開では、コードを変更せずに独自の適格性ルールを定義できます。
- [x] 実稼働構成が欠落していると、明らかなエラーが発生してすぐに失敗します。
- [x] テストでは、デフォルト設定、オーバーライド、および無効な構成を検証します。

## 3. インタビューと調査パイプライン

目標: 将来のユーザーとなる可能性のあるユーザーとのインタビューを管理し、調査結果を実用的な製品シグナルに変換します。

実装範囲:

- [x] 応募者の面接スケジュール フィールドを追加します: 連絡方法、希望時間、割り当てられた面接官、およびステータス。
- [x] 構造化されたカテゴリ (モチベーション、適合性、リスク、フォローアップ アクション) を含むインタビューメモを追加します。
- [x] 管理者または割り当てられた面接官のみが面接メモを読めるようにプライバシー制御を追加します。
- [x] 機密メモを公開せずに調査指標の集計エクスポートを追加します。

受け入れ基準:

- [x] インタビューメモはアクセス制御され、監査されます。
- [x] 管理者は、面接ステータスごとに応募者をリストできます。
- [x] リサーチのエクスポートでは、デフォルトでプライベートな自由記述メモが除外されます。

## 4. 資金調達と運営の準備

目標: 外部からの資金提供、スポンサーシップ、または構造化されたコラボレーションのためにプロジェクトを準備します。

実装範囲:

- [ ] 運用メトリクスを追加します: 登録ユーザー、アクティブ ユーザー、ステータス別のアプリケーション、招待の変換、メッセージ/ジョブの健全性。
- [ ] 既存の `/health/live` および `/health/ready` 基盤を使用して、ヘルス ダッシュボードまたは CLI レポートを追加します。
- [ ] 認証、オンボーディング、バックグラウンド ジョブ、およびアップロード アクセスの決定に関するログを改善します。
- [ ] アプリケーション、インタビューメモ、リカバリトークンのデータ保持ポリシーを追加します。
- [ ] SQLite デプロイメントのバックアップと復元に関するドキュメントを追加します。

受け入れ基準:

- [ ] メンテナンス者は、データベースを直接検査することなく、資金調達の準備ができた使用状況レポートを生成できます。
- [ ] 機密性の高いユーザー データは、公開エクスポートまたはスポンサー向けエクスポートから除外されます。
- [ ] バックアップと復元の手順が文書化され、ローカル データベースに対してテストされます。

## 横断的なエンジニアリングの優先事項

- セキュリティ: 招待トークンの使い捨てセマンティクス、ロールベースのアクセス制御、監査ログ、およびアップロード承認を保持します。
- テスト: カバレッジを CI しきい値以上に保ち、すべてのオンボーディング決定パスにルート/サービス テストを追加します。
- 移行: `src/hanger_app/migrations/` 内の番号付きファイルを通じてのみスキーマ変更を追加します。適用された移行を決して書き換えないでください。
- ドキュメント: コマンド、構成、またはワークフローが変更されるたびに、「AGENTS.md」、「README.md」、および展開ノートを更新します。
- 可観測性: サイレント障害よりも構造化されたログと明示的なヘルスチェックを好みます。

## 推奨される実装順序

1. [x] アプリケーションと招待スキーマを追加します。
2. [x] アプリケーションの決定のためにリポジトリとサービス層を実装します。
3. [x] 管理 CLI コマンドと保護された管理ルートを追加します。
4. [x] 招待専用モードが有効な場合、オープン登録を無効にします。
5. [x] インストール設定と運用検証を追加します。
6. [x] インタビューメモとアクセス制御を追加します。
7. [ ] レポート コマンドとサニタイズされたエクスポートを追加します。
8. [~] 導入、バックアップ、復元、運用ワークフローを文書化します。
# 技术路线图

该路线图将“ROADMAP.md”中的当前产品说明转换为“hanger_app”的可实施工程工作。它重点关注下一个后端、安全、操作和文档里程碑。

## 1. 受控的用户登录

目标：仅注册通过选择过程的用户。

实施范围：

- [x] 添加具有以下状态的应用程序工作流程：“已提交”、“筛选”、“面试”、“已接受”、“已拒绝”和“已邀请”。
- [x] 存储申请答案、审阅者注释、决策时间戳和审阅者用户 ID。
- [x] 将开放注册替换为与接受的申请相关的邀请注册。
- [x] 添加管理路由和 CLI 命令来审核、接受、拒绝和邀请申请人。
  CLI 命令和受保护的管理应用程序路由已实施。
- [x] 为每个应用程序状态更改添加审核事件。
  接受、拒绝、邀请、采访安排、采访完成和注释创建都在服务层进行审核。

验收标准：

- [x] 未经邀请的用户无法创建帐户。
- [x] 被接受的申请人将收到一次性邀请。
- [x] 测试涵盖重复的申请、拒绝的申请、过期的邀请和仅限管理员的决定。

## 2. 每次安装的要求

目标：支持每个部署的服务器不同的资格规则和操作限制。

实施范围：

- [x] 引入一个“installation_settings”表，用于规定入职规则、资格标准、限制和品牌。
- [x] 将服务器特定值从源代码移至环境变量或数据库支持的设置中。
- [x] 在应用程序启动期间验证所需的生产设置。
- [x] 添加管理 UI 或 CLI 以读取和更新安全设置。
  CLI 支持是通过“settings-list”、“settings-get”和“settings-set”实现的。
- [~] 在`README.md`和部署示例中记录所需的配置。
  更新了“README.md”和贡献者命令；更丰富的部署示例仍有待确定。

验收标准：

- [x] 每个部署都可以定义自己的资格规则，无需更改代码。
- [x] 缺少生产配置会快速失败并出现明显错误。
- [x] 测试验证默认设置、覆盖和无效配置。

## 3. 访谈和研究流程

目标：管理与未来可能用户的访谈，并将研究转化为可操作的产品信号。

实施范围：

- [x] 添加申请人面试安排字段：联系方式、首选时间、指定面试官和状态。
- [x] 添加具有结构化类别的访谈记录：动机、适合性、风险和后续行动。
- [x] 添加隐私控制，以便只有管理员或指定的面试官才能阅读面试笔记。
- [x] 添加研究指标的聚合导出，而不暴露敏感注释。

验收标准：

- [x] 采访记录受到访问控制和审核。
- [x] 管理员可以按面试状态列出申请人。
- [x] 研究导出默认排除私人自由文本注释。

## 4. 资金和运营准备情况

目标：为项目准备外部资金、赞助或结构化合作。

实施范围：

- [ ] 添加运营指标：注册用户、活跃用户、按状态划分的应用程序、邀请转化和消息/作业运行状况。
- [ ] 使用现有的 `/health/live` 和 `/health/ready` 基础添加运行状况仪表板或 CLI 报告。
- [ ] 改进有关身份验证、入职、后台作业和上传访问决策的日志记录。
- [ ] 添加应用程序、访谈记录和恢复令牌的数据保留策略。
- [ ] 添加 SQLite 部署的备份和恢复文档。

验收标准：

- [ ] 维护者无需直接检查数据库即可生成资金就绪使用报告。
- [ ] 敏感用户数据不被公开或面向赞助商的导出。
- [ ] 备份和恢复步骤已记录并针对本地数据库进行了测试。

## 跨领域工程优先事项

- 安全性：保留邀请令牌一次性语义、基于角色的访问控制、审核日志和上传授权。
- 测试：将覆盖范围保持在 CI 阈值以上，并为每个入职决策路径添加路由/服务测试。
- 迁移：仅通过“src/hanger_app/migrations/”中的编号文件添加架构更改；切勿重写已应用的迁移。
- 文档：每当命令、配置或工作流程发生更改时，更新“AGENTS.md”、“README.md”和部署说明。
- 可观察性：与无声故障相比，更喜欢结构化日志和显式运行状况检查。

## 建议的实施顺序

1. [x] 添加申请和邀请架构。
2. [x] 为应用程序决策实现存储库和服务层。
3. [x] 添加管理 CLI 命令和受保护的管理路由。
4. [x] 在启用仅限邀请模式时禁用开放注册。
5. [x] 添加安装设置和生产验证。
6. [x] 添加访谈记录和访问控制。
7. [ ] 添加报告命令和清理导出。
8. [~] 文档部署、备份、恢复和操作工作流程。
# 技术路线图

该路线图将“ROADMAP.md”中的当前产品说明转换为“hanger_app”的可实施工程工作。它重点关注下一个后端、安全、操作和文档里程碑。

## 1. 受控的用户登录

目标：仅注册通过选择过程的用户。

实施范围：

- [x] 添加具有以下状态的应用程序工作流程：“已提交”、“筛选”、“面试”、“已接受”、“已拒绝”和“已邀请”。
- [x] 存储申请答案、审阅者注释、决策时间戳和审阅者用户 ID。
- [x] 将开放注册替换为与接受的申请相关的邀请注册。
- [x] 添加管理路由和 CLI 命令来审核、接受、拒绝和邀请申请人。
  CLI 命令和受保护的管理应用程序路由已实施。
- [x] 为每个应用程序状态更改添加审核事件。
  接受、拒绝、邀请、采访安排、采访完成和注释创建都在服务层进行审核。

验收标准：

- [x] 未经邀请的用户无法创建帐户。
- [x] 被接受的申请人将收到一次性邀请。
- [x] 测试涵盖重复的申请、拒绝的申请、过期的邀请和仅限管理员的决定。

## 2. 每次安装的要求

目标：支持每个部署的服务器不同的资格规则和操作限制。

实施范围：

- [x] 引入一个“installation_settings”表，用于规定入职规则、资格标准、限制和品牌。
- [x] 将服务器特定值从源代码移至环境变量或数据库支持的设置中。
- [x] 在应用程序启动期间验证所需的生产设置。
- [x] 添加管理 UI 或 CLI 以读取和更新安全设置。
  CLI 支持是通过“settings-list”、“settings-get”和“settings-set”实现的。
- [~] 在`README.md`和部署示例中记录所需的配置。
  更新了“README.md”和贡献者命令；更丰富的部署示例仍有待确定。

验收标准：

- [x] 每个部署都可以定义自己的资格规则，无需更改代码。
- [x] 缺少生产配置会快速失败并出现明显错误。
- [x] 测试验证默认设置、覆盖和无效配置。

## 3. 访谈和研究流程

目标：管理与未来可能用户的访谈，并将研究转化为可操作的产品信号。

实施范围：

- [x] 添加申请人面试安排字段：联系方式、首选时间、指定面试官和状态。
- [x] 添加具有结构化类别的访谈记录：动机、适合性、风险和后续行动。
- [x] 添加隐私控制，以便只有管理员或指定的面试官才能阅读面试笔记。
- [x] 添加研究指标的聚合导出，而不暴露敏感注释。

验收标准：

- [x] 采访记录受到访问控制和审核。
- [x] 管理员可以按面试状态列出申请人。
- [x] 研究导出默认排除私人自由文本注释。

## 4. 资金和运营准备情况

目标：为项目准备外部资金、赞助或结构化合作。

实施范围：

- [ ] 添加运营指标：注册用户、活跃用户、按状态划分的应用程序、邀请转化和消息/作业运行状况。
- [ ] 使用现有的 `/health/live` 和 `/health/ready` 基础添加运行状况仪表板或 CLI 报告。
- [ ] 改进有关身份验证、入职、后台作业和上传访问决策的日志记录。
- [ ] 添加应用程序、访谈记录和恢复令牌的数据保留策略。
- [ ] 添加 SQLite 部署的备份和恢复文档。

验收标准：

- [ ] 维护者无需直接检查数据库即可生成资金就绪使用报告。
- [ ] 敏感用户数据不被公开或面向赞助商的导出。
- [ ] 备份和恢复步骤已记录并针对本地数据库进行了测试。

## 跨领域工程优先事项

- 安全性：保留邀请令牌一次性语义、基于角色的访问控制、审核日志和上传授权。
- 测试：将覆盖范围保持在 CI 阈值以上，并为每个入职决策路径添加路由/服务测试。
- 迁移：仅通过“src/hanger_app/migrations/”中的编号文件添加架构更改；切勿重写已应用的迁移。
- 文档：每当命令、配置或工作流程发生更改时，更新“AGENTS.md”、“README.md”和部署说明。
- 可观察性：与无声故障相比，更喜欢结构化日志和显式运行状况检查。

## 建议的实施顺序

1. [x] 添加申请和邀请架构。
2. [x] 为应用程序决策实现存储库和服务层。
3. [x] 添加管理 CLI 命令和受保护的管理路由。
4. [x] 在启用仅限邀请模式时禁用开放注册。
5. [x] 添加安装设置和生产验证。
6. [x] 添加访谈记录和访问控制。
7. [ ] 添加报告命令和清理导出。
8. [~] 文档部署、备份、恢复和操作工作流程。
# Технічна дорожня карта

Ця дорожня карта перетворює поточні примітки щодо продукту в `ROADMAP.md` на реалізовану інженерну роботу для `hanger_app`. Він зосереджений на наступному сервері, безпеці, операціях і етапах документації.

## 1. Контрольована адаптація користувачів

Мета: реєструвати лише тих користувачів, які пройшли відбір.

Сфера реалізації:

- [x] Додайте робочий процес заявки зі станами: `надіслано`, `перевірка`, `співбесіда`, `прийнято`, `відхилено` та `запрошено`.
- [x] Зберігайте відповіді на заявки, примітки рецензентів, часові мітки рішень та ідентифікатори користувачів рецензентів.
- [x] Замінити відкриту реєстрацію на реєстрацію лише за запрошеннями, пов’язану з прийнятими заявками.
- [x] Додано маршрути адміністратора та команди CLI для перегляду, прийняття, відхилення та запрошення заявників.
  Реалізовано команди CLI та захищені маршрути додатків адміністратора.
- [x] Додати події аудиту для кожної зміни стану програми.
  Прийняття, відхилення, запрошення, планування співбесіди, завершення співбесіди та створення нотаток перевіряються на рівні обслуговування.

Критерії прийняття:

- [x] Незапрошений користувач не може створити обліковий запис.
- [x] Прийняті заявники отримують одноразове запрошення.
- [x] Тести охоплюють повторювані заявки, відхилені заявки, прострочені запрошення та рішення лише адміністратора.

## 2. Вимоги до інсталяції

Мета: підтримувати різні правила прийнятності та робочі обмеження для кожного розгорнутого сервера.

Сфера реалізації:

- [x] Представлення таблиці `installation_settings` для правил реєстрації, критеріїв прийнятності, обмежень і брендингу.
- [x] Переміщення специфічних для сервера значень із вихідного коду до змінних середовища або налаштувань бази даних.
- [x] Перевірка необхідних робочих налаштувань під час запуску програми.
- [x] Додайте інтерфейс адміністратора або CLI для читання та оновлення безпечних налаштувань.
  Підтримка CLI реалізована за допомогою `settings-list`, `settings-get` і `settings-set`.
- [~] Задокументуйте необхідну конфігурацію в `README.md` і приклади розгортання.
  `README.md` і команди учасників оновлено; багатші приклади розгортання залишаються на розгляді.

Критерії прийняття:

- [x] Кожне розгортання може визначати власні правила відповідності без змін коду.
- [x] Відсутня робоча конфігурація швидко виходить з ладу з явною помилкою.
- [x] Тести перевіряють налаштування за замовчуванням, перевизначення та недійсну конфігурацію.

## 3. Інтерв'ю та дослідження

Мета: провести інтерв’ю з можливими майбутніми користувачами та перетворити дослідження на дієві сигнали про продукт.

Сфера реалізації:

- [x] Додати поля розкладу співбесіди з заявником: спосіб зв’язку, бажаний час, призначеного інтерв’юера та статус.
- [x] Додайте нотатки до інтерв’ю зі структурованими категоріями: мотивація, придатність, ризики та подальші дії.
- [x] Додайте елементи керування конфіденційністю, щоб лише адміністратори або призначені інтерв’юери могли читати нотатки до інтерв’ю.
- [x] Додайте зведені експорти для показників дослідження, не розкриваючи конфіденційні примітки.

Критерії прийняття:

- [x] Замітки з інтерв’ю контролюються та перевіряються.
- [x] Адміністратори можуть складати список претендентів за статусом співбесіди.
- [x] Експорт досліджень виключає приватні довільні текстові нотатки за замовчуванням.

## 4. Готовність до фінансування та операцій

Мета: підготувати проект до зовнішнього фінансування, спонсорства або структурованої співпраці.

Сфера реалізації:

- [ ] Додати оперативні показники: зареєстровані користувачі, активні користувачі, заявки за статусом, перетворення запрошень і стан повідомлень/вакансії.
- [ ] Додайте інформаційні панелі працездатності або звіти CLI за допомогою існуючих основ `/health/live` і `/health/ready`.
- [ ] Покращено журналювання щодо автентифікації, реєстрації, фонових завдань і рішень щодо доступу до завантаження.
- [] Додано політику збереження даних для додатків, записів інтерв’ю та маркерів відновлення.
- [ ] Додати документацію щодо резервного копіювання та відновлення для розгортань SQLite.

Критерії прийняття:

- [ ] Супроводжувачі можуть створити готовий для фінансування звіт про використання без прямої перевірки бази даних.
- [ ] Конфіденційні дані користувача виключаються з загальнодоступного або спонсорського експорту.
- [ ] Кроки резервного копіювання та відновлення задокументовані та перевірені на локальній базі даних.

## Наскрізні інженерні пріоритети

- Безпека: збереження семантики одноразового використання маркера запрошення, контроль доступу на основі ролей, журнали аудиту та авторизація завантаження.
- Тестування: підтримуйте покриття вище порогового значення CI та додайте тести маршруту/послуги для кожного шляху прийняття рішення.
- Міграції: додайте зміни схеми лише через пронумеровані файли в `src/hanger_app/migrations/`; ніколи не переписуйте застосовані міграції.
- Документація: оновлюйте `AGENTS.md`, `README.md` і примітки щодо розгортання кожного разу, коли змінюються команди, конфігурація або робочі процеси.
- Спостережливість: віддавайте перевагу структурованим журналам і явним перевіркам працездатності над тихими помилками.

## Пропонований порядок впровадження

1. [x] Додайте заявку та схему запрошення.
2. [x] Впровадити репозиторій і сервісний рівень для прикладних рішень.
3. [x] Додайте команди CLI адміністратора та захищені маршрути адміністратора.
4. [x] Вимкніть відкриту реєстрацію, коли ввімкнено режим лише за запрошеннями.
5. [x] Додати параметри інсталяції та перевірку продуктивності.
6. [x] Додайте нотатки до інтерв’ю та контроль доступу.
7. [ ] Додайте команди звітування та дезінфікований експорт.
8. [~] Розгортання документів, резервне копіювання, відновлення та робочі процеси.
# Технічна дорожня карта

Ця дорожня карта перетворює поточні примітки щодо продукту в `ROADMAP.md` на реалізовану інженерну роботу для `hanger_app`. Він зосереджений на наступному сервері, безпеці, операціях і етапах документації.

## 1. Контрольована адаптація користувачів

Мета: реєструвати лише тих користувачів, які пройшли відбір.

Сфера реалізації:

- [x] Додайте робочий процес заявки зі станами: `надіслано`, `перевірка`, `співбесіда`, `прийнято`, `відхилено` та `запрошено`.
- [x] Зберігайте відповіді на заявки, примітки рецензентів, часові мітки рішень та ідентифікатори користувачів рецензентів.
- [x] Замінити відкриту реєстрацію на реєстрацію лише за запрошеннями, пов’язану з прийнятими заявками.
- [x] Додано маршрути адміністратора та команди CLI для перегляду, прийняття, відхилення та запрошення заявників.
  Реалізовано команди CLI та захищені маршрути додатків адміністратора.
- [x] Додати події аудиту для кожної зміни стану програми.
  Прийняття, відхилення, запрошення, планування співбесіди, завершення співбесіди та створення нотаток перевіряються на рівні обслуговування.

Критерії прийняття:

- [x] Незапрошений користувач не може створити обліковий запис.
- [x] Прийняті заявники отримують одноразове запрошення.
- [x] Тести охоплюють повторювані заявки, відхилені заявки, прострочені запрошення та рішення лише адміністратора.

## 2. Вимоги до інсталяції

Мета: підтримувати різні правила прийнятності та робочі обмеження для кожного розгорнутого сервера.

Сфера реалізації:

- [x] Представлення таблиці `installation_settings` для правил реєстрації, критеріїв прийнятності, обмежень і брендингу.
- [x] Переміщення специфічних для сервера значень із вихідного коду до змінних середовища або налаштувань бази даних.
- [x] Перевірка необхідних робочих налаштувань під час запуску програми.
- [x] Додайте інтерфейс адміністратора або CLI для читання та оновлення безпечних налаштувань.
  Підтримка CLI реалізована за допомогою `settings-list`, `settings-get` і `settings-set`.
- [~] Задокументуйте необхідну конфігурацію в `README.md` і приклади розгортання.
  `README.md` і команди учасників оновлено; багатші приклади розгортання залишаються на розгляді.

Критерії прийняття:

- [x] Кожне розгортання може визначати власні правила відповідності без змін коду.
- [x] Відсутня робоча конфігурація швидко виходить з ладу з явною помилкою.
- [x] Тести перевіряють налаштування за замовчуванням, перевизначення та недійсну конфігурацію.

## 3. Інтерв'ю та дослідження

Мета: провести інтерв’ю з можливими майбутніми користувачами та перетворити дослідження на дієві сигнали про продукт.

Сфера реалізації:

- [x] Додати поля розкладу співбесіди з заявником: спосіб зв’язку, бажаний час, призначеного інтерв’юера та статус.
- [x] Додайте нотатки до інтерв’ю зі структурованими категоріями: мотивація, придатність, ризики та подальші дії.
- [x] Додайте елементи керування конфіденційністю, щоб лише адміністратори або призначені інтерв’юери могли читати нотатки до інтерв’ю.
- [x] Додайте зведені експорти для показників дослідження, не розкриваючи конфіденційні примітки.

Критерії прийняття:

- [x] Замітки з інтерв’ю контролюються та перевіряються.
- [x] Адміністратори можуть складати список претендентів за статусом співбесіди.
- [x] Експорт досліджень виключає приватні довільні текстові нотатки за замовчуванням.

## 4. Готовність до фінансування та операцій

Мета: підготувати проект до зовнішнього фінансування, спонсорства або структурованої співпраці.

Сфера реалізації:

- [ ] Додати оперативні показники: зареєстровані користувачі, активні користувачі, заявки за статусом, перетворення запрошень і стан повідомлень/вакансії.
- [ ] Додайте інформаційні панелі працездатності або звіти CLI за допомогою існуючих основ `/health/live` і `/health/ready`.
- [ ] Покращено журналювання щодо автентифікації, реєстрації, фонових завдань і рішень щодо доступу до завантаження.
- [] Додано політику збереження даних для додатків, записів інтерв’ю та маркерів відновлення.
- [ ] Додати документацію щодо резервного копіювання та відновлення для розгортань SQLite.

Критерії прийняття:

- [ ] Супроводжувачі можуть створити готовий для фінансування звіт про використання без прямої перевірки бази даних.
- [ ] Конфіденційні дані користувача виключаються з загальнодоступного або спонсорського експорту.
- [ ] Кроки резервного копіювання та відновлення задокументовані та перевірені на локальній базі даних.

## Наскрізні інженерні пріоритети

- Безпека: збереження семантики одноразового використання маркера запрошення, контроль доступу на основі ролей, журнали аудиту та авторизація завантаження.
- Тестування: підтримуйте покриття вище порогового значення CI та додайте тести маршруту/послуги для кожного шляху прийняття рішення.
- Міграції: додайте зміни схеми лише через пронумеровані файли в `src/hanger_app/migrations/`; ніколи не переписуйте застосовані міграції.
- Документація: оновлюйте `AGENTS.md`, `README.md` і примітки щодо розгортання кожного разу, коли змінюються команди, конфігурація або робочі процеси.
- Спостережливість: віддавайте перевагу структурованим журналам і явним перевіркам працездатності над тихими помилками.

## Пропонований порядок впровадження

1. [x] Додайте заявку та схему запрошення.
2. [x] Впровадити репозиторій і сервісний рівень для прикладних рішень.
3. [x] Додайте команди CLI адміністратора та захищені маршрути адміністратора.
4. [x] Вимкніть відкриту реєстрацію, коли ввімкнено режим лише за запрошеннями.
5. [x] Додати параметри інсталяції та перевірку продуктивності.
6. [x] Додайте нотатки до інтерв’ю та контроль доступу.
7. [ ] Додайте команди звітування та дезінфікований експорт.
8. [~] Розгортання документів, резервне копіювання, відновлення та робочі процеси.
# Техническая дорожная карта

Эта дорожная карта преобразует текущие примечания к продукту в ROADMAP.md в реализуемую инженерную работу для Hanger_app. В нем основное внимание уделяется следующим этапам серверной части, безопасности, операций и документации.

## 1. Контролируемая регистрация пользователей

Цель: регистрировать только пользователей, прошедших отбор.

Объем реализации:

- [x] Добавлен рабочий процесс приложения с состояниями: «отправлено», «проверка», «интервью», «принято», «отклонено» и «приглашено».
- [x] Сохраняйте ответы приложений, заметки рецензента, временные метки принятия решения и идентификаторы пользователей рецензента.
- [x] Заменить открытую регистрацию регистрацией только по приглашению, привязанной к принятым заявкам.
- [x] Добавлены маршруты администратора и команды CLI для просмотра, принятия, отклонения и приглашения кандидатов.
  Реализованы команды CLI и защищенные маршруты приложений администратора.
- [x] Добавлять события аудита для каждого изменения состояния приложения.
  Принятие, отклонение, приглашение, планирование собеседований, завершение собеседований и создание заметок проверяются на уровне обслуживания.

Критерии приемки:

- [x] Неприглашенный пользователь не может создать учетную запись.
- [x] Принятые кандидаты получают одноразовое приглашение.
- [x] Тесты охватывают повторяющиеся заявки, отклоненные заявки, приглашения с истекшим сроком действия и решения, принимаемые только администратором.

## 2. Требования к каждой установке

Цель: поддержка различных правил приемлемости и эксплуатационных ограничений для каждого развернутого сервера.

Объем реализации:

- [x] Внедрить таблицу «installation_settings» для правил регистрации, критериев приемлемости, ограничений и брендинга.
- [x] Переместить специфичные для сервера значения из исходного кода в переменные среды или настройки, поддерживаемые базой данных.
- [x] Проверка необходимых производственных настроек во время запуска приложения.
- [x] Добавьте пользовательский интерфейс администратора или интерфейс командной строки для чтения и обновления безопасных настроек.
  Поддержка CLI реализована с помощью «settings-list», «settings-get» и «settings-set».
- [~] Документируйте необходимую конфигурацию в `README.md` и примеры развертывания.
  Обновлен `README.md` и команды участников; примеры более богатого развертывания еще ожидаются.

Критерии приемки:

- [x] Каждое развертывание может определять свои собственные правила отбора без изменения кода.
- [x] Отсутствующая производственная конфигурация быстро завершается с ошибкой с явной ошибкой.
- [x] Тесты проверяют настройки по умолчанию, переопределения и недопустимую конфигурацию.

## 3. Интервью и исследования

Цель: провести интервью с возможными будущими пользователями и превратить исследования в действенные сигналы о продукте.

Объем реализации:

- [x] Добавить поля планирования собеседований с кандидатами: способ связи, предпочтительное время, назначенный интервьюер и статус.
- [x] Добавьте заметки об интервью со структурированными категориями: мотивация, соответствие, риски и последующие действия.
- [x] Добавьте элементы управления конфиденциальностью, чтобы только администраторы или назначенные интервьюеры могли читать записи интервью.
- [x] Добавить совокупный экспорт показателей исследования, не раскрывая конфиденциальные заметки.

Критерии приемки:

- [x] Записи интервью контролируются и проверяются.
- [x] Администраторы могут перечислять кандидатов по статусу собеседования.
- [x] Экспорт исследований по умолчанию исключает частные заметки с произвольным текстом.

## 4. Финансирование и операционная готовность

Цель: подготовить проект к внешнему финансированию, спонсорству или структурированному сотрудничеству.

Объем реализации:

- [ ] Добавление операционных показателей: зарегистрированных пользователей, активных пользователей, заявок по статусу, конверсии приглашений и состояния сообщений/заданий.
- [ ] Добавляйте информационные панели состояния или отчеты CLI, используя существующие основы `/health/live` и `/health/ready`.
- [ ] Улучшено ведение журнала аутентификации, регистрации, фоновых заданий и принятия решений о доступе к загрузке.
- [ ] Добавьте политики хранения данных для приложений, заметок об интервью и токенов восстановления.
- [ ] Добавлена ​​документация по резервному копированию и восстановлению для развертываний SQLite.

Критерии приемки:

- [ ] Специалисты по сопровождению могут создавать готовый к финансированию отчет об использовании без прямой проверки базы данных.
- [ ] Конфиденциальные пользовательские данные исключаются из общедоступного или спонсорского экспорта.
- [ ] Шаги резервного копирования и восстановления документированы и протестированы на локальной базе данных.

## Сквозные инженерные приоритеты

- Безопасность: сохранение семантики одноразового использования токена приглашения, управление доступом на основе ролей, журналы аудита и авторизация загрузки.
- Тестирование: держите покрытие выше порога CI и добавляйте тесты маршрутов/услуг для каждого пути принятия решения.
- Миграции: добавлять изменения схемы только через пронумерованные файлы в `src/hanger_app/migrations/`; никогда не переписывайте прикладные миграции.
- Документация: обновляйте `AGENTS.md`, `README.md` и примечания по развертыванию при каждом изменении команд, конфигурации или рабочих процессов.
- Наблюдаемость: предпочитайте структурированные журналы и явные проверки работоспособности скрытым сбоям.

## Предлагаемый порядок реализации

1. [x] Добавьте заявку и схему приглашения.
2. [x] Реализовать репозиторий и уровень обслуживания для принятия решений приложений.
3. [x] Добавлены команды административного интерфейса командной строки и защищенные маршруты администрирования.
4. [x] Отключить открытую регистрацию при включенном режиме только по приглашению.
5. [x] Добавьте настройки установки и производственную проверку.
6. [x] Добавьте записи интервью и элементы управления доступом.
7. [ ] Добавьте команды отчетности и очищенный экспорт.
8. [~] Документирование рабочих процессов развертывания, резервного копирования, восстановления и эксплуатации.
# Техническая дорожная карта

Эта дорожная карта преобразует текущие примечания к продукту в ROADMAP.md в реализуемую инженерную работу для Hanger_app. В нем основное внимание уделяется следующим этапам серверной части, безопасности, операций и документации.

## 1. Контролируемая регистрация пользователей

Цель: регистрировать только пользователей, прошедших отбор.

Объем реализации:

- [x] Добавлен рабочий процесс приложения с состояниями: «отправлено», «проверка», «интервью», «принято», «отклонено» и «приглашено».
- [x] Сохраняйте ответы приложений, заметки рецензента, временные метки принятия решения и идентификаторы пользователей рецензента.
- [x] Заменить открытую регистрацию регистрацией только по приглашению, привязанной к принятым заявкам.
- [x] Добавлены маршруты администратора и команды CLI для просмотра, принятия, отклонения и приглашения кандидатов.
  Реализованы команды CLI и защищенные маршруты приложений администратора.
- [x] Добавлять события аудита для каждого изменения состояния приложения.
  Принятие, отклонение, приглашение, планирование собеседований, завершение собеседований и создание заметок проверяются на уровне обслуживания.

Критерии приемки:

- [x] Неприглашенный пользователь не может создать учетную запись.
- [x] Принятые кандидаты получают одноразовое приглашение.
- [x] Тесты охватывают повторяющиеся заявки, отклоненные заявки, приглашения с истекшим сроком действия и решения, принимаемые только администратором.

## 2. Требования к каждой установке

Цель: поддержка различных правил приемлемости и эксплуатационных ограничений для каждого развернутого сервера.

Объем реализации:

- [x] Внедрить таблицу «installation_settings» для правил регистрации, критериев приемлемости, ограничений и брендинга.
- [x] Переместить специфичные для сервера значения из исходного кода в переменные среды или настройки, поддерживаемые базой данных.
- [x] Проверка необходимых производственных настроек во время запуска приложения.
- [x] Добавьте пользовательский интерфейс администратора или интерфейс командной строки для чтения и обновления безопасных настроек.
  Поддержка CLI реализована с помощью «settings-list», «settings-get» и «settings-set».
- [~] Документируйте необходимую конфигурацию в `README.md` и примеры развертывания.
  Обновлен `README.md` и команды участников; примеры более богатого развертывания еще ожидаются.

Критерии приемки:

- [x] Каждое развертывание может определять свои собственные правила отбора без изменения кода.
- [x] Отсутствующая производственная конфигурация быстро завершается с ошибкой с явной ошибкой.
- [x] Тесты проверяют настройки по умолчанию, переопределения и недопустимую конфигурацию.

## 3. Интервью и исследования

Цель: провести интервью с возможными будущими пользователями и превратить исследования в действенные сигналы о продукте.

Объем реализации:

- [x] Добавить поля планирования собеседований с кандидатами: способ связи, предпочтительное время, назначенный интервьюер и статус.
- [x] Добавьте заметки об интервью со структурированными категориями: мотивация, соответствие, риски и последующие действия.
- [x] Добавьте элементы управления конфиденциальностью, чтобы только администраторы или назначенные интервьюеры могли читать записи интервью.
- [x] Добавить совокупный экспорт показателей исследования, не раскрывая конфиденциальные заметки.

Критерии приемки:

- [x] Записи интервью контролируются и проверяются.
- [x] Администраторы могут перечислять кандидатов по статусу собеседования.
- [x] Экспорт исследований по умолчанию исключает частные заметки с произвольным текстом.

## 4. Финансирование и операционная готовность

Цель: подготовить проект к внешнему финансированию, спонсорству или структурированному сотрудничеству.

Объем реализации:

- [ ] Добавление операционных показателей: зарегистрированных пользователей, активных пользователей, заявок по статусу, конверсии приглашений и состояния сообщений/заданий.
- [ ] Добавляйте информационные панели состояния или отчеты CLI, используя существующие основы `/health/live` и `/health/ready`.
- [ ] Улучшено ведение журнала аутентификации, регистрации, фоновых заданий и принятия решений о доступе к загрузке.
- [ ] Добавьте политики хранения данных для приложений, заметок об интервью и токенов восстановления.
- [ ] Добавлена ​​документация по резервному копированию и восстановлению для развертываний SQLite.

Критерии приемки:

- [ ] Специалисты по сопровождению могут создавать готовый к финансированию отчет об использовании без прямой проверки базы данных.
- [ ] Конфиденциальные пользовательские данные исключаются из общедоступного или спонсорского экспорта.
- [ ] Шаги резервного копирования и восстановления документированы и протестированы на локальной базе данных.

## Сквозные инженерные приоритеты

- Безопасность: сохранение семантики одноразового использования токена приглашения, управление доступом на основе ролей, журналы аудита и авторизация загрузки.
- Тестирование: держите покрытие выше порога CI и добавляйте тесты маршрутов/услуг для каждого пути принятия решения.
- Миграции: добавлять изменения схемы только через пронумерованные файлы в `src/hanger_app/migrations/`; никогда не переписывайте прикладные миграции.
- Документация: обновляйте `AGENTS.md`, `README.md` и примечания по развертыванию при каждом изменении команд, конфигурации или рабочих процессов.
- Наблюдаемость: предпочитайте структурированные журналы и явные проверки работоспособности скрытым сбоям.

## Предлагаемый порядок реализации

1. [x] Добавьте заявку и схему приглашения.
2. [x] Реализовать репозиторий и уровень обслуживания для принятия решений приложений.
3. [x] Добавлены команды административного интерфейса командной строки и защищенные маршруты администрирования.
4. [x] Отключить открытую регистрацию при включенном режиме только по приглашению.
5. [x] Добавьте настройки установки и производственную проверку.
6. [x] Добавьте записи интервью и элементы управления доступом.
7. [ ] Добавьте команды отчетности и очищенный экспорт.
8. [~] Документирование рабочих процессов развертывания, резервного копирования, восстановления и эксплуатации.