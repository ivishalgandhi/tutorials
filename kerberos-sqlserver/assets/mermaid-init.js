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
    primaryColor:       '#e8f0fe',
    primaryTextColor:   '#1a1a1a',
    primaryBorderColor: '#0056b3',
    lineColor:          '#555',
    secondaryColor:     '#f3f2ee',
    tertiaryColor:      '#faf9f7',
    noteBkgColor:       '#fff8e1',
    noteTextColor:      '#856404',
    fontFamily:         '-apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif',
    fontSize:           '14px',
    actorBkg:           '#1e3a5f',
    actorTextColor:     '#ffffff',
    actorBorderColor:   '#0056b3',
    activationBkgColor: '#e8f0fe',
    activationBorderColor: '#0056b3',
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
