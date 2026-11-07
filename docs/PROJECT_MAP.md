# Project map

Inspection date: 2026-11-07 (Europe/Vienna). Paths below are relative to this workspace unless stated otherwise. Inventory describes files on disk, not tested browser behavior or a deployed PMS installation.

## Workspace and source boundary

- `root_manual` is a Windows junction whose target is `C:\Users\Fred_U\Documents\COPS\PMS`. All inspected manual files lie under `root_manual/Handbuch/de/` (abbreviated `H/` below).
- `.git/` is local repository metadata. At inspection the repository had no commits; `.git/info/exclude` contains `/root_manual/`. That exclusion is local Git configuration, not a portable tracked ignore rule.
- `AGENTS.md`, `docs/` and `.project-memory/` are project-owned guidance, analysis and compact durable memory created for this task. No source files were edited. No pre-existing applicable AGENTS.md was found in the workspace/source or inspected ancestors.

## What this collection is

The corpus is a German PMS help export associated with COPS Software GmbH (copyright text in `H/01-pms_online_handbuch/01-erste_schritte_in_pms_de/01-erste_schritte_in_pms_de.htm`). `H/index.htm` identifies Adobe RoboHelp 11 and WebHelp 5.50. It is generated HTML, scripts, styles, navigation data and images. The JavaScript principally implements the help viewer/index, rather than evidence of the PMS application's implementation. No package manifest, application source project, database instance or build toolchain was found in the inventory.

## Structure and object locations

The foreword defines PMS as “Portfolio- und Risiko-Management-System” (`H/01-pms_online_handbuch/_handbuch_vorwort_de/_handbuch_vorwort_de.htm`, line 108).

Inventory: 24,500 files totaling 741,945,184 bytes: 9,183 JPG, 7,670 PNG, 3,201 HTM, 2,292 GIF, 1,793 JS, 351 CSS, 5 ICO, 4 XML and 1 LNG. Counts include generated navigation/search pages: 3,201 HTM does not mean 3,201 substantive manual chapters.

| Path below H/ | Files / HTM | Role and objects |
| --- | ---: | --- |
| `01-pms_online_handbuch/` | 17,653 / 223 | Main manual; 222 topic directories, plus root-level material. Covers instruments, portfolios/depots, transactions/position keeping, analyses, risk, reporting and administration. |
| `02-pms_online_standardschnittstelle/` | 216 / 93 | 93 topic directories for the ITF standard interface: record formats, instrument/master data, positions, transactions, configuration and imports. |
| `03-pms_aenderungsprotokolle/` | 736 / 17 | ASCII-spelled change-log tree: PMS 7.x through 11 topic families. |
| `03-pms_änderungsprotokolle/` | 1,180 / 18 | Separate Unicode-spelled tree with overlapping version families and a PMS 12 directory. Do not collapse it into the ASCII tree or assume either is wholly current. |
| `whdata/` | 608 / 602 | Generated HTML navigation/index/glossary data (`whtoc.htm`, `whidx.htm`, `whglo.htm` and chunks). |
| `whgdata/` | 2,217 / 2,216 | Generated list/search support pages, e.g. `whlstf*.htm`. |
| `whxdata/` | 1,762 / 0 | XML-like navigation, index and full-text data wrapped in JavaScript (`*_xml.js`, `package_*_xml.js`). |
| `resource/` | 1 / 0 | Localized help-viewer strings in `resource_xml.js`. |
| Files directly in H/ | 127 / included above | Viewer entry points, scripts, skins, icons, XML and language resources. |

Independent SHA-256 comparison by relative path found 736 paths shared by both change-log trees: 463 byte-identical and 273 different. The Unicode tree has 444 additional files; the ASCII tree has no unique relative paths. Shared names therefore do not prove equivalent contents, and this comparison does not establish which version is authoritative.

A topic usually has a descriptive `.htm`, a matching `.css`, and local `imageNNN` files. Image names repeat across topic folders and are meaningful only with their containing path. OriginalFile metadata in the foreword refers to a Word `.docx`; that authoring document is not present in this inventory.

