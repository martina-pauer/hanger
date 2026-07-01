# Accessibility Code Patterns

Practical, copy-paste-ready patterns for common accessibility requirements. Each pattern is self-contained and linked from the main [SKILL.md](../SKILL.md).

---

## Modal focus trap

Trap keyboard focus inside a modal dialog so Tab/Shift+Tab cycle through its focusable elements and Escape closes it.

```javascript
function openModal(modal) {
  const focusableElements = modal.querySelectorAll(
    'button, [href], input, select, textarea, [tabindex]:not([tabindex="-1"])'
  );
  const firstElement = focusableElements[0];
  const lastElement = focusableElements[focusableElements.length - 1];

  modal.addEventListener('keydown', (e) => {
    if (e.key === 'Tab') {
      if (e.shiftKey && document.activeElement === firstElement) {
        e.preventDefault();
        lastElement.focus();
      } else if (!e.shiftKey && document.activeElement === lastElement) {
        e.preventDefault();
        firstElement.focus();
      }
    }
    if (e.key === 'Escape') {
      closeModal();
    }
  });

  firstElement.focus();
}
```

The native `<dialog>` element handles focus trapping automatically—prefer it when browser support allows.

---

## Skip link

Allows keyboard users to bypass repetitive navigation and jump straight to main content.

```html
<body>
  <a href="#main-content" class="skip-link">Skip to main content</a>
  <header><!-- navigation --></header>
  <main id="main-content" tabindex="-1">
    <!-- main content -->
  </main>
</body>
```

```css
.skip-link {
  position: absolute;
  top: -40px;
  left: 0;
  background: #000;
  color: #fff;
  padding: 8px 16px;
  z-index: 100;
}

.skip-link:focus {
  top: 0;
}
```

---

## Error handling

Announce errors to screen readers and focus the first invalid field on submit.

```html
<form novalidate>
  <div class="field" aria-live="polite">
    <label for="email">Email</label>
    <input type="email" id="email"
           aria-invalid="true"
           aria-describedby="email-error">
    <p id="email-error" class="error" role="alert">
      Please enter a valid email address (e.g., name@example.com)
    </p>
  </div>
</form>
```

```javascript
form.addEventListener('submit', (e) => {
  const firstError = form.querySelector('[aria-invalid="true"]');
  if (firstError) {
    e.preventDefault();
    firstError.focus();

    const errorSummary = document.getElementById('error-summary');
    errorSummary.textContent =
      `${errors.length} errors found. Please fix them and try again.`;
    errorSummary.focus();
  }
});
```

---

## Form labels

Every input needs an associated label—either explicit (`for`/`id`) or implicit (wrapping `<label>`).

```html
<!-- ❌ No label association -->
<input type="email" placeholder="Email">

<!-- ✅ Explicit label -->
<label for="email">Email address</label>
<input type="email" id="email" name="email"
       autocomplete="email" required>

<!-- ✅ Implicit label -->
<label>
  Email address
  <input type="email" name="email" autocomplete="email" required>
</label>

<!-- ✅ With instructions -->
<label for="password">Password</label>
<input type="password" id="password"
       aria-describedby="password-requirements">
<p id="password-requirements">
  Must be at least 8 characters with one number.
</p>
```

---

## Dragging movements

Any action triggered by dragging must offer a single-pointer alternative (WCAG 2.5.7).

```html
<!-- ❌ Drag-only reorder -->
<ul class="sortable-list" draggable="true">
  <li>Item 1</li>
  <li>Item 2</li>
</ul>

<!-- ✅ Drag + button alternatives -->
<ul class="sortable-list">
  <li>
    <span>Item 1</span>
    <button aria-label="Move Item 1 up">↑</button>
    <button aria-label="Move Item 1 down">↓</button>
  </li>
  <li>
    <span>Item 2</span>
    <button aria-label="Move Item 2 up">↑</button>
    <button aria-label="Move Item 2 down">↓</button>
  </li>
</ul>
```

Also applies to sliders, map panning, colour pickers, and similar drag-based widgets—always provide an equivalent click/tap or keyboard path.

---

## ARIA tabs

Tabs require `role="tablist"`, `role="tab"`, and `role="tabpanel"` with proper `aria-selected`, `aria-controls`, and keyboard support.

```html
<div role="tablist" aria-label="Product information">
  <button role="tab" id="tab-1" aria-selected="true"
          aria-controls="panel-1">Description</button>
  <button role="tab" id="tab-2" aria-selected="false"
          aria-controls="panel-2" tabindex="-1">Reviews</button>
</div>
<div role="tabpanel" id="panel-1" aria-labelledby="tab-1">
  <!-- Panel content -->
</div>
<div role="tabpanel" id="panel-2" aria-labelledby="tab-2" hidden>
  <!-- Panel content -->
</div>
```

Arrow keys should move focus between tabs; the active tab receives `tabindex="0"` while inactive tabs use `tabindex="-1"`.

---

## Live regions and notifications

Use `aria-live` to announce dynamic content changes to screen readers without moving focus.

```html
<!-- Status updates (polite — waits for pause in speech) -->
<div aria-live="polite" aria-atomic="true" class="status">
  <!-- Content updates announced to screen readers -->
</div>

<!-- Urgent alerts (assertive — interrupts) -->
<div role="alert" aria-live="assertive">
  <!-- Interrupts current announcement -->
</div>
```

```javascript
function showNotification(message, type = 'polite') {
  const container = document.getElementById(`${type}-announcer`);
  container.textContent = '';
  requestAnimationFrame(() => {
    container.textContent = message;
  });
}
```

Clear the container before writing to ensure the same message triggers a new announcement.

---

## Screen reader commands

Quick reference for the most common screen reader shortcuts.

| Action | VoiceOver (Mac) | NVDA (Windows) |
|--------|-----------------|----------------|
| Start/Stop | ⌘ + F5 | Ctrl + Alt + N |
| Next item | VO + → | ↓ |
| Previous item | VO + ← | ↑ |
| Activate | VO + Space | Enter |
| Headings list | VO + U, then arrows | H / Shift + H |
| Links list | VO + U | K / Shift + K |

# Patrones de códigos de accesibilidad

Patrones prácticos, listos para copiar y pegar, para requisitos de accesibilidad comunes. Cada patrón es autónomo y está vinculado desde el [SKILL.md](../SKILL.md) principal.

---

## Trampa de enfoque modal

Atrape el foco del teclado dentro de un cuadro de diálogo modal para que Tab/Shift+Tab recorra sus elementos enfocables y Escape lo cierre.

```javascript
función openModal(modal) {
  const focusableElements = modal.querySelectorAll(
    'botón, [href], entrada, seleccionar, área de texto, [tabindex]:no([tabindex="-1"])'
  );
  const primerElemento = elementos enfocables[0];
  const lastElement = focusableElements[focusableElements.length - 1];

  modal.addEventListener('keydown', (e) => {
    if (e.key === 'Tab') {
      if (e.shiftKey && document.activeElement === primerElemento) {
        e.preventDefault();
        últimoElement.focus();
      } else if (!e.shiftKey && document.activeElement === últimoElemento) {
        e.preventDefault();
        primerElement.focus();
      }
    }
    if (e.key === 'Escape') {
      cerrarModal();
    }
  });

  primerElement.focus();
}
```

El elemento nativo `<dialog>` maneja la captura de foco automáticamente; prefiérelo cuando la compatibilidad del navegador lo permita.

---

## Saltar enlace

Permite a los usuarios del teclado evitar la navegación repetitiva y saltar directamente al contenido principal.

```html
<cuerpo>
  <a href="#main-content" class="skip-link">Saltar al contenido principal</a>
  <encabezado><!-- navegación --></encabezado>
  <id principal="contenido-principal" tabindex="-1">
    <!-- contenido principal -->
  </principal>
</cuerpo>
```

```css
.skip-enlace {
  posición: absoluta;
  arriba: -40px;
  izquierda: 0;
  fondo: #000;
  color: #fff;
  relleno: 8px 16px;
  índice z: 100;
}

.skip-link:enfoque {
  arriba: 0;
}
```

---

## Manejo de errores

Anuncie los errores a los lectores de pantalla y centre el primer campo no válido en el envío.

```html
<formulario novalidar>
  <div class="campo" aria-live="educado">
    <label for="email">Correo electrónico</label>
    <tipo de entrada="correo electrónico" id="correo electrónico"
           aria-invalid="verdadero"
           aria-descrito por="correo electrónico-error">
    <p id="correo electrónico-error" clase="error" rol="alerta">
      Ingrese una dirección de correo electrónico válida (por ejemplo, nombre@ejemplo.com)
    </p>
  </div>
</formulario>
```

```javascript
form.addEventListener('enviar', (e) => {
  const firstError = form.querySelector('[aria-invalid="true"]');
  si (primerError) {
    e.preventDefault();
    primerError.focus();

    const errorSummary = document.getElementById('resumen de errores');
    errorSummary.textContent =
      `${errors.length} errores encontrados. Por favor corríjalos y vuelva a intentarlo.`;
    errorSummary.focus();
  }
});
```

