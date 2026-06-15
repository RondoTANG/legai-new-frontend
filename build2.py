import os
import re

base_dir = "/Users/RondoT/Documents/Axure/HTML/Nissan_LeGai/legai_new_frontend"

css_path = os.path.join(base_dir, "css", "global.css")
with open(css_path, "r", encoding="utf-8") as f:
    css = f.read()

if "column-count:" not in css:
    css = css.replace(".masonry-grid {", ".masonry-grid { column-count: 2; column-gap: 12px; display: block; /* override grid */")
    css = css.replace(".masonry-item {", ".masonry-item { break-inside: avoid; margin-bottom: 12px; display: inline-block; width: 100%;")
    with open(css_path, "w", encoding="utf-8") as f: f.write(css)

def get_4_nav(active_idx):
    tabs = [
        {"name": "首页", "icon": '<path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path><polyline points="9 22 9 12 15 12 15 22"></polyline>', "link": "index.html"},
        {"name": "去改装", "icon": '<path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"></path>', "link": "customization_2d.html"},
        {"name": "商城", "icon": '<circle cx="9" cy="21" r="1"></circle><circle cx="20" cy="21" r="1"></circle><path d="M1 1h4l2.68 13.39a2 2 0 0 0 2 1.61h9.72a2 2 0 0 0 2-1.61L23 6H6"></path>', "link": "mall.html"},
        {"name": "我的", "icon": '<path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path><circle cx="12" cy="7" r="4"></circle>', "link": "profile.html"}
    ]
    
    html = '        <!-- Standard 4-Tab Bottom Nav -->\n'
    html += '        <nav class="bottom-nav" style="position:fixed; bottom:0; left:50%; transform:translateX(-50%); width:100%; max-width:480px; background:#fff; display:flex; justify-content: space-around; padding: 8px 0 calc(8px + env(safe-area-inset-bottom)); border-top:1px solid #eee; z-index:100;">\n'
    
    for i, tab in enumerate(tabs):
        color = "#111; font-weight:bold" if i == active_idx else "#999"
        html += f'            <a href="{tab["link"]}" class="nav-item" style="display:flex; flex-direction:column; align-items:center; text-decoration:none; font-size:10px; color:{color};">\n'
        html += f'                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="width: 22px; height: 22px; margin-bottom: 2px;">{tab["icon"]}</svg>\n'
        html += f'                <span>{tab["name"]}</span>\n'
        html += '            </a>\n'
    html += '        </nav>'
    return html

files_to_update = {"index.html": 0, "customization_2d.html": 1, "mall.html": 2, "profile.html": 3}
for filename, active_idx in files_to_update.items():
    filepath = os.path.join(base_dir, filename)
    if not os.path.exists(filepath): continue
    with open(filepath, "r", encoding="utf-8") as f: content = f.read()
    
    pattern1 = re.compile(r"<!-- Standard.*?</nav>", re.DOTALL)
    new_nav = get_4_nav(active_idx)
    if pattern1.search(content): content = pattern1.sub(new_nav, content)
    
    with open(filepath, "w", encoding="utf-8") as f: f.write(content)

index_html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>首页 - 乐改</title>
    <link rel="stylesheet" href="css/global.css">
    <script src="js/main.js"></script>
