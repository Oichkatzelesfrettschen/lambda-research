// MathJax configuration for Lambda Calculus Research Repository
// Optimized for lambda calculus notation and academic mathematical content

window.MathJax = {
  // Input processors
  tex: {
    // Inline math delimiters
    inlineMath: [["\\(", "\\)"]],
    // Display math delimiters
    displayMath: [["\\[", "\\]"]],
    // Process escaped characters
    processEscapes: true,
    // Process environments
    processEnvironments: true,

    // Custom macros for lambda calculus notation
    macros: {
      // Lambda calculus fundamentals
      "lam": "\\lambda",
      "Lam": "\\Lambda",
      "app": "\\,",
      "abs": ["\\lambda #1.\\, #2", 2],

      // Type theory notation
      "ty": "\\tau",
      "Ty": "\\mathcal{T}",
      "ctx": "\\Gamma",
      "Ctx": "\\mathcal{G}",
      "vdash": "\\vdash",
      "proves": "\\vdash",

      // Lambda cube notation
      "stlc": "\\lambda^{\\to}",
      "systemf": "\\lambda^{2}",
      "lf": "\\lambda^{P}",
      "coc": "\\lambda^{P2}",

      // Type constructors
      "tarr": ["#1 \\to #2", 2],
      "tprod": ["#1 \\times #2", 2],
      "tsum": ["#1 + #2", 2],
      "tall": ["\\forall #1.\\, #2", 2],
      "texists": ["\\exists #1.\\, #2", 2],

      // Reduction relations
      "bred": "\\to_{\\beta}",
      "ered": "\\to_{\\eta}",
      "red": "\\to",
      "redstar": "\\to^*",
      "equiv": "\\equiv",
      "defeq": "\\equiv",

      // Linear logic
      "lollipop": "\\multimap",
      "tensor": "\\otimes",
      "par": "\\bindnasrepma",
      "with": "\\&",
      "plus": "\\oplus",
      "bang": "!",
      "why": "?",

      // Session types
      "send": ["!#1", 1],
      "recv": ["?#1", 1],
      "end": "\\mathsf{end}",
      "branch": ["\\&\\{#1\\}", 1],
      "choice": ["\\oplus\\{#1\\}", 1],

      // Dependent types
      "pi": ["\\Pi #1: #2.\\, #3", 3],
      "sigma": ["\\Sigma #1: #2.\\, #3", 3],
      "dep": ["#1[#2]", 2],

      // Modal logic
      "box": ["\\Box #1", 1],
      "diamond": ["\\Diamond #1", 1],
      "next": ["\\circ #1", 1],
      "prev": ["\\bullet #1", 1],

      // Effect systems
      "eff": ["\\langle #1 \\rangle", 1],
      "pure": "\\mathsf{Pure}",
      "comp": ["\\mathsf{Comp}[#1]", 1],

      // Categorical notation
      "cat": ["\\mathcal{#1}", 1],
      "func": ["\\mathsf{#1}", 1],
      "obj": ["\\mathrm{Obj}(#1)", 1],
      "hom": ["\\mathrm{Hom}(#1, #2)", 2],
      "comp": "\\circ",
      "id": ["\\mathrm{id}_{#1}", 1],

      // Homotopy type theory
      "idtype": ["\\mathrm{Id}_{#1}(#2, #3)", 3],
      "path": ["#1 =_{#2} #3", 3],
      "refl": ["\\mathrm{refl}_{#1}", 1],
      "transport": ["\\mathrm{transport}", 0],
      "univ": ["\\mathcal{U}", 0],

      // Quantum lambda calculus
      "ket": ["|#1\\rangle", 1],
      "bra": ["\\langle #1|", 1],
      "braket": ["\\langle #1 | #2 \\rangle", 2],
      "qbit": "\\mathsf{Qbit}",
      "meas": "\\mathsf{meas}",

      // Common abbreviations
      "iff": "\\Leftrightarrow",
      "implies": "\\Rightarrow",
      "fun": "\\mathsf{fun}",
      "let": "\\mathsf{let}",
      "in": "\\mathsf{in}",
      "fix": "\\mathsf{fix}",
      "rec": "\\mathsf{rec}",
      "case": "\\mathsf{case}",
      "of": "\\mathsf{of}",

      // Set theory
      "emptyset": "\\varnothing",
      "powerset": ["\\mathcal{P}(#1)", 1],
      "union": "\\cup",
      "intersect": "\\cap",
      "subset": "\\subseteq",
      "superset": "\\supseteq",

      // Logic
      "true": "\\mathsf{true}",
      "false": "\\mathsf{false}",
      "and": "\\land",
      "or": "\\lor",
      "not": "\\lnot",
      "forall": "\\forall",
      "exists": "\\exists"
    },

    // Additional packages
    packages: {
      '[+]': ['base', 'ams', 'newcommand', 'configMacros', 'action', 'html']
    },

    // Tags configuration
    tags: 'ams'
  },

  // Output configuration
  chtml: {
    // Font scaling
    scale: 1.0,
    // Minimum scale
    minScale: 0.5,
    // Match font scaling
    matchFontHeight: true,
    // Font URL
    fontURL: 'https://cdn.jsdelivr.net/npm/mathjax@3/es5/output/chtml/fonts/woff-v2'
  },

  // SVG output (alternative)
  svg: {
    // Font cache
    fontCache: 'global',
    // Scale factor
    scale: 1.0,
    // Minimum scale
    minScale: 0.5
  },

  // Loader configuration
  loader: {
    // Load components on demand
    load: ['[tex]/ams', '[tex]/newcommand', '[tex]/configMacros', '[tex]/action', '[tex]/html']
  },

  // Options
  options: {
    // Skip HTML tags
    skipHtmlTags: ['script', 'noscript', 'style', 'textarea', 'pre', 'code'],
    // Include HTML tags
    includeHtmlTags: {
      br: '\n',
      wbr: '',
      '#comment': ''
    },
    // Render actions
    renderActions: {
      addMenu: [150, '', '']
    }
  },

  // Startup configuration
  startup: {
    // Ready function
    ready: function() {
      console.log('MathJax loaded for Lambda Calculus Research Repository');
      MathJax.startup.defaultReady();
    },

    // Page ready function
    pageReady: function() {
      console.log('MathJax page processing complete');
      return MathJax.startup.defaultPageReady().then(function() {
        // Custom post-processing if needed
      });
    }
  }
};

// Document ready handler for Material for MkDocs compatibility
document.addEventListener("DOMContentLoaded", function() {
  // Ensure MathJax processes content after Material's dynamic loading
  if (typeof MathJax !== 'undefined') {
    MathJax.typesetPromise = MathJax.typesetPromise || Promise.resolve();

    // Reprocess math on navigation for instant loading
    document.addEventListener("DOMContentSwitch", function() {
      MathJax.typesetPromise = MathJax.typesetPromise.then(function() {
        return MathJax.typesetPromise();
      });
    });
  }
});

// Compatibility with Material for MkDocs instant loading
window.addEventListener("load", function() {
  if (typeof MathJax !== 'undefined' && MathJax.startup) {
    // Handle instant navigation
    document.body.addEventListener("DOMSubtreeModified", function() {
      if (MathJax.typesetPromise) {
        MathJax.typesetPromise = MathJax.typesetPromise.then(function() {
          return MathJax.typesetPromise([document.body]);
        });
      }
    });
  }
});