---

## Etiquetas de formulario

Cada entrada necesita una etiqueta asociada, ya sea explícita (`for`/`id`) o implícita (que envuelve `<label>`).

```html
<!-- ❌ Sin asociación de etiqueta -->
<tipo de entrada="correo electrónico" marcador de posición="correo electrónico">

<!-- ✅ Etiqueta explícita -->
<label for="email">Dirección de correo electrónico</label>
<tipo de entrada="correo electrónico" id="correo electrónico" nombre="correo electrónico"
       autocompletar="correo electrónico" requerido>

<!-- ✅ Etiqueta implícita -->
<etiqueta>
  Dirección de correo electrónico
  <tipo de entrada="correo electrónico" nombre="correo electrónico" autocompletar="correo electrónico" requerido>
</etiqueta>

<!-- ✅ Con instrucciones -->
<label for="contraseña">Contraseña</label>
<tipo de entrada="contraseña" id="contraseña"
       aria-describedby="requisitos-de-contraseña">
<p id="requisitos-contraseña">
  Debe tener al menos 8 caracteres con un número.
</p>
```

---

## Movimientos de arrastre

Cualquier acción desencadenada por arrastrar debe ofrecer una alternativa de puntero único (WCAG 2.5.7).

```html
<!-- ❌ Reordenar sólo arrastrando -->
<ul class="lista-clasificable" arrastrable="true">
  <li>Artículo 1</li>
  <li>Artículo 2</li>
</ul>

<!-- ✅ Alternativas de arrastrar + botón -->
<ul class="lista-ordenable">
  <li>
    <span>Artículo 1</span>
    <button aria-label="Mover elemento 1 hacia arriba"> ↑</button>
    <button aria-label="Mover elemento 1 hacia abajo">↓</button>
  </li>
  <li>
    <span>Artículo 2</span>
    <button aria-label="Mover elemento 2 hacia arriba"> ↑</button>
    <button aria-label="Mover elemento 2 hacia abajo">↓</button>
  </li>
</ul>
```

También se aplica a controles deslizantes, desplazamiento de mapas, selectores de color y widgets similares basados en arrastrar; siempre proporciona una ruta equivalente de clic/toque o teclado.

---

## pestañas ARIA

Las pestañas requieren `role="tablist"`, `role="tab"` y `role="tabpanel"` con `aria-selected`, `aria-controls` y compatibilidad con teclado adecuados.

```html
<div role="tablist" aria-label="Información del producto">
  <botón rol="tab" id="tab-1" aria-selected="true"
          aria-controls="panel-1">Descripción</botón>
  <botón rol="tab" id="tab-2" aria-selected="false"
          aria-controls="panel-2" tabindex="-1">Reseñas</button>
</div>
<div role="tabpanel" id="panel-1" aria-labelledby="tab-1">
  <!-- Contenido del panel -->
</div>
<div role="tabpanel" id="panel-2" aria-labelledby="tab-2" oculto>
  <!-- Contenido del panel -->
</div>
```

Las teclas de flecha deberían mover el foco entre pestañas; la pestaña activa recibe `tabindex="0"` mientras que las pestañas inactivas usan `tabindex="-1"`.

---

## Regiones en vivo y notificaciones

Utilice `aria-live` para anunciar cambios de contenido dinámico a los lectores de pantalla sin mover el foco.

```html
<!-- Actualizaciones de estado (educado: espera una pausa en el habla) -->
<div aria-live="educado" aria-atomic="true" class="estado">
  <!-- Actualizaciones de contenido anunciadas para los lectores de pantalla -->
</div>

<!-- Alertas urgentes (asertivas — interrumpe) -->
<div role="alerta" aria-live="asertivo">
  <!-- Interrumpe el anuncio actual -->
</div>
```

```javascript
función mostrarNotificación (mensaje, tipo = 'cortés') {
  contenedor const = document.getElementById(`${tipo}-anunciador`);
  contenedor.textContent = '';
  solicitudAnimationFrame(() => {
    contenedor.textContent = mensaje;
  });
}
```

Borre el contenedor antes de escribir para asegurarse de que el mismo mensaje active un nuevo anuncio.

---

## Comandos del lector de pantalla

Referencia rápida para los atajos de lectores de pantalla más comunes.

| Acción | Voz en off (Mac) | NVDA (Windows) |
|--------|-----------------|----------------|
| Iniciar/Parar | ⌘ + F5 | Ctrl + Alt + N |
| Artículo siguiente | VO + → | ↓ |
| Artículo anterior | Vo + ← | ↑ |
| Activar | VO + Espacio | Entrar |
| Lista de encabezados | VO + U, luego flechas | H / Mayús + H |
| Lista de enlaces | VO+U | K / Mayús + K |
# Modèles de codes d'accessibilité

Modèles pratiques et prêts à copier-coller pour les exigences d’accessibilité courantes. Chaque modèle est autonome et lié au principal [SKILL.md](../SKILL.md).

---

## Piège à focalisation modale

Piège le focus du clavier dans une boîte de dialogue modale afin que Tab/Shift+Tab parcoure ses éléments focalisables et Escape le ferme.

```javascript
fonction openModal(modal) {
  const focusableElements = modal.querySelectorAll(
    'bouton, [href], entrée, sélection, zone de texte, [tabindex]:not([tabindex="-1"])'
  );
  const firstElement = focusableElements[0];
  const lastElement = focusableElements[focusableElements.length - 1];

  modal.addEventListener('keydown', (e) => {
    if (e.key === 'Tab') {
      if (e.shiftKey && document.activeElement === firstElement) {
        e.preventDefault();
        lastElement.focus();
      } sinon if (!e.shiftKey && document.activeElement === lastElement) {
        e.preventDefault();
        firstElement.focus();
      }
    }
    if (e.key === 'Échap') {
      closeModal();
    }
  });

  firstElement.focus();
}
```

L'élément natif `<dialog>` gère automatiquement le focus trapping ; préférez-le lorsque la prise en charge du navigateur le permet.

---

## Ignorer le lien

Permet aux utilisateurs de clavier d'éviter la navigation répétitive et d'accéder directement au contenu principal.

```html
<corps>
  <a href="#main-content" class="skip-link">Passer au contenu principal</a>
  <header><!-- navigation --></header>
  <main id="main-content" tabindex="-1">
    <!-- contenu principal -->
  </main>
</corps>
```

```css
.skip-link {
  position : absolue ;
  haut : -40px ;
  gauche : 0 ;
  arrière-plan : #000 ;
  couleur : #fff ;
  remplissage : 8px 16px ;
  indice z : 100 ;
}

.skip-link:focus {
  haut : 0 ;
}
```

---

## Gestion des erreurs

Annoncez les erreurs aux lecteurs d'écran et concentrez le premier champ invalide sur la soumission.

```html
<formulaire novalidate>
  <div class="field" aria-live="polite">
    <label for="email">E-mail</label>
    <input type="email" id="email"
           aria-invalid = "true"
           aria-describeby="email-erreur">
    <p id="email-error" class="error" role="alert">
      Veuillez saisir une adresse e-mail valide (par exemple, nom@exemple.com)
    </p>
  </div>
</form>
```

```javascript
form.addEventListener('submit', (e) => {
  const firstError = form.querySelector('[aria-invalid="true"]');
  si (premièreErreur) {
    e.preventDefault();
    firstError.focus();

    const errorSummary = document.getElementById('error-summary');
    errorSummary.textContent =
      `${errors.length} erreurs trouvées. Veuillez les corriger et réessayer.`;
    errorSummary.focus();
  }
});
```

---

## Étiquettes de formulaire

Chaque entrée nécessite une étiquette associée, soit explicite (`for`/`id`) ou implicite (enveloppant `<label>`).

```html
<!-- ❌ Aucune association de label -->
<input type="email" placeholder="Email">

<!-- ✅Étiquette explicite -->
<label for="email">Adresse e-mail</label>
<input type="email" id="email" nom="email"
       autocomplete="email" requis>

<!-- ✅Étiquette implicite -->
<étiquette>
  Adresse e-mail
  <input type="email" name="email" autocomplete="email" requis>
</étiquette>

<!-- ✅Avec mode d'emploi -->
<label for="password">Mot de passe</label>
<input type="mot de passe" id="mot de passe"
       aria-describeby="mot de passe-exigences">
<p id="mot de passe-exigences">
  Doit contenir au moins 8 caractères avec un chiffre.
</p>
```

---

## Mouvements de glissement

Toute action déclenchée par glissement doit offrir une alternative à un seul pointeur (WCAG 2.5.7).

