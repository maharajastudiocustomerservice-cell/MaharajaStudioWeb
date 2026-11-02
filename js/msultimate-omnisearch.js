/**
 * MSUltimate Ecosystem Omni-Search
 * Enables instant searching across all 450+ attributes and tools from ANY MSUltimate page.
 * Powered by window.MSULTIMATE_ECOSYSTEM_INDEX.
 */
document.addEventListener('DOMContentLoaded', () => {
    const searchInput = document.getElementById('doc-search');
    if (!searchInput) return;

    // Check if index is loaded
    const index = window.MSULTIMATE_ECOSYSTEM_INDEX || [];

    // Ensure search input container is positioned relatively for the dropdown
    const container = searchInput.closest('.mb-3') || searchInput.parentElement;
    container.classList.add('position-relative');

    // Create dropdown element
    let dropdown = document.getElementById('ecosystem-search-results');
    if (!dropdown) {
        dropdown = document.createElement('div');
        dropdown.id = 'ecosystem-search-results';
        dropdown.className = 'ecosystem-search-dropdown shadow-lg d-none';
        container.appendChild(dropdown);
    }

    // Determine current page basename
    const currentPath = window.location.pathname.split('/').pop().toLowerCase() || 'msultimate-docs.html';

    // Helper: Badge class for addon
    function getAddonBadgeClass(addon) {
        switch (addon) {
            case 'Animated Attributes': return 'bg-danger';
            case 'Component Designer': return 'bg-info text-dark';
            case 'Hierarchy Designer': return 'bg-success';
            case 'Validation Module': return 'bg-primary';
            case 'Inspector Customizer': return 'bg-warning text-dark';
            case 'ToolBox Vol. 1': return 'bg-warning text-dark';
            case 'Core Framework': return 'bg-primary';
            default: return 'bg-secondary';
        }
    }

    // Render results
    function renderResults(query, matches) {
        if (!query) {
            dropdown.innerHTML = '';
            dropdown.classList.add('d-none');
            return;
        }

        if (matches.length === 0) {
            dropdown.innerHTML = `
                <div class="eco-search-empty">
                    <i class="fas fa-search me-2 text-muted"></i>
                    No attributes found matching <strong>"${escapeHtml(query)}"</strong> across the ecosystem.
                </div>
            `;
            dropdown.classList.remove('d-none');
            return;
        }

        let html = `
            <div class="eco-search-header">
                <span>Ecosystem Matches (${matches.length})</span>
                <span>Core + 6 Addons</span>
            </div>
            <div class="eco-search-list">
        `;

        matches.forEach(item => {
            const isCurrentPage = currentPath === item.docPage.toLowerCase();
            const targetUrl = isCurrentPage ? item.hash : `${item.docPage}${item.hash}`;
            const badgeClass = getAddonBadgeClass(item.addon);
            const liveBadge = item.status === 'Live'
                ? `<span class="badge bg-success ms-1"><i class="fas fa-eye me-1"></i>Live Preview</span>`
                : '';

            html += `
                <a href="${targetUrl}" class="eco-search-item ${isCurrentPage ? 'is-current-page' : 'is-other-addon'}" data-page="${item.docPage}" data-hash="${item.hash}">
                    <div class="item-title">
                        <span>${escapeHtml(item.name)}</span>
                        <span class="badge ${badgeClass} ms-auto">${escapeHtml(item.addon)}</span>
                        ${liveBadge}
                    </div>
                    <div class="item-desc">${escapeHtml(item.desc)}</div>
                    <div class="item-dest">
                        ${isCurrentPage 
                            ? `<i class="fas fa-check-circle text-success me-1"></i> Jump on this page` 
                            : `<i class="fas fa-arrow-up-right-from-square me-1"></i> Switch to ${escapeHtml(item.addon)} (${escapeHtml(item.docPage)})`
                        }
                    </div>
                </a>
            `;
        });

        html += `</div>`;
        dropdown.innerHTML = html;
        dropdown.classList.remove('d-none');

        // Attach click handlers to search items
        dropdown.querySelectorAll('.eco-search-item').forEach(link => {
            link.addEventListener('click', (e) => {
                const targetPage = link.getAttribute('data-page').toLowerCase();
                const targetHash = link.getAttribute('data-hash');

                if (targetPage === currentPath) {
                    e.preventDefault();
                    dropdown.classList.add('d-none');
                    if (window.location.hash !== targetHash) {
                        window.location.hash = targetHash;
                    } else {
                        // Force hashchange if already on it
                        window.dispatchEvent(new HashChangeEvent('hashchange'));
                    }
                    window.scrollTo({ top: 0, behavior: 'smooth' });
                } else {
                    // Navigate to other page normally
                    dropdown.classList.add('d-none');
                }
            });
        });
    }

    function escapeHtml(text) {
        if (!text) return '';
        return text.replace(/[&<>"']/g, m => ({
            '&': '&amp;',
            '<': '&lt;',
            '>': '&gt;',
            '"': '&quot;',
            "'": '&#039;'
        }[m]));
    }

    // Search query executor
    function performSearch() {
        const query = searchInput.value.trim().toLowerCase();
        if (!query) {
            dropdown.classList.add('d-none');
            return;
        }

        const cleanQuery = query.replace(/[\[\]]/g, '');

        // Match algorithm
        const scoredMatches = [];

        index.forEach(item => {
            const rawLower = item.rawName.toLowerCase();
            const nameLower = item.name.toLowerCase();
            const catLower = item.category.toLowerCase();
            const addonLower = item.addon.toLowerCase();
            const descLower = item.desc.toLowerCase();

            let score = 0;

            if (rawLower === cleanQuery || nameLower === query) {
                score += 100;
            } else if (rawLower.startsWith(cleanQuery)) {
                score += 60;
            } else if (rawLower.includes(cleanQuery)) {
                score += 40;
            } else if (catLower.includes(cleanQuery)) {
                score += 20;
            } else if (addonLower.includes(cleanQuery)) {
                score += 15;
            } else if (descLower.includes(cleanQuery)) {
                score += 10;
            }

            if (item.status === 'Live') {
                score += 5; // Slight boost for live documented attributes
            }

            // Current page boost
            if (currentPath === item.docPage.toLowerCase()) {
                score += 8;
            }

            if (score > 0) {
                scoredMatches.push({ item, score });
            }
        });

        scoredMatches.sort((a, b) => b.score - a.score);
        const topMatches = scoredMatches.slice(0, 18).map(m => m.item);

        renderResults(query, topMatches);
    }

    searchInput.addEventListener('input', performSearch);
    searchInput.addEventListener('focus', () => {
        if (searchInput.value.trim().length > 0) {
            performSearch();
        }
    });

    // Dismiss on click outside
    document.addEventListener('click', (e) => {
        if (!container.contains(e.target)) {
            dropdown.classList.add('d-none');
        }
    });

    // Dismiss on Escape key
    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape') {
            dropdown.classList.add('d-none');
        }
        // Shortcut: Ctrl+K or '/' focuses the search box
        if ((e.ctrlKey && e.key.toLowerCase() === 'k') || (e.key === '/' && document.activeElement !== searchInput && !['INPUT', 'TEXTAREA'].includes(document.activeElement.tagName))) {
            e.preventDefault();
            searchInput.focus();
            searchInput.select();
        }
    });
});

