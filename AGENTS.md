# Repository Guidelines

## Project Structure & Module Organization

Python application code lives in `src/hanger_app/`. `__init__.py` owns the Flask factory, `routes.py` handles HTTP, `services.py` contains use cases, and `repositories.py` isolates SQLite. Versioned schema files live in `src/hanger_app/migrations/`; Jinja templates live in `src/hanger_app/templates/`. `src/hanger.py` and `src/loader.py` are compatibility entry points. Tests live in `tests/`. Agent instructions are stored in `.agents/skills/`, with installed versions recorded in `skills-lock.json`.

## Build, Test, and Development Commands

Create an isolated environment before installing dependencies:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install poetry==2.2.1
poetry install -E dev
```

Run the main application from the repository root:

```bash
poetry run flask --app hanger_app:create_app run --debug
```

Run `poetry run flask --app hanger_app:create_app process-jobs --watch` to process queued deliveries. Use `poetry run python -m compileall -q src tests` as the minimum syntax check. Add schema changes as a new numbered file in `src/hanger_app/migrations/`; never rewrite an applied migration.

Use `poetry run flask --app hanger_app:create_app settings-list` and
`settings-set <key> <json-value>` to manage per-installation settings such as
`branding.site_name` or `eligibility.minimum_age`.
Use `schedule-interview`, `add-interview-note`, `list-interview-notes`, and
`research-export` for the applicant interview pipeline and sanitized research
metrics.

## Coding Style & Naming Conventions

Use four-space indentation and follow PEP 8. Name functions and variables with `snake_case`, classes with `PascalCase`, and constants with `UPPER_SNAKE_CASE`. Add type hints to public methods and route return values. Keep Flask route handlers small; move reusable behavior into `src/hanger_app/services.py`. Prefer `pathlib.Path` and repository-relative paths instead of hard-coded locations. Never interpolate user input into SQL or HTML.

## Testing Guidelines

Add new tests under `tests/`, mirroring the source layout. Name files `test_<module>.py` and test functions `test_<behavior>()`. Run `poetry run pytest -q --cov=hanger_app` and the compile check before submitting. Route changes should cover successful requests, authorization failures, invalid data, and expected status codes.

## Commit & Pull Request Guidelines

History uses short, imperative, title-cased subjects such as `Fix Login Validation` or `Add User Loader`. Keep each commit focused. Pull requests must explain the problem, root cause, user impact, and validation performed. Link relevant issues and include screenshots for changes under `pages/`. Do not mix generated files, credentials, local databases, or unrelated refactors into a PR.
# Directrices del repositorio

## Estructura del proyecto y organización del módulo

El código de la aplicación Python se encuentra en `src/hanger_app/`. `__init__.py` posee la fábrica Flask, `routes.py` maneja HTTP, `services.py` contiene casos de uso y `repositories.py` aísla SQLite. Los archivos de esquema versionados se encuentran en `src/hanger_app/migrations/`; Las plantillas de Jinja se encuentran en `src/hanger_app/templates/`. `src/hanger.py` y `src/loader.py` son puntos de entrada de compatibilidad. Las pruebas se encuentran en `pruebas/`. Las instrucciones del agente se almacenan en `.agents/skills/`, con las versiones instaladas registradas en `skills-lock.json`.

## Comandos de compilación, prueba y desarrollo

Cree un entorno aislado antes de instalar dependencias:

```golpecito
python3 -m venv .venv
fuente .venv/bin/activate
pip instalar poesía == 2.2.1
instalación de poesía -E dev
```

Ejecute la aplicación principal desde la raíz del repositorio:

```golpecito
frasco de ejecución de poesía --app hanger_app:create_app run --debug
```

Ejecute `poetry run flask --app hanger_app:create_app Process-jobs --watch` para procesar las entregas en cola. Utilice `poetry run python -m compileall -q src tests` como verificación de sintaxis mínima. Agregue cambios de esquema como un nuevo archivo numerado en `src/hanger_app/migrations/`; nunca reescriba una migración aplicada.

Utilice `poetry run flask --app hanger_app:create_app settings-list` y
`settings-set <key> <json-value>` para administrar la configuración por instalación, como
`branding.site_name` o `eligibility.minimum_age`.
Utilice `programar-entrevista`, `agregar-nota-de-entrevista`, `listar-notas-de-entrevista` y
`investigación-exportación` para el proceso de entrevistas a los solicitantes y la investigación saneada
métricas.

## Estilo de codificación y convenciones de nomenclatura

Utilice sangría de cuatro espacios y siga PEP 8. Nombra funciones y variables con `snake_case`, clases con `PascalCase` y constantes con `UPPER_SNAKE_CASE`. Agregue sugerencias de tipo a métodos públicos y valores de retorno de ruta. Mantenga pequeños los manejadores de rutas de Flask; mueva el comportamiento reutilizable a `src/hanger_app/services.py`. Prefiera `pathlib.Path` y rutas relativas al repositorio en lugar de ubicaciones codificadas. Nunca interpolar la entrada del usuario en SQL o HTML.

## Pautas de prueba

Agregue nuevas pruebas en `tests/`, reflejando el diseño de origen. Nombra los archivos `test_<módulo>.py` y las funciones de prueba `test_<comportamiento>()`. Ejecute `poetry run pytest -q --cov=hanger_app` y verifique la compilación antes de enviar. Los cambios de ruta deben cubrir solicitudes exitosas, fallas de autorización, datos no válidos y códigos de estado esperados.

## Pautas de solicitud de confirmación y extracción

El historial utiliza temas breves, imperativos y con títulos en mayúsculas, como "Reparar validación de inicio de sesión" o "Agregar cargador de usuario". Mantenga cada compromiso enfocado. Las solicitudes de extracción deben explicar el problema, la causa raíz, el impacto en el usuario y la validación realizada. Vincula problemas relevantes e incluye capturas de pantalla de los cambios en `páginas/`. No mezcle archivos generados, credenciales, bases de datos locales o refactores no relacionados en un PR.
# Directrices del repositorio

## Estructura del proyecto y organización del módulo

El código de la aplicación Python se encuentra en `src/hanger_app/`. `__init__.py` posee la fábrica Flask, `routes.py` maneja HTTP, `services.py` contiene casos de uso y `repositories.py` aísla SQLite. Los archivos de esquema versionados se encuentran en `src/hanger_app/migrations/`; Las plantillas de Jinja se encuentran en `src/hanger_app/templates/`. `src/hanger.py` y `src/loader.py` son puntos de entrada de compatibilidad. Las pruebas se encuentran en `pruebas/`. Las instrucciones del agente se almacenan en `.agents/skills/`, con las versiones instaladas registradas en `skills-lock.json`.

## Comandos de compilación, prueba y desarrollo

Cree un entorno aislado antes de instalar dependencias:

```golpecito
python3 -m venv .venv
fuente .venv/bin/activate
pip instalar poesía == 2.2.1
instalación de poesía -E dev
```

Ejecute la aplicación principal desde la raíz del repositorio:

```golpecito
frasco de ejecución de poesía --app hanger_app:create_app run --debug
```

Ejecute `poetry run flask --app hanger_app:create_app Process-jobs --watch` para procesar las entregas en cola. Utilice `poetry run python -m compileall -q src tests` como verificación de sintaxis mínima. Agregue cambios de esquema como un nuevo archivo numerado en `src/hanger_app/migrations/`; nunca reescriba una migración aplicada.

Utilice `poetry run flask --app hanger_app:create_app settings-list` y
`settings-set <key> <json-value>` para administrar la configuración por instalación, como
`branding.site_name` o `eligibility.minimum_age`.
Utilice `programar-entrevista`, `agregar-nota-de-entrevista`, `listar-notas-de-entrevista` y
`investigación-exportación` para el proceso de entrevistas a los solicitantes y la investigación saneada
métricas.

## Estilo de codificación y convenciones de nomenclatura

Utilice sangría de cuatro espacios y siga PEP 8. Nombra funciones y variables con `snake_case`, clases con `PascalCase` y constantes con `UPPER_SNAKE_CASE`. Agregue sugerencias de tipo a métodos públicos y valores de retorno de ruta. Mantenga pequeños los manejadores de rutas de Flask; mueva el comportamiento reutilizable a `src/hanger_app/services.py`. Prefiera `pathlib.Path` y rutas relativas al repositorio en lugar de ubicaciones codificadas. Nunca interpolar la entrada del usuario en SQL o HTML.

## Pautas de prueba

Agregue nuevas pruebas en `tests/`, reflejando el diseño de origen. Nombra los archivos `test_<módulo>.py` y las funciones de prueba `test_<comportamiento>()`. Ejecute `poetry run pytest -q --cov=hanger_app` y verifique la compilación antes de enviar. Los cambios de ruta deben cubrir solicitudes exitosas, fallas de autorización, datos no válidos y códigos de estado esperados.

## Pautas de solicitud de confirmación y extracción

El historial utiliza temas breves, imperativos y con títulos en mayúsculas, como "Reparar validación de inicio de sesión" o "Agregar cargador de usuario". Mantenga cada compromiso enfocado. Las solicitudes de extracción deben explicar el problema, la causa raíz, el impacto en el usuario y la validación realizada. Vincula problemas relevantes e incluye capturas de pantalla de los cambios en `páginas/`. No mezcle archivos generados, credenciales, bases de datos locales o refactores no relacionados en un PR.
# Directives du référentiel

## Structure du projet et organisation des modules

Le code de l'application Python réside dans `src/hanger_app/`. `__init__.py` possède l'usine Flask, `routes.py` gère HTTP, `services.py` contient des cas d'utilisation et `repositories.py` isole SQLite. Les fichiers de schéma versionnés se trouvent dans `src/hanger_app/migrations/` ; Les modèles Jinja se trouvent dans `src/hanger_app/templates/`. `src/hanger.py` et `src/loader.py` sont des points d'entrée de compatibilité. Les tests vivent dans `tests/`. Les instructions de l'agent sont stockées dans `.agents/skills/`, avec les versions installées enregistrées dans `skills-lock.json`.

## Commandes de construction, de test et de développement

Créez un environnement isolé avant d'installer les dépendances :

```bash
python3 -m venv .venv
source .venv/bin/activer
pip installer la poésie == 2.2.1
poésie installer -E dev
```

Exécutez l'application principale à partir de la racine du référentiel :

```bash
flacon d'exécution de poésie --app hanger_app:create_app run --debug
```

Exécutez `poetry run flask --app hanger_app:create_app process-jobs --watch` pour traiter les livraisons en file d'attente. Utilisez `poetry run python -m compileall -q src tests` comme vérification de syntaxe minimale. Ajoutez les modifications de schéma en tant que nouveau fichier numéroté dans `src/hanger_app/migrations/` ; ne réécrivez jamais une migration appliquée.

Utilisez `poetry run flask --app hanger_app:create_app settings-list` et
`settings-set <key> <json-value>` pour gérer les paramètres par installation tels que
`branding.site_name` ou `eligibility.minimum_age`.
Utilisez `schedule-interview`, `add-interview-note`, `list-interview-notes` et
« recherche-exportation » pour le pipeline d'entretiens avec les candidats et la recherche aseptisée
métriques.

## Style de codage et conventions de dénomination

Utilisez l'indentation à quatre espaces et suivez la PEP 8. Nommez les fonctions et les variables avec `snake_case`, les classes avec `PascalCase` et les constantes avec `UPPER_SNAKE_CASE`. Ajoutez des indications de type aux méthodes publiques et acheminez les valeurs de retour. Gardez les gestionnaires de route Flask petits ; déplacez le comportement réutilisable dans `src/hanger_app/services.py`. Préférez `pathlib.Path` et les chemins relatifs au référentiel plutôt que les emplacements codés en dur. N'interpolez jamais les entrées de l'utilisateur dans SQL ou HTML.

## Directives de test

Ajoutez de nouveaux tests sous `tests/`, reflétant la disposition source. Nommez les fichiers `test_<module>.py` et testez les fonctions `test_<behavior>()`. Exécutez `poetry run pytest -q --cov=hanger_app` et la vérification de la compilation avant de soumettre. Les modifications d'itinéraire doivent couvrir les demandes réussies, les échecs d'autorisation, les données non valides et les codes d'état attendus.

## Directives de validation et de demande de tirage

L'historique utilise des sujets courts et impératifs avec des titres tels que « Corriger la validation de connexion » ou « Ajouter un chargeur d'utilisateur ». Gardez chaque engagement concentré. Les demandes d'extraction doivent expliquer le problème, la cause première, l'impact sur l'utilisateur et la validation effectuée. Liez les problèmes pertinents et incluez des captures d'écran pour les modifications sous « pages/ ». Ne mélangez pas les fichiers générés, les informations d'identification, les bases de données locales ou les refactors non liés dans un PR.
# Directives du référentiel

## Structure du projet et organisation des modules

Le code de l'application Python réside dans `src/hanger_app/`. `__init__.py` possède l'usine Flask, `routes.py` gère HTTP, `services.py` contient des cas d'utilisation et `repositories.py` isole SQLite. Les fichiers de schéma versionnés se trouvent dans `src/hanger_app/migrations/` ; Les modèles Jinja se trouvent dans `src/hanger_app/templates/`. `src/hanger.py` et `src/loader.py` sont des points d'entrée de compatibilité. Les tests vivent dans `tests/`. Les instructions de l'agent sont stockées dans `.agents/skills/`, avec les versions installées enregistrées dans `skills-lock.json`.

## Commandes de construction, de test et de développement

Créez un environnement isolé avant d'installer les dépendances :

```bash
python3 -m venv .venv
source .venv/bin/activer
pip installer la poésie == 2.2.1
poésie installer -E dev
```

Exécutez l'application principale à partir de la racine du référentiel :

```bash
flacon d'exécution de poésie --app hanger_app:create_app run --debug
```

Exécutez `poetry run flask --app hanger_app:create_app process-jobs --watch` pour traiter les livraisons en file d'attente. Utilisez `poetry run python -m compileall -q src tests` comme vérification de syntaxe minimale. Ajoutez les modifications de schéma en tant que nouveau fichier numéroté dans `src/hanger_app/migrations/` ; ne réécrivez jamais une migration appliquée.

Utilisez `poetry run flask --app hanger_app:create_app settings-list` et
`settings-set <key> <json-value>` pour gérer les paramètres par installation tels que
`branding.site_name` ou `eligibility.minimum_age`.
Utilisez `schedule-interview`, `add-interview-note`, `list-interview-notes` et
« recherche-exportation » pour le pipeline d'entretiens avec les candidats et la recherche aseptisée
métriques.

## Style de codage et conventions de dénomination

Utilisez l'indentation à quatre espaces et suivez la PEP 8. Nommez les fonctions et les variables avec `snake_case`, les classes avec `PascalCase` et les constantes avec `UPPER_SNAKE_CASE`. Ajoutez des indications de type aux méthodes publiques et acheminez les valeurs de retour. Gardez les gestionnaires de route Flask petits ; déplacez le comportement réutilisable dans `src/hanger_app/services.py`. Préférez `pathlib.Path` et les chemins relatifs au référentiel plutôt que les emplacements codés en dur. N'interpolez jamais les entrées de l'utilisateur dans SQL ou HTML.

## Directives de test

Ajoutez de nouveaux tests sous `tests/`, reflétant la disposition source. Nommez les fichiers `test_<module>.py` et testez les fonctions `test_<behavior>()`. Exécutez `poetry run pytest -q --cov=hanger_app` et la vérification de la compilation avant de soumettre. Les modifications d'itinéraire doivent couvrir les demandes réussies, les échecs d'autorisation, les données non valides et les codes d'état attendus.

## Directives de validation et de demande de tirage

L'historique utilise des sujets courts et impératifs avec des titres tels que « Corriger la validation de connexion » ou « Ajouter un chargeur d'utilisateur ». Gardez chaque engagement concentré. Les demandes d'extraction doivent expliquer le problème, la cause première, l'impact sur l'utilisateur et la validation effectuée. Liez les problèmes pertinents et incluez des captures d'écran pour les modifications sous « pages/ ». Ne mélangez pas les fichiers générés, les informations d'identification, les bases de données locales ou les refactors non liés dans un PR.
# Repository-Richtlinien

## Projektstruktur und Modulorganisation

Der Python-Anwendungscode befindet sich in „src/hanger_app/“. „__init__.py“ besitzt die Flask-Factory, „routes.py“ verarbeitet HTTP, „services.py“ enthält Anwendungsfälle und „repositories.py“ isoliert SQLite. Versionierte Schemadateien befinden sich in „src/hanger_app/migrations/“; Jinja-Vorlagen befinden sich in „src/hanger_app/templates/“. „src/hanger.py“ und „src/loader.py“ sind Kompatibilitätseinstiegspunkte. Tests leben in „tests/“. Agentenanweisungen werden in „.agents/skills/“ gespeichert, wobei installierte Versionen in „skills-lock.json“ aufgezeichnet werden.

## Build-, Test- und Entwicklungsbefehle

Erstellen Sie eine isolierte Umgebung, bevor Sie Abhängigkeiten installieren:

„Bash
python3 -m venv .venv
Quelle .venv/bin/activate
pip install poet==2.2.1
Poesie install -E dev
„

Führen Sie die Hauptanwendung im Repository-Stammverzeichnis aus:

„Bash
Poesie run flask --app hanger_app:create_app run --debug
„

Führen Sie „poetry run flask --app hanger_app:create_app Process-Jobs --watch“ aus, um Lieferungen in der Warteschlange zu verarbeiten. Verwenden Sie „poetry run python -m Compileall -q src Tests“ als minimale Syntaxprüfung. Schemaänderungen als neue nummerierte Datei in „src/hanger_app/migrations/“ hinzufügen; Schreiben Sie niemals eine angewandte Migration neu.

Verwenden Sie „poetry run flask --app hanger_app:create_appsettings-list“ und
„settings-set <key> <json-value>“ zum Verwalten pro Installationseinstellungen, z
„branding.site_name“ oder „eligibility.minimum_age“.
Verwenden Sie „Interview planen“, „Interview-Notiz hinzufügen“, „Interview-Notizen auflisten“ und
„Forschungsexport“ für die Bewerberinterview-Pipeline und bereinigte Recherche
Metriken.

## Codierungsstil und Namenskonventionen

Verwenden Sie eine Einrückung mit vier Leerzeichen und befolgen Sie PEP 8. Benennen Sie Funktionen und Variablen mit „snake_case“, Klassen mit „PascalCase“ und Konstanten mit „UPPER_SNAKE_CASE“. Fügen Sie Typhinweise zu öffentlichen Methoden hinzu und leiten Sie Rückgabewerte weiter. Halten Sie die Routenhandler von Flask klein; Verschieben Sie wiederverwendbares Verhalten nach „src/hanger_app/services.py“. Bevorzugen Sie „pathlib.Path“ und Repository-relative Pfade statt fest codierter Speicherorte. Interpolieren Sie niemals Benutzereingaben in SQL oder HTML.

## Testrichtlinien

Fügen Sie neue Tests unter „tests/“ hinzu und spiegeln Sie dabei das Quelllayout wider. Benennen Sie die Dateien „test_<module>.py“ und die Testfunktionen „test_<behavior>()“. Führen Sie vor dem Absenden „poetry run pytest -q --cov=hanger_app“ und die Kompilierungsprüfung aus. Routenänderungen sollten erfolgreiche Anfragen, Autorisierungsfehler, ungültige Daten und erwartete Statuscodes abdecken.

## Commit- und Pull-Request-Richtlinien

Der Verlauf verwendet kurze, zwingende Betreffzeilen in Groß- und Kleinschreibung wie „Anmeldevalidierung korrigieren“ oder „Benutzer-Loader hinzufügen“. Konzentrieren Sie sich bei jedem Commit. Pull-Anfragen müssen das Problem, die Grundursache, die Auswirkungen auf den Benutzer und die durchgeführte Validierung erläutern. Verknüpfen Sie relevante Probleme und fügen Sie Screenshots für Änderungen unter „Seiten/“ ein. Mischen Sie keine generierten Dateien, Anmeldeinformationen, lokalen Datenbanken oder nicht verwandte Refaktoren in einem PR.
# Repository-Richtlinien

## Projektstruktur und Modulorganisation

Der Python-Anwendungscode befindet sich in „src/hanger_app/“. „__init__.py“ besitzt die Flask-Factory, „routes.py“ verarbeitet HTTP, „services.py“ enthält Anwendungsfälle und „repositories.py“ isoliert SQLite. Versionierte Schemadateien befinden sich in „src/hanger_app/migrations/“; Jinja-Vorlagen befinden sich in „src/hanger_app/templates/“. „src/hanger.py“ und „src/loader.py“ sind Kompatibilitätseinstiegspunkte. Tests leben in „tests/“. Agentenanweisungen werden in „.agents/skills/“ gespeichert, wobei installierte Versionen in „skills-lock.json“ aufgezeichnet werden.

## Build-, Test- und Entwicklungsbefehle

Erstellen Sie eine isolierte Umgebung, bevor Sie Abhängigkeiten installieren:

„Bash
python3 -m venv .venv
Quelle .venv/bin/activate
pip install poet==2.2.1
Poesie install -E dev
„

Führen Sie die Hauptanwendung im Repository-Stammverzeichnis aus:

„Bash
Poesie run flask --app hanger_app:create_app run --debug
„

Führen Sie „poetry run flask --app hanger_app:create_app Process-Jobs --watch“ aus, um Lieferungen in der Warteschlange zu verarbeiten. Verwenden Sie „poetry run python -m Compileall -q src Tests“ als minimale Syntaxprüfung. Schemaänderungen als neue nummerierte Datei in „src/hanger_app/migrations/“ hinzufügen; Schreiben Sie niemals eine angewandte Migration neu.

Verwenden Sie „poetry run flask --app hanger_app:create_appsettings-list“ und
„settings-set <key> <json-value>“ zum Verwalten pro Installationseinstellungen, z
„branding.site_name“ oder „eligibility.minimum_age“.
Verwenden Sie „Interview planen“, „Interview-Notiz hinzufügen“, „Interview-Notizen auflisten“ und
„Forschungsexport“ für die Bewerberinterview-Pipeline und bereinigte Recherche
Metriken.

## Codierungsstil und Namenskonventionen

Verwenden Sie eine Einrückung mit vier Leerzeichen und befolgen Sie PEP 8. Benennen Sie Funktionen und Variablen mit „snake_case“, Klassen mit „PascalCase“ und Konstanten mit „UPPER_SNAKE_CASE“. Fügen Sie Typhinweise zu öffentlichen Methoden hinzu und leiten Sie Rückgabewerte weiter. Halten Sie die Routenhandler von Flask klein; Verschieben Sie wiederverwendbares Verhalten nach „src/hanger_app/services.py“. Bevorzugen Sie „pathlib.Path“ und Repository-relative Pfade statt fest codierter Speicherorte. Interpolieren Sie niemals Benutzereingaben in SQL oder HTML.

## Testrichtlinien

Fügen Sie neue Tests unter „tests/“ hinzu und spiegeln Sie dabei das Quelllayout wider. Benennen Sie die Dateien „test_<module>.py“ und die Testfunktionen „test_<behavior>()“. Führen Sie vor dem Absenden „poetry run pytest -q --cov=hanger_app“ und die Kompilierungsprüfung aus. Routenänderungen sollten erfolgreiche Anfragen, Autorisierungsfehler, ungültige Daten und erwartete Statuscodes abdecken.

## Commit- und Pull-Request-Richtlinien

Der Verlauf verwendet kurze, zwingende Betreffzeilen in Groß- und Kleinschreibung wie „Anmeldevalidierung korrigieren“ oder „Benutzer-Loader hinzufügen“. Konzentrieren Sie sich bei jedem Commit. Pull-Anfragen müssen das Problem, die Grundursache, die Auswirkungen auf den Benutzer und die durchgeführte Validierung erläutern. Verknüpfen Sie relevante Probleme und fügen Sie Screenshots für Änderungen unter „Seiten/“ ein. Mischen Sie keine generierten Dateien, Anmeldeinformationen, lokalen Datenbanken oder nicht verwandte Refaktoren in einem PR.
# リポジトリのガイドライン

## プロジェクトの構造とモジュールの構成

Python アプリケーション コードは `src/hanger_app/` にあります。 `__init__.py` は Flask ファクトリを所有し、`routes.py` は HTTP を処理し、`services.py` にはユースケースが含まれ、`repositories.py` は SQLite を分離します。バージョン管理されたスキーマ ファイルは `src/hanger_app/migrations/` にあります。 Jinja テンプレートは `src/hanger_app/templates/` にあります。 `src/hanger.py` と `src/loader.py` は互換性のエントリ ポイントです。テストは「tests/」に存在します。エージェントの指示は `.agents/skills/` に保存され、インストールされたバージョンは `skills-lock.json` に記録されます。

## ビルド、テスト、開発コマンド

依存関係をインストールする前に、分離された環境を作成します。

「」バッシュ
python3 -m venv .venv
ソース .venv/bin/activate
pip 詩をインストール==2.2.1
詩のインストール -E dev
「」

リポジトリ ルートからメイン アプリケーションを実行します。

「」バッシュ
詩の実行フラスコ --app ハンガー_app:create_app 実行 --debug
「」

`poetry run flask --apphanger_app:create_app process-jobs --watch` を実行して、キューに入れられた配信を処理します。最低限の構文チェックとして「poetry run python -m COMPileall -q src testing」を使用してください。スキーマの変更を新しい番号付きファイルとして `src/hanger_app/migrations/` に追加します。適用された移行を決して書き換えないでください。

「poetry run flask --apphanger_app:create_app settings-list」を使用し、
`settings-set <key> <json-value>` は、次のようなインストールごとの設定を管理します。
`branding.site_name` または `eligibility.minimum_age`。
`schedule-interview`、`add-interview-note`、`list-interview-notes`、および
申請者の面接パイプラインとサニタイズされた研究のための「研究エクスポート」
メトリクス。

## コーディングスタイルと命名規則

4 スペースのインデントを使用し、PEP 8 に従います。関数と変数には `snake_case`、クラスには `PascalCase`、定数には `UPPER_SNAKE_CASE` で名前を付けます。型ヒントをパブリック メソッドに追加し、戻り値をルーティングします。 Flask ルート ハンドラーを小さく保ちます。再利用可能な動作を `src/hanger_app/services.py` に移動します。ハードコーディングされた場所ではなく、「pathlib.Path」とリポジトリ相対パスを優先してください。ユーザー入力を SQL または HTML に決して挿入しないでください。

## テストガイドライン

ソース レイアウトをミラーリングして、`tests/` の下に新しいテストを追加します。ファイルに「test_<module>.py」という名前を付け、テスト関数に「test_<behavior>()」という名前を付けます。送信する前に `poetry run pytest -q --cov=hanger_app` を実行し、コンパイル チェックを行ってください。ルート変更では、成功したリクエスト、認証の失敗、無効なデータ、予期されるステータス コードをカバーする必要があります。

## コミットおよびプルリクエストのガイドライン

履歴では、「ログイン検証の修正」や「ユーザー ローダーの追加」など、短く、命令的な、タイトルで始まる主題が使用されます。各コミットに焦点を当ててください。プル リクエストでは、問題、根本原因、ユーザーへの影響、実行された検証について説明する必要があります。関連する問題をリンクし、「pages/」の下に変更のスクリーンショットを含めます。生成されたファイル、認証情報、ローカル データベース、または無関係なリファクタリングを PR に混在させないでください。
# リポジトリのガイドライン

## プロジェクトの構造とモジュールの構成

Python アプリケーション コードは `src/hanger_app/` にあります。 `__init__.py` は Flask ファクトリを所有し、`routes.py` は HTTP を処理し、`services.py` にはユースケースが含まれ、`repositories.py` は SQLite を分離します。バージョン管理されたスキーマ ファイルは `src/hanger_app/migrations/` にあります。 Jinja テンプレートは `src/hanger_app/templates/` にあります。 `src/hanger.py` と `src/loader.py` は互換性のエントリ ポイントです。テストは「tests/」に存在します。エージェントの指示は `.agents/skills/` に保存され、インストールされたバージョンは `skills-lock.json` に記録されます。

## ビルド、テスト、開発コマンド

依存関係をインストールする前に、分離された環境を作成します。

「」バッシュ
python3 -m venv .venv
ソース .venv/bin/activate
pip 詩をインストール==2.2.1
詩のインストール -E dev
「」

リポジトリ ルートからメイン アプリケーションを実行します。

「」バッシュ
詩の実行フラスコ --app ハンガー_app:create_app 実行 --debug
「」

`poetry run flask --apphanger_app:create_app process-jobs --watch` を実行して、キューに入れられた配信を処理します。最低限の構文チェックとして「poetry run python -m COMPileall -q src testing」を使用してください。スキーマの変更を新しい番号付きファイルとして `src/hanger_app/migrations/` に追加します。適用された移行を決して書き換えないでください。

「poetry run flask --apphanger_app:create_app settings-list」を使用し、
`settings-set <key> <json-value>` は、次のようなインストールごとの設定を管理します。
`branding.site_name` または `eligibility.minimum_age`。
`schedule-interview`、`add-interview-note`、`list-interview-notes`、および
申請者の面接パイプラインとサニタイズされた研究のための「研究エクスポート」
メトリクス。

## コーディングスタイルと命名規則

4 スペースのインデントを使用し、PEP 8 に従います。関数と変数には `snake_case`、クラスには `PascalCase`、定数には `UPPER_SNAKE_CASE` で名前を付けます。型ヒントをパブリック メソッドに追加し、戻り値をルーティングします。 Flask ルート ハンドラーを小さく保ちます。再利用可能な動作を `src/hanger_app/services.py` に移動します。ハードコーディングされた場所ではなく、「pathlib.Path」とリポジトリ相対パスを優先してください。ユーザー入力を SQL または HTML に決して挿入しないでください。

## テストガイドライン

ソース レイアウトをミラーリングして、`tests/` の下に新しいテストを追加します。ファイルに「test_<module>.py」という名前を付け、テスト関数に「test_<behavior>()」という名前を付けます。送信する前に `poetry run pytest -q --cov=hanger_app` を実行し、コンパイル チェックを行ってください。ルート変更では、成功したリクエスト、認証の失敗、無効なデータ、予期されるステータス コードをカバーする必要があります。

## コミットおよびプルリクエストのガイドライン

履歴では、「ログイン検証の修正」や「ユーザー ローダーの追加」など、短く、命令的な、タイトルで始まる主題が使用されます。各コミットに焦点を当ててください。プル リクエストでは、問題、根本原因、ユーザーへの影響、実行された検証について説明する必要があります。関連する問題をリンクし、「pages/」の下に変更のスクリーンショットを含めます。生成されたファイル、認証情報、ローカル データベース、または無関係なリファクタリングを PR に混在させないでください。
# 存储库指南

## 项目结构和模块组织

Python 应用程序代码位于 `src/hanger_app/` 中。 `__init__.py` 拥有 Flask 工厂，`routes.py` 处理 HTTP，`services.py` 包含用例，而 `repositories.py` 隔离 SQLite。版本化模式文件位于 `src/hanger_app/migrations/` 中； Jinja 模板位于 `src/hanger_app/templates/` 中。 `src/hanger.py` 和 `src/loader.py` 是兼容性入口点。测试位于“tests/”中。代理指令存储在“.agents/skills/”中，安装的版本记录在“skills-lock.json”中。

## 构建、测试和开发命令

在安装依赖之前创建一个隔离的环境：

````bash
python3 -m venv .venv
源 .venv/bin/activate
pip 安装诗歌==2.2.1
诗歌安装-E dev
````

从存储库根运行主应用程序：

````bash
诗歌运行烧瓶--apphanger_app：create_app运行--debug
````

运行 `poetry run Flask --apphanger_app:create_app process-jobs --watch` 来处理排队的交付。使用 `poetry run python -mcompileall -q srctests` 作为最低语法检查。将架构更改添加为“src/hanger_app/migrations/”中的新编号文件；切勿重写已应用的迁移。

使用 `poetry runflask --apphanger_app:create_appsettings-list` 和
`settings-set <key> <json-value>` 来管理每个安装的设置，例如
`branding.site_name` 或 `eligibility.minimum_age`。
使用 `schedule-interview`、`add-interview-note`、`list-interview-notes` 和
申请人面试流程和净化研究的“研究输出”
指标。

## 编码风格和命名约定

使用四空格缩进并遵循 PEP 8。使用“snake_case”命名函数和变量，使用“PascalCase”命名类，使用“UPPER_SNAKE_CASE”命名常量。向公共方法添加类型提示并路由返回值。保持 Flask 路由处理程序较小；将可重用行为移至“src/hanger_app/services.py”。首选“pathlib.Path”和存储库相对路径，而不是硬编码位置。切勿将用户输入插入 SQL 或 HTML。

## 测试指南

在“tests/”下添加新测试，镜像源布局。将文件命名为“test_<module>.py”和测试函数“test_<behavior>()”。运行 `poetry run pytest -q --cov=hanger_app` 并在提交之前进行编译检查。路由更改应涵盖成功的请求、授权失败、无效数据和预期的状态代码。

## 提交和拉取请求指南

History 使用简短、命令式、标题式主题，例如“修复登录验证”或“添加用户加载程序”。保持每次提交的重点。拉取请求必须解释问题、根本原因、用户影响和执行的验证。链接相关问题并包含“pages/”下更改的屏幕截图。不要将生成的文件、凭据、本地数据库或不相关的重构混合到 PR 中。
# 存储库指南

## 项目结构和模块组织

Python 应用程序代码位于 `src/hanger_app/` 中。 `__init__.py` 拥有 Flask 工厂，`routes.py` 处理 HTTP，`services.py` 包含用例，而 `repositories.py` 隔离 SQLite。版本化模式文件位于 `src/hanger_app/migrations/` 中； Jinja 模板位于 `src/hanger_app/templates/` 中。 `src/hanger.py` 和 `src/loader.py` 是兼容性入口点。测试位于“tests/”中。代理指令存储在“.agents/skills/”中，安装的版本记录在“skills-lock.json”中。

## 构建、测试和开发命令

在安装依赖之前创建一个隔离的环境：

````bash
python3 -m venv .venv
源 .venv/bin/activate
pip 安装诗歌==2.2.1
诗歌安装-E dev
````

从存储库根运行主应用程序：

````bash
诗歌运行烧瓶--apphanger_app：create_app运行--debug
````

运行 `poetry run Flask --apphanger_app:create_app process-jobs --watch` 来处理排队的交付。使用 `poetry run python -mcompileall -q srctests` 作为最低语法检查。将架构更改添加为“src/hanger_app/migrations/”中的新编号文件；切勿重写已应用的迁移。

使用 `poetry runflask --apphanger_app:create_appsettings-list` 和
`settings-set <key> <json-value>` 来管理每个安装的设置，例如
`branding.site_name` 或 `eligibility.minimum_age`。
使用 `schedule-interview`、`add-interview-note`、`list-interview-notes` 和
申请人面试流程和净化研究的“研究输出”
指标。

## 编码风格和命名约定

使用四空格缩进并遵循 PEP 8。使用“snake_case”命名函数和变量，使用“PascalCase”命名类，使用“UPPER_SNAKE_CASE”命名常量。向公共方法添加类型提示并路由返回值。保持 Flask 路由处理程序较小；将可重用行为移至“src/hanger_app/services.py”。首选“pathlib.Path”和存储库相对路径，而不是硬编码位置。切勿将用户输入插入 SQL 或 HTML。

## 测试指南

在“tests/”下添加新测试，镜像源布局。将文件命名为“test_<module>.py”和测试函数“test_<behavior>()”。运行 `poetry run pytest -q --cov=hanger_app` 并在提交之前进行编译检查。路由更改应涵盖成功的请求、授权失败、无效数据和预期的状态代码。

## 提交和拉取请求指南

History 使用简短、命令式、标题式主题，例如“修复登录验证”或“添加用户加载程序”。保持每次提交的重点。拉取请求必须解释问题、根本原因、用户影响和执行的验证。链接相关问题并包含“pages/”下更改的屏幕截图。不要将生成的文件、凭据、本地数据库或不相关的重构混合到 PR 中。
# Рекомендації щодо сховища

## Структура проекту та організація модулів

Код програми Python знаходиться в `src/hanger_app/`. `__init__.py` володіє фабрикою Flask, `routes.py` обробляє HTTP, `services.py` містить варіанти використання, а `repositories.py` ізолює SQLite. Версійні файли схеми знаходяться в `src/hanger_app/migrations/`; Шаблони Jinja знаходяться в `src/hanger_app/templates/`. `src/hanger.py` і `src/loader.py` є точками входу сумісності. Тести живуть у `tests/`. Інструкції агента зберігаються в `.agents/skills/`, а встановлені версії записуються в `skills-lock.json`.

## Команди збирання, тестування та розробки

Створіть ізольоване середовище перед встановленням залежностей:

```баш
python3 -m venv .venv
джерело .venv/bin/activate
pip install poetry==2.2.1
poetry install -E dev
```

Запустіть основну програму з кореня сховища:

```баш
poetry run flask --app hanger_app:create_app run --debug
```

Запустіть `poetry run flask --app hanger_app:create_app process-jobs --watch`, щоб обробити доставку в черзі. Використовуйте `poetry run python -m compileall -q src tests` як мінімальну перевірку синтаксису. Додайте зміни схеми як новий пронумерований файл у `src/hanger_app/migrations/`; ніколи не переписуйте застосовану міграцію.

Використовуйте `poetry run flask --app hanger_app:create_app settings-list` і
`settings-set <key> <json-value>`, щоб керувати налаштуваннями встановлення, такими як
`branding.site_name` або `eligibility.minimum_age`.
Використовуйте `schedule-interview`, `add-interview-note`, `list-interview-notes` та
«дослідження-експорт» для каналу співбесід із заявником і оброблених досліджень
метрики.

## Стиль кодування та правила іменування

Використовуйте відступ із чотирьох пробілів і дотримуйтеся PEP 8. Назвіть функції та змінні за допомогою `snake_case`, класи за допомогою `PascalCase`, а константи за допомогою `UPPER_SNAKE_CASE`. Додайте підказки типу до загальнодоступних методів і повертайте значення маршруту. Зберігайте невеликі обробники маршрутів Flask; перемістити багаторазову поведінку в `src/hanger_app/services.py`. Віддавайте перевагу `pathlib.Path` і відносним шляхам до сховища замість жорстко закодованих місць. Ніколи не інтерполюйте дані користувача в SQL або HTML.

## Інструкції з тестування

Додайте нові тести в `tests/`, віддзеркалюючи вихідний макет. Назвіть файли `test_<module>.py` і тестові функції `test_<behavior>()`. Запустіть `poetry run pytest -q --cov=hanger_app` і перевірте компіляцію перед надсиланням. Зміни маршруту мають стосуватися успішних запитів, помилок авторизації, недійсних даних і очікуваних кодів статусу.

## Інструкції щодо запитів на фіксацію та витягування

В історії використовуються короткі, обов’язкові теми в заголовках, такі як «Виправити перевірку входу» або «Додати завантажувач користувача». Тримайте зосередженість на кожному коміті. Запити на вилучення мають пояснювати проблему, першопричину, вплив на користувача та виконану перевірку. Посилайте на відповідні проблеми та додайте знімки екрана для змін у розділі `pages/`. Не змішуйте згенеровані файли, облікові дані, локальні бази даних або непов’язані рефактори в PR.
# Рекомендації щодо сховища

## Структура проекту та організація модулів

Код програми Python знаходиться в `src/hanger_app/`. `__init__.py` володіє фабрикою Flask, `routes.py` обробляє HTTP, `services.py` містить варіанти використання, а `repositories.py` ізолює SQLite. Версійні файли схеми знаходяться в `src/hanger_app/migrations/`; Шаблони Jinja знаходяться в `src/hanger_app/templates/`. `src/hanger.py` і `src/loader.py` є точками входу сумісності. Тести живуть у `tests/`. Інструкції агента зберігаються в `.agents/skills/`, а встановлені версії записуються в `skills-lock.json`.

## Команди збирання, тестування та розробки

Створіть ізольоване середовище перед встановленням залежностей:

```баш
python3 -m venv .venv
джерело .venv/bin/activate
pip install poetry==2.2.1
poetry install -E dev
```

Запустіть основну програму з кореня сховища:

```баш
poetry run flask --app hanger_app:create_app run --debug
```

Запустіть `poetry run flask --app hanger_app:create_app process-jobs --watch`, щоб обробити доставку в черзі. Використовуйте `poetry run python -m compileall -q src tests` як мінімальну перевірку синтаксису. Додайте зміни схеми як новий пронумерований файл у `src/hanger_app/migrations/`; ніколи не переписуйте застосовану міграцію.

Використовуйте `poetry run flask --app hanger_app:create_app settings-list` і
`settings-set <key> <json-value>`, щоб керувати налаштуваннями встановлення, такими як
`branding.site_name` або `eligibility.minimum_age`.
Використовуйте `schedule-interview`, `add-interview-note`, `list-interview-notes` та
«дослідження-експорт» для каналу співбесід із заявником і оброблених досліджень
метрики.

## Стиль кодування та правила іменування

Використовуйте відступ із чотирьох пробілів і дотримуйтеся PEP 8. Назвіть функції та змінні за допомогою `snake_case`, класи за допомогою `PascalCase`, а константи за допомогою `UPPER_SNAKE_CASE`. Додайте підказки типу до загальнодоступних методів і повертайте значення маршруту. Зберігайте невеликі обробники маршрутів Flask; перемістити багаторазову поведінку в `src/hanger_app/services.py`. Віддавайте перевагу `pathlib.Path` і відносним шляхам до сховища замість жорстко закодованих місць. Ніколи не інтерполюйте дані користувача в SQL або HTML.

## Інструкції з тестування

Додайте нові тести в `tests/`, віддзеркалюючи вихідний макет. Назвіть файли `test_<module>.py` і тестові функції `test_<behavior>()`. Запустіть `poetry run pytest -q --cov=hanger_app` і перевірте компіляцію перед надсиланням. Зміни маршруту мають стосуватися успішних запитів, помилок авторизації, недійсних даних і очікуваних кодів статусу.

## Інструкції щодо запитів на фіксацію та витягування

В історії використовуються короткі, обов’язкові теми в заголовках, такі як «Виправити перевірку входу» або «Додати завантажувач користувача». Тримайте зосередженість на кожному коміті. Запити на вилучення мають пояснювати проблему, першопричину, вплив на користувача та виконану перевірку. Посилайте на відповідні проблеми та додайте знімки екрана для змін у розділі `pages/`. Не змішуйте згенеровані файли, облікові дані, локальні бази даних або непов’язані рефактори в PR.
# Рекомендации по репозиторию

## Структура проекта и организация модулей

Код приложения Python находится в `src/hanger_app/`. `__init__.py` владеет фабрикой Flask, `routes.py` обрабатывает HTTP, `services.py` содержит варианты использования, а `repositories.py` изолирует SQLite. Файлы схем с версиями находятся в `src/hanger_app/migrations/`; Шаблоны Jinja находятся в `src/hanger_app/templates/`. `src/hanger.py` и `src/loader.py` являются точками входа совместимости. Тесты живут в `tests/`. Инструкции агента хранятся в `.agents/skills/`, а установленные версии записаны в `skills-lock.json`.

## Команды сборки, тестирования и разработки

Создайте изолированную среду перед установкой зависимостей:

``` баш
python3 -m венв .venv
источник .venv/bin/activate
пип установить поэзию == 2.2.1
установка поэзии -E dev
```

Запустите основное приложение из корня репозитория:

``` баш
поэзия запустить колбу --app Hanger_app:create_app запустить --debug
```

Запустите `poetry run flask --app Hanger_app:create_appprocess-jobs --watch` для обработки поставок в очереди. Используйте `poetry run python -m compileall -q srctests` в качестве минимальной проверки синтаксиса. Добавьте изменения схемы в виде нового пронумерованного файла в `src/hanger_app/migrations/`; никогда не переписывайте прикладную миграцию.

Используйте `poetry run flask --app Hanger_app:create_app settings-list` и
`settings-set <key> <json-value>` для управления настройками каждой установки, такими как
`branding.site_name` или `eligibility.minimum_age`.
Используйте `запланировать-интервью`, `добавить-интервью-заметку`, `список-интервью-заметок` и
«экспорт исследований» для конвейера собеседований с кандидатами и очищенных исследований
метрики.

## Стиль кодирования и соглашения об именах

Используйте отступы в четыре пробела и следуйте PEP 8. Назовите функции и переменные с помощью `snake_case`, классы с помощью `PascalCase` и константы с `UPPER_SNAKE_CASE`. Добавьте подсказки типов к общедоступным методам и маршрутизируйте возвращаемые значения. Сохраняйте обработчики маршрутов Flask небольшими; переместите повторно используемое поведение в `src/hanger_app/services.py`. Предпочитайте `pathlib.Path` и пути относительно репозитория вместо жестко закодированных местоположений. Никогда не интерполируйте вводимые пользователем данные в SQL или HTML.

## Рекомендации по тестированию

Добавьте новые тесты в `tests/`, отражая исходный макет. Назовите файлы `test_<module>.py` и тестовые функции `test_<behavior>()`. Запустите `poetry run pytest -q --cov=hanger_app` и проверьте компиляцию перед отправкой. Изменения маршрута должны охватывать успешные запросы, ошибки авторизации, неверные данные и ожидаемые коды состояния.

## Рекомендации по фиксации и запросу на извлечение

В истории используются короткие, повелительные темы с заголовками, такие как «Исправить проверку входа в систему» или «Добавить загрузчик пользователя». Держите каждый коммит сосредоточенным. Запросы на включение должны объяснять проблему, основную причину, влияние на пользователя и выполненную проверку. Свяжите соответствующие проблемы и добавьте скриншоты изменений в раздел «pages/». Не смешивайте в PR сгенерированные файлы, учетные данные, локальные базы данных или несвязанные рефакторинги.
# Рекомендации по репозиторию

## Структура проекта и организация модулей

Код приложения Python находится в `src/hanger_app/`. `__init__.py` владеет фабрикой Flask, `routes.py` обрабатывает HTTP, `services.py` содержит варианты использования, а `repositories.py` изолирует SQLite. Файлы схем с версиями находятся в `src/hanger_app/migrations/`; Шаблоны Jinja находятся в `src/hanger_app/templates/`. `src/hanger.py` и `src/loader.py` являются точками входа совместимости. Тесты живут в `tests/`. Инструкции агента хранятся в `.agents/skills/`, а установленные версии записаны в `skills-lock.json`.

## Команды сборки, тестирования и разработки

Создайте изолированную среду перед установкой зависимостей:

``` баш
python3 -m венв .venv
источник .venv/bin/activate
пип установить поэзию == 2.2.1
установка поэзии -E dev
```

Запустите основное приложение из корня репозитория:

``` баш
поэзия запустить колбу --app Hanger_app:create_app запустить --debug
```

Запустите `poetry run flask --app Hanger_app:create_appprocess-jobs --watch` для обработки поставок в очереди. Используйте `poetry run python -m compileall -q srctests` в качестве минимальной проверки синтаксиса. Добавьте изменения схемы в виде нового пронумерованного файла в `src/hanger_app/migrations/`; никогда не переписывайте прикладную миграцию.

Используйте `poetry run flask --app Hanger_app:create_app settings-list` и
`settings-set <key> <json-value>` для управления настройками каждой установки, такими как
`branding.site_name` или `eligibility.minimum_age`.
Используйте `запланировать-интервью`, `добавить-интервью-заметку`, `список-интервью-заметок` и
«экспорт исследований» для конвейера собеседований с кандидатами и очищенных исследований
метрики.

## Стиль кодирования и соглашения об именах

Используйте отступы в четыре пробела и следуйте PEP 8. Назовите функции и переменные с помощью `snake_case`, классы с помощью `PascalCase` и константы с `UPPER_SNAKE_CASE`. Добавьте подсказки типов к общедоступным методам и маршрутизируйте возвращаемые значения. Сохраняйте обработчики маршрутов Flask небольшими; переместите повторно используемое поведение в `src/hanger_app/services.py`. Предпочитайте `pathlib.Path` и пути относительно репозитория вместо жестко закодированных местоположений. Никогда не интерполируйте вводимые пользователем данные в SQL или HTML.

## Рекомендации по тестированию

Добавьте новые тесты в `tests/`, отражая исходный макет. Назовите файлы `test_<module>.py` и тестовые функции `test_<behavior>()`. Запустите `poetry run pytest -q --cov=hanger_app` и проверьте компиляцию перед отправкой. Изменения маршрута должны охватывать успешные запросы, ошибки авторизации, неверные данные и ожидаемые коды состояния.

## Рекомендации по фиксации и запросу на извлечение

В истории используются короткие, повелительные темы с заголовками, такие как «Исправить проверку входа в систему» или «Добавить загрузчик пользователя». Держите каждый коммит сосредоточенным. Запросы на включение должны объяснять проблему, основную причину, влияние на пользователя и выполненную проверку. Свяжите соответствующие проблемы и добавьте скриншоты изменений в раздел «pages/». Не смешивайте в PR сгенерированные файлы, учетные данные, локальные базы данных или несвязанные рефакторинги.