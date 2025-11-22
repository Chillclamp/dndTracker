class Api {
    static async listSettlements() {
        const res = await fetch('/api/settlements');
        return res.json();
    }
    static async getSettlement(id) {
        const res = await fetch('/api/settlements/' + encodeURIComponent(id));
        if (!res.ok) throw new Error('not found');
        return res.json();
    }
}


class UI {
    constructor() {
        this.listEl = document.getElementById('settlement-list');
        this.markersEl = document.getElementById('markers');
        this.detailEl = document.getElementById('detail-content');
        this.current = null;
    }


    clearList() { this.listEl.innerHTML = '' }


    addListItem(set) {
        const div = document.createElement('div');
        div.className = 'settlement-item';
        div.dataset.id = set.id;
        div.innerHTML = `<div class="name">${set.name}</div><div class="meta">Pop: ${set.population} — ${set.structures.length} structures</div>`;
        div.addEventListener('click', () => this.select(set.id));
        this.listEl.appendChild(div);
    }


    clearMarkers() { this.markersEl.innerHTML = '' }


    addMarker(set) {
        const m = document.createElement('div');
        m.className = 'marker';
        m.style.left = set.x_perc + '%';
        m.style.top = set.y_perc + '%';
        m.dataset.id = set.id;
        m.innerHTML = `<div class="dot">•</div><div class="label">${set.name}</div>`;
        m.addEventListener('click', (e) => { e.stopPropagation(); this.select(set.id); });
        this.markersEl.appendChild(m);
    }


    async select(id) {
        try {
            const data = await Api.getSettlement(id);
            this.current = data;
            this.renderDetails(data);
            this.highlightMarker(id);
            this.scrollMapTo(data);
        } catch (e) {
            this.detailEl.textContent = 'Failed to load details.';
        }
    }


    renderDetails(data) {
        const html = [];
        html.push(`<h4>${data.name}</h4>`);
        html.push(`<p>${data.description}</p>`);
    }
};