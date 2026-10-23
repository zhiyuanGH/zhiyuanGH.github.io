"""Generate a portable, bilingual academic website using the Python standard library."""
from pathlib import Path
from html import escape
import re

ROOT = Path(__file__).resolve().parent
DIST = ROOT

def t(en, zh, tag='span', cls=''):
    return f'<{tag}'+(f' class="{cls}"' if cls else '')+f' data-zh="{escape(zh, quote=True)}">{en}</{tag}>'

def link(url, text):
    return f'<a href="{url}" target="_blank" rel="noopener noreferrer">{text}</a>'

polyu=link('https://www.polyu.edu.hk/','The Hong Kong Polytechnic University')
comp=link('https://www.polyu.edu.hk/comp/','Department of Computing')
cao=link('https://www4.comp.polyu.edu.hk/~csjcao/','Prof. Jiannong Cao')
lab=link('https://www4.comp.polyu.edu.hk/~labimcl/','Internet and Mobile Computing Lab (IMCL)')
scut=link('https://www.scut.edu.cn/en/','South China University of Technology')

pubs=[
 {'id':'fetchright','category':'systems','venue':'MASS','year':'2026','title':'FetchRight: Two-Stage Network-Adaptive Image Fetching for Fast Edge Container Provisioning','authors':'<strong>Zhiyuan Hu</strong>, Jiannong Cao, Paolo Bellavista, Kaile Wang, Zhaorui Zhang','full':'IEEE International Conference on Mobile Ad Hoc and Smart Systems (MASS), 2026.','url':'https://mass-conf.github.io/2026/technicalsessions.html','label':'Conference program','zhlabel':'会议日程','summary':'Network-adaptive image fetching for faster edge container provisioning.','zhsummary':'根据网络条件调整镜像拉取策略，加速边缘环境中的容器部署。'},
 {'id':'snapshot','category':'systems','venue':'TMC','year':'2026','title':'On-Demand Snapshot Migration: Accelerating Container Migration in Low-Bandwidth Networks','authors':'<strong>Zhiyuan Hu</strong>, Jiannong Cao, Zhaorui Zhang, Yinfeng Cao, Lei Yang','full':'IEEE Transactions on Mobile Computing (TMC), 2026.','url':'https://doi.org/10.1109/TMC.2026.3720463','label':'Paper','zhlabel':'论文','summary':'On-demand snapshot transfer for container migration over bandwidth-limited networks.','zhsummary':'通过按需传输快照数据，提升低带宽网络中的容器迁移效率。'},
 {'id':'platform','category':'ai systems','venue':'SOSE','year':'2026','title':'Towards Edge AI Native Service Platforms: Rethinking Runtime, Deployment, and Migration','authors':'Jiannong Cao, <strong>Zhiyuan Hu</strong>, Mingjin Zhang, Xiaoming Shen, Hongbo Liu','full':'IEEE International Conference on Service-Oriented System Engineering (SOSE), pp. 90–97, 2026.','url':'https://dblp.org/rec/conf/sose/CaoHZSL26','label':'Publication record','zhlabel':'论文记录','summary':'Service platforms designed around the runtime, deployment, and migration needs of edge AI.','zhsummary':'面向边缘人工智能的运行时、部署与迁移需求，探索服务平台设计。'},
 {'id':'polyverse','category':'ai systems','venue':'iMETA','year':'2023','title':'PolyVerse: An Edge Computing-Empowered Metaverse with Physical-to-Virtual Projection','authors':'Yinfeng Cao, Jiannong Cao, Dongbin Bai, <strong>Zhiyuan Hu</strong>, Kaile Wang, Mingjin Zhang','full':'IEEE International Conference on Intelligent Metaverse Technologies & Applications (iMETA), pp. 1–8, 2023.','url':'https://doi.org/10.1109/iMETA59369.2023.10294558','label':'Paper','zhlabel':'论文','summary':'Edge computing and consistent state management for physical-to-virtual projection.','zhsummary':'利用边缘计算和一致性状态管理，实现物理世界到虚拟环境的映射。'}
]

