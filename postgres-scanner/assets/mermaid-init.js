/**
 * mermaid-init.js — Shared Mermaid initialiser for all lessons.
 *
 * Include AFTER the Mermaid CDN script:
 *   <script src="https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.min.js"></script>
 *   <script src="../assets/mermaid-init.js"></script>
 */
mermaid.initialize({
  startOnLoad: true,
  theme: 'base',
  themeVariables: {
    /* Match lesson palette */
    primaryColor:       '#e8f0fe',   /* info-bg blue */
    primaryTextColor:   '#1a1a1a',
    primaryBorderColor: '#1a56db',
    lineColor:          '#555',
    secondaryColor:     '#f3f2ee',   /* code-bg */
    tertiaryColor:      '#faf9f7',   /* page bg */
    noteBkgColor:       '#fff8e1',
    noteTextColor:      '#856404',
    fontFamily:         '-apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif',
    fontSize:           '14px',
    /* Sequence diagram specifics */
    actorBkg:           '#336791',   /* elephant blue */
    actorTextColor:     '#ffffff',
    actorBorderColor:   '#1a56db',
    activationBkgColor: '#e8f0fe',
    activationBorderColor: '#1a56db',
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
});