| Need | Start below `H/01-pms_online_handbuch/` |
| --- | --- |
| Startup and UI | `01-erste_schritte_in_pms_de/` |
| Portfolios and depots | `03-depots_und_portfolios_de/` |
| Financial instruments | `04-instrumente_allgemein_de/`, `05-00-pms_instrumente_de/`, `05-01-...` through `05-37-...` families |
| Transactions/position keeping | `19-00-positionkeeping_de/` and `19-01-...` through `19-21-...` families |
| Data model tables | `appx_g-datenbanktabellen_de/appx_g-datenbanktabellen_de.htm` |
| Entity relationships (images) | `appx_k-er-diagramme_de/appx_k-er-diagramme_de.htm` and neighboring images |
| Configuration/installation | `appx_b-konfigurationseinstellungen_de/`, `appx_j-installationshandbuch_de/` |
| Field/metric definitions | `appx_h-kennzahlen_de/`, `appx_i_instrumente_de/` |
| Modules/reports/integration | `appx_m_modulbeschreibung_de/`, `appx_s-standardreports_de/`, `75-...` families, `98-webservices_de/` |

The table locates documentation for business objects; it does not establish classes, executable modules or live database schemas in this workspace. Exact semantics, keys and dependencies must be read from the relevant topic and version before answering detailed questions.

## Dependencies and navigation

1. `H/index.htm` loads `whver.js`, `whutils.js`, `whmsg.js`, `whstub.js` and selects viewer skins/fallback pages. `PMS_HANDBUCH.htm`, `index_csh.htm` and `index_rhc.htm` are additional help entry points.
2. `H/whproj.htm` sets language ID 1031, `whdata` and TOC/index/glossary files. `H/whproj_xml.js` sets the foreword homepage, `whxdata` and TOC/index/full-text/glossary/browse data. The `*_xml.js` files store XML text in `gXMLBuffer`; references such as `whtoc.xml` may be logical runtime resource names rather than literal files. `H/whxdata/whtdata0_xml.js` names the three main books.
3. Sample topic `H/01-pms_online_handbuch/_handbuch_vorwort_de/_handbuch_vorwort_de.htm` loads its local CSS and shared `../../whmsg.js`, `whver.js`, `whutils.js`, `whproxy.js`, `whlang.js`, `whtopic.js`; linked images resolve relative to the topic directory.
4. That sample topic also references `../../RHStyleMapping.css`, but `H/RHStyleMapping.css` is absent. This is a verified missing dependency in the sample; no exhaustive link audit was performed and no rendering consequence is claimed.
5. Browser DOM/JavaScript and local relative assets support the exported viewer. `whver.js` contains legacy browser detection. Modern browser behavior, local-file restrictions, serving configuration and complete navigation/search operation were not tested.

PMS integrations discussed by the manual (for example Refinitiv/Reuters, Bloomberg, SAP, webservices and ITF import) are business-system documentation, not installed dependencies of this analysis workspace. `H/01-pms_online_handbuch/appx_j-installationshandbuch_de/appx_j-installationshandbuch_de.htm` documents client/server installation scenarios, database server installation and ODBC driver setup (sections J.1–J.3). `H/01-pms_online_handbuch/98-webservices_de/98-webservices_de.htm`, line 193, describes a proposed dispatcher translating SOAP messages to internal socket messages and managing PMS instances. These are documented system relationships; they do not prove this architecture is deployed locally. Required current PMS server/database versions, licensed modules, external services and deployment settings are not established here. No network access or external application execution was used for this analysis.

A concrete documented interface dependency is database state: `H/02-pms_online_standardschnittstelle/01-03-itf_technische_erlaeuterungen_de/01-03-itf_technische_erlaeuterungen_de.htm`, section 1.3.5 “Ebenen der Konsistenzprüfung und Reaktionen bei Fehlern”, lists insertion as requiring an absent record and update/deletion as requiring an existing record (lines 1253–1285), followed by database list and dependency checks. Section 1.2 of `01-02-itf_formale_erlaeuterungen_de/01-02-itf_formale_erlaeuterungen_de.htm` defines field code `S` as requiring a value from the key directory (line 147). These are manual rules, not tested import behavior; consult the specific record topic and configuration before applying them.

## Retrieval and limits

Search substantive topic trees first; use TOC metadata to confirm titles and links, then inspect exact topic headings/anchors and any relevant images. Prefer targeted UTF-8 searches over dumping huge generated HTML or loading every search chunk into context. Keep both change-log trees and version-specific content distinct until comparison proves equivalence. Inventory and selected source reads do not prove all links valid, the export complete, documentation current, or any legal/financial/business statement correct for a current installation. Review details: `docs/REVIEW.md`.
