
function saveCar(brand, model) {
    localStorage.setItem("myCar", JSON.stringify({brand: brand, model: model}));
    location.href = "index.html";
}

function getMyCar() {
    const car = localStorage.getItem("myCar");
    return car ? JSON.parse(car) : null;
}

function addToScheme(itemName, itemPrice) {
    let items = JSON.parse(localStorage.getItem("schemeItems") || "[]");
    items.push({name: itemName, price: itemPrice});
    localStorage.setItem("schemeItems", JSON.stringify(items));
    showToast("已成功加入您的专属改装方案！");
}

function getSchemeItems() {
    return JSON.parse(localStorage.getItem("schemeItems") || "[]");
}

document.addEventListener("DOMContentLoaded", () => {
    // Index.html
    if(window.location.pathname.endsWith("index.html") || window.location.pathname.endsWith("legai_new_frontend/")) {
        const car = getMyCar();
        if(car) {
            const addCarSection = document.getElementById("add-car-section");
            if(addCarSection) {
                addCarSection.innerHTML = `
                    <div style="display: flex; align-items: center; gap: 12px;">
                        <div style="width: 40px; height: 40px; background: #f0f0f0; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 20px;"><svg viewBox="0 0 24 24" fill="none" stroke="#111" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="width:22px;height:22px;"><path d="M19 17h2c.6 0 1-.4 1-1v-3c0-.9-.7-1.7-1.5-1.9C18.7 10.6 16 10 16 10s-1.3-1.4-2.2-2.3c-.5-.4-1.1-.7-1.8-.7H5c-.6 0-1.1.4-1.4.9l-1.4 2.9A3.7 3.7 0 0 0 2 12v4c0 .6.4 1 1 1h2"></path><circle cx="7" cy="17" r="2"></circle><path d="M9 17h6"></path><circle cx="17" cy="17" r="2"></circle></svg></div>
                        <div>
                            <div style="font-size: 15px; font-weight: bold;">${car.brand} ${car.model}</div>
                            <div style="font-size: 12px; color: #666;">您的专属车库</div>
                        </div>
                    </div>
                    <div style="background: #111; color: #fff; padding: 6px 16px; border-radius: 20px; font-size: 13px; cursor: pointer;" onclick="location.href='customization_2d.html'">去定制</div>
                `;
            }
        }
    }
    
    // Customization_2d.html
    if(window.location.pathname.endsWith("customization_2d.html")) {
        const car = getMyCar();
        if(car) {
            let el = document.getElementById("header-title");
            if(el) el.innerText = car.brand + " " + car.model + " 定制";
        }
        const items = getSchemeItems();
        if(items.length > 0) {
            const listDiv = document.getElementById("scheme-items-list");
            if(listDiv) {
                let html = "";
                let addPrice = 0;
                items.forEach(it => {
                    html += `<div style="font-size:12px; color:#666; margin-top:4px;">+ ${it.name} (¥${it.price})</div>`;
                    addPrice += parseInt(it.price.replace(/,/g, ''));
                });
                listDiv.innerHTML = html;
                document.getElementById("total-price").innerText = "¥" + (3500 + addPrice).toLocaleString();
            }
        }
    }
});

// Custom Toast UI implementation
window.showToast = function(message, duration = 2000) {
    let toast = document.getElementById('custom-toast');
    if (!toast) {
        toast = document.createElement('div');
        toast.id = 'custom-toast';
        toast.className = 'custom-toast';
        document.body.appendChild(toast);
    }
    toast.innerText = message;
    toast.classList.add('show');
    
    if (window.toastTimeout) {
        clearTimeout(window.toastTimeout);
    }
    
    window.toastTimeout = setTimeout(() => {
        toast.classList.remove('show');
    }, duration);
};
