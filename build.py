import os
import re

base_dir = "/Users/RondoT/Documents/Axure/HTML/Nissan_LeGai/legai_new_frontend"

js_content = """
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
    alert("已成功加入您的专属改装方案！");
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
                        <div style="width: 40px; height: 40px; background: #f0f0f0; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 20px;">🚙</div>
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
"""

with open(os.path.join(base_dir, "js", "main.js"), "w", encoding="utf-8") as f:
    f.write(js_content)

def get_5_nav(active_idx):
    tabs = [
        {"name": "首页", "icon": '<path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path><polyline points="9 22 9 12 15 12 15 22"></polyline>', "link": "index.html"},
        {"name": "灵感库", "icon": '<rect x="3" y="3" width="7" height="7"></rect><rect x="14" y="3" width="7" height="7"></rect><rect x="14" y="14" width="7" height="7"></rect><rect x="3" y="14" width="7" height="7"></rect>', "link": "scheme_square.html"},
        {"name": "去改装", "icon": '<path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"></path>', "link": "customization_2d.html"},
        {"name": "商城", "icon": '<circle cx="9" cy="21" r="1"></circle><circle cx="20" cy="21" r="1"></circle><path d="M1 1h4l2.68 13.39a2 2 0 0 0 2 1.61h9.72a2 2 0 0 0 2-1.61L23 6H6"></path>', "link": "mall.html"},
        {"name": "我的", "icon": '<path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path><circle cx="12" cy="7" r="4"></circle>', "link": "profile.html"}
    ]
    
    html = '        <!-- Standard 5-Tab Bottom Nav -->\n'
    html += '        <nav class="bottom-nav" style="position:fixed; bottom:0; left:50%; transform:translateX(-50%); width:100%; max-width:480px; background:#fff; display:flex; justify-content: space-around; padding: 8px 0 calc(8px + env(safe-area-inset-bottom)); border-top:1px solid #eee; z-index:100;">\n'
    
    for i, tab in enumerate(tabs):
        color = "#111; font-weight:bold" if i == active_idx else "#999"
        html += f'            <a href="{tab["link"]}" class="nav-item" style="display:flex; flex-direction:column; align-items:center; text-decoration:none; font-size:10px; color:{color};">\n'
        html += f'                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="width: 22px; height: 22px; margin-bottom: 2px;">{tab["icon"]}</svg>\n'
        html += f'                <span>{tab["name"]}</span>\n'
        html += '            </a>\n'
    html += '        </nav>'
    return html

files_to_update = {"index.html": 0, "scheme_square.html": 1, "customization_2d.html": 2, "profile.html": 4}
for filename, active_idx in files_to_update.items():
    filepath = os.path.join(base_dir, filename)
    if not os.path.exists(filepath): continue
    with open(filepath, "r", encoding="utf-8") as f: content = f.read()
    
    if '<script src="js/main.js"></script>' not in content:
        content = content.replace("</head>", '    <script src="js/main.js"></script>\n</head>')
    
    content = content.replace('class="add-car-section"', 'id="add-car-section" class="add-car-section"')
    
    pattern1 = re.compile(r"<!-- Standard.*?</nav>", re.DOTALL)
    pattern2 = re.compile(r"<!-- Bottom Navigation.*?<nav.*?</nav>", re.DOTALL)
    
    new_nav = get_5_nav(active_idx)
    
    if pattern1.search(content): content = pattern1.sub(new_nav, content)
    elif pattern2.search(content): content = pattern2.sub(new_nav, content)
    else: content = content.replace("</body>", new_nav + "\n</body>")
        
    with open(filepath, "w", encoding="utf-8") as f: f.write(content)

with open(os.path.join(base_dir, "mall.html"), "w", encoding="utf-8") as f:
    f.write(f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>商城 - 乐改</title>
    <link rel="stylesheet" href="css/global.css">
    <script src="js/main.js"></script>
</head>
<body style="background: #fafafa; padding-bottom:100px;">
    <div class="app-container">
        <div style="padding: 16px 20px; font-size: 18px; font-weight:bold; background:#fff; position:sticky; top:0; z-index:10; border-bottom:1px solid #eee;">
            商城配件
        </div>
        <div style="padding: 16px 20px; display:grid; grid-template-columns: 1fr 1fr; gap:12px;">
            <div style="background:#fff; border-radius:8px; overflow:hidden; cursor:pointer;" onclick="location.href='product_detail.html'">
                <img src="https://images.unsplash.com/photo-1601362840469-51e4d8d58785?auto=format&fit=crop&w=400&q=80" style="width:100%; height:140px; object-fit:cover;">
                <div style="padding:10px;">
                    <div style="font-size:13px; font-weight:bold; margin-bottom:8px;">TPU材质 隐形车衣</div>
                    <div style="color:#111; font-weight:bold;">¥8,999</div>
                </div>
            </div>
            <div style="background:#fff; border-radius:8px; overflow:hidden;">
                <img src="https://images.unsplash.com/photo-1611016186353-9af58c69a533?auto=format&fit=crop&w=400&q=80" style="width:100%; height:140px; object-fit:cover;">
                <div style="padding:10px;">
                    <div style="font-size:13px; font-weight:bold; margin-bottom:8px;">运动款碳纤维尾翼</div>
                    <div style="color:#111; font-weight:bold;">¥1,200</div>
                </div>
            </div>
        </div>
{get_5_nav(3)}
    </div>
</body>
</html>''')

print("Update completed successfully.")
