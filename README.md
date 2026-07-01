# Hanger

Hanger is an interview-gated social application built with Flask. It includes
registration, login, password recovery, persistent invitations, messaging,
posts, validated image uploads, and a retryable delivery queue.

## Local setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install poetry==2.2.1
poetry install -E dev
poetry run flask --app hanger_app:create_app run --debug
```

Development data is stored under `instance/`. Production requires
`HANGER_SECRET_KEY`, `HANGER_DB_PATH`, `HANGER_UPLOAD_DIR`,
`HANGER_PUBLIC_URL`, `HANGER_REQUIRE_INVITATION`, and
`HANGER_MAX_UPLOAD_BYTES`. Configure SMTP or Twilio credentials before
processing delivery jobs. SQLite and uploaded files must live on the same
persistent volume; this deployment profile is intended for a single application
host.

```bash
poetry run flask --app hanger_app:create_app db-upgrade
poetry run flask --app hanger_app:create_app create-admin
poetry run flask --app hanger_app:create_app process-jobs --watch
poetry run flask --app hanger_app:create_app settings-list
poetry run flask --app hanger_app:create_app settings-set eligibility.minimum_age 21
poetry run flask --app hanger_app:create_app schedule-interview 1
poetry run flask --app hanger_app:create_app add-interview-note 1
poetry run flask --app hanger_app:create_app research-export
poetry run pytest -q
poetry run ruff check src tests
```

Schema changes belong in numbered SQL files under `src/hanger_app/migrations/`.
Development applies them automatically; production must run `db-upgrade` once before web
workers start. Build the included `Dockerfile` for Gunicorn deployment. Health
checks are available at `/health/live` and `/health/ready`.

Per-installation settings are stored in SQLite and managed with the
`settings-list`, `settings-get`, and `settings-set` CLI commands. Supported
settings include `branding.site_name`, `branding.support_contact`,
`branding.logo_url`, `eligibility.minimum_age`,
`eligibility.allowed_contact_kinds`, and `eligibility.application_prompt`.

Interview workflow commands let admins schedule applicant interviews, assigned
interviewers record structured notes, and maintainers export aggregate research
metrics without exposing private note text by default.
# Percha

Hanger es una aplicación social basada en entrevistas creada con Flask. incluye
registro, inicio de sesión, recuperación de contraseña, invitaciones persistentes, mensajería,
publicaciones, cargas de imágenes validadas y una cola de entrega reintentable.

## Configuración local

```golpecito
python3 -m venv .venv
fuente .venv/bin/activate
pip instalar poesía == 2.2.1
instalación de poesía -E dev
frasco de ejecución de poesía --app hanger_app:create_app run --debug
```

Los datos de desarrollo se almacenan en `instancia/`. La producción requiere
`HANGER_SECRET_KEY`, `HANGER_DB_PATH`, `HANGER_UPLOAD_DIR`,
`HANGER_PUBLIC_URL`, `HANGER_REQUIRE_INVITATION` y
`HANGER_MAX_UPLOAD_BYTES`. Configure las credenciales SMTP o Twilio antes
Procesamiento de trabajos de entrega. SQLite y los archivos cargados deben vivir en el mismo
volumen persistente; Este perfil de implementación está pensado para una única aplicación.
anfitrión.

```golpecito
frasco de ejecución de poesía --app hanger_app:create_app db-upgrade
frasco de ejecución de poesía --app hanger_app:create_app create-admin
frasco de ejecución de poesía --app hanger_app:create_app procesos-jobs --watch
frasco de ejecución de poesía --app hanger_app:create_app settings-list
frasco de ejecución de poesía --app hanger_app:create_app settings-set eligibility.minimum_age 21
matraz de ejecución de poesía --app hanger_app:create_app programación-entrevista 1
frasco de ejecución de poesía --app hanger_app:create_app add-interview-note 1
matraz de ejecución de poesía --app hanger_app:create_app investigación-exportación
poesía ejecutar pytest -q
poesía ejecutar pruebas ruff check src
```

Los cambios de esquema pertenecen a archivos SQL numerados en `src/hanger_app/migrations/`.
El desarrollo los aplica automáticamente; La producción debe ejecutar `db-upgrade` una vez antes de la web.
los trabajadores comienzan. Cree el `Dockerfile` incluido para la implementación de Gunicorn. Salud
Las comprobaciones están disponibles en `/health/live` y `/health/ready`.

La configuración por instalación se almacena en SQLite y se administra con el
Comandos CLI `settings-list`, `settings-get` y `settings-set`. Apoyado
las configuraciones incluyen `branding.site_name`, `branding.support_contact`,
`branding.logo_url`, `elegibilidad.edad_mínima`,
`eligibility.allowed_contact_kinds` y `eligibility.application_prompt`.

Los comandos del flujo de trabajo de entrevistas permiten a los administradores programar entrevistas con los candidatos, asignarlas
# Percha

Hanger es una aplicación social basada en entrevistas creada con Flask. incluye
registro, inicio de sesión, recuperación de contraseña, invitaciones persistentes, mensajería,
publicaciones, cargas de imágenes validadas y una cola de entrega reintentable.

## Configuración local

```golpecito
python3 -m venv .venv
fuente .venv/bin/activate
pip instalar poesía == 2.2.1
instalación de poesía -E dev
frasco de ejecución de poesía --app hanger_app:create_app run --debug
```

Los datos de desarrollo se almacenan en `instancia/`. La producción requiere
`HANGER_SECRET_KEY`, `HANGER_DB_PATH`, `HANGER_UPLOAD_DIR`,
`HANGER_PUBLIC_URL`, `HANGER_REQUIRE_INVITATION` y
`HANGER_MAX_UPLOAD_BYTES`. Configure las credenciales SMTP o Twilio antes
Procesamiento de trabajos de entrega. SQLite y los archivos cargados deben vivir en el mismo
volumen persistente; Este perfil de implementación está pensado para una única aplicación.
anfitrión.

```golpecito
frasco de ejecución de poesía --app hanger_app:create_app db-upgrade
frasco de ejecución de poesía --app hanger_app:create_app create-admin
frasco de ejecución de poesía --app hanger_app:create_app procesos-jobs --watch
frasco de ejecución de poesía --app hanger_app:create_app settings-list
frasco de ejecución de poesía --app hanger_app:create_app settings-set eligibility.minimum_age 21
matraz de ejecución de poesía --app hanger_app:create_app programación-entrevista 1
frasco de ejecución de poesía --app hanger_app:create_app add-interview-note 1
matraz de ejecución de poesía --app hanger_app:create_app investigación-exportación
poesía ejecutar pytest -q
poesía ejecutar pruebas ruff check src
```

Los cambios de esquema pertenecen a archivos SQL numerados en `src/hanger_app/migrations/`.
El desarrollo los aplica automáticamente; La producción debe ejecutar `db-upgrade` una vez antes de la web.
los trabajadores comienzan. Cree el `Dockerfile` incluido para la implementación de Gunicorn. Salud
Las comprobaciones están disponibles en `/health/live` y `/health/ready`.

La configuración por instalación se almacena en SQLite y se administra con el
Comandos CLI `settings-list`, `settings-get` y `settings-set`. Apoyado
las configuraciones incluyen `branding.site_name`, `branding.support_contact`,
`branding.logo_url`, `elegibilidad.edad_mínima`,
`eligibility.allowed_contact_kinds` y `eligibility.application_prompt`.

Los comandos del flujo de trabajo de entrevistas permiten a los administradores programar entrevistas con los candidatos, asignarlas
los entrevistadores registran notas estructuradas y los mantenedores exportan investigaciones agregadas
métricas sin exponer el texto de la nota privada de forma predeterminada.
# Cintre

Hanger est une application sociale sécurisée pour les entretiens, construite avec Flask. Il comprend
inscription, connexion, récupération de mot de passe, invitations persistantes, messagerie,
publications, téléchargements d'images validés et file d'attente de livraison réessayable.

## Configuration locale

```bash
python3 -m venv .venv
source .venv/bin/activer
pip installer la poésie == 2.2.1
poésie installer -E dev
flacon d'exécution de poésie --app hanger_app:create_app run --debug
```

Les données de développement sont stockées sous `instance/`. La production nécessite
`HANGER_SECRET_KEY`, `HANGER_DB_PATH`, `HANGER_UPLOAD_DIR`,
`HANGER_PUBLIC_URL`, `HANGER_REQUIRE_INVITATION` et
`HANGER_MAX_UPLOAD_BYTES`. Configurez les informations d'identification SMTP ou Twilio avant
traiter les tâches de livraison. SQLite et les fichiers téléchargés doivent vivre sur le même
volume persistant; ce profil de déploiement est destiné à une seule application
hôte.

```bash
flacon d'exécution de poésie --app hanger_app:create_app db-upgrade
flacon de poésie --app hanger_app:create_app create-admin
flacon d'exécution de poésie --app hanger_app:create_app process-jobs --watch
flacon de poésie --app hanger_app: create_app settings-list
flacon de poésie --app hanger_app:create_app settings-set éligible.minimum_age 21
flacon d'exécution de poésie --app hanger_app:create_app planning-interview 1
flacon de poésie --app hanger_app:create_app add-interview-note 1
flacon de poésie --app hanger_app:create_app recherche-exportation
poésie exécuter pytest -q
poésie exécuter ruff vérifier les tests src
```

Les modifications de schéma appartiennent aux fichiers SQL numérotés sous `src/hanger_app/migrations/`.
Le développement les applique automatiquement ; la production doit exécuter `db-upgrade` une fois avant le Web
les ouvriers démarrent. Créez le « Dockerfile » inclus pour le déploiement de Gunicorn. Santé
les contrôles sont disponibles sur `/health/live` et `/health/ready`.

Les paramètres par installation sont stockés dans SQLite et gérés avec le
Commandes CLI `settings-list`, `settings-get` et `settings-set`. Pris en charge
les paramètres incluent `branding.site_name`, `branding.support_contact`,
`branding.logo_url`, `eligibility.minimum_age`,
`eligibility.allowed_contact_kinds` et `eligibility.application_prompt`.

Les commandes du workflow d'entretien permettent aux administrateurs de planifier des entretiens avec les candidats, attribués
# Cintre

Hanger est une application sociale sécurisée pour les entretiens, construite avec Flask. Il comprend
inscription, connexion, récupération de mot de passe, invitations persistantes, messagerie,
publications, téléchargements d'images validés et file d'attente de livraison réessayable.

## Configuration locale

```bash
python3 -m venv .venv
source .venv/bin/activer
pip installer la poésie == 2.2.1
poésie installer -E dev
flacon d'exécution de poésie --app hanger_app:create_app run --debug
```

Les données de développement sont stockées sous `instance/`. La production nécessite
`HANGER_SECRET_KEY`, `HANGER_DB_PATH`, `HANGER_UPLOAD_DIR`,
`HANGER_PUBLIC_URL`, `HANGER_REQUIRE_INVITATION` et
`HANGER_MAX_UPLOAD_BYTES`. Configurez les informations d'identification SMTP ou Twilio avant
traiter les tâches de livraison. SQLite et les fichiers téléchargés doivent vivre sur le même
volume persistant; ce profil de déploiement est destiné à une seule application
hôte.

```bash
flacon d'exécution de poésie --app hanger_app:create_app db-upgrade
flacon de poésie --app hanger_app:create_app create-admin
flacon d'exécution de poésie --app hanger_app:create_app process-jobs --watch
flacon de poésie --app hanger_app: create_app settings-list
flacon de poésie --app hanger_app:create_app settings-set éligible.minimum_age 21
flacon d'exécution de poésie --app hanger_app:create_app planning-interview 1
flacon de poésie --app hanger_app:create_app add-interview-note 1
flacon de poésie --app hanger_app:create_app recherche-exportation
poésie exécuter pytest -q
poésie exécuter ruff vérifier les tests src
```

Les modifications de schéma appartiennent aux fichiers SQL numérotés sous `src/hanger_app/migrations/`.
Le développement les applique automatiquement ; la production doit exécuter `db-upgrade` une fois avant le Web
les ouvriers démarrent. Créez le « Dockerfile » inclus pour le déploiement de Gunicorn. Santé
les contrôles sont disponibles sur `/health/live` et `/health/ready`.

Les paramètres par installation sont stockés dans SQLite et gérés avec le
Commandes CLI `settings-list`, `settings-get` et `settings-set`. Pris en charge
les paramètres incluent `branding.site_name`, `branding.support_contact`,
`branding.logo_url`, `eligibility.minimum_age`,
`eligibility.allowed_contact_kinds` et `eligibility.application_prompt`.

Les commandes du workflow d'entretien permettent aux administrateurs de planifier des entretiens avec les candidats, attribués
les enquêteurs enregistrent des notes structurées et les responsables exportent la recherche globale
métriques sans exposer le texte de la note privée par défaut.
# Kleiderbügel

Hanger ist eine interviewgesteuerte soziale Anwendung, die mit Flask erstellt wurde. Es beinhaltet
Registrierung, Login, Passwortwiederherstellung, dauerhafte Einladungen, Messaging,
Beiträge, validierte Bild-Uploads und eine wiederholbare Zustellungswarteschlange.

## Lokale Einrichtung

„Bash
python3 -m venv .venv
Quelle .venv/bin/activate
pip install poet==2.2.1
Poesie install -E dev
Poesie run flask --app hanger_app:create_app run --debug
„

Entwicklungsdaten werden unter „instance/“ gespeichert. Produktion erfordert
„HANGER_SECRET_KEY“, „HANGER_DB_PATH“, „HANGER_UPLOAD_DIR“,
„HANGER_PUBLIC_URL“, „HANGER_REQUIRE_INVITATION“ und
„HANGER_MAX_UPLOAD_BYTES“. Konfigurieren Sie vorher SMTP- oder Twilio-Anmeldeinformationen
Bearbeitung von Lieferaufträgen. SQLite und hochgeladene Dateien müssen auf demselben Server gespeichert sein
anhaltendes Volumen; Dieses Bereitstellungsprofil ist für eine einzelne Anwendung gedacht
Gastgeber.

„Bash
poetic run flask --app hanger_app:create_app db-upgrade
Poetry run flask --app hanger_app:create_app create-admin
Poetry run flask --app hanger_app:create_app Process-Jobs --watch
poetic run flask --app hanger_app:create_app-Einstellungsliste
poetic run flask --app hanger_app:create_appsettings-set eligibility.minimum_age 21
poetic run flask --app hanger_app:create_app Schedule-Interview 1
poetic run flask --app hanger_app:create_app add-interview-note 1
Poetry run flask --app hanger_app:create_app Research-Export
Poesie führen Sie pytest -q aus
Poesie Run Ruff Check SRC-Tests
„

Schemaänderungen gehören in nummerierte SQL-Dateien unter „src/hanger_app/migrations/“.
Die Entwicklung wendet sie automatisch an; Die Produktion muss „db-upgrade“ einmal vor dem Web ausführen
Arbeiter beginnen. Erstellen Sie die mitgelieferte „Docker-Datei“ für die Gunicorn-Bereitstellung. Gesundheit
Prüfungen sind unter „/health/live“ und „/health/ready“ verfügbar.

Installationsspezifische Einstellungen werden in SQLite gespeichert und mit verwaltet
„settings-list“, „settings-get“ und „settings-set“ CLI-Befehle. Unterstützt
Zu den Einstellungen gehören „branding.site_name“, „branding.support_contact“,
`branding.logo_url`, `eligibility.minimum_age`,
„eligibility.allowed_contact_kinds“ und „eligibility.application_prompt“.

Mithilfe von Interview-Workflow-Befehlen können Administratoren zugewiesene Bewerberinterviews planen
# Kleiderbügel

Hanger ist eine interviewgesteuerte soziale Anwendung, die mit Flask erstellt wurde. Es beinhaltet
Registrierung, Login, Passwortwiederherstellung, dauerhafte Einladungen, Messaging,
Beiträge, validierte Bild-Uploads und eine wiederholbare Zustellungswarteschlange.

## Lokale Einrichtung

„Bash
python3 -m venv .venv
Quelle .venv/bin/activate
pip install poet==2.2.1
Poesie install -E dev
Poesie run flask --app hanger_app:create_app run --debug
„

Entwicklungsdaten werden unter „instance/“ gespeichert. Produktion erfordert
„HANGER_SECRET_KEY“, „HANGER_DB_PATH“, „HANGER_UPLOAD_DIR“,
„HANGER_PUBLIC_URL“, „HANGER_REQUIRE_INVITATION“ und
„HANGER_MAX_UPLOAD_BYTES“. Konfigurieren Sie vorher SMTP- oder Twilio-Anmeldeinformationen
Bearbeitung von Lieferaufträgen. SQLite und hochgeladene Dateien müssen auf demselben Server gespeichert sein
anhaltendes Volumen; Dieses Bereitstellungsprofil ist für eine einzelne Anwendung gedacht
Gastgeber.

„Bash
poetic run flask --app hanger_app:create_app db-upgrade
Poetry run flask --app hanger_app:create_app create-admin
Poetry run flask --app hanger_app:create_app Process-Jobs --watch
poetic run flask --app hanger_app:create_app-Einstellungsliste
poetic run flask --app hanger_app:create_appsettings-set eligibility.minimum_age 21
poetic run flask --app hanger_app:create_app Schedule-Interview 1
poetic run flask --app hanger_app:create_app add-interview-note 1
Poetry run flask --app hanger_app:create_app Research-Export
Poesie führen Sie pytest -q aus
Poesie Run Ruff Check SRC-Tests
„

Schemaänderungen gehören in nummerierte SQL-Dateien unter „src/hanger_app/migrations/“.
Die Entwicklung wendet sie automatisch an; Die Produktion muss „db-upgrade“ einmal vor dem Web ausführen
Arbeiter beginnen. Erstellen Sie die mitgelieferte „Docker-Datei“ für die Gunicorn-Bereitstellung. Gesundheit
Prüfungen sind unter „/health/live“ und „/health/ready“ verfügbar.

Installationsspezifische Einstellungen werden in SQLite gespeichert und mit verwaltet
„settings-list“, „settings-get“ und „settings-set“ CLI-Befehle. Unterstützt
Zu den Einstellungen gehören „branding.site_name“, „branding.support_contact“,
`branding.logo_url`, `eligibility.minimum_age`,
„eligibility.allowed_contact_kinds“ und „eligibility.application_prompt“.

Mithilfe von Interview-Workflow-Befehlen können Administratoren zugewiesene Bewerberinterviews planen
Interviewer zeichnen strukturierte Notizen auf und Betreuer exportieren aggregierte Forschungsergebnisse
Metriken ohne standardmäßige Offenlegung privater Notiztexte.
# ハンガー

Hanger は、Flask で構築されたインタビューゲート型ソーシャル アプリケーションです。それには以下が含まれます
登録、ログイン、パスワード回復、永続的な招待、メッセージング、
投稿、検証された画像のアップロード、再試行可能な配信キュー。

## ローカルセットアップ

「」バッシュ
python3 -m venv .venv
ソース .venv/bin/activate
pip 詩をインストール==2.2.1
詩のインストール -E dev
詩の実行フラスコ --app ハンガー_app:create_app 実行 --debug
「」

開発データは「instance/」配下に保存されます。生産に必要なもの
`HANGER_SECRET_KEY`、`HANGER_DB_PATH`、`HANGER_UPLOAD_DIR`、
`HANGER_PUBLIC_URL`、`HANGER_REQUIRE_INVITATION`、および
「HANGER_MAX_UPLOAD_BYTES」。前に SMTP または Twilio 資格情報を構成します
配送ジョブの処理。 SQLite とアップロードされたファイルは同じ場所に存在する必要があります
永続ボリューム。この展開プロファイルは単一のアプリケーションを対象としています
ホスト。

「」バッシュ
詩の実行フラスコ --app Hanger_app:create_app db-upgrade
詩を実行するフラスコ --app Hanger_app:create_app create-admin
詩を実行するフラスコ --app Hanger_app:create_app process-jobs --watch
詩を実行するフラスコ --app Hanger_app:create_app settings-list
詩の実行フラスコ --app ハンガー_app:create_app 設定-資格の設定.minimum_age 21
詩実行フラスコ --app ハンガー_app:create_app スケジュール-インタビュー 1
詩を実行するフラスコ --app Hanger_app:create_app add-interview-note 1
詩を実行するフラスコ --app Hanger_app:create_app Research-Export
詩を実行 pytest -q
詩を実行する ruff チェック src テスト
「」

スキーマの変更は、`src/hanger_app/migrations/` の下にある番号付きの SQL ファイルに属します。
開発はそれらを自動的に適用します。本番環境では Web の前に `db-upgrade` を 1 回実行する必要があります
労働者が始める。 Gunicorn デプロイメント用に含まれている `Dockerfile` をビルドします。健康
チェックは `/health/live` および `/health/ready` で利用できます。

インストールごとの設定は SQLite に保存され、
`settings-list`、`settings-get`、および `settings-set` CLI コマンド。サポートされています
設定には `branding.site_name`、`branding.support_contact`、
`branding.logo_url`、`eligibility.minimum_age`、
「eligibility.allowed_contact_kinds」および「eligibility.application_prompt」。

面接ワークフロー コマンドを使用すると、管理者は割り当てられた応募者の面接をスケジュールできます。
# ハンガー

Hanger は、Flask で構築されたインタビューゲート型ソーシャル アプリケーションです。それには以下が含まれます
登録、ログイン、パスワード回復、永続的な招待、メッセージング、
投稿、検証された画像のアップロード、再試行可能な配信キュー。

## ローカルセットアップ

「」バッシュ
python3 -m venv .venv
ソース .venv/bin/activate
pip 詩をインストール==2.2.1
詩のインストール -E dev
詩の実行フラスコ --app ハンガー_app:create_app 実行 --debug
「」

開発データは「instance/」配下に保存されます。生産に必要なもの
`HANGER_SECRET_KEY`、`HANGER_DB_PATH`、`HANGER_UPLOAD_DIR`、
`HANGER_PUBLIC_URL`、`HANGER_REQUIRE_INVITATION`、および
「HANGER_MAX_UPLOAD_BYTES」。前に SMTP または Twilio 資格情報を構成します
配送ジョブの処理。 SQLite とアップロードされたファイルは同じ場所に存在する必要があります
永続ボリューム。この展開プロファイルは単一のアプリケーションを対象としています
ホスト。

「」バッシュ
詩の実行フラスコ --app Hanger_app:create_app db-upgrade
詩を実行するフラスコ --app Hanger_app:create_app create-admin
詩を実行するフラスコ --app Hanger_app:create_app process-jobs --watch
詩を実行するフラスコ --app Hanger_app:create_app settings-list
詩の実行フラスコ --app ハンガー_app:create_app 設定-資格の設定.minimum_age 21
詩実行フラスコ --app ハンガー_app:create_app スケジュール-インタビュー 1
詩を実行するフラスコ --app Hanger_app:create_app add-interview-note 1
詩を実行するフラスコ --app Hanger_app:create_app Research-Export
詩を実行 pytest -q
詩を実行する ruff チェック src テスト
「」

スキーマの変更は、`src/hanger_app/migrations/` の下にある番号付きの SQL ファイルに属します。
開発はそれらを自動的に適用します。本番環境では Web の前に `db-upgrade` を 1 回実行する必要があります
労働者が始める。 Gunicorn デプロイメント用に含まれている `Dockerfile` をビルドします。健康
チェックは `/health/live` および `/health/ready` で利用できます。

インストールごとの設定は SQLite に保存され、
`settings-list`、`settings-get`、および `settings-set` CLI コマンド。サポートされています
設定には `branding.site_name`、`branding.support_contact`、
`branding.logo_url`、`eligibility.minimum_age`、
「eligibility.allowed_contact_kinds」および「eligibility.application_prompt」。

面接ワークフロー コマンドを使用すると、管理者は割り当てられた応募者の面接をスケジュールできます。
インタビュアーは構造化されたメモを記録し、管理者は集計された調査結果をエクスポートします
デフォルトでは非公開のメモテキストを公開せずにメトリクスを表示します。
# 衣架

Hanger 是一款使用 Flask 构建的面试门禁社交应用程序。它包括
注册、登录、密码恢复、持久邀请、消息传递、
帖子、经过验证的图像上传和可重试的传送队列。

## 本地设置

````bash
python3 -m venv .venv
源 .venv/bin/activate
pip 安装诗歌==2.2.1
诗歌安装-E dev
诗歌运行烧瓶--apphanger_app：create_app运行--debug
````

开发数据存储在“instance/”下。生产要求
`HANGER_SECRET_KEY`、`HANGER_DB_PATH`、`HANGER_UPLOAD_DIR`、
`HANGER_PUBLIC_URL`、`HANGER_REQUIRE_INVITATION` 和
`HANGER_MAX_UPLOAD_BYTES`。之前配置 SMTP 或 Twilio 凭据
处理送货作业。 SQLite 和上传的文件必须位于同一目录下
持久量；此部署配置文件适用于单个应用程序
主机。

````bash
诗歌运行烧瓶 --apphanger_app:create_app db-upgrade
诗歌运行烧瓶 --apphanger_app:create_app create-admin
诗歌运行烧瓶--apphanger_app：create_app进程作业--watch
诗歌运行烧瓶 --apphanger_app:create_app 设置列表
诗歌运行烧瓶--apphanger_app：create_app设置-设置资格.最低年龄21
诗歌运行烧瓶 --apphanger_app:create_app 日程安排面试 1
诗歌运行烧瓶 --apphanger_app:create_app add-interview-note 1
诗歌运行烧瓶 --apphanger_app:create_app 研究导出
诗歌运行 pytest -q
诗歌运行 ruff 检查 src 测试
````

架构更改属于“src/hanger_app/migrations/”下的编号 SQL 文件。
开发自动应用它们；生产环境必须在 Web 之前运行一次“db-upgrade”
工人们开始。构建用于 Gunicorn 部署的包含的“Dockerfile”。健康
检查可在“/health/live”和“/health/ready”处进行。

每次安装的设置存储在 SQLite 中并通过以下命令进行管理
`settings-list`、`settings-get` 和 `settings-set` CLI 命令。支持
设置包括“branding.site_name”、“branding.support_contact”、
`branding.logo_url`、`eligibility.minimum_age`、
`eligibility.allowed_contact_kinds` 和 `eligibility.application_prompt`。

面试工作流程命令让管理员可以安排申请人面试、分配
# 衣架

Hanger 是一款使用 Flask 构建的面试门禁社交应用程序。它包括
注册、登录、密码恢复、持久邀请、消息传递、
帖子、经过验证的图像上传和可重试的传送队列。

## 本地设置

````bash
python3 -m venv .venv
源 .venv/bin/activate
pip 安装诗歌==2.2.1
诗歌安装-E dev
诗歌运行烧瓶--apphanger_app：create_app运行--debug
````

开发数据存储在“instance/”下。生产要求
`HANGER_SECRET_KEY`、`HANGER_DB_PATH`、`HANGER_UPLOAD_DIR`、
`HANGER_PUBLIC_URL`、`HANGER_REQUIRE_INVITATION` 和
`HANGER_MAX_UPLOAD_BYTES`。之前配置 SMTP 或 Twilio 凭据
处理送货作业。 SQLite 和上传的文件必须位于同一目录下
持久量；此部署配置文件适用于单个应用程序
主机。

````bash
诗歌运行烧瓶 --apphanger_app:create_app db-upgrade
诗歌运行烧瓶 --apphanger_app:create_app create-admin
诗歌运行烧瓶--apphanger_app：create_app进程作业--watch
诗歌运行烧瓶 --apphanger_app:create_app 设置列表
诗歌运行烧瓶--apphanger_app：create_app设置-设置资格.最低年龄21
诗歌运行烧瓶 --apphanger_app:create_app 日程安排面试 1
诗歌运行烧瓶 --apphanger_app:create_app add-interview-note 1
诗歌运行烧瓶 --apphanger_app:create_app 研究导出
诗歌运行 pytest -q
诗歌运行 ruff 检查 src 测试
````

架构更改属于“src/hanger_app/migrations/”下的编号 SQL 文件。
开发自动应用它们；生产环境必须在 Web 之前运行一次“db-upgrade”
工人们开始。构建用于 Gunicorn 部署的包含的“Dockerfile”。健康
检查可在“/health/live”和“/health/ready”处进行。

每次安装的设置存储在 SQLite 中并通过以下命令进行管理
`settings-list`、`settings-get` 和 `settings-set` CLI 命令。支持
设置包括“branding.site_name”、“branding.support_contact”、
`branding.logo_url`、`eligibility.minimum_age`、
`eligibility.allowed_contact_kinds` 和 `eligibility.application_prompt`。

面试工作流程命令让管理员可以安排申请人面试、分配
采访者记录结构化笔记，维护者输出汇总研究
默认情况下不暴露私人注释文本的指标。
# Вішалка

Hanger — це соціальна програма, створена за допомогою Flask. Він включає в себе
реєстрація, вхід, відновлення пароля, постійні запрошення, обмін повідомленнями,
публікації, перевірені завантаження зображень і чергу доставки з можливістю повторної спроби.

## Локальні налаштування

```баш
python3 -m venv .venv
джерело .venv/bin/activate
pip install poetry==2.2.1
poetry install -E dev
poetry run flask --app hanger_app:create_app run --debug
```

Дані розробки зберігаються в папці `instance/`. Виробництво вимагає
`HANGER_SECRET_KEY`, `HANGER_DB_PATH`, `HANGER_UPLOAD_DIR`,
`HANGER_PUBLIC_URL`, `HANGER_REQUIRE_INVITATION` і
`HANGER_MAX_UPLOAD_BYTES`. Налаштуйте облікові дані SMTP або Twilio раніше
обробка завдань доставки. SQLite та завантажені файли мають існувати в одному місці
стійкий обсяг; цей профіль розгортання призначений для однієї програми
хост.

```баш
poetry run flask --app hanger_app:create_app db-upgrade
poetry run flask --app hanger_app:create_app create-admin
poetry run flask --app hanger_app:create_app process-jobs --watch
poetry run flask --app hanger_app:create_app settings-list
poetry run flask --app hanger_app:create_app settings-set eligibility.minimum_age 21
poetry run flask --app hanger_app:create_app schedule-interview 1
poetry run flask --app hanger_app:create_app add-interview-note 1
poetry run flask --app hanger_app:create_app research-export
поетичний біг pytest -q
poetry run ruff check src tests
```

Зміни схеми належать до пронумерованих файлів SQL у розділі `src/hanger_app/migrations/`.
Розробка застосовує їх автоматично; production має запустити `db-upgrade` один раз перед веб
починають робітники. Створіть включений `Dockerfile` для розгортання Gunicorn. Здоров'я
перевірки доступні за адресами `/health/live` і `/health/ready`.

Параметри інсталяції зберігаються в SQLite і керуються за допомогою
Команди CLI `settings-list`, `settings-get` і `settings-set`. Підтримується
налаштування включають `branding.site_name`, `branding.support_contact`,
`branding.logo_url`, `eligibility.minimum_age`,
`eligibility.allowed_contact_kinds` і `eligibility.application_prompt`.

Команди робочого циклу співбесід дозволяють адміністраторам планувати співбесіди з кандидатами, призначені
# Вішалка

Hanger — це соціальна програма, створена за допомогою Flask. Він включає в себе
реєстрація, вхід, відновлення пароля, постійні запрошення, обмін повідомленнями,
публікації, перевірені завантаження зображень і чергу доставки з можливістю повторної спроби.

## Локальні налаштування

```баш
python3 -m venv .venv
джерело .venv/bin/activate
pip install poetry==2.2.1
poetry install -E dev
poetry run flask --app hanger_app:create_app run --debug
```

Дані розробки зберігаються в папці `instance/`. Виробництво вимагає
`HANGER_SECRET_KEY`, `HANGER_DB_PATH`, `HANGER_UPLOAD_DIR`,
`HANGER_PUBLIC_URL`, `HANGER_REQUIRE_INVITATION` і
`HANGER_MAX_UPLOAD_BYTES`. Налаштуйте облікові дані SMTP або Twilio раніше
обробка завдань доставки. SQLite та завантажені файли мають існувати в одному місці
стійкий обсяг; цей профіль розгортання призначений для однієї програми
хост.

```баш
poetry run flask --app hanger_app:create_app db-upgrade
poetry run flask --app hanger_app:create_app create-admin
poetry run flask --app hanger_app:create_app process-jobs --watch
poetry run flask --app hanger_app:create_app settings-list
poetry run flask --app hanger_app:create_app settings-set eligibility.minimum_age 21
poetry run flask --app hanger_app:create_app schedule-interview 1
poetry run flask --app hanger_app:create_app add-interview-note 1
poetry run flask --app hanger_app:create_app research-export
поетичний біг pytest -q
poetry run ruff check src tests
```

Зміни схеми належать до пронумерованих файлів SQL у розділі `src/hanger_app/migrations/`.
Розробка застосовує їх автоматично; production має запустити `db-upgrade` один раз перед веб
починають робітники. Створіть включений `Dockerfile` для розгортання Gunicorn. Здоров'я
перевірки доступні за адресами `/health/live` і `/health/ready`.

Параметри інсталяції зберігаються в SQLite і керуються за допомогою
Команди CLI `settings-list`, `settings-get` і `settings-set`. Підтримується
налаштування включають `branding.site_name`, `branding.support_contact`,
`branding.logo_url`, `eligibility.minimum_age`,
`eligibility.allowed_contact_kinds` і `eligibility.application_prompt`.

Команди робочого циклу співбесід дозволяють адміністраторам планувати співбесіди з кандидатами, призначені
інтерв'юери записують структуровані нотатки, а супроводжувачі експортують зведені дослідження
метрики, не розкриваючи текст приватної нотатки за замовчуванням.
# Вешалка

Hanger — это социальное приложение для собеседований, созданное с помощью Flask. Он включает в себя
регистрация, вход, восстановление пароля, постоянные приглашения, обмен сообщениями,
публикации, проверенные загрузки изображений и очередь доставки с возможностью повторной попытки.

## Локальная настройка

``` баш
python3 -m венв .venv
источник .venv/bin/activate
пип установить поэзию == 2.2.1
установка поэзии -E dev
поэзия запустить колбу --app Hanger_app:create_app запустить --debug
```

Данные разработки хранятся в папке `instance/`. Производство требует
`HANGER_SECRET_KEY`, `HANGER_DB_PATH`, `HANGER_UPLOAD_DIR`,
HANGER_PUBLIC_URL, HANGER_REQUIRE_INVITATION и
`HANGER_MAX_UPLOAD_BYTES`. Перед этим настройте учетные данные SMTP или Twilio.
обработка заказов на доставку. SQLite и загруженные файлы должны находиться в одном и том же месте.
постоянный объем; этот профиль развертывания предназначен для одного приложения
хозяин.

``` баш
поэзия запустить колбу --app Hanger_app:create_app db-upgrade
поэзия запустить колбу --app Hanger_app:create_app create-admin
поэзия запустить колбу --app Hanger_app:create_app процесс-задания --watch
поэзия запускает колбу --app Hanger_app:create_app settings-list
flask запуска поэзии --app Hanger_app:create_app settings-set eligibility.minimum_age 21
поэзия запускает колбу --app Hanger_app:create_app Schedule-Interview 1
поэзия запускает колбу --app Hanger_app:create_app add-interview-note 1
поэзия запускает колбу --app Hanger_app:create_app Research-Export
поэзия запустить pytest -q
поэзия беги ерш проверка src тесты
```

Изменения схемы хранятся в пронумерованных файлах SQL в папке `src/hanger_app/migrations/`.
Разработка применяет их автоматически; производство должно запустить `db-upgrade` один раз, прежде чем веб-версия
рабочие начинают. Создайте включенный файл Dockerfile для развертывания Gunicorn. Здоровье
проверки доступны в каталогах `/health/live` и `/health/ready`.

Настройки для каждой установки хранятся в SQLite и управляются с помощью
Команды CLI `settings-list`, `settings-get` и `settings-set`. Поддерживается
настройки включают `branding.site_name`, `branding.support_contact`,
`branding.logo_url`, `eligibility.minimum_age`,
`eligibility.allowed_contact_kinds` и `eligibility.application_prompt`.

Команды рабочего процесса собеседования позволяют администраторам планировать собеседования с кандидатами, назначенные