def publication(p):
    return f'''<article class="publication" id="pub-{p['id']}" data-category="{p['category']}">
    <h3>{p['title']}</h3><p class="authors">{p['authors']}</p><p class="venue"><strong>{p['venue']} {p['year']}</strong> · {p['full']}</p>
    {t(p['summary'],p['zhsummary'],'p','pub-summary')}
    <div class="publication-links">{link(p['url'],t(p['label'],p['zhlabel']))}<button class="bibtex-button" data-citation="{p['id']}">BibTeX</button></div></article>'''

def home():
    return t('About me','关于我','h1') + t(
      f'I am a Ph.D. student at {polyu}, supervised by {cao}, and a member of the {lab}. From November 2025 to June 2026, I was a visiting Ph.D. student at the University of Bologna, working with Prof. Paolo Bellavista. I received my B.Eng. in <strong>Software Engineering</strong> from {scut} in 2021, advised by Prof. Lei Yang.',
      '我是'+link('https://www.polyu.edu.hk/','香港理工大学')+'的博士研究生，导师是'+link('https://www4.comp.polyu.edu.hk/~csjcao/','曹建农教授')+'，也是'+link('https://www4.comp.polyu.edu.hk/~labimcl/','互联网与移动计算实验室（IMCL）')+'的成员。2025 年 11 月至 2026 年 6 月，我在博洛尼亚大学担任访问博士生，与 Paolo Bellavista 教授合作。我于 2021 年获得'+link('https://www.scut.edu.cn/','华南理工大学')+'<strong>软件工程专业工学学士</strong>学位，本科导师为杨磊教授。','p') + t(
      'My current research focuses on <strong>on-device large language models (LLMs)</strong>, particularly <strong>optimizing LLM inference and agent execution on mobile devices</strong>. My previous research explored container virtualization and edge computing.',
      '我目前的研究聚焦于<strong>端侧大语言模型（LLM）</strong>，尤其是<strong>移动设备上的 LLM 推理优化与智能体执行优化</strong>。此前，我主要研究容器虚拟化与边缘计算。','p') + \
      '<p class="inline-contact"><strong>Email:</strong> <a href="mailto:zhi-yuan.hu@connect.polyu.hk">zhi-yuan.hu@connect.polyu.hk</a></p>' + \
      '<section id="news">'+t('Recent news','近期动态','h2')+'<ul class="news-list">'+ \
      t('<strong>Oct 2026.</strong> Our work '+link('https://mass-conf.github.io/2026/technicalsessions.html','FetchRight')+' appears at IEEE MASS 2026 in Hong Kong.','<strong>2026 年 10 月。</strong>我们的研究 '+link('https://mass-conf.github.io/2026/technicalsessions.html','FetchRight')+' 在香港举办的 IEEE MASS 2026 上发表。','li')+ \
      t('<strong>Jul 2026.</strong> Our paper on '+link('https://doi.org/10.1109/TMC.2026.3720463','on-demand snapshot migration')+' was accepted by IEEE Transactions on Mobile Computing.','<strong>2026 年 7 月。</strong>我们的'+link('https://doi.org/10.1109/TMC.2026.3720463','按需快照迁移论文')+'被 IEEE Transactions on Mobile Computing 录用。','li')+ \
      t('<strong>Jul 2026.</strong> Contributed to <a href="publications.html#pub-platform">Towards Edge AI Native Service Platforms</a> at IEEE SOSE 2026.','<strong>2026 年 7 月。</strong>参与的研究 <a href="publications.html#pub-platform">Towards Edge AI Native Service Platforms</a> 在 IEEE SOSE 2026 发表。','li')+'</ul></section>'+ \
      '<section id="contact">'+t('Contact','联系我','h2')+t('I welcome discussions about on-device LLMs, mobile inference optimization, and agent execution. Please feel free to get in touch by email.','欢迎交流端侧大语言模型、移动设备推理优化与智能体执行相关的研究问题。你可以通过邮件联系我。','p')+'<p><a href="mailto:zhi-yuan.hu@connect.polyu.hk">zhi-yuan.hu@connect.polyu.hk</a> <button id="copy-email" class="small-button">'+t('Copy email','复制邮箱')+'</button></p></section>'

