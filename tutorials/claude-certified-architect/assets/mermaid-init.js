/**
 * mermaid-init.js — Shared Mermaid initialiser for CCA lessons.
 *
 * Include AFTER the Mermaid CDN script:
 *   <script src="https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.min.js"></script>
 *   <script src="../assets/mermaid-init.js"></script>
 */
mermaid.initialize({
  startOnLoad: true,
  theme: 'base',
  themeVariables: {
    /* Amber / Anthropic palette */
    primaryColor:       '#fff7ed',   /* info-bg amber */
    primaryTextColor:   '#1a1a1a',
    primaryBorderColor: '#d97706',
    lineColor:          '#555',
    secondaryColor:     '#f3f2ee',   /* code-bg */
    tertiaryColor:      '#faf9f7',   /* page bg */
    noteBkgColor:       '#fff8e1',
    noteTextColor:      '#856404',
    fontFamily:         '-apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif',
    fontSize:           '14px',
    /* Sequence diagram specifics */
    actorBkg:           '#d97706',
    actorTextColor:     '#ffffff',
    actorBorderColor:   '#b45309',
    activationBkgColor: '#fff7ed',
    activationBorderColor: '#d97706',
    sequenceNumberColor:'#ffffff',
  },
  sequence: {
    diagramMarginX:  20,
    diagramMarginY:  10,
    actorMargin:     60,
    width:           160,
    height:          40,
    boxMargin:       10,
    boxTextMargin:   5,
    noteMargin:      10,
    messageMargin:   40,
    useMaxWidth:     true,
  },
  flowchart: {
    useMaxWidth: true,
    htmlLabels: true,
    curve: 'basis',
  },
});