</head>
<body style="background: #fafafa; padding-bottom: 80px;">
    <div class="app-container">
        <div class="header" style="display: flex; justify-content: space-between; align-items: center; position:sticky; top:0; background:#fff; z-index:10; border-bottom:1px solid #eee;">
            <div style="font-size: 20px; font-weight: bold; letter-spacing: 1px;">乐改 <span style="font-size:12px; color:#c92a2a; font-weight:normal;">社区</span></div>
            <div style="display: flex; gap: 16px;">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="width: 20px; height: 20px;"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
            </div>
        </div>

        <div id="add-car-section" class="add-car-section" style="margin: 16px; padding: 16px; background: #fff; border-radius: 12px; display: flex; justify-content: space-between; align-items: center; box-shadow: 0 2px 8px rgba(0,0,0,0.02);">
            <div style="font-size: 15px; font-weight: bold;">添加车型 定制专属改装方案</div>
            <div style="border: 1px solid #111; color: #111; padding: 6px 16px; border-radius: 20px; font-size: 13px; cursor: pointer;" onclick="location.href='brand_select.html'">+立即添加</div>
        </div>

        <div style="padding: 0 16px;">
            <div class="masonry-grid">
                <div class="masonry-item" onclick="location.href='scheme_detail.html'">
                    <img src="https://images.unsplash.com/photo-1549399542-7e3f8b79c341?auto=format&fit=crop&w=400&q=80" style="width:100%; border-radius:8px 8px 0 0;" alt="Scheme">
                    <div class="item-info" style="padding:10px; background:#fff; border-radius:0 0 8px 8px;">
                        <div class="item-title" style="font-size:13px; font-weight:bold; margin-bottom:8px; display:-webkit-box; -webkit-line-clamp:2; -webkit-box-orient:vertical; overflow:hidden;">黑武士风格，全车哑光黑改色膜+熏黑轮毂，低调有质感</div>
                        <div class="item-meta" style="display:flex; justify-content:space-between; font-size:11px; color:#999;">
                            <div class="author">车友A</div>
                            <div class="likes">❤️ 128</div>
                        </div>
                    </div>
                </div>
                
                <div class="masonry-item">
                    <img src="https://images.unsplash.com/photo-1611016186353-9af58c69a533?auto=format&fit=crop&w=400&h=500&q=80" style="width:100%; border-radius:8px 8px 0 0;" alt="Scheme">
                    <div class="item-info" style="padding:10px; background:#fff; border-radius:0 0 8px 8px;">
                        <div class="item-title" style="font-size:13px; font-weight:bold; margin-bottom:8px; display:-webkit-box; -webkit-line-clamp:2; -webkit-box-orient:vertical; overflow:hidden;">碳纤维尾翼加持，运动感拉满</div>
                        <div class="item-meta" style="display:flex; justify-content:space-between; font-size:11px; color:#999;">
                            <div class="author">速度迷</div>
                            <div class="likes">❤️ 89</div>
                        </div>
                    </div>
                </div>

                <div class="masonry-item">
                    <img src="https://images.unsplash.com/photo-1580273916550-e323be2ae537?auto=format&fit=crop&w=400&q=80" style="width:100%; border-radius:8px 8px 0 0;" alt="Scheme">
                    <div class="item-info" style="padding:10px; background:#fff; border-radius:0 0 8px 8px;">
                        <div class="item-title" style="font-size:13px; font-weight:bold; margin-bottom:8px; display:-webkit-box; -webkit-line-clamp:2; -webkit-box-orient:vertical; overflow:hidden;">水泥灰永远滴神！质感无敌了</div>
                        <div class="item-meta" style="display:flex; justify-content:space-between; font-size:11px; color:#999;">
                            <div class="author">改装老炮</div>
                            <div class="likes">❤️ 256</div>
                        </div>
                    </div>
                </div>

                <div class="masonry-item">
                    <img src="https://images.unsplash.com/photo-1601362840469-51e4d8d58785?auto=format&fit=crop&w=400&h=300&q=80" style="width:100%; border-radius:8px 8px 0 0;" alt="Scheme">
                    <div class="item-info" style="padding:10px; background:#fff; border-radius:0 0 8px 8px;">
                        <div class="item-title" style="font-size:13px; font-weight:bold; margin-bottom:8px; display:-webkit-box; -webkit-line-clamp:2; -webkit-box-orient:vertical; overflow:hidden;">刚贴完隐形车衣，来交个作业</div>
                        <div class="item-meta" style="display:flex; justify-content:space-between; font-size:11px; color:#999;">
                            <div class="author">新手小白</div>
                            <div class="likes">❤️ 45</div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
{get_4_nav(0)}
    </div>