def publications():
    out=t('Publications','学术论文','h1')+t('Selected publications. My name is highlighted in the author lists.','以下为部分研究成果，我的姓名已在作者列表中加粗。','p','page-intro')
    out+='<div class="publication-toolbar"><div class="filters" role="group" aria-label="Filter publications">'
    for key,en,zh in [('all','All','全部'),('systems','Systems','计算系统'),('ai','Edge AI','边缘智能')]:
        out+=f'<button class="filter {"active" if key=="all" else ""}" data-filter="{key}" aria-pressed="{str(key=="all").lower()}">{t(en,zh)}</button>'
    out+='</div><span id="pub-count" aria-live="polite">4 publications</span></div>'
    out+=t('2026','2026','h2','year-heading')+''.join(publication(p) for p in pubs if p['year']=='2026')
    out+=t('2023','2023','h2','year-heading')+''.join(publication(p) for p in pubs if p['year']=='2023')
    return out

def experience():
    return t('Experience & service','经历与学术服务','h1')+'<section>'+t('Research & work experience','科研与工作经历','h2')+ \
      '<div class="dated-entry"><div class="entry-date">Nov 2025 – Jun 2026</div><div><h3>University of Bologna</h3>'+t('Visiting Ph.D. Student','访问博士生','p')+t('Worked with Prof. Paolo Bellavista.','与 Paolo Bellavista 教授合作。','p','entry-detail')+'</div></div>'+ \
      '<div class="dated-entry"><div class="entry-date">Sep 2021 – May 2022</div><div><h3>'+polyu+'</h3>'+t('Research Assistant','研究助理','p')+t('Developed a prototype of EdgeOS.','参与 EdgeOS 原型系统开发。','p','entry-detail')+'</div></div>'+ \
      '<div class="dated-entry"><div class="entry-date">Aug 2020 – Feb 2021</div><div><h3>Haplox Biotechnology Co., Ltd.</h3>'+t('Front-end Developer Intern · Shenzhen, China','前端开发实习生 · 中国深圳','p')+t('Developed and maintained a biomedical materials management system.','开发与维护生物医学材料管理系统。','p','entry-detail')+'</div></div></section>'+ \
      '<section>'+t('Teaching experience','教学经历','h2')+t('Teaching Assistant for the following courses at PolyU:','曾在香港理工大学担任以下课程的助教：','p')+'<ul><li><strong>COMP1012</strong> · Programming Fundamentals and Applications</li><li><strong>COMP4442</strong> · Service and Cloud Computing</li><li><strong>COMP6657</strong> · Distributed Algorithms and Protocols for Blockchains</li></ul></section>'+ \
      '<section>'+t('Academic service','学术服务','h2')+'<ul>'+t('<strong>Reviewer:</strong> Concurrency and Computation: Practice and Experience (CCPE)','<strong>审稿人：</strong>Concurrency and Computation: Practice and Experience（CCPE）','li')+t('<strong>Subreviewer:</strong> IEEE ICDCS 2024','<strong>协助审稿：</strong>IEEE ICDCS 2024','li')+t('<strong>Subreviewer:</strong> IEEE ICPADS 2025','<strong>协助审稿：</strong>IEEE ICPADS 2025','li')+'</ul></section>'

icons={
 'location':'<path d="M16 7c0 5-6 10-6 10S4 12 4 7a6 6 0 0 1 12 0Z"/><circle cx="10" cy="7" r="2"/>',
 'mail':'<rect x="2" y="4" width="16" height="12" rx="1"/><path d="m2 5 8 6 8-6"/>',
 'github':'<path d="M7 17v-3c-4 1-4-2-5-2m13 5v-4c1-1 2-2 2-5 0-1-1-2-1-3 0-1 0-2-1-3l-3 1H8L5 2 4 5C1 8 3 12 7 13"/>',
 'school':'<path d="m1 7 9-5 9 5-9 5Zm3 2v6c4 3 8 3 12 0V9M18 8v8"/>'
}
def icon(key):return '<svg viewBox="0 0 20 20" aria-hidden="true">'+icons[key]+'</svg>'

