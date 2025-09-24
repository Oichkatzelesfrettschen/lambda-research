# Bibliography Standardization Guide for Lambda Calculus Research Repository

## Standard Citation Format

**Target Format for ALL bibliography entries:**

```
**Author, A.B.** (Year). *Title of Paper*. Venue Name, Volume(Issue), Pages.
- **Key Contribution**: Brief description of the paper's main contribution
- **DOI**: Include when available
- **URL**: For papers accessible online (when DOI not available)
```

## Formatting Rules

### Author Names
- Use initials for first/middle names: **Smith, J.A.** not **Smith, John Andrew**
- Multiple authors: **Smith, J.A. & Jones, B.C.**
- Three or more authors: **Smith, J.A., Jones, B.C., & Brown, D.E.**

### Years
- Always in parentheses: **(1984)**
- For multi-year works: **(1932-1933)**

### Titles
- Always in italics: ***Title of Paper***
- Preserve original capitalization and special characters (λ, etc.)
- No quotes around titles

### Venues
- Journal format: *Journal Name, Volume(Issue), Pages*
- Conference format: *Conference Proceedings, Pages*
- Book format: *Publisher Name* or *Book Title, Pages. Publisher*

### DOIs and URLs
- **DOI**: 10.xxxx/xxxxx (when available)
- **URL**: provide an accessible link (when DOI is unavailable)

## Section Organization

### Required Sections (maintain existing structure)
1. **Foundational Works** - Historical papers (pre-1970)
2. **Core Theory** - Main theoretical developments
3. **Modern Developments** - Recent advances (1990+)
4. **Implementation/Practice** - Practical applications

### Chronological Ordering
- Within each section, order by publication year (earliest first)
- For same year, order alphabetically by first author surname

## Key Contributions Format

Each entry must have a **Key Contribution** line explaining:
- The paper's main theoretical advance
- Its significance to the field
- How it relates to other work (if foundational)

## Examples of Standardized Entries

### Journal Paper
```
**Church, A.** (1936). *An Unsolvable Problem of Elementary Number Theory*. American Journal of Mathematics, 58(2), 345-363.
- **Key Contribution**: First introduction of lambda calculus concepts and establishes undecidability results
- **DOI**: 10.2307/2371045
```

### Conference Paper
```
**Damas, L. & Milner, R.** (1982). *Principal Type-Schemes for Functional Programs*. Proceedings of the 9th ACM SIGPLAN-SIGACT Symposium on Principles of Programming Languages.
- **Key Contribution**: Definitive paper on principal types in functional programming
- **DOI**: 10.1145/582153.582176
```

### Book/Monograph
```
**Barendregt, H.P.** (1984). *The Lambda Calculus: Its Syntax and Semantics*. Studies in Logic and Foundations of Mathematics, vol. 103. North-Holland.
- **Key Contribution**: The definitive modern reference on lambda calculus (615 pp., revised edition)
```

### PhD Thesis
```
**Damas, L.** (1985). *Type Assignment in Programming Languages*. PhD Thesis, University of Edinburgh.
- **Key Contribution**: Formal analysis and proof of Hindley-Milner algorithm
```

## Files Completed
- ✅ `/01-untyped-lambda-calculus/papers/bibliography.md` - STANDARDIZED
- 🔄 `/02-simply-typed-lambda-calculus/papers/bibliography.md` - PARTIALLY STANDARDIZED
- ✅ `/05-martin-lof-type-theory/papers/bibliography.md` - ALREADY IN STANDARD FORMAT

## Files Requiring Standardization

### Priority Order (01-05 first, then 06-31)
1. `/02-simply-typed-lambda-calculus/papers/bibliography.md` - CONTINUE FROM LINE 60
2. `/03-system-f-polymorphic/papers/bibliography.md`
3. `/04-calculus-of-constructions/papers/bibliography.md`
4. `/06-linear-lambda-calculus/papers/bibliography.md`
5. `/07-session-types/papers/bibliography.md`
6. ... (continue through 31)

### Root-level Files
- `comprehensive_type_theory_bibliography.md`
- `linear_lambda_calculus_bibliography.md`
- `session_types_bibliography.md`
- `dependent_types_bibliography.md`
- `combinatory_logic_bibliography.md`
- `gradual_typing_bibliography.md`
- `effect_systems_bibliography.md`
- `martin-lof-type-theory-bibliography.md`

## DOI Research Resources

### Academic Databases for DOI Lookup
1. **Semantic Scholar**: https://www.semanticscholar.org/
2. **DBLP**: https://dblp.org/
3. **ACM Digital Library**: https://dl.acm.org/
4. **IEEE Xplore**: https://ieeexplore.ieee.org/
5. **Springer Link**: https://link.springer.com/
6. **ScienceDirect**: https://www.sciencedirect.com/
7. **JSTOR**: https://www.jstor.org/

### Search Strategy
1. Search by title + author + year
2. Look for official publisher pages
3. Cross-reference multiple sources
4. Verify DOI format: 10.xxxx/xxxxx

## Quality Assurance Checklist

For each file:
- [ ] All entries follow standard format
- [ ] Chronological ordering within sections
- [ ] Key contributions described
- [ ] DOIs added where available
- [ ] No numbered entries (### 1., ### 2., etc.)
- [ ] Consistent author name formatting
- [ ] Italicized titles, no quotes
- [ ] Proper venue formatting

## Next Steps

1. Complete `/02-simply-typed-lambda-calculus/papers/bibliography.md`
2. Standardize `/03-system-f-polymorphic/papers/bibliography.md`
3. Standardize `/04-calculus-of-constructions/papers/bibliography.md`
4. Move to numbered directories 06-31
5. Address root-level bibliography files
6. Final consistency check across all files

This standardization improves academic quality and citation consistency across the entire lambda calculus research repository.