</body>
</html>"""
with open(os.path.join(base_dir, "index.html"), "w", encoding="utf-8") as f: f.write(index_html)

mall_html = f"""<!DOCTYPE html>
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
        <div style="padding: 16px 20px; display:flex; justify-content:space-between; align-items:center; background:#fff; position:sticky; top:0; z-index:10; border-bottom:1px solid #eee;">
            <div style="font-size: 20px; font-weight:bold; letter-spacing:1px;">乐改 <span style="font-size:12px; color:#c92a2a; font-weight:normal;">商城</span></div>
            <div style="display: flex; gap: 16px;">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="width: 20px; height: 20px;"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="width: 20px; height: 20px;" onclick="location.href='cart.html'"><circle cx="9" cy="21" r="1"></circle><circle cx="20" cy="21" r="1"></circle><path d="M1 1h4l2.68 13.39a2 2 0 0 0 2 1.61h9.72a2 2 0 0 0 2-1.61L23 6H6"></path></svg>
            </div>
        </div>
        
        <div style="padding:16px;">
            <div style="width:100%; height:140px; background:#111; border-radius:12px; overflow:hidden; position:relative;">
                <img src="https://images.unsplash.com/photo-1549399542-7e3f8b79c341?auto=format&fit=crop&w=800&q=80" style="width:100%; height:100%; object-fit:cover; opacity:0.7;">
                <div style="position:absolute; bottom:16px; left:16px; color:#fff;">
                    <div style="font-size:18px; font-weight:bold; margin-bottom:4px;">官方黑武士套件</div>
                    <div style="font-size:12px;">限时首发 抢先体验</div>
                </div>
            </div>
        </div>

        <div style="padding: 16px;">
            <div style="font-size: 18px; font-weight: bold; margin-bottom: 12px;">官方精选套件</div>
            <div style="display:flex; overflow-x:auto; gap:12px; padding-bottom:8px; scrollbar-width:none;">
                <div style="min-width:260px; background:#fff; border-radius:8px; overflow:hidden; box-shadow:0 2px 6px rgba(0,0,0,0.03);" onclick="location.href='scheme_detail.html'">
                    <img src="https://images.unsplash.com/photo-1611016186353-9af58c69a533?auto=format&fit=crop&w=400&q=80" style="width:100%; height:140px; object-fit:cover;">
                    <div style="padding:12px;">
                        <div style="font-size:14px; font-weight:bold; margin-bottom:4px;">天籁·黑武士暗夜行者轻改方案</div>
                        <div style="font-size:16px; color:#c92a2a; font-weight:bold;">¥4,280.00 <span style="font-size:12px; color:#999; font-weight:normal;">参考价</span></div>
                    </div>
                </div>
                <div style="min-width:260px; background:#fff; border-radius:8px; overflow:hidden; box-shadow:0 2px 6px rgba(0,0,0,0.03);" onclick="location.href='scheme_detail.html'">
                    <img src="https://images.unsplash.com/photo-1580273916550-e323be2ae537?auto=format&fit=crop&w=400&q=80" style="width:100%; height:140px; object-fit:cover;">
                    <div style="padding:12px;">
                        <div style="font-size:14px; font-weight:bold; margin-bottom:4px;">轩逸·运动姿态基础套件</div>
                        <div style="font-size:16px; color:#c92a2a; font-weight:bold;">¥2,999.00 <span style="font-size:12px; color:#999; font-weight:normal;">参考价</span></div>
                    </div>
                </div>
            </div>
        </div>

        <div style="padding: 16px;">
            <div style="font-size: 18px; font-weight: bold; margin-bottom: 12px;">优选单品</div>
            <div style="display:grid; grid-template-columns: 1fr 1fr; gap:12px;">
                <div style="background:#fff; border-radius:8px; overflow:hidden; cursor:pointer;" onclick="location.href='product_detail.html'">
                    <img src="https://images.unsplash.com/photo-1601362840469-51e4d8d58785?auto=format&fit=crop&w=400&q=80" style="width:100%; height:140px; object-fit:cover;">
                    <div style="padding:10px;">
                        <div style="font-size:10px; background:#f0f0f0; color:#666; display:inline-block; padding:2px 6px; border-radius:4px; margin-bottom:6px;">纯正精品</div>
                        <div style="font-size:13px; font-weight:bold; margin-bottom:8px;">TPU材质 隐形车衣</div>
                        <div style="color:#c92a2a; font-weight:bold;">¥8,999</div>
                    </div>
                </div>
                <div style="background:#fff; border-radius:8px; overflow:hidden;">
                    <div style="width:100%; height:140px; background:#f5f5f5; display:flex; align-items:center; justify-content:center; font-size:40px;">🛞</div>
                    <div style="padding:10px;">
                        <div style="font-size:10px; background:#f0f0f0; color:#666; display:inline-block; padding:2px 6px; border-radius:4px; margin-bottom:6px;">乐改甄选</div>
                        <div style="font-size:13px; font-weight:bold; margin-bottom:8px;">运动款锻造轮毂</div>
                        <div style="color:#c92a2a; font-weight:bold;">¥1,200</div>
                    </div>
                </div>
            </div>
        </div>
{get_4_nav(2)}
    </div>
</body>
</html>"""
with open(os.path.join(base_dir, "mall.html"), "w", encoding="utf-8") as f: f.write(mall_html)
