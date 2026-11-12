(function () {
    'use strict';

    const root = document.documentElement;
    const reducedMotion = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;

    // -------------------------------------------------------------------------
    // 1. Theme Persistence (Compatible with doc pages using js/main.js)
    // -------------------------------------------------------------------------
    const getInitialTheme = () => {
        const saved = localStorage.getItem('theme');
        if (saved === 'dark' || saved === 'light') return saved;
        const attr = root.getAttribute('data-theme');
        return (attr === 'light' || attr === 'dark') ? attr : 'dark';
    };

    const applyTheme = (theme) => {
        root.setAttribute('data-theme', theme);
        root.setAttribute('data-bs-theme', theme);
        document.querySelectorAll('[data-theme-toggle]').forEach((btn) => {
            btn.setAttribute('aria-label', theme === 'dark' ? 'Switch to light theme' : 'Switch to dark theme');
            btn.setAttribute('aria-pressed', theme === 'light' ? 'true' : 'false');
        });
    };

    applyTheme(getInitialTheme());

    document.addEventListener('DOMContentLoaded', () => {
        document.querySelectorAll('[data-theme-toggle]').forEach((btn) => {
            btn.addEventListener('click', () => {
                const next = root.getAttribute('data-theme') === 'dark' ? 'light' : 'dark';
                applyTheme(next);
                localStorage.setItem('theme', next);
            });
        });

        if (window.matchMedia) {
            window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', (e) => {
                if (!localStorage.getItem('theme')) {
                    applyTheme(e.matches ? 'dark' : 'light');
                }
            });
        }

        // ---------------------------------------------------------------------
        // 2. Navigation Scroll, Dropdown & Mobile Drawer
        // ---------------------------------------------------------------------
        const nav = document.querySelector('.site-nav');
        if (nav) {
            const onScroll = () => nav.classList.toggle('is-scrolled', window.scrollY > 12);
            window.addEventListener('scroll', onScroll, { passive: true });
            onScroll();
        }

        const dropdowns = document.querySelectorAll('.nav-dropdown');
        dropdowns.forEach((dd) => {
            const trigger = dd.querySelector('[data-dropdown-trigger]');
            if (!trigger) return;
            trigger.addEventListener('click', (e) => {
                e.stopPropagation();
                const open = dd.classList.toggle('is-open');
                trigger.setAttribute('aria-expanded', open ? 'true' : 'false');
            });
        });

        document.addEventListener('click', (e) => {
            dropdowns.forEach((dd) => {
                if (!dd.contains(e.target)) {
                    dd.classList.remove('is-open');
                    const tr = dd.querySelector('[data-dropdown-trigger]');
                    if (tr) tr.setAttribute('aria-expanded', 'false');
                }
            });
        });

        document.addEventListener('keydown', (e) => {
            if (e.key === 'Escape') {
                dropdowns.forEach((dd) => {
                    dd.classList.remove('is-open');
                    const tr = dd.querySelector('[data-dropdown-trigger]');
                    if (tr) tr.setAttribute('aria-expanded', 'false');
                });
                closeMobileDrawer();
            }
        });

        const menuBtn = document.querySelector('[data-mobile-menu-toggle]');
        const drawer = document.querySelector('.mobile-drawer');
        const HAMBURGER_SVG = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><line x1="4" x2="20" y1="7" y2="7"/><line x1="4" x2="20" y1="12" y2="12"/><line x1="4" x2="20" y1="17" y2="17"/></svg>';
        const CLOSE_SVG = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>';

        function closeMobileDrawer() {
            if (!drawer || !menuBtn) return;
            drawer.classList.remove('is-open');
            menuBtn.setAttribute('aria-expanded', 'false');
            menuBtn.setAttribute('aria-label', 'Open navigation menu');
            menuBtn.innerHTML = HAMBURGER_SVG;
            document.body.classList.remove('nav-open');
        }

        if (menuBtn && drawer) {
            menuBtn.addEventListener('click', (e) => {
                e.stopPropagation();
                const open = drawer.classList.toggle('is-open');
                menuBtn.setAttribute('aria-expanded', open ? 'true' : 'false');
                menuBtn.setAttribute('aria-label', open ? 'Close navigation menu' : 'Open navigation menu');
                menuBtn.innerHTML = open ? CLOSE_SVG : HAMBURGER_SVG;
                document.body.classList.toggle('nav-open', open);
            });

            drawer.querySelectorAll('a').forEach((link) => {
                link.addEventListener('click', closeMobileDrawer);
            });

            document.addEventListener('click', (e) => {
                if (drawer.classList.contains('is-open') && !drawer.contains(e.target) && !menuBtn.contains(e.target)) {
                    closeMobileDrawer();
                }
            });
        }

        // ---------------------------------------------------------------------
        // 3. Pointer Hairline Border Spotlight
        // ---------------------------------------------------------------------
        document.querySelectorAll('.spotlight-card').forEach((card) => {
            card.addEventListener('pointermove', (e) => {
                const rect = card.getBoundingClientRect();
                card.style.setProperty('--mx', `${e.clientX - rect.left}px`);
                card.style.setProperty('--my', `${e.clientY - rect.top}px`);
            });
        });

        // ---------------------------------------------------------------------
        // 4. Tabular Stat Count-Up
        // ---------------------------------------------------------------------
        const counters = document.querySelectorAll('[data-count-to]');
        if (counters.length) {
            const runCount = (el) => {
                const target = Number(el.dataset.countTo || 0);
                const suffix = el.dataset.countSuffix || '';
                const prefix = el.dataset.countPrefix || '';
                if (reducedMotion || !Number.isFinite(target)) {
                    el.textContent = `${prefix}${target.toLocaleString()}${suffix}`;
                    return;
                }
                const duration = 560;
                const start = performance.now();
                const tick = (now) => {
                    const t = Math.min(1, (now - start) / duration);
                    const eased = 1 - Math.pow(1 - t, 3);
                    const val = Math.round(target * eased);
                    el.textContent = `${prefix}${val.toLocaleString()}${suffix}`;
                    if (t < 1) requestAnimationFrame(tick);
                };
                requestAnimationFrame(tick);
            };

            const countObs = new IntersectionObserver((entries) => {
                entries.forEach((entry) => {
                    if (entry.isIntersecting) {
                        runCount(entry.target);
                        countObs.unobserve(entry.target);
                    }
                });
            }, { threshold: 0.3 });

            counters.forEach((el) => countObs.observe(el));
        }

        // ---------------------------------------------------------------------
        // 5. Tab Groups (Interactive Preview Switchers & Reactive Hero Copy)
        // ---------------------------------------------------------------------
        const HERO_ASSET_DATA = {
            msultimate: {
                eyebrow: 'MSUltimate Ecosystem · UI Toolkit & IMGUI Suite',
                title: 'Next-generation inspector styling & editor architecture',
                desc: 'Comprehensive UI Toolkit & IMGUI editor suite featuring 454+ concrete attributes across 6 decoupled addons, visual Makeover node graphs, custom collection serializers, and an automated 1-click validation test suite.',
                primaryText: 'Explore MSUltimate',
                primaryHref: 'msultimate.html',
                secondaryText: 'Read documentation',
                secondaryHref: 'msultimate-docs.html',
                meta: [
                    '454+ Documented Attributes',
                    '156+ Free in Community Core',
                    '6,115 Automated Tests'
                ],
                stats: [
                    { label: 'Attributes total', value: '454+', countTo: 454, countSuffix: '+', note: '463 attribute classes total', noteClass: 'accent' },
                    { label: 'Community tier', value: 'Free', note: '156+ attributes in Community Core', noteClass: 'positive' },
                    { label: 'Standalone addons', value: '6 Addons', countTo: 6, countSuffix: ' Addons', note: '100% decoupled modular architecture', noteClass: '' },
                    { label: 'Automated tests', value: '6,115', countTo: 6115, note: '573 test files · 39 CLI rules', noteClass: '' }
                ]
            },
            msmotion: {
                eyebrow: 'MSMotion v2.0 · PlayableGraph Animation Engine',
                title: 'Multi-actor choreography & dynamic timeline framework',
                desc: 'Author synchronized combat duets, partner grapples, dynamic weapon summons, and motion warping with 8 frame-accurate FX event channels without animator controller spaghetti.',
                primaryText: 'Explore MSMotion',
                primaryHref: 'ms-motion.html',
                secondaryText: 'Read documentation',
                secondaryHref: 'ms-motion-docs.html',
                meta: [
                    'Multi-Actor Duet Sync',
                    'Dynamic Weapon Summons',
                    '8 Dedicated FX Types'
                ],
                stats: [
                    { label: 'Multi-Actor duets', value: 'Sync Duets', note: 'Lead, partner & dynamic summons', noteClass: 'accent' },
                    { label: 'Dedicated FX timeline', value: '8 FX Types', countTo: 8, countSuffix: ' FX Types', note: 'Audio, decals, VFX Graph & callbacks', noteClass: '' },
                    { label: 'Motion warping', value: 'Bezier Paths', note: 'Root distance clamps & target snapping', noteClass: 'positive' },
                    { label: 'Secondary bone physics', value: 'Spring-Mass', note: 'Anti-clipping colliders & volume preservation', noteClass: '' }
                ]
            },
            scriptable: {
                eyebrow: 'Scriptable Studio Pro v4.5 · Data Grid & Prefab Studio',
                title: 'Spreadsheet-speed bulk editing for ScriptableObjects & Prefabs',
                desc: 'Bulk edit thousands of ScriptableObjects and Prefab components in an Excel-grade virtualized grid with dynamic formula calculations (=[Level]*100), delta-safe serialization, and multi-format export.',
                primaryText: 'Explore Scriptable Studio',
                primaryHref: 'scriptable-studio-pro.html',
                secondaryText: 'Read documentation',
                secondaryHref: 'scriptable-studio-pro-docs.html',
                meta: [
                    '10,000+ Row Virtual Grid',
                    'Delta-Safe Prefab Studio',
                    'Dynamic Formula Engine'
                ],
                stats: [
                    { label: 'Bulk grid engine', value: '10,000+', countTo: 10000, countSuffix: '+', note: 'Virtualized rows with instant filtering', noteClass: 'accent' },
                    { label: 'Prefab Studio', value: 'Delta-Safe', note: 'Edit components without breaking overrides', noteClass: 'positive' },
                    { label: 'Dynamic calculations', value: 'Live Formulas', note: 'Cross-column math: =[Level]*100', noteClass: '' },
                    { label: 'Data exchange', value: 'Multi-Format', note: 'Bidirectional CSV, JSON & Google Sheets', noteClass: '' }
                ]
            },
            tactical: {
                eyebrow: 'Tactical Cover & Retreat AI v3.0 · Jobs & Burst Architecture',
                title: 'Dynamic cover finding, retreat paths & squad combat AI',
                desc: 'Production-ready tactical AI combining 21 spatial spot providers, 47 tactical scorers, ballistic suppression tracking, and smart combat locomotion for high-stakes encounters.',
                primaryText: 'Explore Tactical AI',
                primaryHref: 'tactical-cover-retreat-ai-system.html',
                secondaryText: 'Read documentation',
                secondaryHref: 'tactical-cover-retreat-ai-system-docs.html',
                meta: [
                    '21 Spatial Spot Providers',
                    '47 Tactical Burst Scorers',
                    'Ballistic Suppression Field'
                ],
                stats: [
                    { label: 'Spatial spot providers', value: '21 Providers', countTo: 21, countSuffix: ' Providers', note: 'Octree, NavMesh edges & geometry corners', noteClass: 'accent' },
                    { label: 'Burst tactical scorers', value: '47 Scorers', countTo: 47, countSuffix: ' Scorers', note: 'Flank safety, line-of-fire & density', noteClass: '' },
                    { label: 'Ballistic suppression', value: 'Real-Time', note: 'Bullet trajectory density & pin-down', noteClass: 'positive' },
                    { label: 'Scene diagnostic checks', value: '7 Checks', countTo: 7, countSuffix: ' Checks', note: 'Automated validation with 1-click Auto-Fix', noteClass: '' }
                ]
            },
            finder: {
                eyebrow: 'Object Finder Pro v2.0 · Async Search & Query Engine',
                title: 'Instant search & dependency analysis across Unity projects',
                desc: 'Query scenes, prefabs, and unloaded project assets asynchronously with smart query syntax (t:, m:, p:, b:), 35+ signature filters, and deep asset dependency tracking.',
                primaryText: 'Explore Object Finder',
                primaryHref: 'object-finder-pro.html',
                secondaryText: 'Read documentation',
                secondaryHref: 'object-finder-pro-docs.html',
                meta: [
                    'Smart Search Syntax (t:, m:, p:)',
                    '5 Search Scopes',
                    '35+ Extensible Filters'
                ],
                stats: [
                    { label: 'Search engine', value: 'Non-Blocking', note: 'Async project scan with live progress', noteClass: 'positive' },
                    { label: 'Smart query syntax', value: 't: m: p: b:', note: 'Type, missing scripts, polycount & bounds', noteClass: 'accent' },
                    { label: 'Search scopes', value: '5 Scopes', countTo: 5, countSuffix: ' Scopes', note: 'Active Scene, Open, Project, Unloaded, Root', noteClass: '' },
                    { label: 'Pre-built filters', value: '35+ Filters', countTo: 35, countSuffix: '+ Filters', note: 'Extensible CustomFilterBase C# API', noteClass: '' }
                ]
            },
            quick: {
                eyebrow: 'Ultimate Quick Inspector · Workflow & Pinning Drawer',
                title: 'Instant drag-and-drop quick access for active scenes & assets',
                desc: 'Eliminate deep folder digging by pinning frequently used prefabs, scene GameObjects, materials, and scripts into categorized multi-page drawers with persistent GUID tracking.',
                primaryText: 'Explore Quick Inspector',
                primaryHref: 'ultimate-quick-inspector.html',
                secondaryText: 'Read documentation',
                secondaryHref: 'ultimate-quick-inspector-docs.html',
                meta: [
                    'Multi-Page Drawer Tabs',
                    'Persistent GUID Tracking',
                    'Zero-Allocation SO Storage'
                ],
                stats: [
                    { label: 'Pin organization', value: 'Multi-Page', note: 'Categorized drawers for prefabs & scripts', noteClass: 'accent' },
                    { label: 'Reference tracking', value: 'Persistent GUID', note: 'Safe across scene renames & reloads', noteClass: 'positive' },
                    { label: 'Setup workflow', value: 'Drag & Drop', note: 'Instant pinning from Project or Hierarchy', noteClass: '' },
                    { label: 'Storage footprint', value: 'Zero-Alloc SO', note: 'Version-control safe ScriptableObjects', noteClass: '' }
                ]
            }
        };

        const heroCopy = document.getElementById('hero-asset-copy');
        const heroEyebrow = document.getElementById('hero-eyebrow-text');
        const heroTitle = document.getElementById('hero-title');
        const heroDesc = document.getElementById('hero-desc');
        const heroPrimaryBtn = document.getElementById('hero-btn-primary');
        const heroPrimaryText = document.getElementById('hero-btn-primary-text');
        const heroSecondaryBtn = document.getElementById('hero-btn-secondary');
        const heroMeta1 = document.getElementById('hero-meta-1');
        const heroMeta2 = document.getElementById('hero-meta-2');
        const heroMeta3 = document.getElementById('hero-meta-3');
        const statsStrip = document.getElementById('hero-asset-stats');

        let heroFadeTimer = null;

        function updateHeroAsset(targetKey) {
            const data = HERO_ASSET_DATA[targetKey];
            if (!data || !heroCopy) return;

            if (heroFadeTimer) clearTimeout(heroFadeTimer);
            heroCopy.classList.add('is-fading');
            if (statsStrip) statsStrip.classList.add('is-fading');

            heroFadeTimer = setTimeout(() => {
                if (heroEyebrow) heroEyebrow.textContent = data.eyebrow;
                if (heroTitle) heroTitle.textContent = data.title;
                if (heroDesc) heroDesc.textContent = data.desc;
                if (heroPrimaryBtn) {
                    heroPrimaryBtn.setAttribute('href', data.primaryHref);
                }
                if (heroPrimaryText) {
                    heroPrimaryText.textContent = data.primaryText;
                }
                if (heroSecondaryBtn) {
                    heroSecondaryBtn.setAttribute('href', data.secondaryHref);
                    heroSecondaryBtn.textContent = data.secondaryText;
                }
                if (heroMeta1 && data.meta[0]) heroMeta1.textContent = data.meta[0];
                if (heroMeta2 && data.meta[1]) heroMeta2.textContent = data.meta[1];
                if (heroMeta3 && data.meta[2]) heroMeta3.textContent = data.meta[2];

                if (statsStrip && data.stats && data.stats.length === 4) {
                    const cells = statsStrip.querySelectorAll('.stat-cell');
                    data.stats.forEach((st, idx) => {
                        const cell = cells[idx];
                        if (!cell) return;
                        const lbl = cell.querySelector('.stat-label');
                        const val = cell.querySelector('.stat-value');
                        const note = cell.querySelector('.stat-note');

                        if (lbl) lbl.textContent = st.label;
                        if (val) {
                            val.textContent = st.value;
                            if (st.countTo !== undefined) {
                                val.dataset.countTo = String(st.countTo);
                                if (st.countSuffix) {
                                    val.dataset.countSuffix = st.countSuffix;
                                } else {
                                    delete val.dataset.countSuffix;
                                }
                            } else {
                                delete val.dataset.countTo;
                                delete val.dataset.countSuffix;
                            }
                        }
                        if (note) {
                            note.textContent = st.note;
                            note.className = 'stat-note' + (st.noteClass ? ` ${st.noteClass}` : '');
                        }
                    });
                }

                heroCopy.classList.remove('is-fading');
                if (statsStrip) statsStrip.classList.remove('is-fading');
            }, 110);
        }

        document.querySelectorAll('[data-tab-group]').forEach((group) => {
            const tabs = group.querySelectorAll('[data-tab-target]');
            const panes = group.querySelectorAll('[data-tab-pane]');
            tabs.forEach((tab) => {
                tab.addEventListener('click', () => {
                    const target = tab.dataset.tabTarget;
                    tabs.forEach((t) => {
                        const active = t.dataset.tabTarget === target;
                        t.classList.toggle('active', active);
                        t.setAttribute('aria-selected', active ? 'true' : 'false');
                    });
                    panes.forEach((p) => {
                        p.hidden = p.dataset.tabPane !== target;
                    });
                    if (heroCopy && HERO_ASSET_DATA[target]) {
                        updateHeroAsset(target);
                    }
                    if (typeof tab.scrollIntoView === 'function') {
                        tab.scrollIntoView({ behavior: 'smooth', block: 'nearest', inline: 'center' });
                    }
                });
            });
        });

        // ---------------------------------------------------------------------
        // 6. Hero Glyph Field Canvas (Unslop Effect — 12fps, DPR<=2, Paused offscreen)
        // ---------------------------------------------------------------------
        const heroCanvas = document.querySelector('.hero-canvas');
        if (heroCanvas) {
            initHeroGlyphCanvas(heroCanvas);
        }

        // ---------------------------------------------------------------------
        // 7. SoftbodyMeshPro Spring Lattice Canvas (Index Roadmap)
        // ---------------------------------------------------------------------
        const softbodyCanvas = document.getElementById('softbody-canvas');
        if (softbodyCanvas) {
            initSoftbodyCanvas(softbodyCanvas);
        }

        // ---------------------------------------------------------------------
        // 8. MSUltimate Documentation Workspace (Hash Routing, Copy, Sidebar)
        // ---------------------------------------------------------------------
        initDocsWorkspace();
    });

    function initDocsWorkspace() {
        // Copy buttons inside generated documentation code blocks
        document.addEventListener('click', (e) => {
            const copyBtn = e.target.closest('.copy-code-btn');
            if (copyBtn) {
                const wrapper = copyBtn.closest('.code-block-wrapper');
                const codeEl = wrapper && wrapper.querySelector('pre code');
                if (!codeEl || !navigator.clipboard) return;
                navigator.clipboard.writeText(codeEl.textContent || '').then(() => {
                    const label = copyBtn.querySelector('.copy-label');
                    if (label) label.textContent = 'Copied';
                    copyBtn.classList.add('is-copied');
                    setTimeout(() => {
                        if (label) label.textContent = 'Copy';
                        copyBtn.classList.remove('is-copied');
                    }, 1800);
                }).catch(() => {});
                return;
            }

            const catToggleBtn = e.target.closest('.docs-cat-btn, .docs-cat-toggle');
            if (catToggleBtn) {
                const group = catToggleBtn.closest('.docs-cat-group');
                if (group) {
                    const collapsed = group.classList.toggle('is-collapsed');
                    catToggleBtn.setAttribute('aria-expanded', collapsed ? 'false' : 'true');
                }
            }
        });

        // Interactive Category Index Explorers (filter input + target pills)
        document.querySelectorAll('[data-cat-explorer]').forEach((explorer) => {
            const filterInput = explorer.querySelector('.cat-filter-input');
            const pills = Array.from(explorer.querySelectorAll('.cat-target-pill'));
            const rows = Array.from(explorer.querySelectorAll('[data-cat-row]'));
            const countLabel = explorer.querySelector('.cat-filter-count');
            let activeTarget = 'all';

            const applyFilter = () => {
                const q = filterInput ? filterInput.value.toLowerCase().trim() : '';
                let shown = 0;
                rows.forEach((row) => {
                    const hay = (row.dataset.catSearch || row.textContent || '').toLowerCase();
                    const rowTargets = (row.dataset.catTargets || '').toLowerCase();
                    const matchQ = !q || hay.includes(q);
                    const matchT = activeTarget === 'all' || rowTargets.split('|').includes(activeTarget);
                    const visible = matchQ && matchT;
                    row.style.display = visible ? '' : 'none';
                    if (visible) shown++;
                });
                if (countLabel) {
                    countLabel.textContent = `Showing ${shown} of ${rows.length}`;
                }
            };

            if (filterInput) {
                filterInput.addEventListener('input', applyFilter);
            }

            pills.forEach((pill) => {
                pill.addEventListener('click', () => {
                    activeTarget = (pill.dataset.targetFilter || 'all').toLowerCase();
                    pills.forEach((p) => p.classList.toggle('is-active', p === pill));
                    applyFilter();
                });
            });
        });

        const sidebar = document.querySelector('.docs-sidebar');
        const docsMain = document.querySelector('.docs-main');
        const sidebarToggle = document.getElementById('doc-sidebar-toggle');
        const closeMobileSidebar = () => {
            if (!sidebar) return;
            sidebar.classList.remove('is-mobile-open');
            if (sidebarToggle) sidebarToggle.setAttribute('aria-expanded', 'false');
        };
        if (sidebar && sidebarToggle) {
            sidebarToggle.addEventListener('click', () => {
                const open = sidebar.classList.toggle('is-mobile-open');
                sidebarToggle.setAttribute('aria-expanded', open ? 'true' : 'false');
            });
            sidebar.querySelectorAll('[data-doc-sidebar-close]').forEach((btn) => {
                btn.addEventListener('click', closeMobileSidebar);
            });
            sidebar.querySelectorAll('a').forEach((link) => {
                link.addEventListener('click', closeMobileSidebar);
            });
            document.addEventListener('keydown', (e) => {
                if (e.key === 'Escape' && sidebar.classList.contains('is-mobile-open')) {
                    closeMobileSidebar();
                }
            });
        }

        const searchInput = document.getElementById('doc-search');
        const hubChips = Array.from(document.querySelectorAll('.hub-attr-chip'));
        if (searchInput && hubChips.length) {
            const hubCats = Array.from(document.querySelectorAll('.hub-cat-group'));
            const hubCards = Array.from(document.querySelectorAll('.hub-pkg-card'));
            searchInput.addEventListener('input', () => {
                const term = searchInput.value.toLowerCase().trim();
                hubChips.forEach((chip) => {
                    const text = (chip.dataset.hubItem || chip.textContent || '').toLowerCase();
                    chip.style.display = !term || text.includes(term) ? '' : 'none';
                });
                hubCats.forEach((grp) => {
                    const anyVisible = Array.from(grp.querySelectorAll('.hub-attr-chip')).some((c) => c.style.display !== 'none');
                    grp.style.display = !term || anyVisible ? '' : 'none';
                });
                hubCards.forEach((card) => {
                    const anyCat = Array.from(card.querySelectorAll('.hub-cat-group')).some((g) => g.style.display !== 'none');
                    card.style.display = !term || anyCat ? '' : 'none';
                });
            });
        }

        const sections = Array.from(document.querySelectorAll('.docs-section'));
        if (!sections.length) return;

        const navLinks = Array.from(document.querySelectorAll('.docs-nav-link'));
        const subnavPills = Array.from(document.querySelectorAll('.eco-pill[data-doc-prefixes]'));
        const prevBtn = document.getElementById('prev-doc');
        const nextBtn = document.getElementById('next-doc');
        const navItems = Array.from(document.querySelectorAll('.docs-nav-menu li'));
        const catGroups = Array.from(document.querySelectorAll('.docs-cat-group'));

        let currentIndex = 0;

        const getSectionTitle = (sec) => {
            if (!sec) return '';
            return sec.dataset.docTitle || (sec.querySelector('h1') ? sec.querySelector('h1').textContent.trim() : sec.id);
        };

        const renderSection = (scrollMode) => {
            const hash = window.location.hash || `#${sections[0].id}`;
            let idx = sections.findIndex((s) => `#${s.id}` === hash);
            if (idx === -1) idx = 0;
            currentIndex = idx;

            const activeSectionId = sections[currentIndex].id;
            const activeId = `#${activeSectionId}`;
            sections.forEach((sec, i) => sec.classList.toggle('active', i === currentIndex));

            subnavPills.forEach((pill) => {
                const prefixes = (pill.dataset.docPrefixes || '')
                    .split(',')
                    .map((p) => p.trim())
                    .filter(Boolean);
                const active = prefixes.some((p) => activeSectionId === p || activeSectionId.startsWith(p));
                pill.classList.toggle('is-active', active);
            });

            let activeLink = null;
            navLinks.forEach((link) => {
                const isMatch = link.getAttribute('href') === activeId;
                link.classList.toggle('active', isMatch);
                if (isMatch) activeLink = link;
            });

            if (activeLink) {
                const group = activeLink.closest('.docs-cat-group');
                if (group) {
                    group.classList.remove('is-collapsed');
                    const toggleBtn = group.querySelector('.docs-cat-btn, .docs-cat-toggle');
                    if (toggleBtn) toggleBtn.setAttribute('aria-expanded', 'true');
                }
                const sidebarBody = sidebar ? sidebar.querySelector('.docs-sidebar-body') : null;
                if (sidebarBody && window.innerWidth > 1024) {
                    const bodyRect = sidebarBody.getBoundingClientRect();
                    const linkRect = activeLink.getBoundingClientRect();
                    if (linkRect.top < bodyRect.top + 8) {
                        sidebarBody.scrollTop -= (bodyRect.top + 8 - linkRect.top);
                    } else if (linkRect.bottom > bodyRect.bottom - 8) {
                        sidebarBody.scrollTop += (linkRect.bottom - bodyRect.bottom + 8);
                    }
                }
            }

            if (prevBtn) {
                prevBtn.disabled = currentIndex <= 0;
                const prevTitle = prevBtn.querySelector('.docs-pager-title');
                if (prevTitle) {
                    prevTitle.textContent = currentIndex > 0 ? getSectionTitle(sections[currentIndex - 1]) : 'Start of guide';
                }
            }

            if (nextBtn) {
                nextBtn.disabled = currentIndex >= sections.length - 1;
                const nextTitle = nextBtn.querySelector('.docs-pager-title');
                if (nextTitle) {
                    nextTitle.textContent = currentIndex < sections.length - 1 ? getSectionTitle(sections[currentIndex + 1]) : 'End of guide';
                }
            }

            if (sidebar) {
                sidebar.classList.remove('is-mobile-open');
                if (sidebarToggle) sidebarToggle.setAttribute('aria-expanded', 'false');
            }

            if (scrollMode === 'smooth') {
                window.scrollTo({ top: 0, behavior: 'smooth' });
            } else if (scrollMode === 'instant') {
                window.scrollTo({ top: 0, behavior: 'instant' });
                requestAnimationFrame(() => window.scrollTo({ top: 0, behavior: 'instant' }));
            }
        };

        navLinks.concat(subnavPills).forEach((link) => {
            link.addEventListener('click', (e) => {
                const href = link.getAttribute('href') || '';
                if (!href.startsWith('#')) return;
                e.preventDefault();
                if (window.location.hash !== href) {
                    window.location.hash = href;
                } else {
                    renderSection('smooth');
                }
            });
        });

        // Handle in-article anchor links pointing to another section in this same doc page
        document.querySelectorAll('.docs-main').forEach((mainEl) => {
            mainEl.addEventListener('click', (e) => {
                const link = e.target.closest('a[href^="#"]');
                if (!link) return;
                const href = link.getAttribute('href');
                if (sections.some((s) => `#${s.id}` === href)) {
                    e.preventDefault();
                    if (window.location.hash !== href) {
                        window.location.hash = href;
                    } else {
                        renderSection('smooth');
                    }
                }
            });
        });

        if (prevBtn) {
            prevBtn.addEventListener('click', () => {
                if (currentIndex > 0) {
                    window.location.hash = `#${sections[currentIndex - 1].id}`;
                }
            });
        }

        if (nextBtn) {
            nextBtn.addEventListener('click', () => {
                if (currentIndex < sections.length - 1) {
                    window.location.hash = `#${sections[currentIndex + 1].id}`;
                }
            });
        }

        if (searchInput) {
            searchInput.addEventListener('input', () => {
                const term = searchInput.value.toLowerCase().trim();
                navItems.forEach((li) => {
                    const link = li.querySelector('a');
                    if (!link) return;
                    const text = (link.textContent || '').toLowerCase();
                    li.style.display = !term || text.includes(term) ? '' : 'none';
                });

                catGroups.forEach((group) => {
                    const catLink = group.querySelector('.docs-cat-link');
                    const catMatch = term && catLink && (catLink.textContent || '').toLowerCase().includes(term);
                    const visibleItems = Array.from(group.querySelectorAll('li')).filter((li) => li.style.display !== 'none');
                    if (!term) {
                        group.style.display = '';
                    } else if (visibleItems.length > 0 || catMatch) {
                        group.style.display = '';
                        group.classList.remove('is-collapsed');
                        if (catMatch && visibleItems.length === 0) {
                            group.querySelectorAll('li').forEach((li) => { li.style.display = ''; });
                        }
                    } else {
                        group.style.display = 'none';
                    }
                });
            });
        }

        window.addEventListener('hashchange', () => renderSection('smooth'));
        renderSection(window.location.hash ? 'instant' : 'none');
    }

    function initHeroGlyphCanvas(canvas) {
        const ctx = canvas.getContext('2d');
        if (!ctx) return;

        const mode = canvas.dataset.glyphMode || 'studio';
        const charSets = {
            studio: ['.', ':', '+', '/', '[', ']', '=', '>'],
            ecosystem: ['.', ':', '[', ']', '#', '-', '>'],
            motion: ['.', '-', '~', '+', '|', '>'],
            search: ['.', ':', '?', '/', '*', '[', ']'],
            grid: ['.', ':', '=', '#', '+', '@'],
            tactical: ['.', '+', '/', '|', '\\', '>'],
            inspector: ['.', ':', '#', '0', '1', ']']
        };
        const chars = charSets[mode] || charSets.studio;

        const cell = 18;
        let width = 0;
        let height = 0;
        let cols = 0;
        let rows = 0;
        let dpr = 1;
        let visible = true;
        let step = 0;
        let pointer = { x: -9999, y: -9999, active: false };

        const readColors = () => {
            const styles = getComputedStyle(root);
            return {
                neutral: styles.getPropertyValue('--glyph-rgb').trim() || '237, 237, 237',
                accent: styles.getPropertyValue('--glyph-accent-rgb').trim() || '245, 158, 11'
            };
        };

        const resize = () => {
            const rect = canvas.parentElement.getBoundingClientRect();
            dpr = Math.min(window.devicePixelRatio || 1, 2);
            width = Math.max(1, Math.floor(rect.width));
            height = Math.max(1, Math.floor(rect.height));
            canvas.width = Math.floor(width * dpr);
            canvas.height = Math.floor(height * dpr);
            ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
            cols = Math.ceil(width / cell);
            rows = Math.ceil(height / cell);
        };

        resize();
        window.addEventListener('resize', resize, { passive: true });

        const hero = canvas.closest('.hero');
        if (hero) {
            hero.addEventListener('pointermove', (e) => {
                const rect = canvas.getBoundingClientRect();
                pointer.x = e.clientX - rect.left;
                pointer.y = e.clientY - rect.top;
                pointer.active = true;
            });
            hero.addEventListener('pointerleave', () => {
                pointer.active = false;
            });
        }

        const draw = (t) => {
            const { neutral, accent } = readColors();
            const isLight = root.getAttribute('data-theme') === 'light';
            ctx.clearRect(0, 0, width, height);
            ctx.font = '500 11px "JetBrains Mono", monospace';
            ctx.textAlign = 'center';
            ctx.textBaseline = 'middle';

            const phase = t * 0.08;
            for (let y = 0; y < rows; y++) {
                const py = y * cell + cell * 0.5;
                for (let x = 0; x < cols; x++) {
                    const px = x * cell + cell * 0.5;
                    let energy = 0;

                    if (mode === 'motion') {
                        const waveY = height * 0.52 + Math.sin(x * 0.22 - phase * 1.4) * (height * 0.16);
                        const dist = Math.abs(py - waveY);
                        energy = Math.max(0, 1 - dist / (cell * 4.5));
                    } else if (mode === 'tactical') {
                        const cx = width * 0.72;
                        const cy = height * 0.5;
                        const dx = px - cx;
                        const dy = py - cy;
                        const angle = Math.atan2(dy, dx);
                        const sweep = ((phase * 0.7) % (Math.PI * 2)) - Math.PI;
                        let diff = Math.abs(angle - sweep);
                        if (diff > Math.PI) diff = Math.PI * 2 - diff;
                        const dist = Math.hypot(dx, dy);
                        const ring = Math.abs((dist % 110) - 55) < 12 ? 0.35 : 0;
                        energy = Math.max(ring, diff < 0.45 && dist < width * 0.45 ? (1 - diff / 0.45) * 0.9 : 0);
                    } else if (mode === 'search') {
                        const scanX = ((phase * 3.5) % (cols + 12)) - 6;
                        const dist = Math.abs(x - scanX);
                        energy = dist < 4 ? (1 - dist / 4) * 0.85 : 0;
                    } else if (mode === 'grid') {
                        const activeRow = Math.floor(phase * 1.4) % Math.max(1, rows);
                        energy = y === activeRow ? 0.8 : (Math.sin(x * 0.3 + y * 0.25 + phase) + 1) * 0.18;
                    } else {
                        const w1 = Math.sin(x * 0.18 + phase) * Math.cos(y * 0.22 - phase * 0.7);
                        const w2 = Math.sin((x + y) * 0.12 - phase * 0.6);
                        energy = Math.max(0, (w1 + w2) * 0.38 + 0.16);
                    }

                    let pointerBoost = 0;
                    if (pointer.active) {
                        const pd = Math.hypot(px - pointer.x, py - pointer.y);
                        if (pd < 150) pointerBoost = (1 - pd / 150) * 0.85;
                    }

                    const total = Math.min(1, energy + pointerBoost);
                    if (total < 0.08) continue;

                    const charIdx = Math.min(chars.length - 1, Math.floor(total * chars.length));
                    const useAccent = pointerBoost > 0.25 || energy > 0.68;
                    const baseAlpha = isLight ? 0.06 + total * 0.24 : 0.04 + total * 0.22;
                    const accentAlpha = isLight ? 0.16 + total * 0.46 : 0.18 + total * 0.52;

                    ctx.fillStyle = useAccent
                        ? `rgba(${accent}, ${accentAlpha.toFixed(3)})`
                        : `rgba(${neutral}, ${baseAlpha.toFixed(3)})`;

                    ctx.fillText(chars[charIdx], px, py);
                }
            }
        };

        draw(0);
        if (reducedMotion) return;

        new IntersectionObserver(([entry]) => {
            visible = entry.isIntersecting;
        }).observe(canvas);

        let last = 0;
        const fpsInterval = 1000 / 12;
        const loop = (now) => {
            requestAnimationFrame(loop);
            if (!visible || now - last < fpsInterval) return;
            last = now;
            draw(++step);
        };
        requestAnimationFrame(loop);
    }

    function initSoftbodyCanvas(canvas) {
        const ctx = canvas.getContext('2d');
        if (!ctx) return;

        const cols = 11;
        const rows = 6;
        let width = 0;
        let height = 0;
        let dpr = 1;
        let visible = true;
        let time = 0;
        let pointer = { x: -999, y: -999, active: false };

        const resize = () => {
            const rect = canvas.parentElement.getBoundingClientRect();
            dpr = Math.min(window.devicePixelRatio || 1, 2);
            width = Math.max(1, Math.floor(rect.width));
            height = Math.max(1, Math.floor(rect.height));
            canvas.width = Math.floor(width * dpr);
            canvas.height = Math.floor(height * dpr);
            ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
        };

        resize();
        window.addEventListener('resize', resize, { passive: true });

        canvas.addEventListener('pointermove', (e) => {
            const rect = canvas.getBoundingClientRect();
            pointer.x = e.clientX - rect.left;
            pointer.y = e.clientY - rect.top;
            pointer.active = true;
        });

        canvas.addEventListener('pointerleave', () => {
            pointer.active = false;
        });

        const draw = (t) => {
            const styles = getComputedStyle(root);
            const neutral = styles.getPropertyValue('--glyph-rgb').trim() || '237, 237, 237';
            const accent = styles.getPropertyValue('--glyph-accent-rgb').trim() || '245, 158, 11';

            ctx.clearRect(0, 0, width, height);
            const padX = 32;
            const padY = 26;
            const spanX = width - padX * 2;
            const spanY = height - padY * 2;

            const pts = [];
            for (let r = 0; r < rows; r++) {
                const rowPts = [];
                for (let c = 0; c < cols; c++) {
                    const bx = padX + (c / (cols - 1)) * spanX;
                    const by = padY + (r / (rows - 1)) * spanY;
                    let ox = Math.sin(t * 0.05 + r * 0.65 + c * 0.4) * 3.5;
                    let oy = Math.cos(t * 0.045 + c * 0.55) * 4.5;

                    if (pointer.active) {
                        const dx = bx - pointer.x;
                        const dy = by - pointer.y;
                        const dist = Math.hypot(dx, dy);
                        if (dist < 110 && dist > 0.1) {
                            const force = (1 - dist / 110) * 18;
                            ox += (dx / dist) * force;
                            oy += (dy / dist) * force;
                        }
                    }
                    rowPts.push({ x: bx + ox, y: by + oy });
                }
                pts.push(rowPts);
            }

            const isLight = root.getAttribute('data-theme') === 'light';
            ctx.lineWidth = 1.25;
            ctx.strokeStyle = `rgba(${neutral}, ${isLight ? 0.28 : 0.24})`;
            for (let r = 0; r < rows; r++) {
                ctx.beginPath();
                for (let c = 0; c < cols; c++) {
                    const p = pts[r][c];
                    if (c === 0) ctx.moveTo(p.x, p.y);
                    else ctx.lineTo(p.x, p.y);
                }
                ctx.stroke();
            }

            for (let c = 0; c < cols; c++) {
                ctx.beginPath();
                for (let r = 0; r < rows; r++) {
                    const p = pts[r][c];
                    if (r === 0) ctx.moveTo(p.x, p.y);
                    else ctx.lineTo(p.x, p.y);
                }
                ctx.stroke();
            }

            for (let r = 0; r < rows; r++) {
                for (let c = 0; c < cols; c++) {
                    const p = pts[r][c];
                    const centerHighlight = (r === 2 || r === 3) && c === 5;
                    ctx.fillStyle = centerHighlight
                        ? `rgb(${accent})`
                        : `rgba(${neutral}, ${isLight ? 0.56 : 0.48})`;
                    ctx.beginPath();
                    ctx.arc(p.x, p.y, centerHighlight ? 3.5 : 2.1, 0, Math.PI * 2);
                    ctx.fill();
                }
            }
        };

        draw(0);
        if (reducedMotion) return;

        new IntersectionObserver(([entry]) => {
            visible = entry.isIntersecting;
        }).observe(canvas);

        let last = 0;
        const loop = (now) => {
            requestAnimationFrame(loop);
            if (!visible || now - last < 1000 / 24) return;
            last = now;
            draw(++time);
        };
        requestAnimationFrame(loop);
    }
})();