```html
<!-- ❌ Réorganisation par glisser-déposer -->
<ul class="sortable-list" draggable="true">
  <li>Élément 1</li>
  <li>Élément 2</li>
</ul>

<!-- ✅ Alternatives au bouton Glisser + -->
<ul class="liste-triable">
  <li>
    <span>Élément 1</span>
    <button aria-label="Déplacer l'élément 1 vers le haut">↑</button>
    <button aria-label="Déplacer l'élément 1 vers le bas">↓</button>
  </li>
  <li>
    <span>Article 2</span>
    <button aria-label="Déplacer l'élément 2 vers le haut">↑</button>
    <button aria-label="Déplacer l'élément 2 vers le bas">↓</button>
  </li>
</ul>
```

S'applique également aux curseurs, aux panoramiques de carte, aux sélecteurs de couleurs et aux widgets similaires basés sur le glissement : fournissez toujours un chemin de clic/appui ou de clavier équivalent.

---

## Onglets ARIA

Les onglets nécessitent `role="tablist"`, `role="tab"` et `role="tabpanel"` avec une prise en charge appropriée de `aria-selected`, `aria-controls` et du clavier.

```html
<div role="tablist" aria-label="Informations sur le produit">
  <bouton role="tab" id="tab-1" aria-selected="true"
          aria-controls="panel-1">Description</bouton>
  <bouton role="tab" id="tab-2" aria-selected="false"
          aria-controls="panel-2" tabindex="-1">Avis</button>
</div>
<div role="tabpanel" id="panel-1" aria-labelledby="tab-1">
  <!-- Contenu du panneau -->
</div>
<div role="tabpanel" id="panel-2" aria-labelledby="tab-2" caché>
  <!-- Contenu du panneau -->
</div>
```

Les touches fléchées doivent déplacer le focus entre les onglets ; l'onglet actif reçoit `tabindex="0"` tandis que les onglets inactifs utilisent `tabindex="-1"`.

---

## Régions et notifications en direct

Utilisez « aria-live » pour annoncer les modifications dynamiques du contenu aux lecteurs d'écran sans déplacer le focus.

```html
<!-- Mises à jour du statut (poli — attend une pause dans le discours) -->
<div aria-live="polite" aria-atomic="true" class="status">
  <!-- Mises à jour du contenu annoncées aux lecteurs d'écran -->
</div>

<!-- Alertes urgentes (affirmatives — interruptions) -->
<div role="alert" aria-live="assertive">
  <!-- Interrompt l'annonce en cours -->
</div>
```

```javascript
function showNotification (message, type = 'poli') {
  const conteneur = document.getElementById(`${type}-announcer`);
  conteneur.textContent = '';
  requêteAnimationFrame(() => {
    conteneur.textContent = message ;
  });
}
```

Effacez le conteneur avant d'écrire pour garantir que le même message déclenche une nouvelle annonce.

---

## Commandes du lecteur d'écran

Référence rapide pour les raccourcis des lecteurs d'écran les plus courants.

| Actions | Voix off (Mac) | NVDA (Windows) |
|--------|-----------------|----------------|
| Démarrer/Arrêter | ⌘ + F5 | Ctrl + Alt + N |
| Article suivant | VO + → | ↓ |
| Article précédent | VO + ← | ↑ |
| Activer | VO + Espace | Entrez |
| Liste des titres | VO + U, puis flèches | H / Maj + H |
| Liste de liens | VO + U | K / Maj + K |
# Codemuster für Barrierefreiheit

Praktische Muster zum Kopieren und Einfügen für allgemeine Barrierefreiheitsanforderungen. Jedes Muster ist in sich geschlossen und vom Haupt-[SKILL.md](../SKILL.md) aus verknüpft.

---

## Modale Fokusfalle

Fangen Sie den Tastaturfokus in einem modalen Dialog ein, sodass Tab/Umschalt+Tab durch seine fokussierbaren Elemente blättert und Escape ihn schließt.

„Javascript
Funktion openModal(modal) {
  const focusableElements = modal.querySelectorAll(
    'button, [href], input, select, textarea, [tabindex]:not([tabindex="-1"])'
  );
  const firstElement = focusableElements[0];
  const lastElement = focusableElements[focusableElements.length - 1];

  modal.addEventListener('keydown', (e) => {
    if (e.key === 'Tab') {
      if (e.shiftKey && document.activeElement === firstElement) {
        e.preventDefault();
        lastElement.focus();
      } else if (!e.shiftKey && document.activeElement === lastElement) {
        e.preventDefault();
        firstElement.focus();
      }
    }
    if (e.key === 'Escape') {
      closeModal();
    }
  });

  firstElement.focus();
}
„

Das native „<dialog>“-Element verarbeitet das Fokus-Trapping automatisch – bevorzugen Sie es, wenn die Browserunterstützung dies zulässt.

---

## Link überspringen

Ermöglicht Tastaturbenutzern, sich wiederholende Navigation zu umgehen und direkt zum Hauptinhalt zu springen.

```html
<Körper>
  <a href="#main-content" class="skip-link">Zum Hauptinhalt springen</a>
  <header><!-- navigation --></header>
  <main id="main-content" tabindex="-1">
    <!-- Hauptinhalt -->
  </main>
</body>
„

„css
.skip-link {
  Position: absolut;
  oben: -40px;
  links: 0;
  Hintergrund: #000;
  Farbe: #fff;
  Polsterung: 8px 16px;
  Z-Index: 100;
}

.skip-link:focus {
  oben: 0;
}
„

---

## Fehlerbehandlung

Melden Sie Fehler den Screenreadern und fokussieren Sie beim Absenden das erste ungültige Feld.

```html
<Formular Novalidat>
  <div class="field" aria-live="polite">
    <label for="email">E-Mail</label>
    <input type="email" id="email"
           aria-invalid="true"
           aria-describedby="email-error">
    <p id="email-error" class="error" role="alert">
      Bitte geben Sie eine gültige E-Mail-Adresse ein (z. B. name@example.com)
    </p>
  </div>
</form>
„

„Javascript
form.addEventListener('submit', (e) => {
  const firstError = form.querySelector('[aria-invalid="true"]');
  if (firstError) {
    e.preventDefault();
    firstError.focus();

    const errorSummary = document.getElementById('error-summary');
    errorSummary.textContent =
      `${errors.length} Fehler gefunden. Bitte beheben Sie sie und versuchen Sie es erneut.`;
    errorSummary.focus();
  }
});
„

---

## Formularbeschriftungen

Jede Eingabe benötigt ein zugehöriges Label – entweder explizit (`for`/`id`) oder implizit (umschließendes `<label>`).

```html
<!-- ❌ Keine Labelzuordnung -->
<input type="email" placeholder="Email">

<!-- ✅ Explizite Bezeichnung -->
<label for="email">E-Mail-Adresse</label>
<input type="email" id="email" name="email"
       autocomplete="email" erforderlich>

<!-- ✅ Implizite Bezeichnung -->
<Beschriftung>
  E-Mail-Adresse
  <input type="email" name="email" autocomplete="email" erforderlich>
</label>

<!-- ✅ Mit Anleitung -->
<label for="password">Passwort</label>
<input type="password" id="password"
       aria-describedby="password-requirements">
<p id="password-requirements">
  Muss mindestens 8 Zeichen lang sein und eine Zahl enthalten.
</p>
„

---

## Ziehende Bewegungen

Jede durch Ziehen ausgelöste Aktion muss eine Single-Pointer-Alternative bieten (WCAG 2.5.7).

```html
<!-- ❌ Nur per Drag-and-Drag neu anordnen -->
<ul class="sortable-list" draggable="true">
  <li>Punkt 1</li>
  <li>Punkt 2</li>
</ul>

<!-- ✅ Drag + Button-Alternativen -->
<ul class="sortable-list">
  <li>
    <span>Punkt 1</span>
    <button aria-label="Element 1 nach oben verschieben"> ↑</button>
    <button aria-label="Element 1 nach unten verschieben">↓</button>
  </li>
  <li>
    <span>Punkt 2</span>
    <button aria-label="Element 2 nach oben verschieben"> ↑</button>
    <button aria-label="Element 2 nach unten verschieben">↓</button>
  </li>
</ul>
„

Gilt auch für Schieberegler, Kartenschwenken, Farbwähler und ähnliche ziehbasierte Widgets – stellen Sie immer einen entsprechenden Klick-/Tippen- oder Tastaturpfad bereit.

---

## ARIA-Registerkarten

Tabs erfordern „role="tablist"`, `role="tab"` und `role="tabpanel"` mit ordnungsgemäßer aria-selected-, aria-controls- und Tastaturunterstützung.

```html
<div role="tablist" aria-label="Produktinformationen">
  <button Role="tab" id="tab-1" aria-selected="true"
          aria-controls="panel-1">Beschreibung</button>
  <button Role="tab" id="tab-2" aria-selected="false"
          aria-controls="panel-2" tabindex="-1">Bewertungen</button>
</div>
<div Role="tabpanel" id="panel-1" aria-labelledby="tab-1">
  <!-- Panelinhalt -->
</div>
<div Role="tabpanel" id="panel-2" aria-labelledby="tab-2" versteckt>
  <!-- Panelinhalt -->
</div>
„

