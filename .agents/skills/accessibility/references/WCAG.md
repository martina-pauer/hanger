# WCAG 2.2 Quick Reference

## Success criteria by level

### Level A (minimum)

| Criterion | Description |
|-----------|-------------|
| **1.1.1** Non-text Content | All images, icons have text alternatives |
| **1.2.1** Audio-only/Video-only | Provide transcript or audio description |
| **1.2.2** Captions | Video with audio has captions |
| **1.2.3** Audio Description | Video has audio description |
| **1.3.1** Info and Relationships | Information conveyed through presentation is available programmatically |
| **1.3.2** Meaningful Sequence | Reading order is logical |
| **1.3.3** Sensory Characteristics | Instructions don't rely solely on shape, color, size, location, orientation, or sound |
| **1.4.1** Use of Color | Color is not the only visual means of conveying information |
| **1.4.2** Audio Control | Audio playing automatically can be paused/stopped |
| **2.1.1** Keyboard | All functionality available via keyboard |
| **2.1.2** No Keyboard Trap | Keyboard focus can be moved away from any component |
| **2.1.4** Character Key Shortcuts | Single-key shortcuts can be turned off or remapped |
| **2.2.1** Timing Adjustable | Time limits can be extended |
| **2.2.2** Pause, Stop, Hide | Moving/blinking content can be paused |
| **2.3.1** Three Flashes | Nothing flashes more than 3 times per second |
| **2.4.1** Bypass Blocks | Skip link or landmark navigation available |
| **2.4.2** Page Titled | Pages have descriptive titles |
| **2.4.3** Focus Order | Focus order preserves meaning |
| **2.4.4** Link Purpose | Link purpose clear from link text or context |
| **2.5.1** Pointer Gestures | Multi-point gestures have single-pointer alternatives |
| **2.5.2** Pointer Cancellation | Down-event doesn't trigger action (use up-event or click) |
| **2.5.3** Label in Name | Accessible name contains visible label text |
| **2.5.4** Motion Actuation | Motion-triggered functions have alternatives |
| **3.1.1** Language of Page | Default language specified in HTML |
| **3.2.1** On Focus | Focus doesn't trigger unexpected changes |
| **3.2.2** On Input | Input doesn't trigger unexpected changes |
| **3.2.6** Consistent Help | Help mechanisms appear in the same relative order across pages |
| **3.3.1** Error Identification | Input errors clearly described |
| **3.3.2** Labels or Instructions | Form inputs have labels or instructions |
| **3.3.7** Redundant Entry | Information previously entered is auto-populated or available to select |
| **4.1.2** Name, Role, Value | UI components have accessible names and correct roles |

### Level AA (standard)

| Criterion | Description |
|-----------|-------------|
| **1.2.4** Captions (Live) | Live audio has captions |
| **1.2.5** Audio Description | Pre-recorded video has audio description |
| **1.3.4** Orientation | Content doesn't restrict orientation |
| **1.3.5** Identify Input Purpose | Input purpose can be programmatically determined |
| **1.4.3** Contrast (Minimum) | 4.5:1 for normal text, 3:1 for large text |
| **1.4.4** Resize Text | Text can be resized to 200% without loss of functionality |
| **1.4.5** Images of Text | Text used instead of images of text |
| **1.4.10** Reflow | Content reflows at 320px width without horizontal scroll |
| **1.4.11** Non-text Contrast | UI components have 3:1 contrast |
| **1.4.12** Text Spacing | Content adapts to text spacing changes |
| **1.4.13** Content on Hover/Focus | Additional content is dismissible, hoverable, persistent |
| **2.4.5** Multiple Ways | Multiple ways to find pages |
| **2.4.6** Headings and Labels | Headings and labels are descriptive |
| **2.4.7** Focus Visible | Focus indicator is visible |
| **2.4.11** Focus Not Obscured (Minimum) | Focused element is not entirely hidden by author-created content |
| **2.5.7** Dragging Movements | Dragging actions have single-pointer alternatives |
| **2.5.8** Target Size (Minimum) | Interactive targets are at least 24×24 CSS pixels (with exceptions) |
| **3.1.2** Language of Parts | Language changes are marked |
| **3.2.3** Consistent Navigation | Navigation is consistent across pages |
| **3.2.4** Consistent Identification | Same functionality uses same labels |
| **3.3.3** Error Suggestion | Error corrections suggested when known |
| **3.3.4** Error Prevention (Legal) | Actions can be reversed or confirmed |
| **3.3.8** Accessible Authentication (Minimum) | No cognitive function test for login unless an alternative or assistance is provided |
| **4.1.3** Status Messages | Status messages announced to screen readers |

### Level AAA (enhanced)

| Criterion | Description |
|-----------|-------------|
| **1.4.6** Contrast (Enhanced) | 7:1 for normal text, 4.5:1 for large text |
| **1.4.8** Visual Presentation | Foreground/background colors can be selected |
| **1.4.9** Images of Text (No Exception) | No images of text |
| **2.1.3** Keyboard (No Exception) | All functionality keyboard accessible |
| **2.2.3** No Timing | No time limits |
| **2.2.4** Interruptions | Interruptions can be postponed |
| **2.2.5** Re-authenticating | Data preserved on re-authentication |
| **2.2.6** Timeouts | Users warned about data loss from inactivity |
| **2.3.2** Three Flashes | No content flashes more than 3 times |
| **2.3.3** Animation from Interactions | Motion animation can be disabled |
| **2.4.8** Location | User location within site is available |
| **2.4.9** Link Purpose (Link Only) | Link purpose clear from link text alone |
| **2.4.10** Section Headings | Sections have headings |
| **2.4.12** Focus Not Obscured (Enhanced) | No part of the focused element is hidden by author-created content |
| **2.4.13** Focus Appearance | Focus indicator has sufficient area, contrast, and is not obscured |
| **3.1.3** Unusual Words | Definitions available for unusual words |
| **3.1.4** Abbreviations | Abbreviations expanded |
| **3.1.5** Reading Level | Alternative content for complex text |
| **3.1.6** Pronunciation | Pronunciation available where needed |
| **3.2.5** Change on Request | Changes initiated only by user |
| **3.3.5** Help | Context-sensitive help available |
| **3.3.6** Error Prevention (All) | All form submissions can be reviewed |
| **3.3.9** Accessible Authentication (Enhanced) | No cognitive function test for login (no object or personal content recognition exceptions) |

## Common ARIA patterns

### Buttons
```html
<button>Label</button>
<!-- or -->
<button aria-label="Close dialog">×</button>
```

### Links
```html
<a href="/page">Descriptive link text</a>
<!-- External links -->
<a href="https://external.com" target="_blank" rel="noopener">
  External site
  <span class="visually-hidden">(opens in new tab)</span>
</a>
```

### Form fields
```html
<label for="email">Email address</label>
<input type="email" id="email" aria-describedby="email-hint">
<p id="email-hint">We'll never share your email.</p>
```

### Error states
```html
<label for="email">Email</label>
<input type="email" id="email" aria-invalid="true" aria-describedby="email-error">
<p id="email-error" role="alert">Please enter a valid email address.</p>
```

### Navigation
```html
<nav aria-label="Main">
  <ul>
    <li><a href="/" aria-current="page">Home</a></li>
    <li><a href="/about">About</a></li>
  </ul>
</nav>
```

### Modals
```html
<div role="dialog" aria-modal="true" aria-labelledby="dialog-title">
  <h2 id="dialog-title">Confirm Action</h2>
  <!-- content -->
</div>
```

### Live regions
```html
<!-- Polite (waits for pause in speech) -->
<div aria-live="polite">Status update here</div>

<!-- Assertive (interrupts immediately) -->
<div aria-live="assertive" role="alert">Error message here</div>

<!-- Status (polite, implicit) -->
<div role="status">Loading complete</div>
```

## What changed from 2.1 to 2.2

| Change | Criterion | Level |
|--------|-----------|-------|
| **Removed** | 4.1.1 Parsing | A |
| **Added** | 2.4.11 Focus Not Obscured (Minimum) | AA |
| **Added** | 2.4.12 Focus Not Obscured (Enhanced) | AAA |
| **Added** | 2.4.13 Focus Appearance | AAA |
| **Added** | 2.5.7 Dragging Movements | AA |
| **Added** | 2.5.8 Target Size (Minimum) | AA |
| **Added** | 3.2.6 Consistent Help | A |
| **Added** | 3.3.7 Redundant Entry | A |
| **Added** | 3.3.8 Accessible Authentication (Minimum) | AA |
| **Added** | 3.3.9 Accessible Authentication (Enhanced) | AAA |

## Testing tools

