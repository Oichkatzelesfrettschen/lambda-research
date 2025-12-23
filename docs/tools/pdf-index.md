# PDF Index and Health Check

**Complete index of all accessible PDFs in this repository**

---

## Essential Papers Collection

### [PDF] Church (1936) - An Unsolvable Problem
**Path**: `/lambda-research/papers/essential/1936_church_unsolvable_problem_oa.pdf`
**Status**: Should be accessible
**Size**: ~500KB
[Direct Link](../papers/essential/1936_church_unsolvable_problem_oa.pdf)

### [PDF] Girard (1989) - Proofs and Types
**Path**: `/lambda-research/papers/essential/1989_girard_proofs_types_oa.pdf`
**Status**: Should be accessible
**Size**: ~950KB
[Direct Link](../papers/essential/1989_girard_proofs_types_oa.pdf)

---

## Historical Collection

### [PDF] Church (1941) - Calculi of Lambda-Conversion
**Path**: `/lambda-research/papers/historical/1941_church_calculi_lambda_conversion_pd.pdf`
**Status**: Should be accessible
**Size**: ~2MB
[Direct Link](../historical/church-lambda-calculus/1941_church_calculi_lambda_conversion_pd.pdf)

---

## Health Check Instructions

If you're experiencing PDF access issues:

### Step 1: Check Direct Links
Try clicking the direct links above. They should open the PDFs directly in your browser.

### Step 2: Verify PDF.js Viewer
Our embedded viewers use Mozilla PDF.js. If embeds aren't working, try:
- Desktop browser (Chrome, Firefox, Safari)
- Disable ad blockers temporarily
- Check browser console for JavaScript errors

### Step 3: Alternative Access
If GitHub Pages links fail:
- Check the [GitHub repository directly](https://github.com/Oichkatzelesfrettschen/lambda-research/tree/main/papers)
- Use the raw GitHub URLs for direct download

### Step 4: Report Issues
If PDFs are consistently inaccessible, please:
- [Open an issue](#) with details
- Include your browser and operating system
- Specify which PDFs are affected

---

## Technical Details

### Build Process
1. MkDocs processes `docs/` directory -> `site/`
2. GitHub Actions copies `papers/` -> `site/papers/`
3. GitHub Pages serves from `site/`
4. PDFs accessible at `/lambda-research/papers/...`

### Path Mapping
```
Repository:   /papers/essential/file.pdf
GitHub Pages: /lambda-research/papers/essential/file.pdf
Direct URL:   https://oichkatzelesfrettschen.github.io/lambda-research/papers/essential/1936_church_unsolvable_problem_oa.pdf
```

---

*This index is automatically updated during site builds to ensure accuracy.*