pages=[('index.html','About','关于我',home),('publications.html','Publications','学术论文',publications),('experience.html','Experience','经历与服务',experience)]
def shell(filename,name,body):
    nav=''.join(f'<a href="{file}"'+(' aria-current="page"' if file==filename else '')+'>'+t(en,zh)+'</a>' for file,en,zh,_ in pages)
    sidebar='<aside class="sidebar" aria-label="Profile"><a class="portrait-link" href="index.html"><img class="portrait" src="assets/zhiyuan-hu.jpg" alt="Zhiyuan Hu" width="170" height="170"></a><div class="profile-summary"><h2>Zhiyuan Hu <span lang="zh-Hans">胡致远</span></h2>'+t('Ph.D. Student, PolyU','香港理工大学 · 博士研究生','p','profile-role')+t('On-device LLMs · Mobile inference · Agent execution','端侧大语言模型 · 移动端推理 · 智能体执行','p','profile-interests')+'</div><ul class="profile-links"><li>'+icon('location')+t('Hong Kong','中国香港')+'</li><li>'+icon('mail')+'<a href="mailto:zhi-yuan.hu@connect.polyu.hk">'+t('Email','电子邮件')+'</a></li><li>'+icon('github')+link('https://github.com/zhiyuanGH','GitHub')+'</li><li>'+icon('school')+link('https://www4.comp.polyu.edu.hk/~labimcl/profile/zhiyuan-hu.html',t('IMCL profile','实验室主页'))+'</li></ul></aside>'
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><meta name="description" content="{name} — Zhiyuan Hu, PhD student at The Hong Kong Polytechnic University. On-device LLMs, mobile inference optimization, and agent execution."><meta name="theme-color" content="#ffffff"><title>{name} - Zhiyuan Hu (胡致远)</title><link rel="icon" href="assets/favicon.svg" type="image/svg+xml"><link rel="stylesheet" href="styles.css"><script src="app.js" defer></script></head><body>
    <a class="skip-link" href="#main">{t('Skip to content','跳转到正文')}</a><header class="masthead"><div class="masthead-inner"><a class="site-title" href="index.html">Zhiyuan Hu <span lang="zh-Hans">(胡致远)</span></a><nav class="desktop-nav" aria-label="Main navigation">{nav}</nav><button id="language-toggle" aria-label="Switch to Chinese">中文</button><button id="menu-toggle" aria-label="Open navigation" aria-expanded="false" aria-controls="mobile-nav">☰</button></div><nav class="mobile-nav" id="mobile-nav" aria-label="Mobile navigation" hidden>{nav}</nav></header>
    <div class="page-layout">{sidebar}<main id="main" class="page-content">{body}</main></div>
    <footer class="site-footer"><div><span>© 2026 Zhiyuan Hu.</span> {t('Last updated: October 2026.','更新于 2026 年 10 月。')}<a href="#">{t('Back to top','回到顶部')} ↑</a></div></footer>
    <dialog id="citation-dialog" aria-labelledby="citation-title"><div class="dialog-heading"><h2 id="citation-title">{t('Cite this work','引用论文')}</h2><button class="close-dialog" aria-label="Close citation">×</button></div><pre id="citation-text"></pre><p id="citation-status" role="status" aria-live="polite"></p><button class="small-button" id="copy-citation">{t('Copy BibTeX','复制 BibTeX')}</button></dialog><div id="toast" class="toast" role="status" aria-live="polite"></div>
    </body></html>'''

if __name__=='__main__':
    for filename,en,zh,body in pages:(DIST/filename).write_text(shell(filename,en,body()),encoding='utf8')
    print(f'Generated {len(pages)} academic website pages.')
