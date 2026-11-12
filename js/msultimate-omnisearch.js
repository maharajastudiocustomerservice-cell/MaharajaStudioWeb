/**
 * MSUltimate Ecosystem Omni-Search
 * Enables instant searching across all 454+ attributes and guides from any MSUltimate docs page.
 * Powered by window.MSULTIMATE_ECOSYSTEM_INDEX.
 */
document.addEventListener('DOMContentLoaded', () => {
    const searchInput = document.getElementById('doc-search');
    if (!searchInput) return;

    const index = window.MSULTIMATE_ECOSYSTEM_INDEX || [];
    const container = searchInput.closest('.docs-sidebar-head') || searchInput.closest('.hub-search-box') || searchInput.parentElement;

    let dropdown = document.getElementById('ecosystem-search-results');
    if (!dropdown) {
        dropdown = document.createElement('div');
        dropdown.id = 'ecosystem-search-results';
        dropdown.className = 'eco-search-dropdown is-hidden';
        container.appendChild(dropdown);
    }

    const currentPath = window.location.pathname.split('/').pop().toLowerCase() || 'msultimate-docs.html';

    function getAddonTagClass(addon) {
        switch (addon) {
            case 'Core Framework': return 'tag-positive';
            case 'Animated Attributes':
            case 'Inspector Customizer':
            case 'ToolBox Vol. 1':
                return 'tag-accent';
            default:
                return '';
        }
    }

    function escapeHtml(text) {
        if (!text) return '';
        return String(text).replace(/[&<>"']/g, (m) => ({
            '&': '&amp;',
            '<': '&lt;',
            '>': '&gt;',
            '"': '&quot;',
            "'": '&#039;'
        }[m]));
    }

    function hideDropdown() {
        dropdown.classList.add('is-hidden');
    }

    function renderResults(query, matches) {
        if (!query) {
            dropdown.innerHTML = '';
            hideDropdown();
            return;
        }

        if (matches.length === 0) {
            dropdown.innerHTML = `
                <div class="eco-search-empty">
                    No entries found matching <strong>"${escapeHtml(query)}"</strong> across the MSUltimate ecosystem.
                </div>
            `;
            dropdown.classList.remove('is-hidden');
            return;
        }

        let html = `
            <div class="eco-search-header">
                <span>Ecosystem matches (${matches.length})</span>
                <span>Core + 6 Addons</span>
            </div>
            <div class="eco-search-list">
        `;

        matches.forEach((item) => {
            const isCurrentPage = currentPath === (item.docPage || '').toLowerCase();
            const targetUrl = isCurrentPage ? item.hash : `${item.docPage}${item.hash}`;
            const tagClass = getAddonTagClass(item.addon);

            html += `
                <a href="${targetUrl}" class="eco-search-item" data-page="${escapeHtml(item.docPage)}" data-hash="${escapeHtml(item.hash)}">
                    <div class="eco-search-item-head">
                        <span class="eco-search-item-title">${escapeHtml(item.name)}</span>
                        <span class="tag ${tagClass}">${escapeHtml(item.addon)}</span>
                    </div>
                    <div class="eco-search-item-desc">${escapeHtml(item.desc)}</div>
                    <div class="eco-search-item-dest">
                        ${isCurrentPage
                            ? 'Jump to section on this page'
                            : `Open in ${escapeHtml(item.addon)} (${escapeHtml(item.docPage)})`}
                    </div>
                </a>
            `;
        });

        html += '</div>';
        dropdown.innerHTML = html;
        dropdown.classList.remove('is-hidden');

        dropdown.querySelectorAll('.eco-search-item').forEach((link) => {
            link.addEventListener('click', (e) => {
                const targetPage = (link.getAttribute('data-page') || '').toLowerCase();
                const targetHash = link.getAttribute('data-hash') || '';

                hideDropdown();
                if (targetPage === currentPath && targetHash) {
                    e.preventDefault();
                    if (window.location.hash !== targetHash) {
                        window.location.hash = targetHash;
                    } else {
                        window.dispatchEvent(new HashChangeEvent('hashchange'));
                    }
                    window.scrollTo({ top: 0, behavior: 'smooth' });
                }
            });
        });
    }

    function performSearch() {
        const query = searchInput.value.trim().toLowerCase();
        if (!query) {
            hideDropdown();
            return;
        }

        const cleanQuery = query.replace(/[\[\]]/g, '');
        const scoredMatches = [];

        index.forEach((item) => {
            const rawLower = (item.rawName || '').toLowerCase();
            const nameLower = (item.name || '').toLowerCase();
            const catLower = (item.category || '').toLowerCase();
            const addonLower = (item.addon || '').toLowerCase();
            const descLower = (item.desc || '').toLowerCase();

            let score = 0;
            if (rawLower === cleanQuery || nameLower === query) score += 100;
            else if (rawLower.startsWith(cleanQuery) || nameLower.startsWith(query)) score += 60;
            else if (rawLower.includes(cleanQuery) || nameLower.includes(cleanQuery)) score += 40;
            else if (catLower.includes(cleanQuery)) score += 20;
            else if (addonLower.includes(cleanQuery)) score += 15;
            else if (descLower.includes(cleanQuery)) score += 10;

            if (currentPath === (item.docPage || '').toLowerCase() && score > 0) {
                score += 8;
            }

            if (score > 0) {
                scoredMatches.push({ item, score });
            }
        });

        scoredMatches.sort((a, b) => b.score - a.score);
        renderResults(query, scoredMatches.slice(0, 18).map((m) => m.item));
    }

    searchInput.addEventListener('input', performSearch);
    searchInput.addEventListener('focus', () => {
        if (searchInput.value.trim().length > 0) performSearch();
    });

    document.addEventListener('click', (e) => {
        if (!container.contains(e.target)) {
            hideDropdown();
        }
    });

    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape') {
            hideDropdown();
        }
        const tag = document.activeElement ? document.activeElement.tagName : '';
        if ((e.ctrlKey && e.key.toLowerCase() === 'k') || (e.key === '/' && document.activeElement !== searchInput && !['INPUT', 'TEXTAREA'].includes(tag))) {
            e.preventDefault();
            searchInput.focus();
            searchInput.select();
        }
    });
});