Mit den Pfeiltasten sollte der Fokus zwischen den Registerkarten verschoben werden. Der aktive Tab erhält „tabindex="0"`, während inaktive Tabs „tabindex="-1"` verwenden.

---

## Live-Regionen und Benachrichtigungen

Verwenden Sie „aria-live“, um dynamische Inhaltsänderungen an Screenreader anzukündigen, ohne den Fokus zu verschieben.

```html
<!-- Statusaktualisierungen (höflich – wartet auf Sprechpause) -->
<div aria-live="polite" aria-atomic="true" class="status">
  <!-- Inhaltsaktualisierungen für Screenreader angekündigt -->
</div>

<!-- Dringende Warnungen (durchsetzungsfähig – Unterbrechungen) -->
<div role="alert" aria-live="assertive">
  <!-- Unterbricht die aktuelle Ankündigung -->
</div>
„

„Javascript
Funktion showNotification(message, type = 'höflich') {
  const container = document.getElementById(`${type}-announcer`);
  container.textContent = '';
  requestAnimationFrame(() => {
    container.textContent = Nachricht;
  });
}
„

Leeren Sie den Container vor dem Schreiben, um sicherzustellen, dass dieselbe Nachricht eine neue Ankündigung auslöst.

---

## Screenreader-Befehle

Kurzanleitung für die gängigsten Screenreader-Tastenkombinationen.

| Aktion | VoiceOver (Mac) | NVDA (Windows) |
|--------|-----------------|----------------|
| Start/Stopp | ⌘ + F5 | Strg + Alt + N |
| Nächster Artikel | VO + → | ↓ |
| Vorheriger Artikel | VO + ← | ↑ |
| Aktivieren | VO + Leertaste | Geben Sie | ein
| Überschriftenliste | VO + U, dann Pfeile | H / Umschalt + H |
| Linkliste | VO + U | K / Umschalt + K |
# アクセシビリティ コード パターン

一般的なアクセシビリティ要件に対応する、コピー＆ペースト可能な実用的なパターン。各パターンは自己完結型であり、メインの [SKILL.md](../SKILL.md) からリンクされています。

---

## モーダル フォーカス トラップ

キーボード フォーカスをモーダル ダイアログ内にトラップして、Tab/Shift+Tab でフォーカス可能な要素を循環させ、Escape でダイアログを閉じます。

```JavaScript
関数 openModal(モーダル) {
  const focusableElements = modal.querySelectorAll(
    'ボタン、[href]、入力、選択、テキストエリア、[tabindex]:not([tabindex="-1"])'
  );
  const firstElement = focusableElements[0];
  const lastElement = focusableElements[focusableElements.length - 1];

  modal.addEventListener('keydown', (e) => {
    if (e.key === 'タブ') {
      if (e.shiftKey && document.activeElement === firstElement) {
        e.preventDefault();
        lastElement.focus();
      } else if (!e.shiftKey && document.activeElement === lastElement) {
        e.preventDefault();
        firstElement.focus();
      }
    }
    if (e.key === 'エスケープ') {
      closeModal();
    }
  });

  firstElement.focus();
}
「」

ネイティブの `<dialog>` 要素はフォーカス トラッピングを自動的に処理します。ブラウザのサポートが許可する場合は、この要素を使用することをお勧めします。

---

## リンクをスキップ

キーボード ユーザーが繰り返しのナビゲーションをバイパスして、メイン コンテンツに直接ジャンプできるようにします。

```html
<本文>
  <a href="#main-content" class="skip-link">メイン コンテンツにスキップ</a>
  <header><!-- ナビゲーション --></header>
  <main id="メインコンテンツ" tabindex="-1">
    <!-- メインコンテンツ -->
  </メイン>
</body>
「」

```css
.スキップリンク {
  位置: 絶対;
  上: -40px;
  左: 0;
  背景: #000;
  色: #fff;
  パディング: 8px 16px;
  z インデックス: 100;
}

.skip-link:focus {
  トップ: 0;
}
「」

---

## エラー処理

スクリーン リーダーにエラーを通知し、送信時に最初の無効なフィールドに焦点を当てます。

```html
<フォームの検証>
  <div class="field" aria-live="polite">
    <label for="email">メール</label>
    <input type="電子メール" id="電子メール"
           aria-invalid="true"
           aria-descriptionby="電子メールエラー">
    <p id="email-error" class="error" role="alert">
      有効な電子メール アドレスを入力してください (例: name@example.com)
    </p>
  </div>
</form>
「」

```JavaScript
form.addEventListener('submit', (e) => {
  const firstError = form.querySelector('[aria-invalid="true"]');
  if (firstError) {
    e.preventDefault();
    firstError.focus();

    const errorsummary = document.getElementById('error-summary');
    error概要.textContent =
      `${errors.length} 個のエラーが見つかりました。修正して再試行してください。`;
    error概要.focus();
  }
});
「」

---

## フォームラベル

すべての入力には、明示的 (`for`/`id`) または暗黙的 (`<label>` のラッピング) のいずれかの関連付けられたラベルが必要です。

```html
<!-- ❌ ラベルの関連付けがありません -->
<input type="email" placeholder="Email">

<!-- ✅ 明示的なラベル -->
<label for="email">メールアドレス</label>
<input type="電子メール" id="電子メール" name="電子メール"
       autocomplete="電子メール" 必須>

<!-- ✅ 暗黙的なラベル -->
<ラベル>
  メールアドレス
  <input type="email" name="email" autocomplete="email" 必須>
</label>

<!-- ✅ 説明書付き -->
<label for="password">パスワード</label>
<input type="パスワード" id="パスワード"
       aria-descriptedby="パスワード要件">
<p id="パスワード要件">
  少なくとも 8 文字と 1 つの数字を含める必要があります。
</p>
「」

---

## ドラッグ動作

ドラッグによってトリガーされるアクションはすべて、単一ポインターの代替手段を提供する必要があります (WCAG 2.5.7)。

```html
<!-- ❌ ドラッグのみで並べ替え -->
<ul class="sortable-list" draggable="true">
  <li>項目 1</li>
  <li>項目 2</li>
</ul>

<!-- ✅ ドラッグ + ボタンの代替 -->
<ul class="sortable-list">
  <リ>
    <span>アイテム 1</span>
    <button aria-label="項目 1 を上に移動">↑</button>
    <button aria-label="項目 1 を下に移動">↓</button>
  </li>
  <リ>
    <span>アイテム 2</span>
    <button aria-label="項目 2 を上に移動">↑</button>
    <button aria-label="項目 2 を下に移動">↓</button>
  </li>
</ul>
「」

スライダー、マップ パン、カラー ピッカー、および同様のドラッグ ベースのウィジェットにも適用され、常に同等のクリック/タップまたはキーボード パスが提供されます。

---

## ARIA タブ

タブには、適切な `aria-selected`、`aria-controls`、およびキーボード サポートを備えた `role="tablist"`、`role="tab"`、および `role="tabpanel"` が必要です。

```html
<div role="tablist" aria-label="製品情報">
  <button role="tab" id="tab-1" aria-selected="true"
          aria-controls="panel-1">説明</button>
  <button role="tab" id="tab-2" aria-selected="false"
          aria-controls="panel-2" tabindex="-1">レビュー</button>
</div>
<div role="tabpanel" id="panel-1" aria-labeledby="tab-1">
  <!-- パネルのコンテンツ -->
</div>
<div role="tabpanel" id="panel-2" aria-labelledby="tab-2" hidden>
  <!-- パネルのコンテンツ -->
</div>
「」

矢印キーはタブ間でフォーカスを移動する必要があります。アクティブなタブは `tabindex="0"` を受け取りますが、非アクティブなタブは `tabindex="-1"` を使用します。

---

## ライブリージョンと通知

`aria-live` を使用すると、フォーカスを移動せずに動的なコンテンツの変更をスクリーン リーダーに通知できます。

```html
<!-- ステータス更新 (礼儀正しく — スピーチの一時停止を待ちます) -->
<div aria-live="polite" aria-atomic="true" class="status">
  <!-- スクリーン リーダーにコンテンツの更新を発表 -->
</div>

<!-- 緊急アラート (アサティブ — 割り込み) -->
<div role="alert" aria-live="assertive">
  <!-- 現在のアナウンスを中断します -->
</div>
「」