| Tool | Type | URL |
|------|------|-----|
| axe DevTools | Browser extension | [deque.com/axe](https://www.deque.com/axe/) |
| WAVE | Browser extension | [wave.webaim.org](https://wave.webaim.org/) |
| Lighthouse | Built into Chrome | DevTools → Lighthouse |
| NVDA | Screen reader (Windows) | [nvaccess.org](https://www.nvaccess.org/) |
| VoiceOver | Screen reader (Mac) | Built into macOS |
| Colour Contrast Analyser | Desktop app | [tpgi.com](https://www.tpgi.com/color-contrast-checker/) |

## Sources

- [WCAG 2.2 W3C Recommendation](https://www.w3.org/TR/WCAG22/)
- [WCAG 2.2 Quick Reference](https://www.w3.org/WAI/WCAG22/quickref/)
- [What's New in WCAG 2.2](https://www.w3.org/WAI/standards-guidelines/wcag/new-in-22/)

# Referencia rápida de las WCAG 2.2

## Criterios de éxito por nivel

### Nivel A (mínimo)

| Criterio | Descripción |
|-----------|-------------|
| **1.1.1** Contenido no textual | Todas las imágenes, los íconos tienen alternativas de texto |
| **1.2.1** Solo audio/Solo video | Proporcionar transcripción o descripción de audio |
| **1.2.2** Subtítulos | El vídeo con audio tiene subtítulos |
| **1.2.3** Audiodescripción | El vídeo tiene audio descripción |
| **1.3.1** Información y Relaciones | La información transmitida a través de la presentación está disponible mediante programación |
| **1.3.2** Secuencia significativa | El orden de lectura es lógico |
| **1.3.3** Características sensoriales | Las instrucciones no se basan únicamente en la forma, el color, el tamaño, la ubicación, la orientación o el sonido.
| **1.4.1** Uso del color | El color no es el único medio visual para transmitir información |
| **1.4.2** Control de audio | La reproducción de audio se puede pausar/detener automáticamente |
| **2.1.1** Teclado | Todas las funciones disponibles a través del teclado |
| **2.1.2** Sin trampa de teclado | El foco del teclado se puede alejar de cualquier componente |
| **2.1.4** Atajos de teclas de caracteres | Los atajos de una sola tecla se pueden desactivar o reasignar |
| **2.2.1** Temporización ajustable | Los plazos pueden ampliarse |
| **2.2.2** Pausar, detener, ocultar | El contenido en movimiento/parpadeante se puede pausar |
| **2.3.1** Tres destellos | Nada parpadea más de 3 veces por segundo |
| **2.4.1** Bloques de derivación | Saltar enlace o navegación por puntos de referencia disponibles |
| **2.4.2** Página titulada | Las páginas tienen títulos descriptivos |
| **2.4.3** Orden de enfoque | El orden de enfoque conserva el significado |
| **2.4.4** Propósito del enlace | Propósito del enlace claro del texto o contexto del enlace |
| **2.5.1** Gestos del puntero | Los gestos multipunto tienen alternativas de un solo puntero |
| **2.5.2** Cancelación de puntero | El evento descendente no activa la acción (use el evento descendente o haga clic) |
| **2.5.3** Etiqueta en Nombre | El nombre accesible contiene texto de etiqueta visible |
| **2.5.4** Actuación por movimiento | Las funciones activadas por movimiento tienen alternativas |
| **3.1.1** Idioma de la página | Idioma predeterminado especificado en HTML |
| **3.2.1** En foco | El enfoque no provoca cambios inesperados |
| **3.2.2** En entrada | La entrada no provoca cambios inesperados |
| **3.2.6** Ayuda consistente | Los mecanismos de ayuda aparecen en el mismo orden relativo en todas las páginas |
| **3.3.1** Identificación de errores | Errores de entrada claramente descritos |
| **3.3.2** Etiquetas o Instrucciones | Las entradas del formulario tienen etiquetas o instrucciones |
| **3.3.7** Entrada redundante | La información ingresada previamente se completa automáticamente o está disponible para seleccionar |
| **4.1.2** Nombre, Función, Valor | Los componentes de la interfaz de usuario tienen nombres accesibles y funciones correctas |

### Nivel AA (estándar)

| Criterio | Descripción |
|-----------|-------------|
| **1.2.4** Subtítulos (en vivo) | El audio en vivo tiene subtítulos |
| **1.2.5** Audiodescripción | El vídeo pregrabado tiene audiodescripción |
| **1.3.4** Orientación | El contenido no restringe la orientación |
| **1.3.5** Identificar el propósito de la entrada | El propósito de la entrada se puede determinar mediante programación |
| **1.4.3** Contraste (Mínimo) | 4,5:1 para texto normal, 3:1 para texto grande |
| **1.4.4** Cambiar tamaño del texto | El tamaño del texto se puede cambiar al 200% sin pérdida de funcionalidad |
| **1.4.5** Imágenes de texto | Texto utilizado en lugar de imágenes de texto |
| **1.4.10** Reflujo | El contenido se redistribuye a 320 px de ancho sin desplazamiento horizontal |
| **1.4.11** Contraste sin texto | Los componentes de la interfaz de usuario tienen un contraste de 3:1 |
| **1.4.12** Espaciado de texto | El contenido se adapta a los cambios de espaciado del texto |
| **1.4.13** Contenido al pasar el cursor/enfocar | El contenido adicional es descartable, flotante y persistente |
| **2.4.5** Múltiples formas | Múltiples formas de encontrar páginas |
| **2.4.6** Encabezados y etiquetas | Los títulos y etiquetas son descriptivos |
| **2.4.7** Enfoque visible | El indicador de enfoque es visible |
| **2.4.11** Enfoque no oscurecido (mínimo) | El elemento enfocado no está completamente oculto por el contenido creado por el autor |
| **2.5.7** Movimientos de arrastre | Las acciones de arrastre tienen alternativas de un solo puntero |
| **2.5.8** Tamaño objetivo (mínimo) | Los objetivos interactivos tienen al menos 24×24 píxeles CSS (con excepciones) |
| **3.1.2** Idioma de las partes | Los cambios de idioma están marcados |
| **3.2.3** Navegación consistente | La navegación es consistente en todas las páginas |
| **3.2.4** Identificación coherente | La misma funcionalidad usa las mismas etiquetas |
| **3.3.3** Sugerencia de error | Correcciones de errores sugeridas cuando se conocen |
| **3.3.4** Prevención de errores (legal) | Las acciones se pueden revertir o confirmar |
| **3.3.8** Autenticación accesible (mínimo) | No hay prueba de función cognitiva para iniciar sesión a menos que se proporcione una alternativa o asistencia |
| **4.1.3** Mensajes de estado | Mensajes de estado anunciados a los lectores de pantalla |

### Nivel AAA (mejorado)

| Criterio | Descripción |
|-----------|-------------|
| **1.4.6** Contraste (mejorado) | 7:1 para texto normal, 4,5:1 para texto grande |
| **1.4.8** Presentación visual | Se pueden seleccionar los colores de primer plano/fondo |
| **1.4.9** Imágenes de texto (sin excepción) | No hay imágenes de texto |
| **2.1.3** Teclado (sin excepción) | Todas las funciones del teclado son accesibles |
| **2.2.3** Sin sincronización | Sin límites de tiempo |
| **2.2.4** Interrupciones | Las interrupciones pueden posponerse |
| **2.2.5** Reautenticación | Datos conservados tras la reautenticación |
| **2.2.6** Tiempos de espera | Usuarios advirtieron sobre pérdida de datos por inactividad |
| **2.3.2** Tres destellos | Ningún contenido parpadea más de 3 veces |
| **2.3.3** Animación a partir de interacciones | La animación en movimiento se puede desactivar |
| **2.4.8** Ubicación | La ubicación del usuario dentro del sitio está disponible |
| **2.4.9** Propósito del enlace (solo enlace) | El propósito del enlace se aclara solo a partir del texto del enlace |
| **2.4.10** Encabezados de sección | Las secciones tienen títulos |
| **2.4.12** Enfoque no oscurecido (mejorado) | Ninguna parte del elemento enfocado está oculta por el contenido creado por el autor |
| **2.4.13** Apariencia de enfoque | El indicador de enfoque tiene suficiente área y contraste y no está oscurecido |
| **3.1.3** Palabras inusuales | Definiciones disponibles para palabras inusuales |
| **3.1.4** Abreviaturas | Abreviaturas ampliadas |
| **3.1.5** Nivel de lectura | Contenido alternativo para texto complejo |
| **3.1.6** Pronunciación | Pronunciación disponible donde sea necesario |
| **3.2.5** Cambio a petición | Cambios iniciados sólo por el usuario |
| **3.3.5** Ayuda | Ayuda contextual disponible |
| **3.3.6** Prevención de errores (Todos) | Todos los envíos de formularios se pueden revisar |
| **3.3.9** Autenticación accesible (mejorada) | Sin prueba de función cognitiva para iniciar sesión (sin excepciones de reconocimiento de objetos o contenido personal) |

## Patrones ARIA comunes

### Botones
```html
<botón>Etiqueta</botón>
<!-- o -->
<button aria-label="Cerrar diálogo">×</button>
```

### Enlaces
```html
<a href="/page">Texto de enlace descriptivo</a>
<!-- Enlaces externos -->
<a href="https://external.com" target="_blank" rel="noopener">
  Sitio externo
  <span class="visually-hidden">(se abre en una nueva pestaña)</span>
</a>
```

### Campos de formulario
```html
<label for="email">Dirección de correo electrónico</label>
<tipo de entrada="correo electrónico" id="correo electrónico" aria-describedby="correo-email-hint">
<p id="email-hint">Nunca compartiremos tu correo electrónico.</p>
```

### Estados de error
```html
<label for="email">Correo electrónico</label>
<tipo de entrada="correo electrónico" id="correo electrónico" aria-invalid="true" aria-describedby="correo electrónico-error">
<p id="email-error" role="alert">Ingrese una dirección de correo electrónico válida.</p>
```

### Navegación
```html
<nav aria-label="Principal">
  <ul>
    <li><a href="/" aria-current="page">Inicio</a></li>
    <li><a href="/about">Acerca de</a></li>
  </ul>
</nav>
```

### modales
```html
<div role="dialog" aria-modal="true" aria-labelledby="dialog-title">
  <h2 id="dialog-title">Confirmar acción</h2>
  <!-- contenido -->
</div>
```

### Regiones en vivo
```html
<!-- Cortés (espera una pausa en el discurso) -->
<div aria-live="polite">Actualización de estado aquí</div>

<!-- Asertivo (interrumpe inmediatamente) -->
<div aria-live="assertive" role="alert">Mensaje de error aquí</div>

<!-- Estado (educado, implícito) -->
<div role="status">Carga completa</div>
```

## ¿Qué cambió de 2.1 a 2.2?

| Cambiar | Criterio | Nivel |
|--------|-----------|-------|
| **Eliminado** | 4.1.1 Análisis | Un |
| **Agregado** | 2.4.11 Enfoque no oscurecido (mínimo) | AA |
| **Agregado** | 2.4.12 Enfoque no oscurecido (mejorado) | AAA |
| **Agregado** | 2.4.13 Apariencia del enfoque | AAA |
| **Agregado** | 2.5.7 Movimientos de arrastre | AA |
| **Agregado** | 2.5.8 Tamaño objetivo (mínimo) | AA |
| **Agregado** | 3.2.6 Ayuda coherente | Un |
| **Agregado** | 3.3.7 Entrada redundante | Un |
| **Agregado** | 3.3.8 Autenticación accesible (mínimo) | AA |
| **Agregado** | 3.3.9 Autenticación accesible (mejorada) | AAA |

## Herramientas de prueba

| Herramienta | Tipo | URL |
|------|------|-----|
| hacha DevTools | Extensión del navegador | [deque.com/axe](https://www.deque.com/axe/) |
| ONDA | Extensión del navegador | [wave.webaim.org](https://wave.webaim.org/) |
| Faro | Integrado en Chrome | Herramientas de desarrollo → Faro |
| NVDA | Lector de pantalla (Windows) | [nvaccess.org](https://www.nvaccess.org/) |
| Voz en off | Lector de pantalla (Mac) | Integrado en macOS |
| Analizador de contraste de color | Aplicación de escritorio | [tpgi.com](https://www.tpgi.com/color-contrast-checker/) |

## Fuentes

- [Recomendación W3C WCAG 2.2](https://www.w3.org/TR/WCAG22/)
- [Referencia rápida de las WCAG 2.2](https://www.w3.org/WAI/WCAG22/quickref/)
- [Novedades de WCAG 2.2](https://www.w3.org/WAI/standards-guidelines/wcag/new-in-22/)
# Référence rapide WCAG 2.2

## Critères de réussite par niveau

### Niveau A (minimum)

| Critère | Descriptif |
|---------------|-------------|
| **1.1.1** Contenu non textuel | Toutes les images et icônes ont des alternatives de texte |
| **1.2.1** Audio uniquement/Vidéo uniquement | Fournir une transcription ou une description audio |
| **1.2.2** Légendes | La vidéo avec audio comporte des sous-titres |
| **1.2.3** Description audio | La vidéo a une description audio |
| **1.3.1** Informations et relations | Les informations transmises via la présentation sont disponibles par programme |
| **1.3.2** Séquence significative | L'ordre de lecture est logique |
| **1.3.3** Caractéristiques sensorielles | Les instructions ne reposent pas uniquement sur la forme, la couleur, la taille, l'emplacement, l'orientation ou le son |
| **1.4.1** Utilisation de la couleur | La couleur n'est pas le seul moyen visuel de transmettre des informations |
| **1.4.2** Contrôle audio | La lecture audio peut être automatiquement mise en pause/arrêtée |
| **2.1.1** Clavier | Toutes les fonctionnalités disponibles via le clavier |
| **2.1.2** Pas de piège au clavier | Le focus du clavier peut être éloigné de n'importe quel composant |
| **2.1.4** Raccourcis clavier des personnages | Les raccourcis à une seule touche peuvent être désactivés ou remappés |
| **2.2.1** Synchronisation réglable | Les délais peuvent être prolongés |
| **2.2.2** Pause, Arrêter, Masquer | Le contenu en mouvement/clignotant peut être mis en pause |
| **2.3.1** Trois flashs | Rien ne clignote plus de 3 fois par seconde |
| **2.4.1** Contourner les blocs | Passer le lien ou la navigation par point de repère disponible |
| **2.4.2** Page intitulée | Les pages ont des titres descriptifs |
| **2.4.3** Ordre de mise au point | L'ordre de mise au point préserve le sens |
| **2.4.4** Objectif du lien | Objectif du lien effacé du texte ou du contexte du lien |
| **2.5.1** Gestes du pointeur | Les gestes multipoints ont des alternatives à un seul pointeur |
| **2.5.2** Annulation du pointeur | L'événement down ne déclenche pas d'action (utilisez l'événement up ou cliquez) |
| **2.5.3** Étiquette dans le nom | Le nom accessible contient le texte de l'étiquette visible |
| **2.5.4** Actionnement par mouvement | Les fonctions déclenchées par le mouvement ont des alternatives |
| **3.1.1** Langue de la page | Langue par défaut spécifiée en HTML |
| **3.2.1** Au point | La concentration ne déclenche pas de changements inattendus |
| **3.2.2** Lors de l'entrée | L'entrée ne déclenche pas de changements inattendus |
| **3.2.6** Aide cohérente | Les mécanismes d'aide apparaissent dans le même ordre relatif sur les pages |
| **3.3.1** Identification des erreurs | Erreurs de saisie clairement décrites |
| **3.3.2** Étiquettes ou instructions | Les entrées de formulaire ont des étiquettes ou des instructions |
| **3.3.7** Entrée redondante | Les informations saisies précédemment sont automatiquement renseignées ou disponibles pour sélectionner |
| **4.1.2** Nom, rôle, valeur | Les composants de l'interface utilisateur ont des noms accessibles et des rôles corrects |

### Niveau AA (standard)

| Critère | Descriptif |
|---------------|-------------|
| **1.2.4** Sous-titres (en direct) | L'audio en direct a des sous-titres |
| **1.2.5** Description audio | La vidéo préenregistrée a une description audio |
| **1.3.4** Orientation | Le contenu ne restreint pas l'orientation |
| **1.3.5** Identifier le but de la saisie | Le but de la saisie peut être déterminé par programme |
| **1.4.3** Contraste (minimum) | 4,5:1 pour le texte normal, 3:1 pour le texte volumineux |
| **1.4.4** Redimensionner le texte | Le texte peut être redimensionné à 200 % sans perte de fonctionnalité |
| **1.4.5** Images de texte | Texte utilisé à la place d'images de texte |
| **1.4.10** Redistribution | Le contenu est redistribué à une largeur de 320 px sans défilement horizontal |
| **1.4.11** Contraste non textuel | Les composants de l'interface utilisateur ont un contraste de 3:1 |
| **1.4.12** Espacement du texte | Le contenu s'adapte aux changements d'espacement du texte |
| **1.4.13** Contenu en survol/mise au point | Le contenu supplémentaire peut être ignoré, planable et persistant |
| **2.4.5** Plusieurs façons | Plusieurs façons de trouver des pages |
| **2.4.6** Titres et étiquettes | Les titres et les étiquettes sont descriptifs |
| **2.4.7** Mise au point visible | L'indicateur de mise au point est visible |
| **2.4.11** Mise au point non masquée (minimum) | L'élément ciblé n'est pas entièrement masqué par le contenu créé par l'auteur |
| **2.5.7** Mouvements de glissement | Les actions de glissement ont des alternatives à un seul pointeur |
| **2.5.8** Taille cible (minimale) | Les cibles interactives mesurent au moins 24 × 24 pixels CSS (sauf exceptions) |
| **3.1.2** Langue des pièces | Les changements de langue sont marqués |
| **3.2.3** Navigation cohérente | La navigation est cohérente sur toutes les pages |
| **3.2.4** Identification cohérente | La même fonctionnalité utilise les mêmes étiquettes |
| **3.3.3** Suggestion d'erreur | Corrections d'erreurs suggérées lorsqu'elles sont connues |
| **3.3.4** Prévention des erreurs (juridique) | Les actions peuvent être annulées ou confirmées |
| **3.3.8** Authentification accessible (minimum) | Aucun test de fonction cognitive pour la connexion, sauf si une alternative ou une assistance est fournie |
| **4.1.3** Messages d'état | Messages d'état annoncés aux lecteurs d'écran |

### Niveau AAA (amélioré)

| Critère | Descriptif |
|---------------|-------------|
| **1.4.6** Contraste (amélioré) | 7:1 pour un texte normal, 4,5:1 pour un texte volumineux |
| **1.4.8** Présentation visuelle | Les couleurs de premier plan/arrière-plan peuvent être sélectionnées |
| **1.4.9** Images de texte (sans exception) | Aucune image du texte |
| **2.1.3** Clavier (sans exception) | Toutes les fonctionnalités du clavier accessibles |
| **2.2.3** Pas de timing | Aucune limite de temps |
| **2.2.4** Interruptions | Les interruptions peuvent être reportées |
| **2.2.5** Ré-authentification | Données conservées lors de la réauthentification |
| **2.2.6** Délais d'attente | Les utilisateurs sont avertis de la perte de données due à l'inactivité |
| **2.3.2** Trois flashs | Aucun contenu ne clignote plus de 3 fois |
| **2.3.3** Animation à partir d'interactions | L'animation de mouvement peut être désactivée |
| **2.4.8** Localisation | L'emplacement de l'utilisateur sur le site est disponible |
| **2.4.9** Objectif du lien (lien uniquement) | L’objectif du lien est clair à partir du texte du lien uniquement |
| **2.4.10** Titres des sections | Les sections ont des titres |
| **2.4.12** Mise au point non masquée (améliorée) | Aucune partie de l'élément ciblé n'est masquée par le contenu créé par l'auteur |
| **2.4.13** Apparence de mise au point | L'indicateur de mise au point a une surface et un contraste suffisants et n'est pas obscurci |
| **3.1.3** Mots inhabituels | Définitions disponibles pour les mots inhabituels |
| **3.1.4** Abréviations | Abréviations développées |
| **3.1.5** Niveau de lecture | Contenu alternatif pour texte complexe |
| **3.1.6** Prononciation | Prononciation disponible si nécessaire |
| **3.2.5** Modification sur demande | Modifications initiées uniquement par l'utilisateur |
| **3.3.5** Aide | Aide contextuelle disponible |
| **3.3.6** Prévention des erreurs (tous) | Toutes les soumissions de formulaire peuvent être examinées |
| **3.3.9** Authentification accessible (améliorée) | Pas de test des fonctions cognitives pour la connexion (pas d'exceptions de reconnaissance d'objets ou de contenu personnel) |

## Modèles ARIA courants

### Boutons
```html
<bouton>Étiquette</bouton>
<!-- ou -->
<button aria-label="Fermer la boîte de dialogue">×</button>
```

### Liens
```html
<a href="/page">Texte du lien descriptif</a>
<!-- Liens externes -->
<a href="https://external.com" target="_blank" rel="noopener">
  Site externe
  <span class="visually-hidden">(s'ouvre dans un nouvel onglet)</span>
</a>
```

### Champs du formulaire
```html
<label for="email">Adresse e-mail</label>
<input type="email" id="email" aria-describeby="email-hint">
<p id="email-hint">Nous ne partagerons jamais votre e-mail.</p>
```

### États d'erreur
```html
<label for="email">E-mail</label>
<input type="email" id="email" aria-invalid="true" aria-describeby="email-error">
<p id="email-error" role="alert">Veuillez saisir une adresse e-mail valide.</p>
```

### Navigation
```html
<nav aria-label="Main">
  <ul>
    <li><a href="/" aria-current="page">Accueil</a></li>
    <li><a href="/about">À propos</a></li>
  </ul>
</nav>
```

### Modaux
```html
<div role="dialog" aria-modal="true" aria-labelledby="dialog-title">
  <h2 id="dialog-title">Confirmer l'action</h2>
  <!-- contenu -->
</div>
```

### Régions en direct
```html
<!-- Poli (attend une pause dans le discours) -->
<div aria-live="polite">Mise à jour du statut ici</div>

<!-- Assertif (interrompt immédiatement) -->
<div aria-live="assertive" role="alert">Message d'erreur ici</div>

<!-- Statut (poli, implicite) -->
<div role="status">Chargement terminé</div>
```

## Ce qui a changé de la version 2.1 à la version 2.2

| Changement | Critère | Niveau |
|--------|-----------|-------|
| **Supprimé** | 4.1.1 Analyse | Un |
| **Ajouté** | 2.4.11 Mise au point non obscurcie (minimum) | AA |
| **Ajouté** | 2.4.12 Mise au point non masquée (améliorée) | AAA |
| **Ajouté** | 2.4.13 Apparence de mise au point | AAA |
| **Ajouté** | 2.5.7 Mouvements de glissement | AA |
| **Ajouté** | 2.5.8 Taille cible (minimale) | AA |
| **Ajouté** | 3.2.6 Aide cohérente | Un |
| **Ajouté** | 3.3.7 Entrée redondante | Un |
| **Ajouté** | 3.3.8 Authentification accessible (minimum) | AA |
| **Ajouté** | 3.3.9 Authentification accessible (améliorée) | AAA |

## Outils de test

| Outil | Tapez | URL |
|------|------|-----|
| hache DevTools | Extension de navigateur | [deque.com/axe](https://www.deque.com/axe/) |
| VAGUE | Extension de navigateur | [wave.webaim.org](https://wave.webaim.org/) |
| Phare | Intégré à Chrome | DevTools → Phare |
| NVDA | Lecteur d'écran (Windows) | [nvaccess.org](https://www.nvaccess.org/) |
| Voix off | Lecteur d'écran (Mac) | Intégré à macOS |
| Analyseur de contraste de couleur | Application de bureau | [tpgi.com](https://www.tpgi.com/color-contrast-checker/) |

##Sources

- [Recommandation WCAG 2.2 du W3C](https://www.w3.org/TR/WCAG22/)
- [Référence rapide WCAG 2.2](https://www.w3.org/WAI/WCAG22/quickref/)
- [Quoi de neuf dans WCAG 2.2](https://www.w3.org/WAI/standards-guidelines/wcag/new-in-22/)
# WCAG 2.2 Kurzreferenz

## Erfolgskriterien nach Level

### Level A (mindestens)

| Kriterium | Beschreibung |
|-----------|-------------|
| **1.1.1** Nicht-Text-Inhalt | Alle Bilder und Symbole verfügen über Textalternativen |
| **1.2.1** Nur Audio/Nur Video | Stellen Sie ein Transkript oder eine Audiobeschreibung bereit |
| **1.2.2** Bildunterschriften | Video mit Audio hat Untertitel |
| **1.2.3** Audiobeschreibung | Video hat Audiobeschreibung |
| **1.3.1** Informationen und Beziehungen | Durch Präsentation vermittelte Informationen sind programmatisch verfügbar |
| **1.3.2** Sinnvolle Sequenz | Lesereihenfolge ist logisch |
| **1.3.3** Sensorische Eigenschaften | Anweisungen basieren nicht nur auf Form, Farbe, Größe, Ort, Ausrichtung oder Klang |
| **1.4.1** Verwendung von Farbe | Farbe ist nicht das einzige visuelle Mittel zur Informationsvermittlung |
| **1.4.2** Audiosteuerung | Die automatische Audiowiedergabe kann angehalten/gestoppt werden |
| **2.1.1** Tastatur | Alle Funktionen über die Tastatur verfügbar |
| **2.1.2** Keine Tastaturfalle | Der Tastaturfokus kann von jeder Komponente weg verschoben werden |
| **2.1.4** Tastenkombinationen für Zeichen | Einzeltastenkürzel können deaktiviert oder neu zugeordnet werden |
| **2.2.1** Timing einstellbar | Fristen können verlängert werden |
| **2.2.2** Anhalten, Stoppen, Ausblenden | Sich bewegende/blinkende Inhalte können angehalten werden |
| **2.3.1** Drei Blitze | Nichts blinkt mehr als 3 Mal pro Sekunde |
| **2.4.1** Bypass-Blöcke | Link- oder Orientierungspunktnavigation überspringen verfügbar |
| **2.4.2** Seite mit dem Titel | Seiten haben beschreibende Titel |
| **2.4.3** Fokusreihenfolge | Fokusreihenfolge bewahrt Bedeutung |
| **2.4.4** Link-Zweck | Linkzweck aus Linktext oder Kontext ersichtlich |
| **2.5.1** Zeigergesten | Für Mehrpunktgesten gibt es Einzelzeiger-Alternativen |
| **2.5.2** Zeigerlöschung | Down-Event löst keine Aktion aus (Up-Event verwenden oder klicken) |
| **2.5.3** Bezeichnung im Namen | Der zugängliche Name enthält sichtbaren Beschriftungstext |
| **2.5.4** Bewegungsbetätigung | Für bewegungsgesteuerte Funktionen gibt es Alternativen |
| **3.1.1** Sprache der Seite | In HTML | angegebene Standardsprache
| **3.2.1** Im Fokus | Fokus löst keine unerwarteten Änderungen aus |
| **3.2.2** Bei Eingabe | Eingabe löst keine unerwarteten Änderungen aus |
| **3.2.6** Konsistente Hilfe | Hilfemechanismen erscheinen auf allen Seiten in derselben relativen Reihenfolge |
| **3.3.1** Fehleridentifizierung | Eingabefehler klar beschrieben |
| **3.3.2** Etiketten oder Anweisungen | Formulareingaben haben Beschriftungen oder Anweisungen |
| **3.3.7** Redundanter Eintrag | Zuvor eingegebene Informationen werden automatisch ausgefüllt oder stehen zur Auswahl | zur Verfügung
| **4.1.2** Name, Rolle, Wert | UI-Komponenten haben zugängliche Namen und korrekte Rollen |

### Stufe AA (Standard)

| Kriterium | Beschreibung |
|-----------|-------------|
| **1.2.4** Untertitel (Live) | Live-Audio hat Untertitel |
| **1.2.5** Audiobeschreibung | Voraufgezeichnetes Video mit Audiobeschreibung |
| **1.3.4** Ausrichtung | Inhalt schränkt die Orientierung nicht ein |
| **1.3.5** Eingabezweck identifizieren | Eingabezweck kann programmgesteuert bestimmt werden |
| **1.4.3** Kontrast (Minimum) | 4,5:1 für normalen Text, 3:1 für großen Text |
| **1.4.4** Textgröße ändern | Die Textgröße kann ohne Funktionsverlust auf 200 % geändert werden |
| **1.4.5** Bilder von Text | Anstelle von Textbildern wird Text verwendet |
| **1.4.10** Reflow | Der Inhalt wird mit einer Breite von 320 Pixel ohne horizontales Scrollen umfließen |
| **1.4.11** Nicht-Text-Kontrast | UI-Komponenten haben einen Kontrast von 3:1 |
| **1.4.12** Textabstand | Inhalt passt sich an Änderungen des Textabstands an |
| **1.4.13** Inhalt bei Hover/Fokus | Zusätzlicher Inhalt ist verwerfbar, schwebend, dauerhaft |
| **2.4.5** Mehrere Wege | Mehrere Möglichkeiten, Seiten zu finden |
| **2.4.6** Überschriften und Beschriftungen | Überschriften und Beschriftungen sind beschreibend |
| **2.4.7** Fokus sichtbar | Fokusanzeige ist sichtbar |
| **2.4.11** Fokus nicht verdeckt (Minimum) | Fokussiertes Element wird durch vom Autor erstellte Inhalte nicht vollständig ausgeblendet |
| **2.5.7** Schleppbewegungen | Für Ziehaktionen gibt es Einzelzeiger-Alternativen |
| **2.5.8** Zielgröße (Minimum) | Interaktive Ziele sind mindestens 24×24 CSS-Pixel (mit Ausnahmen) |
| **3.1.2** Sprache der Teile | Sprachänderungen sind mit | markiert
| **3.2.3** Konsistente Navigation | Die Navigation ist seitenübergreifend konsistent |
| **3.2.4** Konsistente Identifizierung | Dieselbe Funktionalität verwendet dieselben Beschriftungen |
| **3.3.3** Fehlervorschlag | Fehlerkorrekturen werden vorgeschlagen, sofern bekannt |
| **3.3.4** Fehlervermeidung (Recht) | Aktionen können rückgängig gemacht oder bestätigt werden |
| **3.3.8** Barrierefreie Authentifizierung (Minimum) | Kein kognitiver Funktionstest für die Anmeldung, es sei denn, es wird eine Alternative oder Hilfe bereitgestellt |
| **4.1.3** Statusmeldungen | Den Screenreadern angekündigte Statusmeldungen |

### Stufe AAA (erweitert)

| Kriterium | Beschreibung |
|-----------|-------------|
| **1.4.6** Kontrast (erweitert) | 7:1 für normalen Text, 4,5:1 für großen Text |
| **1.4.8** Visuelle Präsentation | Vordergrund-/Hintergrundfarben wählbar |
| **1.4.9** Bilder von Text (keine Ausnahme) | Keine Bilder von Text |
| **2.1.3** Tastatur (keine Ausnahme) | Alle Funktionen über die Tastatur zugänglich |
| **2.2.3** Kein Timing | Keine Fristen |
| **2.2.4** Unterbrechungen | Unterbrechungen können verschoben werden |
| **2.2.5** Erneute Authentifizierung | Daten bleiben bei erneuter Authentifizierung erhalten |
| **2.2.6** Zeitüberschreitungen | Benutzer vor Datenverlust durch Inaktivität gewarnt |
| **2.3.2** Drei Blitze | Kein Inhalt blinkt mehr als dreimal |
| **2.3.3** Animation aus Interaktionen | Bewegungsanimation kann deaktiviert werden |
| **2.4.8** Standort | Benutzerstandort innerhalb der Website ist verfügbar |
| **2.4.9** Link-Zweck (nur Link) | Linkzweck allein aus Linktext ersichtlich |
| **2.4.10** Abschnittsüberschriften | Abschnitte haben Überschriften |
| **2.4.12** Fokus nicht verdeckt (erweitert) | Kein Teil des fokussierten Elements wird durch vom Autor erstellte Inhalte verdeckt |
| **2.4.13** Fokusdarstellung | Der Fokusindikator hat eine ausreichende Fläche und einen ausreichenden Kontrast und ist nicht verdeckt |
| **3.1.3** Ungewöhnliche Wörter | Verfügbare Definitionen für ungewöhnliche Wörter |
| **3.1.4** Abkürzungen | Abkürzungen erweitert |
| **3.1.5** Leseniveau | Alternativer Inhalt für komplexen Text |
| **3.1.6** Aussprache | Aussprache bei Bedarf verfügbar |
| **3.2.5** Änderung auf Anfrage | Nur vom Benutzer initiierte Änderungen |
| **3.3.5** Hilfe | Kontextsensitive Hilfe verfügbar |
| **3.3.6** Fehlervermeidung (Alle) | Alle Formulareinsendungen können überprüft werden |
| **3.3.9** Barrierefreie Authentifizierung (erweitert) | Kein kognitiver Funktionstest für die Anmeldung (keine Ausnahmen bei der Erkennung von Objekten oder persönlichen Inhalten) |

## Gängige ARIA-Muster

### Schaltflächen
```html
<button>Beschriftung</button>
<!-- oder -->
<button aria-label="Dialog schließen">×</button>
„

### Links
```html
<a href="/page">Beschreibender Linktext</a>
<!-- Externe Links -->
<a href="https://external.com" target="_blank" rel="noopener">
  Externe Seite
  <span class="visually-hidden">(öffnet sich in neuem Tab)</span>
</a>
„

### Formularfelder
```html
<label for="email">E-Mail-Adresse</label>
<input type="email" id="email" aria-describedby="email-hint">
<p id="email-hint">Wir geben Ihre E-Mail-Adresse niemals weiter.</p>
„

### Fehlerzustände
```html
<label for="email">E-Mail</label>
<input type="email" id="email" aria-invalid="true" aria-describedby="email-error">
<p id="email-error" role="alert">Bitte geben Sie eine gültige E-Mail-Adresse ein.</p>
„

### Navigation
```html
<nav aria-label="Main">
  <ul>
    <li><a href="/" aria-current="page">Startseite</a></li>
    <li><a href="/about">Über</a></li>
  </ul>
</nav>
„

### Modalitäten
```html
<div role="dialog" aria-modal="true" aria-labelledby="dialog-title">
  <h2 id="dialog-title">Aktion bestätigen</h2>
  <!-- content -->
</div>
„

### Live-Regionen
```html
<!-- Höflich (wartet auf Sprechpause) -->
<div aria-live="polite">Statusaktualisierung hier</div>

<!-- Durchsetzungsfähig (unterbricht sofort) -->
<div aria-live="assertive" role="alert">Fehlermeldung hier</div>

<!-- Status (höflich, implizit) -->
<div role="status">Ladevorgang abgeschlossen</div>
„

## Was hat sich von 2.1 zu 2.2 geändert?

| Ändern | Kriterium | Ebene |
|--------|-----------|-------|
| **Entfernt** | 4.1.1 Parsen | A |
| **Hinzugefügt** | 2.4.11 Fokus nicht verdeckt (Minimum) | AA |
| **Hinzugefügt** | 2.4.12 Fokus nicht verdeckt (erweitert) | AAA |
| **Hinzugefügt** | 2.4.13 Fokusdarstellung | AAA |
| **Hinzugefügt** | 2.5.7 Schleppbewegungen | AA |
| **Hinzugefügt** | 2.5.8 Zielgröße (Minimum) | AA |
| **Hinzugefügt** | 3.2.6 Konsistente Hilfe | A |
| **Hinzugefügt** | 3.3.7 Redundanter Eintrag | A |
| **Hinzugefügt** | 3.3.8 Barrierefreie Authentifizierung (Minimum) | AA |
| **Hinzugefügt** | 3.3.9 Barrierefreie Authentifizierung (erweitert) | AAA |

## Testwerkzeuge

| Werkzeug | Geben Sie | ein URL |
|------|------|-----|
| ax DevTools | Browser-Erweiterung | [deque.com/axe](https://www.deque.com/axe/) |
| WELLE | Browser-Erweiterung | [wave.webaim.org](https://wave.webaim.org/) |
| Leuchtturm | In Chrome integriert | DevTools → Leuchtturm |
| NVDA | Bildschirmleser (Windows) | [nvaccess.org](https://www.nvaccess.org/) |
| VoiceOver | Bildschirmleser (Mac) | Integriert in macOS |
| Farbkontrastanalysator | Desktop-App | [tpgi.com](https://www.tpgi.com/color-contrast-checker/) |

## Quellen

- [WCAG 2.2 W3C-Empfehlung](https://www.w3.org/TR/WCAG22/)
- [WCAG 2.2 Kurzreferenz](https://www.w3.org/WAI/WCAG22/quickref/)
- [Was ist neu in WCAG 2.2](https://www.w3.org/WAI/standards-guidelines/wcag/new-in-22/)
# WCAG 2.2 クイックリファレンス

## レベル別の成功基準

### レベル A (最低)

|基準 |説明 |
|----------|---------------|
| **1.1.1** 非テキストコンテンツ |すべての画像、アイコンには代替テキストが含まれています。
| **1.2.1** 音声のみ/ビデオのみ |トランスクリプトまたは音声による説明を提供する |
| **1.2.2** キャプション |音声付きビデオにはキャプションが付いています |
| **1.2.3** 音声説明 |ビデオには音声説明が付いています |
| **1.3.1** 情報と関係 |プレゼンテーションを通じて伝えられる情報はプログラムで利用可能 |
| **1.3.2** 意味のあるシーケンス |読み取り順序は論理的です |
| **1.3.3** 感覚特性 |指示は、形、色、サイズ、位置、方向、音だけに依存するわけではありません。
| **1.4.1** 色の使用 |情報を伝える視覚的な手段は色だけではありません。
| **1.4.2** オーディオコントロール |オーディオの自動再生は一時停止/停止可能 |
| **2.1.1** キーボード |すべての機能はキーボードから利用可能 |
| **2.1.2** キーボード トラップなし |キーボードのフォーカスを任意のコンポーネントから遠ざけることができます。
| **2.1.4** 文字キーのショートカット |単一キーのショートカットはオフにしたり、再マップしたりできます。
| **2.2.1** タイミング調整可能 |制限時間は延長可能 |
| **2.2.2** 一時停止、停止、非表示 |移動/点滅コンテンツは一時停止可能 |
| **2.3.1** 3 回のフラッシュ | 1 秒間に 3 回を超えて点滅するものはありません。
| **2.4.1** バイパスブロック |スキップリンクまたはランドマークナビゲーションが利用可能 |
| **2.4.2** ページのタイトル |ページには説明的なタイトルが付いています。
| **2.4.3** フォーカス順序 |フォーカスの順序は意味を保持します。
| **2.4.4** リンクの目的 |リンクの目的はリンク テキストまたはコンテキストから明確 |
| **2.5.1** ポインタ ジェスチャ |マルチポイント ジェスチャにはシングル ポインタの代替手段があります。
| **2.5.2** ポインタのキャンセル |ダウンイベントはアクションをトリガーしません (アップイベントまたはクリックを使用します)。
| **2.5.3** 名前のラベル |アクセシブルな名前には、表示されるラベル テキストが含まれます。
| **2.5.4** モーション作動 |モーショントリガー機能には代替手段があります。
| **3.1.1** ページの言語 | HTML で指定されたデフォルト言語 |
| **3.2.1** 焦点について |集中しても予期せぬ変化は起こらない |
| **3.2.2** 入力時 |入力によって予期しない変更が引き起こされることはありません |
| **3.2.6** 一貫したヘルプ |ヘルプ メカニズムはページ間で同じ相対順序で表示されます。
| **3.3.1** エラーの特定 |入力エラーを明確に説明 |
| **3.3.2** ラベルまたは説明書 |フォーム入力にはラベルまたは指示があります |
| **3.3.7** 冗長エントリ |以前に入力された情報は自動入力されるか、選択することができます。
| **4.1.2** 名前、役割、値 | UI コンポーネントにはアクセス可能な名前と正しい役割があります。

### レベル AA (標準)

|基準 |説明 |
|----------|---------------|
| **1.2.4** キャプション (ライブ) |ライブ音声にはキャプションが付いています |
| **1.2.5** 音声説明 |事前に録画されたビデオには音声説明が付いています。
| **1.3.4** 方向 |コンテンツは向きを制限しません |
| **1.3.5** 入力の目的を特定する |入力の目的はプログラムで決定可能 |
| **1.4.3** コントラスト (最小) |通常のテキストの場合は 4.5:1、大きなテキストの場合は 3:1 |
| **1.4.4** テキストのサイズを変更する |機能を損なうことなくテキストのサイズを 200% まで変更できます。
| **1.4.5** テキストの画像 |テキストの画像の代わりにテキストを使用 |
| **1.4.10** リフロー |コンテンツは水平スクロールなしで幅 320 ピクセルでリフローします。
| **1.4.11** 非テキストのコントラスト | UI コンポーネントのコントラストは 3:1 です。
| **1.4.12** テキストの間隔 |コンテンツはテキスト間隔の変更に適応します。
| **1.4.13** ホバー/フォーカスのコンテンツ |追加コンテンツは消去可能、ホバー可能、永続的です。
| **2.4.5** 複数の方法 |ページを見つけるための複数の方法 |
| **2.4.6** 見出しとラベル |見出しとラベルは説明的なものです。
| **2.4.7** フォーカスが表示されます |フォーカスインジケーターが表示されます |
| **2.4.11** 焦点がぼやけていない (最小) |フォーカスされた要素は、作成者が作成したコンテンツによって完全に非表示になるわけではありません。
| **2.5.7** ドラッグ動作 |ドラッグ操作には単一ポインタの代替手段があります。
| **2.5.8** ターゲット サイズ (最小) |インタラクティブなターゲットは少なくとも 24×24 CSS ピクセルです (例外あり) |
| **3.1.2** 部品の言語 |言語の変更はマークされています |
| **3.2.3** 一貫したナビゲーション |ナビゲーションはページ間で一貫しています。
| **3.2.4** 一貫した識別 |同じ機能は同じラベルを使用します。
| **3.3.3** エラーの提案 |既知の場合はエラー修正を提案 |
| **3.3.4** エラー防止 (法的) |アクションは元に戻すことも確認することもできます |
| **3.3.8** アクセス可能な認証 (最小) |代替手段または支援が提供されない限り、ログイン時の認知機能テストは行われません。
| **4.1.3** ステータス メッセージ |スクリーン リーダーに通知されるステータス メッセージ |

### レベル AAA (強化)

|基準 |説明 |
|----------|---------------|
| **1.4.6** コントラスト (強化) |通常のテキストの場合は 7:1、大きなテキストの場合は 4.5:1 |
| **1.4.8** ビジュアル プレゼンテーション |前景色/背景色を選択可能 |
| **1.4.9** テキストの画像 (例外なし) |テキストの画像はありません |
| **2.1.3** キーボード (例外なし) |すべての機能のキーボードにアクセス可能 |
| **2.2.3** タイミングなし |時間制限なし |
| **2.2.4** 中断 |中断は延期できる |
| **2.2.5** 再認証中 |再認証時にデータが保存される |
| **2.2.6** タイムアウト |ユーザーは非アクティブによるデータ損失について警告 |
| **2.3.2** 3 回のフラッシュ | 3 回を超えて点滅するコンテンツはありません |
| **2.3.3** インタラクションからのアニメーション |モーションアニメーションを無効にすることができます |
| **2.4.8** 場所 |サイト内のユーザーの位置情報が利用可能 |
| **2.4.9** リンクの目的 (リンクのみ) |リンクテキストだけでリンクの目的が明確 |
| **2.4.10** セクション見出し |セクションには見出しがあります |
| **2.4.12** フォーカスが隠れない (強化) |フォーカスされた要素のどの部分も、作成者が作成したコンテンツによって隠されることはありません。
| **2.4.13** フォーカスの外観 |フォーカスインジケーターには十分な面積とコントラストがあり、隠れていない |
| **3.1.3** 珍しい言葉 |珍しい単語の定義 |
| **3.1.4** 略語 |略語を展開 |
| **3.1.5** 読解レベル |複雑なテキストの代替コンテンツ |
| **3.1.6** 発音 |必要に応じて発音を利用可能 |
| **3.2.5** リクエストに応じて変更 |ユーザーのみが開始した変更 |
| **3.3.5** ヘルプ |状況依存のヘルプが利用可能 |
| **3.3.6** エラー防止 (すべて) |すべてのフォーム送信内容を確認できます |
| **3.3.9** アクセシブルな認証 (拡張) |ログイン時の認知機能テストなし (オブジェクトまたは個人コンテンツの認識例外なし) |

## 一般的な ARIA パターン

### ボタン
```html
<button>ラベル</button>
<!-- または -->
<button aria-label="ダイアログを閉じる">×</button>
「」

### リンク
```html
<a href="/page">説明リンク テキスト</a>
<!-- 外部リンク -->
<a href="https://external.com" target="_blank" rel="noopener">
  外部サイト
  <span class="visually-hidden">(新しいタブで開きます)</span>
</a>
「」

### フォームフィールド
```html
<label for="email">メールアドレス</label>
<input type="email" id="email" aria-descriptedby="email-hint">
<p id="email-hint">あなたのメールが共有されることはありません。</p>
「」

### エラー状態
```html
<label for="email">メール</label>
<input type="email" id="email" aria-invalid="true" aria-descriptionby="email-error">
<p id="email-error" role="alert">有効なメール アドレスを入力してください。</p>
「」

### ナビゲーション
```html
<nav aria-label="メイン">
  <ul>
    <li><a href="/" aria-current="page">ホーム</a></li>
    <li><a href="/about">概要</a></li>
  </ul>
</nav>
「」

### モーダル
```html
<div role="dialog" aria-modal="true" aria-labeledby="dialog-title">
  <h2 id="dialog-title">アクションの確認</h2>
  <!-- 内容 -->
</div>
「」

### ライブリージョン
```html
<!-- 礼儀正しい (スピーチの一時停止を待ちます) -->
<div aria-live="polite">ステータス更新はこちら</div>

<!-- アサーティブ (すぐに中断) -->
<div aria-live="assertive" role="alert">ここにエラー メッセージが表示されます</div>

<!-- ステータス (丁寧、暗黙的) -->
<div role="status">読み込みが完了しました</div>
「」

## 2.1 から 2.2 への変更点

|変更 |基準 |レベル |
|----------|-----------|----------|
| **削除されました** | 4.1.1 解析 |あ |
| **追加** | 2.4.11 焦点がぼやけていない (最小) | AA |
| **追加** | 2.4.12 フォーカスが隠れない (拡張) | AAA |
| **追加** | 2.4.13 フォーカスの外観 | AAA |
| **追加** | 2.5.7 ドラッグ動作 | AA |
| **追加** | 2.5.8 ターゲット サイズ (最小) | AA |
| **追加** | 3.2.6 一貫したヘルプ |あ |
| **追加** | 3.3.7 冗長エントリ |あ |
| **追加** | 3.3.8 アクセス可能な認証 (最小限) | AA |
| **追加** | 3.3.9 アクセシブルな認証 (拡張) | AAA |

## テストツール

|ツール |タイプ | URL |
|------|------|-----|
| ax 開発ツール |ブラウザ拡張機能 | [deque.com/axe](https://www.deque.com/axe/) |
|ウェーブ |ブラウザ拡張機能 | [wave.webaim.org](https://wave.webaim.org/) |
|灯台 | Chrome に組み込まれています |開発ツール → ライトハウス |
| NVDA |スクリーン リーダー (Windows) | [nvaccess.org](https://www.nvaccess.org/) |
|ナレーション |スクリーン リーダー (Mac) | macOS に組み込まれています |
|カラーコントラストアナラ​​イザー |デスクトップアプリ | [tpgi.com](https://www.tpgi.com/color-contrast-checker/) |

## ソース

- [WCAG 2.2 W3C 勧告](https://www.w3.org/TR/WCAG22/)
- [WCAG 2.2 クイック リファレンス](https://www.w3.org/WAI/WCAG22/quickref/)
- [WCAG 2.2 の新機能](https://www.w3.org/WAI/standards-guidelines/wcag/new-in-22/)
# WCAG 2.2 快速参考

## 按级别划分的成功标准

### A 级（最低）

|标准|描述 |
|------------|-------------|
| **1.1.1** 非文本内容 |所有图像、图标都有替代文本 |
| **1.2.1** 仅音频/仅视频 |提供文字记录或音频描述 |
| **1.2.2** 字幕 |带音频的视频有字幕 |
| **1.2.3** 音频描述 |视频有音频描述 |
| **1.3.1** 信息和关系 |通过演示传达的信息可以通过编程方式获得 |
| **1.3.2** 有意义的序列 |阅读顺序合乎逻辑 |
| **1.3.3** 感官特性|说明不仅仅依赖于形状、颜色、大小、位置、方向或声音 |
| **1.4.1** 颜色的使用 |颜色并不是传达信息的唯一视觉方式|
| **1.4.2** 音频控制 |音频自动播放可暂停/停止 |
| **2.1.1** 键盘 |所有功能均可通过键盘实现 |
| **2.1.2** 无键盘陷阱 |键盘焦点可以从任何组件上移开 |
| **2.1.4** 字符快捷键 |单键快捷键可以关闭或重新映射 |
| **2.2.1** 定时可调 |时间限制可以延长|
| **2.2.2** 暂停、停止、隐藏 |移动/闪烁的内容可以暂停 |
| **2.3.1** 三闪 |没有任何东西每秒闪烁超过 3 次 |
| **2.4.1** 旁路块 |可以跳过链接或地标导航 |
| **2.4.2** 页面标题为 |页面有描述性标题 |
| **2.4.3** 焦点订单 |焦点顺序保留意义 |
| **2.4.4** 链接目的 |从链接文本或上下文中可以清楚地看出链接目的 |
| **2.5.1** 指针手势 |多点手势有单指针替代方案 |
| **2.5.2** 指针取消 |向下事件不触发操作（使用向上事件或单击）|
| **2.5.3** 名称中的标签 |可访问的名称包含可见的标签文本 |
| **2.5.4** 运动驱动 |运动触发功能有替代方案 |
| **3.1.1** 页面语言 | HTML | 中指定的默认语言
| **3.2.1** 焦点 |焦点不会引发意外的变化 |
| **3.2.2** 输入时 |输入不会触发意外的变化 |
| **3.2.6** 一致的帮助 |帮助机制在页面中以相同的相对顺序出现 |
| **3.3.1** 错误识别 |输入错误描述清楚 |
| **3.3.2** 标签或说明|表单输入有标签或说明 |
| **3.3.7** 冗余条目|先前输入的信息会自动填充或可供选择 |
| **4.1.2** 名称、角色、值 | UI 组件具有可访问的名称和正确的角色 |

### AA 级（标准）

|标准|描述 |
|------------|-------------|
| **1.2.4** 字幕（实时）|现场音频有字幕 |
| **1.2.5** 音频描述 |预先录制的视频有音频描述 |
| **1.3.4** 方向 |内容不限制方向 |
| **1.3.5** 确定输入目的 |输入目的可以通过编程方式确定 |
| **1.4.3** 对比度（最小）|普通文本为 4.5:1，大文本为 3:1 |
| **1.4.4** 调整文本大小 |文本大小可调整至 200%，且功能不受影响 |
| **1.4.5** 文本图像|使用文本代替文本图像 |
| **1.4.10** 回流焊 |内容以 320 像素宽度重排，无需水平滚动 |
| **1.4.11** 非文本对比 | UI 组件具有 3:1 对比度 |
| **1.4.12** 文本间距 |内容适应文本间距变化 |
| **1.4.13** 悬停/焦点上的内容 |附加内容可忽略、可悬停、持久 |
| **2.4.5** 多种方式 |多种方式查找页面 |
| **2.4.6** 标题和标签 |标题和标签具有描述性 |
| **2.4.7** 焦点可见 |焦点指示器可见 |
| **2.4.11** 焦点不被遮挡（最小）|重点元素并未完全被作者创建的内容隐藏 |
| **2.5.7** 拖动运动 |拖动操作有单指针替代方案 |
| **2.5.8** 目标尺寸（最小）|交互式目标至少为 24×24 CSS 像素（有例外）|
| **3.1.2** 零件语言 |语言更改已标记 |
| **3.2.3** 一致的导航 |跨页面导航保持一致 |
| **3.2.4** 一致的识别 |相同的功能使用相同的标签|
| **3.3.3** 错误建议 |已知错误时建议更正 |
| **3.3.4** 错误预防（法律） |操作可以撤销或确认 |
| **3.3.8** 可访问的身份验证（最低）|除非提供替代方案或帮助，否则不会对登录进行认知功能测试 |
| **4.1.3** 状态消息 |向屏幕阅读器公布的状态消息 |

### AAA 级（增强）

|标准|描述 |
|------------|-------------|
| **1.4.6** 对比度（增强）|普通文本为 7:1，大文本为 4.5:1 |
| **1.4.8** 视觉呈现 |可以选择前景色/背景色 |
| **1.4.9** 文本图像（无例外）|没有文字图像 |
| **2.1.3** 键盘（无例外）|所有功能均可使用键盘 |
| **2.2.3** 无计时 |无时间限制 |
| **2.2.4** 中断 |中断可以推迟 |
| **2.2.5** 重新验证 |重新验证时保留的数据 |
| **2.2.6** 超时 |用户警告称，不活动会导致数据丢失
| **2.3.2** 三闪 |没有内容闪烁超过 3 次 |
| **2.3.3** 交互动画 |可以禁用运动动画|
| **2.4.8** 地点 |网站内的用户位置可用 |
| **2.4.9** 链接目的（仅链接）|仅从链接文本即可明确链接目的 |
| **2.4.10** 章节标题 |章节有标题 |
| **2.4.12** 焦点不被遮挡（增强）|作者创建的内容不会隐藏焦点元素的任何部分 |
| **2.4.13** 焦点外观 |焦点指示器面积充足、对比度高、不被遮挡 |
| **3.1.3** 不常用词 |不常用词的可用定义 |
| **3.1.4** 缩写 |缩写扩展|
| **3.1.5** 阅读水平 |复杂文本的替代内容 |
| **3.1.6** 发音 |需要时可提供发音 |
| **3.2.5** 根据要求进行更改 |仅由用户发起的更改 |
| **3.3.5** 帮助 |提供上下文相关帮助 |
| **3.3.6** 错误预防（全部）|所有提交的表单均可审核 |
| **3.3.9** 可访问的身份验证（增强）|登录无需进行认知功能测试（无物体或个人内容识别例外）|

## 常见的 ARIA 模式

### 按钮
````html
<按钮>标签</按钮>
<!-- 或 -->
<button aria-label="关闭对话框">×</button>
````

### 链接
````html
<a href="/page">描述性链接文本</a>
<!-- 外部链接 -->
<a href="https://external.com" target="_blank" rel="noopener">
  外部网站
  <span class="visually-hidden">（在新选项卡中打开）</span>
</a>
````

### 表单字段
````html
<label for="email">电子邮件地址</label>
<input type="email" id="email" aria-scribedby="email-hint">
<p id="email-hint">我们绝不会分享您的电子邮件。</p>
````

### 错误状态
````html
<标签=“电子邮件”>电子邮件</标签>
<input type="email" id="email" aria-invalid="true" aria-scribedby="email-error">
<p id="email-error" role="alert">请输入有效的电子邮件地址。</p>
````

### 导航
````html
<nav aria-label="主">
  <ul>
    <li><a href="/" aria-current="page">首页</a></li>
    <li><a href="/about">关于</a></li>
  </ul>
</导航>
````

### 情态动词
````html
<div role="dialog" aria-modal="true" aria-labelledby="dialog-title">
  <h2 id="dialog-title">确认操作</h2>
  <!-- 内容 -->
</div>
````

### 实时区域
````html
<!-- 礼貌（等待讲话暂停）-->
<div aria-live="polite">此处更新状态</div>

<!-- 断言（立即打断）-->
<div aria-live="assertive" role="alert">此处出现错误消息</div>

<!-- 状态（礼貌、含蓄）-->
<div role="status">加载完成</div>
````

## 2.1 到 2.2 发生了什么变化

|改变 |标准|水平|
|--------|------------|--------|
| **已删除** | 4.1.1 解析|一个 |
| **添加** | 2.4.11 焦点不被遮挡（最小）| AA |
| **添加** | 2.4.12 焦点不被遮挡（增强）| AAA |
| **添加** | 2.4.13 焦点外观 | AAA |
| **添加** | 2.5.7 拖动运动| AA |
| **添加** | 2.5.8 目标尺寸（最小）| AA |
| **添加** | 3.2.6 一致的帮助 |一个 |
| **添加** | 3.3.7 冗余条目|一个 |
| **添加** | 3.3.8 可访问的身份验证（最低）| AA |
| **添加** | 3.3.9 可访问的身份验证（增强）| AAA |

## 测试工具

|工具|类型 |网址 |
|------|------|-----|
|斧头开发工具 |浏览器扩展 | [deque.com/axe](https://www.deque.com/axe/) |
|波|浏览器扩展 | [wave.webaim.org](https://wave.webaim.org/) |
|灯塔|内置于 Chrome |开发工具 → 灯塔 |
|英伟达 |屏幕阅读器 (Windows) | [nvaccess.org](https://www.nvaccess.org/) |
|画外音 |屏幕阅读器 (Mac) |内置于 macOS |
|色彩对比分析仪|桌面应用程序 | [tpgi.com](https://www.tpgi.com/color-contrast-checker/) |

## 来源

- [WCAG 2.2 W3C 建议](https://www.w3.org/TR/WCAG22/)
- [WCAG 2.2 快速参考](https://www.w3.org/WAI/WCAG22/quickref/)
- [WCAG 2.2 的新增功能](https://www.w3.org/WAI/standards-guidelines/wcag/new-in-22/)
# Короткий довідник WCAG 2.2

## Критерії успіху за рівнем

### Рівень А (мінімум)

| Критерій | Опис |
|-----------|-------------|
| **1.1.1** Нетекстовий вміст | Усі зображення, іконки мають текстові альтернативи |
| **1.2.1** Лише аудіо/Лише відео | Надайте розшифровку або аудіоопис |
| **1.2.2** Підписи | Відео з аудіо має субтитри |
| **1.2.3** Аудіоопис | Відео має звуковий опис |
| **1.3.1** Інформація та зв’язки | Інформація, що передається через презентацію, доступна програмно |
| **1.3.2** Значуща послідовність | Порядок читання логічний |
| **1.3.3** Сенсорні характеристики | Інструкції не залежать лише від форми, кольору, розміру, розташування, орієнтації чи звуку |
| **1.4.1** Використання кольору | Колір не єдиний візуальний засіб передачі інформації |
| **1.4.2** Керування звуком | Автоматичне відтворення аудіо можна призупинити/зупинити |
| **2.1.1** Клавіатура | Усі функції доступні через клавіатуру |
| **2.1.2** Без перехоплення клавіатури | Фокус клавіатури можна відсунути від будь-якого компонента |
| **2.1.4** Сполучення клавіш із символами | Комбінації швидкого доступу з однією клавішею можна вимкнути або змінити |
| **2.2.1** Регульований час | Терміни можуть бути продовжені |
| **2.2.2** Призупинити, зупинити, приховати | Рухомий/миготливий вміст можна призупинити |
| **2.3.1** Три спалахи | Ніщо не блимає більше 3 разів на секунду |
| **2.4.1** Обхідні блоки | Доступне посилання для пропуску або орієнтир |
| **2.4.2** Сторінка під назвою | Сторінки мають описові заголовки |
| **2.4.3** Порядок фокусування | Порядок фокусування зберігає значення |
| **2.4.4** Мета посилання | Мета посилання зрозуміла з тексту посилання чи контексту |
| **2.5.1** Жести вказівника | Багатоточкові жести мають альтернативу одним вказівником |
| **2.5.2** Скасування покажчика | Подія «вниз» не викликає дії (використовуйте подію «вгору» або клацання) |
| **2.5.3** Мітка в назві | Доступне ім’я містить видимий текст мітки |
| **2.5.4** Активація руху | Функції, що запускаються рухом, мають альтернативи |
| **3.1.1** Мова сторінки | Мова за умовчанням, указана в HTML |
| **3.2.1** У фокусі | Фокус не викликає неочікуваних змін |
| **3.2.2** При введенні | Введення не викликає неочікуваних змін |
| **3.2.6** Послідовна довідка | Механізми довідки відображаються в однаковому відносному порядку на сторінках |
| **3.3.1** Ідентифікація помилки | Чітко описані помилки введення |
| **3.3.2** Мітки чи інструкції | Вхідні дані форми мають мітки або інструкції |
| **3.3.7** Надлишковий запис | Попередньо введена інформація заповнюється автоматично або доступна для вибору |
| **4.1.2** Ім’я, роль, значення | Компоненти інтерфейсу користувача мають доступні імена та правильні ролі |

### Рівень AA (стандарт)

| Критерій | Опис |
|-----------|-------------|
| **1.2.4** Підписи (живі) | Живе аудіо має субтитри |
| **1.2.5** Аудіоопис | Попередньо записане відео має звуковий опис |
| **1.3.4** Орієнтація | Вміст не обмежує орієнтацію |
| **1.3.5** Визначте мету введення | Мета введення може бути визначена програмно |
| **1.4.3** Контраст (мінімальний) | 4,5:1 для звичайного тексту, 3:1 для великого тексту |
| **1.4.4** Змінити розмір тексту | Розмір тексту можна змінити до 200% без втрати функціональності |
| **1.4.5** Зображення тексту | Текст використовується замість зображень тексту |
| **1.4.10** Reflow | Вміст перекомпоновується на ширину 320 пікселів без горизонтального прокручування |
| **1.4.11** Нетекстовий контраст | Компоненти інтерфейсу користувача мають контраст 3:1 |
| **1.4.12** Інтервал між текстом | Вміст адаптується до зміни міжтекстового інтервалу |
| **1.4.13** Вміст під час наведення/фокусування | Додатковий вміст можна відхилити, навести, постійно |
| **2.4.5** Кілька способів | Кілька способів пошуку сторінок |
| **2.4.6** Заголовки та мітки | Заголовки та написи є описовими |
| **2.4.7** Видимий фокус | Видно індикатор фокусування |
| **2.4.11** Фокус не затемнений (мінімум) | Виділений елемент не повністю прихований вмістом, створеним автором |
| **2.5.7** Рухи перетягування | Дії перетягування мають альтернативи з одним вказівником |
| **2.5.8** Цільовий розмір (мінімальний) | Інтерактивні цілі мають принаймні 24 × 24 пікселів CSS (за винятком) |
| **3.1.2** Мова частин | Мовні зміни позначені |
| **3.2.3** Послідовна навігація | Навігація на сторінках узгоджена |
| **3.2.4** Послідовна ідентифікація | Однакові функції використовують однакові мітки |
| **3.3.3** Помилка Пропозиція | Запропоновані виправлення помилок, якщо відомо |
| **3.3.4** Запобігання помилкам (юридичне) | Дії можна скасувати або підтвердити |
| **3.3.8** Доступна автентифікація (мінімум) | Немає перевірки когнітивних функцій для входу, якщо не надається альтернатива чи допомога |
| **4.1.3** Повідомлення про стан | Повідомлення про статус, оголошені програмам зчитування з екрана |

### Рівень AAA (розширений)

| Критерій | Опис |
|-----------|-------------|
| **1.4.6** Контраст (підвищений) | 7:1 для звичайного тексту, 4,5:1 для великого тексту |
| **1.4.8** Візуальна презентація | Можна вибрати кольори переднього/фонового плану |
| **1.4.9** Зображення тексту (без винятку) | Немає зображень тексту |
| **2.1.3** Клавіатура (без винятку) | Усі функції клавіатури доступні |
| **2.2.3** Немає часу | Немає часових обмежень |
| **2.2.4** Переривання | Перерви можна відкласти |
| **2.2.5** Повторна автентифікація | Дані зберігаються під час повторної автентифікації |
| **2.2.6** Час очікування | Користувачів попередили про втрату даних через бездіяльність |
| **2.3.2** Три спалахи | Жоден вміст не блимає більше ніж 3 рази |
| **2.3.3** Анімація з Interactions | Анімацію руху можна вимкнути |
| **2.4.8** Розташування | Розташування користувача на сайті доступне |
| **2.4.9** Мета посилання (лише посилання) | Мета посилання зрозуміла лише з тексту посилання |
| **2.4.10** Заголовки розділів | Розділи мають заголовки |
| **2.4.12** Фокус не затемнений (покращено) | Жодна частина виділеного елемента не прихована вмістом, створеним автором |
| **2.4.13** Вигляд фокуса | Індикатор фокусування має достатню площу, контрастність і не затемнений |
| **3.1.3** Незвичайні слова | Доступні визначення незвичайних слів |
| **3.1.4** Скорочення | Скорочення розширено |
| **3.1.5** Рівень читання | Альтернативний контент для складного тексту |
| **3.1.6** Вимова | Вимова доступна, де це необхідно |
| **3.2.5** Зміна за запитом | Зміни ініційовані лише користувачем |
| **3.3.5** Довідка | Доступна контекстно-залежна довідка |
| **3.3.6** Запобігання помилкам (усі) | Усі подані форми можна переглянути |
| **3.3.9** Доступна автентифікація (розширена) | Немає перевірки когнітивних функцій для входу (немає винятків для розпізнавання об’єктів або особистого вмісту) |

## Загальні шаблони ARIA

### Кнопки
```html
<button>Мітка</button>
<!-- або -->
<button aria-label="Закрити діалогове вікно">×</button>
```

### Посилання
```html
<a href="/page">Описовий текст посилання</a>
<!-- Зовнішні посилання -->
<a href="https://external.com" target="_blank" rel="noopener">
  Зовнішній сайт
  <span class="visually-hidden">(відкривається в новій вкладці)</span>
</a>
```

### Поля форми
```html
<label for="email">Адреса електронної пошти</label>
<input type="email" id="email" aria-describedby="email-hint">
<p id="email-hint">Ми ніколи не розголошуватимемо вашу електронну адресу.</p>
```

### Стани помилок
```html
<label for="email">Електронна пошта</label>
<input type="email" id="email" aria-invalid="true" aria-describedby="email-error">
<p id="email-error" role="alert">Будь ласка, введіть дійсну адресу електронної пошти.</p>
```

### Навігація
```html
<nav aria-label="Main">
  <ul>
    <li><a href="/" aria-current="page">Домашня сторінка</a></li>
    <li><a href="/about">Про</a></li>
  </ul>
</nav>
```

### Модальні
```html
<div role="dialog" aria-modal="true" aria-labelledby="dialog-title">
  <h2 id="dialog-title">Підтвердити дію</h2>
  <!-- вміст -->
</div>
```

### Живі регіони
```html
<!-- Ввічливий (чекає паузи в мовленні) -->
<div aria-live="polite">Оновлення статусу тут</div>

<!-- Напористий (миттєво перебиває) -->
<div aria-live="assertive" role="alert">Повідомлення про помилку тут</div>

<!-- Статус (ввічливий, неявний) -->
<div role="status">Завантаження завершено</div>
```

## Що змінилося з 2.1 на 2.2

| Змінити | Критерій | Рівень |
|--------|----------|-------|
| **Видалено** | 4.1.1 Розбір | A |
| **Додано** | 2.4.11 Фокус не затемнений (мінімум) | АА |
| **Додано** | 2.4.12 Фокус не затемнений (покращено) | AAA |
| **Додано** | 2.4.13 Зовнішній вигляд фокуса | AAA |
| **Додано** | 2.5.7 Рухи перетягування | АА |
| **Додано** | 2.5.8 Розмір цілі (мінімальний) | АА |
| **Додано** | 3.2.6 Послідовна допомога | A |
| **Додано** | 3.3.7 Надлишковий запис | A |
| **Додано** | 3.3.8 Доступна автентифікація (мінімум) | АА |
| **Додано** | 3.3.9 Доступна автентифікація (розширена) | AAA |

## Інструменти тестування

| Інструмент | Тип | URL |
|------|------|-----|
| ax DevTools | Розширення для браузера | [deque.com/axe](https://www.deque.com/axe/) |
| ХВИЛЯ | Розширення для браузера | [wave.webaim.org](https://wave.webaim.org/) |
| Маяк | Вбудовано в Chrome | Інструменти розробника → Маяк |
| NVDA | Зчитувач з екрана (Windows) | [nvaccess.org](https://www.nvaccess.org/) |
| VoiceOver | Програма зчитування з екрана (Mac) | Вбудовано в macOS |
| Аналізатор колірного контрасту | Настільна програма | [tpgi.com](https://www.tpgi.com/color-contrast-checker/) |

## Джерела

- [Рекомендація WCAG 2.2 W3C](https://www.w3.org/TR/WCAG22/)
- [Короткий довідник WCAG 2.2](https://www.w3.org/WAI/WCAG22/quickref/)
- [Що нового в WCAG 2.2](https://www.w3.org/WAI/standards-guidelines/wcag/new-in-22/)
# WCAG 2.2 Краткий справочник

## Критерии успеха по уровням

### Уровень А (минимум)

| Критерий | Описание |
|-----------|-------------|
| **1.1.1** Нетекстовый контент | Все изображения и значки имеют альтернативный текст |
| **1.2.1** Только аудио/только видео | Предоставьте расшифровку или аудиоописание |
| **1.2.2** Подписи | Видео со звуком имеет субтитры |
| **1.2.3** Аудиоописание | Видео имеет аудиоописание |
| **1.3.1** Информация и отношения | Информация, передаваемая посредством презентации, доступна программно |
| **1.3.2** Значимая последовательность | Порядок чтения логичен |
| **1.3.3** Сенсорные характеристики | Инструкции не зависят исключительно от формы, цвета, размера, местоположения, ориентации или звука |
| **1.4.1** Использование цвета | Цвет – не единственное визуальное средство передачи информации |
| **1.4.2** Управление звуком | Автоматическое воспроизведение звука можно приостановить/остановить |
| **2.1.1** Клавиатура | Все функции доступны через клавиатуру |
| **2.1.2** Нет ловушки клавиатуры | Фокус клавиатуры можно переместить с любого компонента |
| **2.1.4** Сочетания клавиш символов | Сочетания клавиш можно отключить или переназначить |
| **2.2.1** Регулируемая синхронизация | Сроки могут быть продлены |
| **2.2.2** Пауза, Стоп, Скрыть | Перемещение/мигание контента можно приостановить |
| **2.3.1** Три мигания | Ничто не мигает чаще 3 раз в секунду |
| **2.4.1** Обходные блоки | Пропустить ссылку или доступна навигация по ориентирам |
| **2.4.2** Страница с названием | Страницы имеют описательные заголовки |
| **2.4.3** Порядок фокусировки | Порядок фокуса сохраняет смысл |
| **2.4.4** Цель ссылки | Цель ссылки ясна из текста или контекста ссылки |
| **2.5.1** Жесты указателя | У многоточечных жестов есть альтернативы с одним указателем |
| **2.5.2** Отмена указателя | Событие «вниз» не запускает действие (используйте событие «вверх» или щелкните мышью) |
| **2.5.3** Метка в имени | Доступное имя содержит видимый текст метки |
| **2.5.4** Активация движения | У функций, запускаемых движением, есть альтернативы |
| **3.1.1** Язык страницы | Язык по умолчанию указан в HTML |
| **3.2.1** В фокусе | Фокус не вызывает неожиданных изменений |
| **3.2.2** При вводе | Ввод не вызывает неожиданных изменений |
| **3.2.6** Постоянная справка | Механизмы помощи отображаются на страницах в одинаковом относительном порядке |
| **3.3.1** Идентификация ошибок | Ошибки ввода четко описаны |
| **3.3.2** Этикетки или инструкции | Входные данные формы имеют метки или инструкции |
| **3.3.7** Дублирующая запись | Ранее введенная информация заполняется автоматически или доступна для выбора |
| **4.1.2** Имя, роль, значение | Компоненты пользовательского интерфейса имеют доступные имена и правильные роли |

### Уровень AA (стандартный)

| Критерий | Описание |
|-----------|-------------|
| **1.2.4** Субтитры (в реальном времени) | Живой звук имеет субтитры |
| **1.2.5** Аудиоописание | Предварительно записанное видео имеет аудиоописание |
| **1.3.4** Ориентация | Содержание не ограничивает ориентацию |
| **1.3.5** Определить назначение ввода | Цель ввода может быть определена программно |
| **1.4.3** Контраст (минимум) | 4,5:1 для обычного текста, 3:1 для крупного текста |
| **1.4.4** Изменение размера текста | Размер текста можно изменить до 200% без потери функциональности |
| **1.4.5** Изображения текста | Вместо изображений текста используется текст |
| **1.4.10** Перекомпоновка | Содержимое перерисовывается при ширине 320 пикселей без горизонтальной прокрутки |
| **1.4.11** Нетекстовый контраст | Компоненты пользовательского интерфейса имеют контрастность 3:1 |
| **1.4.12** Расстояние между текстами | Контент адаптируется к изменениям межтекстового интервала |
| **1.4.13** Содержимое при наведении/фокусе | Дополнительный контент можно игнорировать, зависать, сохраняться |
| **2.4.5** Несколько способов | Несколько способов поиска страниц |
| **2.4.6** Заголовки и метки | Заголовки и метки носят описательный характер |
| **2.4.7** Фокус видимый | Виден индикатор фокуса |
| **2.4.11** Фокус не скрыт (минимум) | Выделенный элемент не полностью скрыт авторским контентом |
| **2.5.7** Перетаскивание движений | У действий перетаскивания есть альтернативы с одним указателем |
| **2.5.8** Целевой размер (минимум) | Интерактивные цели имеют размер не менее 24×24 CSS-пикселей (с исключениями) |
| **3.1.2** Язык частей | Языковые изменения отмечены |
| **3.2.3** Согласованная навигация | Навигация единообразна на всех страницах |
| **3.2.4** Согласованная идентификация | Та же функциональность использует те же метки |
| **3.3.3** Предложение об ошибке | Исправления ошибок, предлагаемые, если они известны |
| **3.3.4** Предотвращение ошибок (юридическая информация) | Действия можно отменить или подтвердить |
| **3.3.8** Доступная аутентификация (минимум) | Тест когнитивных функций для входа в систему невозможен, если не предоставлена ​​альтернатива или помощь |
| **4.1.3** Сообщения о состоянии | Сообщения о состоянии, объявляемые программам чтения с экрана |

### Уровень AAA (улучшенный)

| Критерий | Описание |
|-----------|-------------|
| **1.4.6** Контраст (повышенный) | 7:1 для обычного текста, 4,5:1 для крупного текста |
| **1.4.8** Визуальная презентация | Можно выбрать цвета переднего плана/фона |
| **1.4.9** Изображения текста (без исключений) | Нет изображений текста |
| **2.1.3** Клавиатура (без исключений) | Доступны все функциональные возможности клавиатуры |
| **2.2.3** Нет времени | Нет ограничений по времени |
| **2.2.4** Перебои | Перебои можно отложить |
| **2.2.5** Повторная аутентификация | Данные сохраняются при повторной аутентификации |
| **2.2.6** Тайм-ауты | Пользователей предупредили о потере данных из-за бездействия |
| **2.3.2** Три мигания | Никакой контент не мигает более 3 раз |
| **2.3.3** Анимация из взаимодействий | Анимацию движения можно отключить |
| **2.4.8** Местоположение | Доступно местоположение пользователя на сайте |
| **2.4.9** Цель ссылки (только ссылка) | Цель ссылки ясна только из текста ссылки |
| **2.4.10** Заголовки разделов | Разделы имеют заголовки |
| **2.4.12** Фокус не скрыт (улучшенный) | Никакая часть элемента, находящегося в фокусе, не скрыта созданным автором контентом |
| **2.4.13** Внешний вид фокуса | Индикатор фокусировки имеет достаточную площадь, контрастность и не затеняется |
| **3.1.3** Необычные слова | Доступны определения необычных слов |
| **3.1.4** Сокращения | Расширение сокращений |
| **3.1.5** Уровень чтения | Альтернативный контент для сложного текста |
| **3.1.6** Произношение | Произношение доступно там, где необходимо |
| **3.2.5** Изменение по запросу | Изменения, инициированные только пользователем |
| **3.3.5** Справка | Доступна контекстно-зависимая справка |
| **3.3.6** Предотвращение ошибок (все) | Все отправленные формы можно просмотреть |
| **3.3.9** Доступная аутентификация (расширенная) | Нет проверки когнитивных функций при входе в систему (нет исключений для распознавания объектов или личного контента) |

## Общие шаблоны ARIA

### Кнопки
```html
<button>Метка</button>
<!-- или -->
<button aria-label="Закрыть диалог">×</button>
```

### Ссылки
```html
<a href="/page">Описательный текст ссылки</a>
<!-- Внешние ссылки -->
<a href="https://external.com" target="_blank" rel="noopener">
  Внешний сайт
  <span class="visually-hidden">(откроется в новой вкладке)</span>
</а>
```

### Поля формы
```html
<label for="email">Адрес электронной почты</label>
<input type="email" id="email" aria-describedby="email-hint">
<p id="email-hint">Мы никогда не передадим ваш адрес электронной почты.</p>
```

### Состояния ошибок
```html
<label for="email">Электронная почта</label>
<input type="email" id="email" aria-invalid="true" aria-describedby="email-error">
<p id="email-error" role="alert">Введите действительный адрес электронной почты.</p>
```

### Навигация
```html
<nav aria-label="Основной">
  <ул>
    <li><a href="/" aria-current="page">Главная</a></li>
    <li><a href="/about">О программе</a></li>
  </ul>
</нав>
```

### Модальные окна
```html
<div role="dialog" aria-modal="true" aria-labelledby="dialog-title">
  <h2 id="dialog-title">Подтвердить действие</h2>
  <!-- содержимое -->
</div>
```

### Живые регионы
```html
<!-- Вежливо (ждёт паузы в речи) -->
<div aria-live="polite">Обновление статуса здесь</div>

<!-- Настойчиво (сразу прерывает) -->
<div aria-live="assertive" role="alert">Здесь сообщение об ошибке</div>

<!-- Статус (вежливый, неявный) -->
<div role="status">Загрузка завершена</div>
```

## Что изменилось с версии 2.1 на 2.2

| Изменить | Критерий | Уровень |
|--------|-----------|-------|
| **Удалено** | 4.1.1 Анализ | А |
| **Добавлено** | 2.4.11 Фокус не скрыт (минимум) | АА |
| **Добавлено** | 2.4.12 Фокус не скрыт (улучшенный) | ААА |
| **Добавлено** | 2.4.13 Внешний вид фокуса | ААА |
| **Добавлено** | 2.5.7 Перетаскивание | АА |
| **Добавлено** | 2.5.8 Целевой размер (минимальный) | АА |
| **Добавлено** | 3.2.6 Постоянная справка | А |
| **Добавлено** | 3.3.7 Дублирующий ввод | А |
| **Добавлено** | 3.3.8 Доступная аутентификация (минимум) | АА |
| **Добавлено** | 3.3.9 Доступная аутентификация (расширенная) | ААА |

## Инструменты тестирования

| Инструмент | Тип | URL-адрес |
|------|------|-----|
| топор DevTools | Расширение для браузера | [deque.com/axe](https://www.deque.com/axe/) |
| ВОЛНА | Расширение для браузера | [wave.webaim.org](https://wave.webaim.org/) |
| Маяк | Встроено в Chrome | Инструменты разработчика → Маяк |
| НВДА | Программа чтения с экрана (Windows) | [nvaccess.org](https://www.nvaccess.org/) |
| Голос за кадром | Программа чтения с экрана (Mac) | Встроено в macOS |
| Анализатор цветового контраста | Настольное приложение | [tpgi.com](https://www.tpgi.com/color-contrast-checker/) |

## Источники

- [Рекомендация WCAG 2.2 W3C] (https://www.w3.org/TR/WCAG22/)
- [Краткий справочник WCAG 2.2] (https://www.w3.org/WAI/WCAG22/quickref/)
- [Что нового в WCAG 2.2] (https://www.w3.org/WAI/standards-guidelines/wcag/new-in-22/)
# WCAG 2.2 Guida rapida

## Criteri di successo per livello

### Livello A (minimo)

| Criterio | Descrizione |
|-----------|-------------|
| **1.1.1** Contenuti non testuali | Tutte le immagini e le icone hanno alternative di testo |
| **1.2.1** Solo audio/Solo video | Fornire la trascrizione o la descrizione audio |
| **1.2.2** Didascalie | Il video con audio ha didascalie |
| **1.2.3** Descrizione audio | Il video ha una descrizione audio |
| **1.3.1** Informazioni e Relazioni | Le informazioni trasmesse attraverso la presentazione sono disponibili a livello di programmazione |
| **1.3.2** Sequenza significativa | L'ordine di lettura è logico |
| **1.3.3** Caratteristiche sensoriali | Le istruzioni non si basano esclusivamente su forma, colore, dimensione, posizione, orientamento o suono |
| **1.4.1** Uso del colore | Il colore non è l'unico mezzo visivo per trasmettere informazioni |
| **1.4.2** Controllo audio | La riproduzione audio automatica può essere messa in pausa/interrotta |
| **2.1.1** Tastiera | Tutte le funzionalità disponibili tramite tastiera |
| **2.1.2** Nessuna trappola sulla tastiera | Il focus della tastiera può essere spostato da qualsiasi componente |
| **2.1.4** Scorciatoie da tastiera con caratteri | Le scorciatoie a tasto singolo possono essere disattivate o rimappate |
| **2.2.1** Temporizzazione regolabile | I termini possono essere prorogati |
| **2.2.2** Pausa, Interrompi, Nascondi | È possibile mettere in pausa i contenuti in movimento/lampeggianti |
| **2.3.1** Tre lampeggi | Niente lampeggia più di 3 volte al secondo |
| **2.4.1** Ignora blocchi | Salta collegamento o navigazione punto di riferimento disponibile |
| **2.4.2** Pagina intitolata | Le pagine hanno titoli descrittivi |
| **2.4.3** Ordine dei focus | L'ordine del focus preserva il significato |
| **2.4.4** Scopo del collegamento | Scopo del collegamento chiaro dal testo o dal contesto del collegamento |
| **2.5.1** Gesti del puntatore | I gesti multipunto hanno alternative a puntatore singolo |
| **2.5.2** Cancellazione puntatore | L'evento down non attiva l'azione (utilizzare l'evento up o fare clic) |
| **2.5.3** Etichetta nel nome | Il nome accessibile contiene il testo dell'etichetta visibile |
| **2.5.4** Attuazione del movimento | Le funzioni attivate dal movimento hanno alternative |
| **3.1.1** Lingua della pagina | Lingua predefinita specificata in HTML |
| **3.2.1** In primo piano | Il focus non innesca cambiamenti inaspettati |
| **3.2.2** Su ingresso | L'input non attiva modifiche impreviste |
| **3.2.6** Aiuto coerente | I meccanismi di aiuto appaiono nello stesso ordine relativo nelle pagine |
| **3.3.1** Identificazione errore | Errori di input chiaramente descritti |
| **3.3.2** Etichette o istruzioni | Gli input del modulo hanno etichette o istruzioni |
| **3.3.7** Voce ridondante | Le informazioni immesse in precedenza vengono compilate automaticamente o sono disponibili per selezionare |
| **4.1.2** Nome, Ruolo, Valore | I componenti dell'interfaccia utente hanno nomi accessibili e ruoli corretti |

### Livello AA (standard)

| Criterio | Descrizione |
|-----------|-------------|
| **1.2.4** Sottotitoli (Live) | L'audio dal vivo ha didascalie |
| **1.2.5** Descrizione audio | Il video preregistrato ha una descrizione audio |
| **1.3.4** Orientamento | Il contenuto non limita l'orientamento |
| **1.3.5** Identificare lo scopo dell'input | Lo scopo dell'input può essere determinato a livello di codice |
| **1.4.3** Contrasto (minimo) | 4,5:1 per testo normale, 3:1 per testo grande |
| **1.4.4** Ridimensiona testo | Il testo può essere ridimensionato al 200% senza perdita di funzionalità |
| **1.4.5** Immagini di testo | Testo utilizzato al posto delle immagini del testo |
| **1.4.10** Ridisponi | Il contenuto si adatta alla larghezza di 320 px senza scorrimento orizzontale |
| **1.4.11** Contrasto non testuale | I componenti dell'interfaccia utente hanno un contrasto 3:1 |
| **1.4.12** Spaziatura testo | Il contenuto si adatta alle modifiche della spaziatura del testo |
| **1.4.13** Contenuti al passaggio del mouse/messa a fuoco | Il contenuto aggiuntivo è ignorabile, trasferibile, persistente |
| **2.4.5** Modi multipli | Diversi modi per trovare pagine |
| **2.4.6** Intestazioni ed etichette | I titoli e le etichette sono descrittivi |
| **2.4.7** Focus visibile | L'indicatore di messa a fuoco è visibile |
| **2.4.11** Messa a fuoco non oscurata (minimo) | L'elemento focalizzato non è completamente nascosto dal contenuto creato dall'autore |
| **2.5.7** Movimenti di trascinamento | Le azioni di trascinamento hanno alternative a puntatore singolo |
| **2.5.8** Dimensione target (minima) | I target interattivi sono almeno 24×24 pixel CSS (con eccezioni) |
| **3.1.2** Lingua delle parti | Le modifiche alla lingua sono contrassegnate |
| **3.2.3** Navigazione coerente | La navigazione è coerente tra le pagine |
| **3.2.4** Identificazione coerente | La stessa funzionalità utilizza le stesse etichette |
| **3.3.3** Suggerimento errore | Correzioni di errori suggerite quando note |
| **3.3.4** Prevenzione degli errori (legale) | Le azioni possono essere annullate o confermate |
| **3.3.8** Autenticazione accessibile (minimo) | Nessun test delle funzioni cognitive per l'accesso a meno che non venga fornita un'alternativa o assistenza |
| **4.1.3** Messaggi di stato | Messaggi di stato annunciati agli screen reader |

### Livello AAA (potenziato)

| Criterio | Descrizione |
|-----------|-------------|
| **1.4.6** Contrasto (migliorato) | 7:1 per testo normale, 4,5:1 per testo grande |
| **1.4.8** Presentazione visiva | È possibile selezionare i colori di primo piano/sfondo |
| **1.4.9** Immagini di testo (nessuna eccezione) | Nessuna immagine di testo |
| **2.1.3** Tastiera (nessuna eccezione) | Tutte le funzionalità accessibili tramite tastiera |
| **2.2.3** Nessuna tempistica | Nessun limite di tempo |
| **2.2.4** Interruzioni | Le interruzioni possono essere rinviate |
| **2.2.5** Riautenticazione | Dati conservati durante la riautenticazione |
| **2.2.6** Timeout | Gli utenti sono stati avvisati della perdita di dati dovuta all'inattività |
| **2.3.2** Tre lampeggi | Nessun contenuto lampeggia più di 3 volte |
| **2.3.3** Animazione dalle interazioni | L'animazione del movimento può essere disabilitata |
| **2.4.8** Posizione | La posizione dell'utente all'interno del sito è disponibile |
| **2.4.9** Scopo del collegamento (solo collegamento) | Lo scopo del collegamento è chiaro solo dal testo del collegamento |
| **2.4.10** Titoli delle sezioni | Le sezioni hanno intestazioni |
| **2.4.12** Messa a fuoco non oscurata (migliorata) | Nessuna parte dell'elemento focalizzato è nascosta dal contenuto creato dall'autore |
| **2.4.13** Aspetto del focus | L'indicatore di messa a fuoco ha un'area e un contrasto sufficienti e non è oscurato |
| **3.1.3** Parole insolite | Definizioni disponibili per parole insolite |
| **3.1.4** Abbreviazioni | Abbreviazioni ampliate |
| **3.1.5** Livello di lettura | Contenuti alternativi per testi complessi |
| **3.1.6** Pronuncia | Pronuncia disponibile dove necessario |
| **3.2.5** Modifica su richiesta | Modifiche avviate solo dall'utente |
| **3.3.5** Aiuto | Guida sensibile al contesto disponibile |
| **3.3.6** Prevenzione degli errori (tutti) | Tutti i moduli inviati possono essere esaminati |
| **3.3.9** Autenticazione accessibile (avanzata) | Nessun test delle funzioni cognitive per il login (nessuna eccezione per il riconoscimento di oggetti o contenuti personali) |

## Modelli ARIA comuni

### Pulsanti
```html
<button>Etichetta</button>
<!-- o -->
<button aria-label="Chiudi finestra di dialogo">×</button>
```

### Collegamenti
```html
<a href="/page">Testo del collegamento descrittivo</a>
<!-- Collegamenti esterni -->
<a href="https://external.com" target="_blank" rel="noopener">
  Sito esterno
  <span class="visually-hidden">(si apre in una nuova scheda)</span>
</a>
```

### Campi del modulo
```html
<label for="email">Indirizzo email</label>
<input type="email" id="email" aria-descriptionby="email-hint">
<p id="email-hint">Non condivideremo mai la tua email.</p>
```

### Stati di errore
```html
<label for="email">E-mail</label>
<input type="email" id="email" aria-invalid="true" aria-descriptionby="email-error">
<p id="email-error" role="alert">Inserisci un indirizzo email valido.</p>
```

### Navigazione
```html
<nav aria-label="Principale">
  <ul>
    <li><a href="/" aria-current="page">Home</a></li>
    <li><a href="/about">Informazioni</a></li>
  </ul>
</nav>
```

### Modali
```html
<div role="dialogo" aria-modal="true" aria-labelledby="dialogo-titolo">
  <h2 id="dialog-title">Conferma azione</h2>
  <!-- contenuto -->
</div>
```

### Regioni vive
```html
<!-- Gentile (attende la pausa nel discorso) -->
<div aria-live="polite">Aggiornamento stato qui</div>

<!-- Assertivo (interrompe immediatamente) -->
<div aria-live="assertive" role="alert">Messaggio di errore qui</div>

<!-- Stato (educato, implicito) -->
<div role="status">Caricamento completato</div>
```

## Cosa è cambiato dalla versione 2.1 alla versione 2.2

| Cambia | Criterio | Livello |
|--------|-----------|-------|
| **Rimosso** | 4.1.1 Analisi | A |
| **Aggiunto** | 2.4.11 Messa a fuoco non oscurata (minima) | AA |
| **Aggiunto** | 2.4.12 Focus non oscurato (migliorato) | AAA |
| **Aggiunto** | 2.4.13 Aspetto del focus | AAA |
| **Aggiunto** | 2.5.7 Movimenti di trascinamento | AA |
| **Aggiunto** | 2.5.8 Dimensione target (minima) | AA |
| **Aggiunto** | 3.2.6 Aiuto coerente | A |
| **Aggiunto** | 3.3.7 Voce ridondante | A |
| **Aggiunto** | 3.3.8 Autenticazione accessibile (minima) | AA |
| **Aggiunto** | 3.3.9 Autenticazione accessibile (avanzata) | AAA |

## Strumenti di test

| Strumento | Digitare | URL |
|------|------|-----|
| axDevTools | Estensione del browser | [deque.com/axe](https://www.deque.com/axe/) |
| ONDA | Estensione del browser | [wave.webaim.org](https://wave.webaim.org/) |
| Faro | Integrato in Chrome | DevTools → Faro |
| NVDA | Lettore di schermo (Windows) | [nvaccess.org](https://www.nvaccess.org/) |
| Voce fuori campo | Lettore di schermo (Mac) | Integrato in macOS |
| Analizzatore del contrasto colore | Applicazione desktop | [tpgi.com](https://www.tpgi.com/color-contrast-checker/) |

## Fonti

- [Raccomandazione W3C WCAG 2.2](https://www.w3.org/TR/WCAG22/)
- [Riferimento rapido WCAG 2.2](https://www.w3.org/WAI/WCAG22/quickref/)
- [Novità nelle WCAG 2.2](https://www.w3.org/WAI/standards-guidelines/wcag/new-in-22/)
# Referência rápida WCAG 2.2

## Critérios de sucesso por nível

### Nível A (mínimo)

| Critério | Descrição |
|-----------|------------|
| **1.1.1** Conteúdo não textual | Todas as imagens e ícones possuem alternativas de texto |
| **1.2.1** Somente áudio/Somente vídeo | Fornecer transcrição ou audiodescrição |
| **1.2.2** Legendas | Vídeo com áudio possui legenda |
| **1.2.3** Descrição de áudio | Vídeo possui audiodescrição |
| **1.3.1** Informações e Relacionamentos | As informações transmitidas por meio de apresentação estão disponíveis de forma programática |
| **1.3.2** Sequência significativa | A ordem de leitura é lógica |
| **1.3.3** Características sensoriais | As instruções não dependem apenas de forma, cor, tamanho, localização, orientação ou som |
| **1.4.1** Uso de cores | A cor não é o único meio visual de transmitir informações |
| **1.4.2** Controle de áudio | A reprodução de áudio automaticamente pode ser pausada/parada |
| **2.1.1** Teclado | Todas as funcionalidades disponíveis via teclado |
| **2.1.2** Sem armadilha de teclado | O foco do teclado pode ser afastado de qualquer componente |
| **2.1.4** Atalhos de teclas de caracteres | Atalhos de tecla única podem ser desativados ou remapeados |
| **2.2.1** Tempo ajustável | Os prazos podem ser prorrogados |
| **2.2.2** Pausar, Parar, Ocultar | Conteúdo em movimento/piscando pode ser pausado |
| **2.3.1** Três flashes | Nada pisca mais de 3 vezes por segundo |
| **2.4.1** Bloqueios de desvio | Pular link ou navegação de ponto de referência disponível |
| **2.4.2** Página intitulada | As páginas têm títulos descritivos |
| **2.4.3** Ordem de foco | A ordem do foco preserva o significado |
| **2.4.4** Finalidade do link | Finalidade do link clara no texto ou contexto do link |
| **2.5.1** Gestos de ponteiro | Gestos multiponto têm alternativas de ponteiro único |
| **2.5.2** Cancelamento do ponteiro | Evento inativo não aciona ação (use evento ativo ou clique) |
| **2.5.3** Etiqueta no nome | O nome acessível contém texto de rótulo visível |
| **2.5.4** Atuação de movimento | Funções acionadas por movimento têm alternativas |
| **3.1.1** Idioma da página | Idioma padrão especificado em HTML |
| **3.2.1** Em foco | O foco não desencadeia mudanças inesperadas |
| **3.2.2** Na entrada | A entrada não desencadeia alterações inesperadas |
| **3.2.6** Ajuda consistente | Os mecanismos de ajuda aparecem na mesma ordem relativa nas páginas |
| **3.3.1** Identificação de erros | Erros de introdução claramente descritos |
| **3.3.2** Etiquetas ou instruções | As entradas do formulário possuem rótulos ou instruções |
| **3.3.7** Entrada Redundante | As informações inseridas anteriormente são preenchidas automaticamente ou ficam disponíveis para seleção |
| **4.1.2** Nome, Função, Valor | Os componentes da UI têm nomes acessíveis e funções corretas |

### Nível AA (padrão)

| Critério | Descrição |
|-----------|------------|
| **1.2.4** Legendas (ao vivo) | Áudio ao vivo tem legendas |
| **1.2.5** Descrição de áudio | Vídeo pré-gravado possui audiodescrição |
| **1.3.4** Orientação | Conteúdo não restringe orientação |
| **1.3.5** Identificar a finalidade da entrada | A finalidade da entrada pode ser determinada programaticamente |
| **1.4.3** Contraste (Mínimo) | 4,5:1 para texto normal, 3:1 para texto grande |
| **1.4.4** Redimensionar texto | O texto pode ser redimensionado para 200% sem perda de funcionalidade |
| **1.4.5** Imagens de texto | Texto usado em vez de imagens de texto |
| **1.4.10** Refluxo | O conteúdo reflui com largura de 320px sem rolagem horizontal |
| **1.4.11** Contraste sem texto | Os componentes da UI têm contraste 3:1 |
| **1.4.12** Espaçamento de texto | O conteúdo se adapta às alterações de espaçamento do texto |
| **1.4.13** Conteúdo ao passar o mouse/foco | O conteúdo adicional pode ser descartado, pairável e persistente |
| **2.4.5** Múltiplas maneiras | Várias maneiras de encontrar páginas |
| **2.4.6** Títulos e Rótulos | Os títulos e rótulos são descritivos |
| **2.4.7** Foco visível | O indicador de foco está visível |
| **2.4.11** Foco não obscurecido (mínimo) | O elemento em foco não está totalmente oculto pelo conteúdo criado pelo autor |
| **2.5.7** Movimentos de arrastamento | Ações de arrastar têm alternativas de ponteiro único |
| **2.5.8** Tamanho alvo (mínimo) | Os alvos interativos têm pelo menos 24×24 pixels CSS (com exceções) |
| **3.1.2** Idioma das Peças | As alterações de idioma estão marcadas |
| **3.2.3** Navegação Consistente | A navegação é consistente nas páginas |
| **3.2.4** Identificação Consistente | A mesma funcionalidade usa os mesmos rótulos |
| **3.3.3** Sugestão de erro | Correções de erros sugeridas quando conhecidas |
| **3.3.4** Prevenção de erros (legal) | Ações podem ser revertidas ou confirmadas |
| **3.3.8** Autenticação acessível (mínimo) | Nenhum teste de função cognitiva para login, a menos que seja fornecida uma alternativa ou assistência |
| **4.1.3** Mensagens de status | Mensagens de status anunciadas para leitores de tela |

### Nível AAA (aprimorado)

| Critério | Descrição |
|-----------|------------|
| **1.4.6** Contraste (aprimorado) | 7:1 para texto normal, 4,5:1 para texto grande |
| **1.4.8** Apresentação Visual | As cores de primeiro plano/fundo podem ser selecionadas |
| **1.4.9** Imagens de texto (sem exceção) | Sem imagens de texto |
| **2.1.3** Teclado (sem exceção) | Todas as funcionalidades do teclado acessíveis |
| **2.2.3** Sem tempo | Sem limites de tempo |
| **2.2.4** Interrupções | As interrupções podem ser adiadas |
| **2.2.5** Reautenticação | Dados preservados na reautenticação |
| **2.2.6** Tempos limite | Usuários alertados sobre perda de dados por inatividade |
| **2.3.2** Três flashes | Nenhum conteúdo pisca mais de 3 vezes |
| **2.3.3** Animação de interações | A animação em movimento pode ser desativada |
| **2.4.8** Localização | A localização do usuário no site está disponível |
| **2.4.9** Finalidade do link (somente link) | A finalidade do link fica clara apenas no texto do link |
| **2.4.10** Títulos de seção | As seções têm títulos |
| **2.4.12** Foco não obscurecido (aprimorado) | Nenhuma parte do elemento em foco fica oculta pelo conteúdo criado pelo autor |
| **2.4.13** Aparência do foco | O indicador de foco tem área e contraste suficientes e não está obscurecido |
| **3.1.3** Palavras incomuns | Definições disponíveis para palavras incomuns |
| **3.1.4** Abreviações | Abreviaturas expandidas |
| **3.1.5** Nível de leitura | Conteúdo alternativo para textos complexos |
| **3.1.6** Pronúncia | Pronúncia disponível quando necessário |
| **3.2.5** Alteração mediante solicitação | Mudanças iniciadas apenas pelo usuário |
| **3.3.5** Ajuda | Ajuda contextual disponível |
| **3.3.6** Prevenção de erros (todas) | Todos os envios de formulários podem ser revisados ​​|
| **3.3.9** Autenticação acessível (aprimorada) | Nenhum teste de função cognitiva para login (sem exceções de reconhecimento de objeto ou conteúdo pessoal) |

## Padrões ARIA comuns

### Botões
```html
<button>Rótulo</button>
<!-- ou -->
<button aria-label="Fechar diálogo">×</button>
```

###Links
```html
<a href="/page">Texto descritivo do link</a>
<!-- Links externos -->
<a href="https://external.com" target="_blank" rel="noopener">
  Site externo
  <span class="visually-hidden">(abre em uma nova aba)</span>
</a>
```

### Campos do formulário
```html
<label for="email">Endereço de e-mail</label>
<input type="email" id="email" aria-describedby="email-hint">
<p id="email-hint">Nunca compartilharemos seu e-mail.</p>
```

### Estados de erro
```html
<label for="email">E-mail</label>
<input type="email" id="email" aria-invalid="true" aria-describedby="email-error">
<p id="email-error" role="alert">Insira um endereço de e-mail válido.</p>
```

### Navegação
```html
<nav aria-label="Principal">
  <ul>
    <li><a href="/" aria-current="page">Página inicial</a></li>
    <li><a href="/about">Sobre</a></li>
  </ul>
</nav>
```

### Modais
```html
<div role="dialog" aria-modal="true" aria-labelledby="dialog-title">
  <h2 id="dialog-title">Confirmar ação</h2>
  <!-- conteúdo -->
</div>
```

### Regiões ativas
```html
<!-- Educado (aguarda pausa na fala) -->
<div aria-live="polite">Atualização de status aqui</div>

<!-- Assertivo (interrompe imediatamente) -->
<div aria-live="assertive" role="alert">Mensagem de erro aqui</div>

<!-- Status (educado, implícito) -->
<div role="status">Carregamento concluído</div>
```

## O que mudou de 2.1 para 2.2

| Alterar | Critério | Nível |
|--------|-----------|-------|
| **Removido** | 4.1.1 Análise | Um |
| **Adicionado** | 2.4.11 Foco não obscurecido (mínimo) | AA |
| **Adicionado** | 2.4.12 Foco não obscurecido (aprimorado) | AAA |
| **Adicionado** | 2.4.13 Aparência do foco | AAA |
| **Adicionado** | 2.5.7 Movimentos de Arrasto | AA |
| **Adicionado** | 2.5.8 Tamanho alvo (mínimo) | AA |
| **Adicionado** | 3.2.6 Ajuda consistente | Um |
| **Adicionado** | 3.3.7 Entrada Redundante | Um |
| **Adicionado** | 3.3.8 Autenticação Acessível (Mínima) | AA |
| **Adicionado** | 3.3.9 Autenticação Acessível (Aprimorada) | AAA |

## Ferramentas de teste

| Ferramenta | Tipo | URL |
|------|------|-----|
| machado DevTools | Extensão do navegador | [deque.com/axe](https://www.deque.com/axe/) |
| ONDA | Extensão do navegador | [wave.webaim.org](https://wave.webaim.org/) |
| Farol | Integrado ao Chrome | DevTools → Farol |
| NVDA | Leitor de tela (Windows) | [nvaccess.org](https://www.nvaccess.org/) |
| VozOver | Leitor de tela (Mac) | Integrado ao macOS |
| Analisador de contraste de cores | Aplicativo de desktop | [tpgi.com](https://www.tpgi.com/color-contrast-checker/) |

## Fontes

- [Recomendação WCAG 2.2 W3C](https://www.w3.org/TR/WCAG22/)
- [Referência rápida do WCAG 2.2](https://www.w3.org/WAI/WCAG22/quickref/)
- [O que há de novo nas WCAG 2.2](https://www.w3.org/WAI/standards-guidelines/wcag/new-in-22/)