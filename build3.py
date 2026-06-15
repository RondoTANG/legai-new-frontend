import os

base_dir = "/Users/RondoT/Documents/Axure/HTML/Nissan_LeGai/legai_new_frontend"

# 1. Update main.js to use an SVG car icon instead of the emoji
js_path = os.path.join(base_dir, "js", "main.js")
with open(js_path, "r", encoding="utf-8") as f:
    js_content = f.read()

car_svg = """<svg viewBox="0 0 24 24" fill="none" stroke="#111" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="width:22px;height:22px;"><path d="M19 17h2c.6 0 1-.4 1-1v-3c0-.9-.7-1.7-1.5-1.9C18.7 10.6 16 10 16 10s-1.3-1.4-2.2-2.3c-.5-.4-1.1-.7-1.8-.7H5c-.6 0-1.1.4-1.4.9l-1.4 2.9A3.7 3.7 0 0 0 2 12v4c0 .6.4 1 1 1h2"></path><circle cx="7" cy="17" r="2"></circle><path d="M9 17h6"></path><circle cx="17" cy="17" r="2"></circle></svg>"""
js_content = js_content.replace(">🚙<", f">{car_svg}<")
with open(js_path, "w", encoding="utf-8") as f:
    f.write(js_content)


# 2. Rebuild index.html with Categorized Layout & reliable 2-column CSS
def get_4_nav(active_idx):
    tabs = [
        {"name": "首页", "icon": "<path d='M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z'></path><polyline points='9 22 9 12 15 12 15 22'></polyline>", "link": "index.html"},
        {"name": "去改装", "icon": "<path d='M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z'></path>", "link": "customization_2d.html"},
        {"name": "商城", "icon": "<circle cx='9' cy='21' r='1'></circle><circle cx='20' cy='21' r='1'></circle><path d='M1 1h4l2.68 13.39a2 2 0 0 0 2 1.61h9.72a2 2 0 0 0 2-1.61L23 6H6'></path>", "link": "mall.html"},
        {"name": "我的", "icon": "<path d='M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2'></path><circle cx='12' cy='7' r='4'></circle>", "link": "profile.html"}
    ]
    html = "        <!-- Standard 4-Tab Bottom Nav -->\n"
    html += "        <nav class=\"bottom-nav\" style=\"position:fixed; bottom:0; left:50%; transform:translateX(-50%); width:100%; max-width:480px; background:#fff; display:flex; justify-content: space-around; padding: 8px 0 calc(8px + env(safe-area-inset-bottom)); border-top:1px solid #eee; z-index:100;\">\n"
    for i, tab in enumerate(tabs):
        color = "#111; font-weight:bold" if i == active_idx else "#999"
        html += f"            <a href=\"{tab['link']}\" class=\"nav-item\" style=\"display:flex; flex-direction:column; align-items:center; text-decoration:none; font-size:10px; color:{color};\">\n"
        html += f"                <svg viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\" stroke-linecap=\"round\" stroke-linejoin=\"round\" style=\"width: 22px; height: 22px; margin-bottom: 2px;\">{tab['icon']}</svg>\n"
        html += f"                <span>{tab['name']}</span>\n"
        html += "            </a>\n"
    html += "        </nav>"
    return html

index_html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>首页 - 乐改</title>
    <link rel="stylesheet" href="css/global.css">
    <script src="js/main.js"></script>
    <style>
        .grid-2col {{
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 12px;
        }}
        .card {{
            background: #fff;
            border-radius: 8px;
            overflow: hidden;
            box-shadow: 0 2px 8px rgba(0,0,0,0.03);
            cursor: pointer;
        }}
        .card img {{
            width: 100%;
            object-fit: cover;
        }}
        .card-info {{
            padding: 10px;
        }}
        .card-title {{
            font-size: 13px;
            font-weight: bold;
            margin-bottom: 8px;
            display: -webkit-box;
            -webkit-line-clamp: 2;
            -webkit-box-orient: vertical;
            overflow: hidden;
        }}
        .card-meta {{
            display: flex;
            justify-content: space-between;
            font-size: 11px;
            color: #999;
        }}
    </style>