```JavaScript
function showNotification(message, type = 'polite') {
  const コンテナ = document.getElementById(`${type}-announcer`);
  コンテナ.テキストコンテンツ = '';
  requestAnimationFrame(() => {
    コンテナ.テキストコンテンツ = メッセージ;
  });
}
「」

同じメッセージが新しいアナウンスをトリガーするように、書き込む前にコンテナをクリアしてください。

---

## スクリーン リーダー コマンド

最も一般的なスクリーン リーダーのショートカットのクイック リファレンス。

|アクション | VoiceOver (Mac) | NVDA (Windows) |
|------|-----------------|----------------|
|スタート/ストップ | ⌘ + F5 | Ctrl + Alt + N |
|次の項目 | VO + → | ↓ |
|前の項目 | VO + ← | ↑ |
|アクティブにする | VO + スペース | | を入力してください
|見出しリスト | VO + U、次に矢印 | H / Shift + H |
|リンクリスト | VO + U | K / Shift + K |
# 辅助功能代码模式

实用、可复制粘贴的模式，可满足常见的可访问性要求。每个模式都是独立的，并从主 [SKILL.md](../SKILL.md) 链接。

---

## 模态焦点陷阱

将键盘焦点捕获在模式对话框内，以便 Tab/Shift+Tab 循环浏览其可聚焦元素，然后 Escape 将其关闭。

```javascript
函数 openModal(模态) {
  const focusableElements = modal.querySelectorAll(
    '按钮，[href]，输入，选择，文本区域，[tabindex]：not（[tabindex =“-1”]）'
  ）；
  常量firstElement = focusableElements[0];
  const lastElement = focusableElements[focusableElements.length - 1];

  modal.addEventListener('keydown', (e) => {
    if (e.key === 'Tab') {
      if (e.shiftKey && document.activeElement === firstElement) {
        e.preventDefault();
        最后元素.focus();
      } else if (!e.shiftKey && document.activeElement === lastElement) {
        e.preventDefault();
        firstElement.focus();
      }
    }
    if (e.key === 'Escape') {
      关闭模态（）；
    }
  });

  firstElement.focus();
}
````

本机“<dialog>”元素自动处理焦点捕获 - 在浏览器支持允许的情况下首选它。

---

## 跳过链接

允许键盘用户绕过重复的导航并直接跳转到主要内容。

````html
<正文>
  <a href="#main-content" class="skip-link">跳至主要内容</a>
  <header><!-- 导航 --></header>
  <main id="main-content" tabindex="-1">
    <!-- 主要内容 -->
  </主要>
</正文>
````

````CSS
.skip-link {
  位置：绝对；
  顶部：-40px；
  左：0；
  背景：#000；
  颜色：#fff；
  内边距：8 像素 16 像素；
  z 索引：100；
}

.skip-link:焦点{
  顶部：0；
}
````

---

## 错误处理

向屏幕阅读器宣布错误，并将第一个无效字段集中在提交上。

````html
<形式novalidate>
  <div class="field" aria-live="polite">
    <标签=“电子邮件”>电子邮件</标签>
    <输入类型=“电子邮件”ID=“电子邮件”
           咏叹调无效=“真”
           aria-描述的=“电子邮件错误”>
    <p id="email-error" class="error" role="alert">
      请输入有效的电子邮件地址（例如 name@example.com）
    </p>
  </div>
</形式>
````

```javascript
form.addEventListener('提交', (e) => {
  const firstError = form.querySelector('[aria-invalid="true"]');
  如果（第一个错误）{
    e.preventDefault();
    FirstError.focus();

    const errorSummary = document.getElementById('错误摘要');
    错误摘要.textContent =
      发现`${errors.length} 错误。请修复它们并重试。`;
    errorSummary.focus();
  }
});
````

---

## 表单标签

每个输入都需要一个关联的标签 - 显式（`for`/`id`）或隐式（包装 `<label>`）。

````html
<!-- ❌ 无标签关联 -->
<输入类型=“电子邮件”占位符=“电子邮件”>

<!-- ✅ 显式标签 -->
<label for="email">电子邮件地址</label>
<输入类型=“电子邮件”id=“电子邮件”名称=“电子邮件”
       自动完成=“需要电子邮件”>

<!-- ✅ 隐式标签 -->
<标签>
  电子邮件地址
  <输入类型=“电子邮件”名称=“电子邮件”自动完成=“电子邮件”必需>
</标签>

<!-- ✅ 有说明 -->
<label for="password">密码</label>
<输入类型=“密码”id=“密码”
       aria-描述的=“密码要求”>
<p id="密码要求">
  必须至少包含 8 个字符和 1 个数字。
</p>
````

---

## 拖动动作

由拖动触发的任何操作都必须提供单指针替代方案 (WCAG 2.5.7)。

````html
<!-- ❌ 仅拖动重新排序 -->
<ul class="sortable-list"draggable="true">
  <li>第 1 项</li>
  <li>第 2 项</li>
</ul>

<!-- ✅ 拖动 + 按钮替代方案 -->
<ul class="可排序列表">
  <li>
    <span>项目 1</span>
    <button aria-label="向上移动项目 1">↑</button>
    <button aria-label="向下移动项目 1">↓</button>
  </li>
  <li>
    <span>项目 2</span>
    <button aria-label="向上移动项目 2">↑</button>
    <button aria-label="向下移动项目 2">↓</button>
  </li>
</ul>
````

也适用于滑块、地图平移、颜色选择器和类似的基于拖动的小部件 - 始终提供等效的单击/点击或键盘路径。

---

## ARIA 标签

选项卡需要 `role="tablist"`、`role="tab"` 和 `role="tabpanel"` 以及适当的 `aria-selected`、`aria-controls` 和键盘支持。

````html
<div role="tablist" aria-label="产品信息">
  <按钮角色=“选项卡”id=“tab-1”aria-selected=“true”
          aria-controls="panel-1">说明</button>
  <按钮角色=“选项卡”id=“tab-2”aria-selected=“假”
          aria-controls="panel-2" tabindex="-1">评论</button>
</div>
<div role="tabpanel" id="panel-1" aria-labelledby="tab-1">
  <!-- 面板内容 -->
</div>
<div role="tabpanel" id="panel-2" aria-labelledby="tab-2" 隐藏>
  <!-- 面板内容 -->
</div>
````

箭头键应在选项卡之间移动焦点；活动选项卡接收 `tabindex="0"`，而非活动选项卡使用 `tabindex="-1"`。

---

## 实时区域和通知

使用“aria-live”向屏幕阅读器宣布动态内容更改，而无需移动焦点。

````html
<!-- 状态更新（礼貌 — 等待讲话暂停）-->
<div aria-live="礼貌" aria-atomic="true" class="status">
  <!-- 向屏幕阅读器宣布内容更新 -->
</div>

<!-- 紧急警报（断言 — 中断）-->
<div role="alert" aria-live="assertive">
  <!-- 中断当前公告 -->
</div>
````

```javascript
函数 showNotification(消息, type = '礼貌') {
  const container = document.getElementById(`${type}-announcer`);
  容器.textContent = '';
  请求动画帧(() => {
    容器.textContent = 消息;
  });
}
````

在写入之前清除容器，以确保相同的消息触发新的公告。

---

## 屏幕阅读器命令

最常见屏幕阅读器快捷方式的快速参考。

|行动|旁白 (Mac) | NVDA（Windows）|
|--------|-----------------|----------------|
|开始/停止| ⌘ + F5 | Ctrl + Alt + N |
|下一项 | VO + → | ↓ |
|上一条 |画外音 + ← | ↑ |
|激活 |画外音 + 空间 |输入|
|标题列表 | VO + U，然后是箭头 | H / Shift + H |
|链接列表 | VO + U | K / Shift + K |
# Шаблони коду доступності

Практичні шаблони, готові до копіювання та вставлення, для стандартних вимог до доступності. Кожен шаблон є самодостатнім і пов’язаний із головним [SKILL.md](../SKILL.md).

---

## Модальна пастка фокусування

Перехоплюйте фокус клавіатури в модальному діалоговому вікні, щоб Tab/Shift+Tab циклічно переходили між його елементами, на які можна фокусувати, а Escape закривав його.

```javascript
функція openModal(modal) {
  const focusableElements = modal.querySelectorAll(
    'button, [href], input, select, textarea, [tabindex]:not([tabindex="-1"])'
  );
  const firstElement = focusableElements[0];
  const lastElement = focusableElements[focusableElements.length - 1];

  modal.addEventListener('keydown', (e) => {
    if (e.key === 'Tab') {
      if (e.shiftKey && document.activeElement === firstElement) {
        e.preventDefault();
        lastElement.focus();
      } else if (!e.shiftKey && document.activeElement === lastElement) {
        e.preventDefault();
        firstElement.focus();
      }
    }
    if (e.key === 'Escape') {
      closeModal();
    }
  });

  firstElement.focus();
}
```

Власний елемент `<dialog>` автоматично обробляє захоплення фокусу — віддавайте перевагу, якщо це дозволяє підтримка браузера.

---

## Пропустити посилання

Дозволяє користувачам клавіатури обходити повторювану навігацію та переходити прямо до основного вмісту.

```html
<тіло>
  <a href="#main-content" class="skip-link">Перейти до основного вмісту</a>
  <header><!-- navigation --></header>
  <main id="main-content" tabindex="-1">
    <!-- основний зміст -->
  </main>
</body>
```

```css
.skip-link {
  позиція: абсолютна;
  зверху: -40px;
  ліворуч: 0;
  фон: #000;
  колір: #fff;
  відступ: 8px 16px;
  z-індекс: 100;
}

.skip-link:focus {
  зверху: 0;
}
```

---

## Обробка помилок

Повідомте про помилки програмі зчитування з екрана та зосередьте перше недійсне поле під час надсилання.

```html
<form novalidate>
  <div class="field" aria-live="pote">
    <label for="email">Електронна пошта</label>
    <input type="email" id="email"
           aria-invalid="true"
           aria-describedby="email-error">
    <p id="email-error" class="error" role="alert">
      Введіть дійсну адресу електронної пошти (наприклад, name@example.com)
    </p>
  </div>
</form>
```

```javascript
form.addEventListener('submit', (e) => {
  const firstError = form.querySelector('[aria-invalid="true"]');
  if (firstError) {
    e.preventDefault();
    firstError.focus();

    const errorSummary = document.getElementById('error-summary');
    errorSummary.textContent =
      `${errors.length} знайдено помилок. Виправте їх і повторіть спробу.`;
    errorSummary.focus();
  }
});
```

---

## Мітки форм

Кожен вхід потребує пов’язаної мітки — явної (`for`/`id`) або неявної (обертання `<label>`).

```html
<!-- ❌ Немає асоціації з міткою -->
<input type="email" placeholder="Email">

<!-- ✅ Відвертий ярлик -->
<label for="email">Адреса електронної пошти</label>
<input type="email" id="email" name="email"
       autocomplete="email" потрібно>

<!-- ✅ Неявна мітка -->
<мітка>
  Адреса електронної пошти
  <input type="email" name="email" autocomplete="email" потрібно>
</label>

<!-- ✅ З інструкціями -->
<label for="password">Пароль</label>
<input type="password" id="password"
       aria-describedby="вимоги до пароля">
<p id="вимоги до пароля">
  Має бути не менше 8 символів з одним числом.
</p>
```

---

## Рухи перетягування

Будь-яка дія, викликана перетягуванням, має пропонувати альтернативу з одним вказівником (WCAG 2.5.7).

```html
<!-- ❌ Перевпорядкування лише перетягуванням -->
<ul class="sortable-list" draggable="true">
  <li>Пункт 1</li>
  <li>Пункт 2</li>
</ul>

<!-- ✅ Перетягніть + альтернативні кнопки -->
<ul class="sortable-list">
  <li>
    <span>Пункт 1</span>
    <button aria-label="Перемістити елемент 1 вгору">↑</button>
    <button aria-label="Перемістити елемент 1 вниз">↓</button>
  </li>
  <li>
    <span>Пункт 2</span>
    <button aria-label="Перемістити елемент 2 вгору">↑</button>
    <button aria-label="Перемістити елемент 2 вниз">↓</button>
  </li>
</ul>
```

Також стосується повзунків, панорамування карти, засобів вибору кольорів і подібних віджетів на основі перетягування — завжди надавайте еквівалентний шлях клацання/дотику чи клавіатури.

---

## вкладки ARIA

Для вкладок потрібні `role="tablist"`, `role="tab"` і `role="tabpanel"` з належною підтримкою `aria-selected`, `aria-controls` і клавіатури.

```html
<div role="tablist" aria-label="Інформація про продукт">
  <button role="tab" id="tab-1" aria-selected="true"
          aria-controls="panel-1">Опис</button>
  <button role="tab" id="tab-2" aria-selected="false"
          aria-controls="panel-2" tabindex="-1">Відгуки</button>
</div>
<div role="tabpanel" id="panel-1" aria-labelledby="tab-1">
  <!-- Вміст панелі -->
</div>
<div role="tabpanel" id="panel-2" aria-labelledby="tab-2" hidden>
  <!-- Вміст панелі -->
</div>
```

Клавіші зі стрілками повинні переміщувати фокус між вкладками; активна вкладка отримує `tabindex="0"`, тоді як неактивні вкладки використовують `tabindex="-1"`.

---

## Активні регіони та сповіщення

Використовуйте `aria-live`, щоб сповіщати про динамічні зміни вмісту програмами зчитування з екрана без переміщення фокуса.

```html
<!-- Оновлення статусу (ввічливий — очікує паузи в мовленні) -->
<div aria-live="ввічливий" aria-atomic="true" class="статус">
  <!-- Оновлення вмісту для програм зчитування з екрана -->
</div>

<!-- Термінові сповіщення (асертивні — переривання) -->
<div role="alert" aria-live="assertive">
  <!-- Перериває поточне оголошення -->
</div>
```

```javascript
функція showNotification(повідомлення, тип = 'ввічливий') {
  const container = document.getElementById(`${type}-announcer`);
  container.textContent = '';
  requestAnimationFrame(() => {
    container.textContent = повідомлення;
  });
}
```

Очистіть контейнер перед написанням, щоб переконатися, що те саме повідомлення ініціює нове оголошення.

---

## Команди програми зчитування з екрана

Короткий довідник для найпоширеніших комбінацій клавіш програми зчитування з екрана.

| Дія | VoiceOver (Mac) | NVDA (Windows) |
|--------|----------------|----------------|
| Пуск/Зупинка | ⌘ + F5 | Ctrl + Alt + N |
| Наступний пункт | VO + → | ↓ |
| Попередній пункт | VO + ← | ↑ |
| Активувати | VO + пробіл | Введіть |
| Список заголовків | VO + U, потім стрілки | H / Shift + H |
| Список посилань | VO + U | K / Shift + K |
# Шаблоны кода доступности

Практичные шаблоны, готовые к копированию и вставке, отвечающие общим требованиям доступности. Каждый шаблон является автономным и связан с основным файлом [SKILL.md](../SKILL.md).

---

## Модальная ловушка фокуса

Захватите фокус клавиатуры внутри модального диалогового окна, чтобы клавиши Tab/Shift+Tab циклически перемещались по фокусируемым элементам, а Escape закрывал его.

```Javascript
функция openModal(модальный) {
  const focusableElements = modal.querySelectorAll(
    'кнопка, [href], ввод, выбор, текстовая область, [tabindex]:not([tabindex="-1"])'
  );
  const firstElement = focusableElements[0];
  const LastElement = focusableElements[focusableElements.length - 1];

  modal.addEventListener('keydown', (e) => {
    if (e.key === 'Tab') {
      if (e.shiftKey && document.activeElement === firstElement) {
        е.preventDefault();
        последнийЭлемент.фокус();
      } else if (!e.shiftKey && document.activeElement === LastElement) {
        е.preventDefault();
        первыйЭлемент.фокус();
      }
    }
    if (e.key === 'Escape') {
      закрытьМодальный();
    }
  });

  первыйЭлемент.фокус();
}
```

Собственный элемент `<dialog>` автоматически обрабатывает захват фокуса — предпочтите его, если это позволяет поддержка браузера.

---

## Пропустить ссылку

Позволяет пользователям клавиатуры обходить повторяющуюся навигацию и сразу переходить к основному содержимому.

```html
<тело>
  <a href="#main-content" class="skip-link">Перейти к основному содержанию</a>
  <header><!-- навигация --></header>
  <main id="main-content" tabindex="-1">
    <!-- основное содержание -->
  </главный>
</тело>
```

``` CSS
.skip-ссылка {
  позиция: абсолютная;
  верх: -40 пикселей;
  слева: 0;
  фон: #000;
  цвет: #fff;
  отступы: 8 пикселей 16 пикселей;
  z-индекс: 100;
}

.skip-link:focus {
  верх: 0;
}
```

---

## Обработка ошибок

Сообщайте об ошибках программам чтения с экрана и фокусируйте внимание на первом недопустимом поле при отправке.

```html
<форма novalidate>
  <div class="field" aria-live="polite">
    <label for="email">Электронная почта</label>
    <input type="электронная почта" id="электронная почта"
           ария-инвалид="истина"
           aria-describedby="email-error">
    <p id="email-error" class="error" role="alert">
      Введите действительный адрес электронной почты (например, name@example.com).
    </p>
  </div>
</форма>
```

```Javascript
form.addEventListener('submit', (e) => {
  const firstError = form.querySelector('[aria-invalid="true"]');
  если (первая ошибка) {
    е.preventDefault();
    первая ошибка.фокус();

    const errorSummary = document.getElementById('error-summary');
    errorSummary.textContent =
      `${errors.length} Обнаружены ошибки. Пожалуйста, исправьте их и повторите попытку.`;
    errorSummary.focus();
  }
});
```

---

## Метки формы

Каждому входу требуется связанная метка — явная (for/id) или неявная (обертка <label>).

```html
<!-- ❌ Без привязки меток -->
<input type="электронная почта" Placeholder="Электронная почта">

<!-- ✅ Явная метка -->
<label for="email">Адрес электронной почты</label>
<input type="email" id="email" name="email"
       требуется autocomplete="электронная почта">

<!-- ✅ Неявная метка -->
<метка>
  Адрес электронной почты
  <input type="email" name="email" autocomplete="email" требуется>
</метка>

<!-- ✅ С инструкцией -->
<label for="password">Пароль</label>
<input type="пароль" id="пароль"
       aria-describedby="требования к паролю">
<p id="требования к паролю">
  Должно быть не менее 8 символов с одной цифрой.
</p>
```

---

## Перетаскивание движений

Любое действие, запускаемое перетаскиванием, должно предлагать альтернативу с одним указателем (WCAG 2.5.7).

```html
<!-- ❌ Изменение порядка только перетаскиванием -->
<ul class="sortable-list" draggable="true">
  <li>Пункт 1</li>
  <li>Пункт 2</li>
</ul>

<!-- ✅ Альтернативы перетаскивания + кнопки -->
<ul class="сортируемый-список">
  <ли>
    <span>Элемент 1</span>
    <button aria-label="Переместить элемент 1 вверх">↑</button>
    <button aria-label="Переместить элемент 1 вниз">↓</button>
  </li>
  <ли>
    <span>Пункт 2</span>
    <button aria-label="Переместить элемент 2 вверх">↑</button>
    <button aria-label="Переместить элемент 2 вниз">↓</button>
  </li>
</ul>
```

Также применимо к ползункам, панорамированию карты, палитрам цветов и аналогичным виджетам на основе перетаскивания — всегда предоставляйте эквивалентный щелчок/касание или путь с клавиатуры.

---

## вкладки ARIA

Для вкладок требуются `role="tablist"`, `role="tab"` и `role="tabpanel"` с соответствующей поддержкой `aria-selected`, `aria-controls` и клавиатуры.

```html
<div role="tablist" aria-label="Информация о продукте">
  <button role="tab" id="tab-1" aria-selected="true"
          aria-controls="panel-1">Описание</button>
  <button role="tab" id="tab-2" aria-selected="false"
          aria-controls="panel-2" tabindex="-1">Отзывы</button>
</div>
<div role="tabpanel" id="panel-1" aria-labelledby="tab-1">
  <!-- Содержимое панели -->
</div>
<div role="tabpanel" id="panel-2" aria-labelledby="tab-2" скрыто>
  <!-- Содержимое панели -->
</div>
```

Клавиши со стрелками должны перемещать фокус между вкладками; активная вкладка получает `tabindex="0"`, а неактивные вкладки используют `tabindex="-1"`.

---

## Живые регионы и уведомления

Используйте `aria-live`, чтобы объявлять динамические изменения контента для программ чтения с экрана без перемещения фокуса.

```html
<!-- Обновление статуса (вежливо — ждет паузы в речи) -->
<div aria-live="polite" aria-atomic="true" class="status">
  <!-- Объявлены обновления контента для программ чтения с экрана -->
</div>

<!-- Срочные оповещения (напористые — прерывания) -->
<div role="alert" aria-live="assertive">
  <!-- Прерывает текущее объявление -->
</div>
```

```Javascript
функция showNotification(message, type = 'вежливый') {
  constContainer = document.getElementById(`${type}-announcer`);
  Container.textContent = '';
  requestAnimationFrame(() => {
    Container.textContent = сообщение;
  });
}
```

Очистите контейнер перед записью, чтобы одно и то же сообщение вызывало новое объявление.

---

## Команды чтения с экрана

Краткий справочник по наиболее распространенным сочетаниям клавиш для чтения с экрана.

| Действие | VoiceOver (Mac) | НВДА (Windows) |
|--------|-----------------|----------------|
| Старт/Стоп | ⌘ + F5 | Ctrl + Alt + Н |
| Следующий элемент | ВО + → | ↓ |
| Предыдущий элемент | ВО + ← | ↑ |
| Активировать | VO + Космос | Войти |
| Список рубрик | VO + U, затем стрелки | Ч / Shift + Ч |
| Список ссылок | ВО + У | К / Shift + К |
# Modelli di codici di accessibilità

Modelli pratici e pronti per il copia-incolla per i requisiti comuni di accessibilità. Ogni pattern è autonomo e collegato dal file principale [SKILL.md](../SKILL.md).

---

## Trappola del focus modale

Intrappola il focus della tastiera all'interno di una finestra di dialogo modale in modo che Tab/Maiusc+Tab scorra gli elementi attivabili ed Escape la chiuda.

```javascript
funzione openModale(modale) {
  const focusableElements = modal.querySelectorAll(
    'pulsante, [href], input, seleziona, textarea, [tabindex]:not([tabindex="-1"])'
  );
  const primoElemento = focusableElements[0];
  const ultimoElemento = focusableElements[focusableElements.length - 1];

  modal.addEventListener('keydown', (e) => {
    if (e.tasto === 'Tab') {
      if (e.shiftKey && document.activeElement === primoElemento) {
        e.preventDefault();
        ultimoElemento.focus();
      } else if (!e.shiftKey && document.activeElement === lastElement) {
        e.preventDefault();
        primoElemento.focus();
      }
    }
    if (e.key === 'Escape') {
      chiudiModale();
    }
  });

  primoElemento.focus();
}
```

L'elemento nativo "<dialog>" gestisce automaticamente il focus trapping: è preferibile quando il supporto del browser lo consente.

---

## Salta il collegamento

Consente agli utenti della tastiera di ignorare la navigazione ripetitiva e passare direttamente al contenuto principale.

```html
<corpo>
  <a href="#main-content" class="skip-link">Vai al contenuto principale</a>
  <header><!-- navigazione --></header>
  <main id="contenuto-principale" tabindex="-1">
    <!-- contenuto principale -->
  </main>
</corpo>
```

```css
.salta collegamento {
  posizione: assoluta;
  in alto: -40px;
  a sinistra: 0;
  sfondo: #000;
  colore: #fff;
  imbottitura: 8px 16px;
  indice z: 100;
}

.skip-link:focus {
  superiore: 0;
}
```

---

## Gestione degli errori

Annuncia gli errori agli screen reader e focalizza il primo campo non valido sull'invio.

```html
<form novalidate>
  <div class="field" aria-live="educato">
    <label for="email">E-mail</label>
    <input type="e-mail" id="e-mail"
           aria-invalid="vero"
           aria-descriptionby="email-error">
    <p id="email-error" class="error" role="alert">
      Inserisci un indirizzo email valido (ad esempio, nome@esempio.com)
    </p>
  </div>
</forma>
```

```javascript
form.addEventListener('invia', (e) => {
  const firstError = form.querySelector('[aria-invalid="true"]');
  se (primoErrore) {
    e.preventDefault();
    primoErrore.focus();

    const errorSummary = document.getElementById('error-summary');
    errorSummary.textContent =
      `Trovati errori ${errors.length}. Correggili e riprova.`;
    errorSummary.focus();
  }
});
```

---

## Etichette del modulo

Ogni input necessita di un'etichetta associata, esplicita (`for`/`id`) o implicita (che racchiude `<label>`).

```html
<!-- ❌ Nessuna associazione di etichette -->
<input type="email" placeholder="Email">

<!-- ✅ Etichetta esplicita -->
<label for="email">Indirizzo email</label>
<input type="e-mail" id="e-mail" nome="e-mail"
       completamento automatico="email" obbligatorio>

<!-- ✅ Etichetta implicita -->
<etichetta>
  Indirizzo e-mail
  <input type="email" name="email" autocomplete="email" richiesto>
</etichetta>

<!-- ✅ Con istruzioni -->
<label for="password">Password</label>
<tipo input="password" id="password"
       aria-descriptionby="requisiti-password">
<p id="requisiti-password">
  Deve contenere almeno 8 caratteri con un numero.
</p>
```

---

## Movimenti di trascinamento

Qualsiasi azione innescata dal trascinamento deve offrire un'alternativa a puntatore singolo (WCAG 2.5.7).

```html
<!-- ❌ Riordino con solo trascinamento -->
<ul class="sortable-list" draggable="true">
  <li>Elemento 1</li>
  <li>Articolo 2</li>
</ul>

<!-- ✅ Trascina + pulsanti alternativi -->
<ul class="lista-ordinabile">
  <li>
    <span>Elemento 1</span>
    <button aria-label="Sposta elemento 1 in alto">↑</button>
    <button aria-label="Sposta elemento 1 verso il basso">↓</button>
  </li>
  <li>
    <span>Elemento 2</span>
    <button aria-label="Sposta elemento 2 in alto">↑</button>
    <button aria-label="Sposta elemento 2 verso il basso">↓</button>
  </li>
</ul>
```

Si applica anche a dispositivi di scorrimento, panoramica della mappa, selettori di colori e widget simili basati sul trascinamento: fornisci sempre un clic/tocco equivalente o un percorso da tastiera.

---

## Schede ARIA

Le schede richiedono `role="tablist"`, `role="tab"` e `role="tabpanel"` con il corretto supporto per `aria-selected`, `aria-controls` e tastiera.

```html
<div role="tablist" aria-label="Informazioni sul prodotto">
  <button role="tab" id="tab-1" aria-selected="true"
          aria-controls="panel-1">Descrizione</button>
  <button role="tab" id="tab-2" aria-selected="false"
          aria-controls="panel-2" tabindex="-1">Recensioni</button>
</div>
<div role="tabpanel" id="panel-1" aria-labelledby="tab-1">
  <!-- Contenuto del pannello -->
</div>
<div role="tabpanel" id="panel-2" aria-labelledby="tab-2" nascosto>
  <!-- Contenuto del pannello -->
</div>
```

I tasti freccia dovrebbero spostare lo stato attivo tra le schede; la scheda attiva riceve `tabindex="0"` mentre le schede inattive utilizzano `tabindex="-1"`.

---

## Regioni e notifiche in tempo reale

Utilizza "aria-live" per annunciare le modifiche ai contenuti dinamici agli screen reader senza spostare il focus.

```html
<!-- Aggiornamenti di stato (educato - attende la pausa nel discorso) -->
<div aria-live="educato" aria-atomic="true" class="status">
  <!-- Aggiornamenti dei contenuti annunciati agli screen reader -->
</div>

<!-- Avvisi urgenti (assertivo - interruzioni) -->
<div role="alert" aria-live="assertivo">
  <!-- Interrompe l'annuncio corrente -->
</div>
```

```javascript
funzione mostraNotifica(messaggio, tipo = 'educato') {
  const contenitore = document.getElementById(`${type}-announcer`);
  contenitore.testoContenuto = '';
  requestAnimationFrame(() => {
    contenitore.textContent = messaggio;
  });
}
```

Svuotare il contenitore prima di scrivere per garantire che lo stesso messaggio attivi un nuovo annuncio.

---

## Comandi del lettore di schermo

Riferimento rapido per le scorciatoie più comuni dello screen reader.

| Azione | VoiceOver (Mac) | NVDA (Windows) |
|--------|-----------------|----------------|
| Avvia/Interrompi | ⌘ + F5 | Ctrl + Alt + N |
| Articolo successivo | VO + → | ↓ |
| Elemento precedente | VO + ← | ↑ |
| Attiva | VO + Spazio | Inserisci |
| Elenco titoli | VO + U, poi frecce | H / Maiusc + H |
| Elenco collegamenti | VO + U | K / Maiusc + K |
# Padrões de código de acessibilidade

Padrões práticos e prontos para copiar e colar para requisitos comuns de acessibilidade. Cada padrão é independente e vinculado ao [SKILL.md](../SKILL.md) principal.

---

## Armadilha de foco modal

Trapa o foco do teclado dentro de uma caixa de diálogo modal para que Tab/Shift+Tab percorra seus elementos focáveis e Escape o feche.

```javascript
função openModal(modal) {
  const focusableElements = modal.querySelectorAll(
    'botão, [href], entrada, seleção, área de texto, [tabindex]:not([tabindex="-1"])'
  );
  const primeiroElement = focusableElements[0];
  const lastElement = focusableElements[focusableElements.length - 1];

  modal.addEventListener('keydown', (e) => {
    if (e.key === 'Tab') {
      if (e.shiftKey && document.activeElement === firstElement) {
        e.preventDefault();
        lastElement.focus();
      } else if (!e.shiftKey && document.activeElement === lastElement) {
        e.preventDefault();
        primeiroElement.focus();
      }
    }
    if (e.key === 'Escape') {
      fecharModal();
    }
  });

  primeiroElement.focus();
}
```

O elemento nativo `<dialog>` lida com a captura de foco automaticamente – prefira-o quando o suporte do navegador permitir.

---

## Pular link

Permite que os usuários do teclado ignorem a navegação repetitiva e pulem direto para o conteúdo principal.

```html
<corpo>
  <a href="#main-content" class="skip-link">Pular para o conteúdo principal</a>
  <header><!-- navegação --></header>
  <main id="main-content" tabindex="-1">
    <!-- conteúdo principal -->
  </principal>
</body>
```

```css
.skip-link {
  posição: absoluta;
  superior: -40px;
  esquerda: 0;
  plano de fundo: #000;
  cor: #fff;
  preenchimento: 8px 16px;
  índice z: 100;
}

.skip-link:foco {
  superior: 0;
}
```

---

## Tratamento de erros

Anuncie erros aos leitores de tela e concentre o primeiro campo inválido no envio.

```html
<formulário novalidate>
  <div class="campo" aria-live="educado">
    <label for="email">E-mail</label>
    <input type="e-mail" id="e-mail"
           aria-inválido="verdadeiro"
           aria-describedby="email-error">
    <p id="email-error" class="error" role="alert">
      Insira um endereço de e-mail válido (por exemplo, nome@example.com)
    </p>
  </div>
</form>
```

```javascript
form.addEventListener('enviar', (e) => {
  const firstError = form.querySelector('[aria-invalid="true"]');
  if (primeiroErro) {
    e.preventDefault();
    primeiroErro.focus();

    const errorSummary = document.getElementById('resumo do erro');
    errorSummary.textContent =
      `${errors.length} erros encontrados. Por favor, corrija-os e tente novamente.`;
    erroSummary.focus();
  }
});
```

---

## Rótulos de formulário

Cada entrada precisa de um rótulo associado - seja explícito (`for`/`id`) ou implícito (quebrando `<label>`).

```html
<!-- ❌ Sem associação de rótulo -->
<input type="e-mail" placeholder="E-mail">

<!-- ✅ Rótulo explícito -->
<label for="email">Endereço de e-mail</label>
<input type="e-mail" id="e-mail" nome="e-mail"
       preenchimento automático = "e-mail" obrigatório>

<!-- ✅ Rótulo implícito -->
<rótulo>
  Endereço de e-mail
  <input type="email" name="email" autocomplete="email" obrigatório>
</label>

<!-- ✅ Com instruções -->
<label for="senha">Senha</label>
<input type="senha" id="senha"
       aria-describedby="requisitos de senha">
<p id="requisitos de senha">
  Deve ter pelo menos 8 caracteres com um número.
</p>
```

---

## Arrastar movimentos

Qualquer ação desencadeada por arrastar deve oferecer uma alternativa de ponteiro único (WCAG 2.5.7).

```html
<!-- ❌ Reordenar apenas arrastando -->
<ul class="lista classificável" draggable="true">
  <li>Item 1</li>
  <li>Item 2</li>
</ul>

<!-- ✅ Alternativas de arrastar + botão -->
<ul class="lista classificável">
  <li>
    <span>Item 1</span>
    <button aria-label="Mover item 1 para cima">↑</button>
    <button aria-label="Mover item 1 para baixo">↓</button>
  </li>
  <li>
    <span>Item 2</span>
    <button aria-label="Mover item 2 para cima">↑</button>
    <button aria-label="Mover item 2 para baixo">↓</button>
  </li>
</ul>
```

Também se aplica a controles deslizantes, deslocamento de mapa, seletores de cores e widgets semelhantes baseados em arrastar – sempre forneça um clique/toque ou caminho de teclado equivalente.

---

## abas ARIA

As guias requerem `role="tablist"`, `role="tab"` e `role="tabpanel"` com `aria-selected`, `aria-controls` adequados e suporte de teclado.

```html
<div role="tablist" aria-label="Informações do produto">
  <button role="tab" id="tab-1" aria-selected="true"
          aria-controls="panel-1">Descrição</button>
  <button role="tab" id="tab-2" aria-selected="false"
          aria-controls="panel-2" tabindex="-1">Comentários</button>
</div>
<div role="tabpanel" id="panel-1" aria-labelledby="tab-1">
  <!-- Conteúdo do painel -->
</div>
<div role="tabpanel" id="panel-2" aria-labelledby="tab-2" oculto>
  <!-- Conteúdo do painel -->
</div>
```

As teclas de seta devem mover o foco entre as guias; a aba ativa recebe `tabindex="0"` enquanto as abas inativas usam `tabindex="-1"`.

---

## Regiões e notificações ativas

Use `aria-live` para anunciar mudanças dinâmicas de conteúdo para leitores de tela sem mover o foco.

```html
<!-- Atualizações de status (educado — aguarda pausa na fala) -->
<div aria-live="educado" aria-atomic="true" class="status">
  <!-- Atualizações de conteúdo anunciadas para leitores de tela -->
</div>

<!-- Alertas urgentes (assertivos — interrupções) -->
<div role="alert" aria-live="assertive">
  <!-- Interrompe o anúncio atual -->
</div>
```

```javascript
function showNotification(mensagem, tipo = 'educado') {
  const contêiner = document.getElementById(`${type}-announcer`);
  container.textContent = '';
  requestAnimationFrame(() => {
    container.textContent = mensagem;
  });
}
```

Limpe o contêiner antes de escrever para garantir que a mesma mensagem acione um novo anúncio.

---

## Comandos do leitor de tela

Referência rápida para os atalhos mais comuns do leitor de tela.

| Ação | VozOver (Mac) | NVDA (Windows) |
|--------|-----------------|----------------|
| Iniciar/Parar | ⌘+F5 | Ctrl+Alt+N |
| Próximo item | VO+ → | ↓ |
| Ponto anterior | VO + ← | ↑ |
| Ativar | VO + Espaço | Entrar |
| Lista de títulos | VO + U, depois setas | H / Mudança + H |
| Lista de links | VO + você | K / Mudança + K |