</head>
<body style="background: #fafafa; padding-bottom: 80px;">
    <div class="app-container">
        <!-- Header -->
        <div class="header" style="display: flex; justify-content: space-between; align-items: center; position:sticky; top:0; background:#fff; z-index:10; border-bottom:1px solid #eee; padding:12px 16px;">
            <div style="font-size: 20px; font-weight: bold; letter-spacing: 1px;">乐改 <span style="font-size:12px; color:#c92a2a; font-weight:normal;">发现</span></div>
            <div style="display: flex; gap: 16px;">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="width: 20px; height: 20px;"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
            </div>
        </div>

        <!-- Add Car -->
        <div id="add-car-section" class="add-car-section" style="margin: 16px; padding: 16px; background: #fff; border-radius: 12px; display: flex; justify-content: space-between; align-items: center; box-shadow: 0 2px 8px rgba(0,0,0,0.02);">
            <div style="font-size: 15px; font-weight: bold;">添加车型 定制专属改装方案</div>
            <div style="border: 1px solid #111; color: #111; padding: 6px 16px; border-radius: 20px; font-size: 13px; cursor: pointer;" onclick="location.href='brand_select.html'">+立即添加</div>
        </div>

        <!-- Official Recommended (2-col grid) -->
        <div style="padding: 0 16px 20px;">
            <div style="font-size: 16px; font-weight: bold; margin-bottom: 12px; display:flex; justify-content:space-between; align-items:center;">
                官方精选方案
                <span style="font-size:12px; color:#999; font-weight:normal;">更多 ›</span>
            </div>
            <div class="grid-2col">
                <div class="card" onclick="location.href='scheme_detail.html'">
                    <img src="https://images.unsplash.com/photo-1611016186353-9af58c69a533?auto=format&fit=crop&w=400&q=80" style="height:120px;">
                    <div class="card-info">
                        <div class="card-title">天籁·黑武士暗夜行者全车轻改方案</div>
                        <div class="card-meta">
                            <div style="color:#c92a2a; font-weight:bold; font-size:13px;">¥4,280</div>
                            <div>❤️ 890</div>
                        </div>
                    </div>
                </div>
                <div class="card" onclick="location.href='scheme_detail.html'">
                    <img src="https://images.unsplash.com/photo-1580273916550-e323be2ae537?auto=format&fit=crop&w=400&q=80" style="height:120px;">
                    <div class="card-info">
                        <div class="card-title">轩逸·运动姿态基础套件升级</div>
                        <div class="card-meta">
                            <div style="color:#c92a2a; font-weight:bold; font-size:13px;">¥2,999</div>
                            <div>❤️ 652</div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- Popular DIY (Masonry via 2-col grid for stability) -->
        <div style="padding: 0 16px 20px;">
            <div style="font-size: 16px; font-weight: bold; margin-bottom: 12px;">热门DIY改装方案</div>
            <div class="grid-2col">
                <div class="card" onclick="location.href='scheme_detail.html'">
                    <img src="https://images.unsplash.com/photo-1549399542-7e3f8b79c341?auto=format&fit=crop&w=400&q=80" style="height:180px;">
                    <div class="card-info">
                        <div class="card-title">黑武士风格，全车哑光黑改色膜+熏黑轮毂</div>
                        <div class="card-meta">
                            <div>车友A</div>
                            <div>❤️ 128</div>
                        </div>
                    </div>
                </div>
                
                <div class="card">
                    <img src="https://images.unsplash.com/photo-1601362840469-51e4d8d58785?auto=format&fit=crop&w=400&h=300&q=80" style="height:140px;">
                    <div class="card-info">
                        <div class="card-title">刚贴完隐形车衣，来交个作业</div>
                        <div class="card-meta">
                            <div>新手小白</div>
                            <div>❤️ 45</div>
                        </div>
                    </div>
                </div>

                <div class="card">
                    <img src="https://images.unsplash.com/photo-1551806235-a05ff3cebf28?auto=format&fit=crop&w=400&q=80" style="height:160px;">
                    <div class="card-info">
                        <div class="card-title">轻度改装，换了个碳纤维牛角后视镜壳</div>
                        <div class="card-meta">
                            <div>老炮</div>
                            <div>❤️ 211</div>
                        </div>
                    </div>
                </div>

                <div class="card">
                    <img src="https://images.unsplash.com/photo-1611016186353-9af58c69a533?auto=format&fit=crop&w=400&h=500&q=80" style="height:190px;">
                    <div class="card-info">
                        <div class="card-title">碳纤维尾翼加持，运动感拉满</div>
                        <div class="card-meta">
                            <div>速度迷</div>
                            <div>❤️ 89</div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

{get_4_nav(0)}
    </div>
</body>
</html>"""
with open(os.path.join(base_dir, "index.html"), "w", encoding="utf-8") as f:
    f.write(index_html)

print("Index and SVG updated successfully.")
