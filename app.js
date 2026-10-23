'use strict';

const citations = {
  fetchright: `@inproceedings{hu2026fetchright,
  title = {{FetchRight}: Two-Stage Network-Adaptive Image Fetching for Fast Edge Container Provisioning},
  author = {Hu, Zhiyuan and Cao, Jiannong and Bellavista, Paolo and Wang, Kaile and Zhang, Zhaorui},
  booktitle = {2026 IEEE 23rd International Conference on Mobile Ad Hoc and Smart Systems (MASS)},
  year = {2026}
}`,
  snapshot: `@article{hu2026snapshot,
  title = {On-Demand Snapshot Migration: Accelerating Container Migration in Low-Bandwidth Networks},
  author = {Hu, Zhiyuan and Cao, Jiannong and Zhang, Zhaorui and Cao, Yinfeng and Yang, Lei},
  journal = {IEEE Transactions on Mobile Computing},
  year = {2026},
  doi = {10.1109/TMC.2026.3720463}
}`,
  platform: `@inproceedings{cao2026edgeai,
  title = {Towards Edge {AI} Native Service Platforms: Rethinking Runtime, Deployment, and Migration},
  author = {Cao, Jiannong and Hu, Zhiyuan and Zhang, Mingjin and Shen, Xiaoming and Liu, Hongbo},
  booktitle = {2026 IEEE International Conference on Service-Oriented System Engineering (SOSE)},
  pages = {90--97},
  year = {2026}
}`,
  polyverse: `@inproceedings{cao2023polyverse,
  title = {{PolyVerse}: An Edge Computing-Empowered Metaverse with Physical-to-Virtual Projection},
  author = {Cao, Yinfeng and Cao, Jiannong and Bai, Dongbin and Hu, Zhiyuan and Wang, Kaile and Zhang, Mingjin},
  booktitle = {2023 International Conference on Intelligent Metaverse Technologies and Applications (iMETA)},
  pages = {1--8},
  year = {2023},
  doi = {10.1109/iMETA59369.2023.10294558}
}`
};


let language = 'en';
let citationTrigger;
let toastTimer;
const translated = [...document.querySelectorAll('[data-zh]')];
const originals = new Map(translated.map(el => [el, el.innerHTML]));
const menuButton = document.getElementById('menu-toggle');
const mobileNav = document.getElementById('mobile-nav');
const dialog = document.getElementById('citation-dialog');
function updateCount() {
  const counter = document.getElementById('pub-count');
  if (!counter) return;
  const count = [...document.querySelectorAll('.publication')].filter(p => !p.hidden).length;
  counter.textContent = language === 'zh' ? `${count} 篇论文` : `${count} publications`;
  document.querySelectorAll('.year-heading').forEach(heading => {
    let el = heading.nextElementSibling, visible = false;
    while (el && !el.classList.contains('year-heading')) {
      if (el.classList.contains('publication') && !el.hidden) visible = true;
      el = el.nextElementSibling;
    }
    heading.hidden = !visible;
  });
}
function setLanguage(next) {
  language = next === 'zh' ? 'zh' : 'en';
  document.documentElement.lang = language === 'zh' ? 'zh-Hans' : 'en';
  translated.forEach(el => el.innerHTML = language === 'zh' ? el.dataset.zh : originals.get(el));
  const toggle = document.getElementById('language-toggle');
  toggle.textContent = language === 'zh' ? 'EN' : '中文';
  toggle.setAttribute('aria-label', language === 'zh' ? 'Switch to English' : 'Switch to Chinese');
  menuButton.setAttribute('aria-label', language === 'zh' ? '打开导航菜单' : 'Open navigation');
  updateCount();
  try {localStorage.setItem('zhiyuan-language', language);} catch {}
}
document.getElementById('language-toggle').addEventListener('click', () => setLanguage(language === 'en' ? 'zh' : 'en'));
function closeMenu() {
  if (mobileNav.contains(document.activeElement)) menuButton.focus();
  mobileNav.hidden = true;
  menuButton.setAttribute('aria-expanded', 'false');
}
menuButton.addEventListener('click', () => {
  const isOpen = menuButton.getAttribute('aria-expanded') === 'true';
  mobileNav.hidden = isOpen;
  menuButton.setAttribute('aria-expanded', String(!isOpen));
});
document.addEventListener('keydown', e => {if(e.key === 'Escape') closeMenu();});
window.addEventListener('resize', () => {if(window.innerWidth > 760) closeMenu();});
mobileNav.addEventListener('click', e => {if(e.target.closest('a')) closeMenu();});
document.querySelectorAll('.filter').forEach(button => button.addEventListener('click', () => {
  document.querySelectorAll('.filter').forEach(el => {
    el.classList.toggle('active', el === button);
    el.setAttribute('aria-pressed', String(el === button));
  });
  document.querySelectorAll('.publication').forEach(el => {
    el.hidden = button.dataset.filter !== 'all' && !el.dataset.category.split(' ').includes(button.dataset.filter);
  });
  updateCount();
}));
async function copyText(text) {
  try {await navigator.clipboard.writeText(text);}
  catch {
    const area = document.createElement('textarea'); area.value = text;
    area.setAttribute('readonly', ''); area.style.cssText = 'position:fixed;left:-9999px;top:0';
    (dialog.open ? dialog : document.body).appendChild(area); area.select();
    const success = document.execCommand('copy'); area.remove();
    if (!success) throw Error('Clipboard unavailable');
  }
}
document.querySelectorAll('.bibtex-button').forEach(button => button.addEventListener('click', () => {
  citationTrigger = button; document.getElementById('citation-status').textContent = '';
  document.getElementById('citation-text').textContent = citations[button.dataset.citation]; dialog.showModal();
}));
document.querySelector('.close-dialog').addEventListener('click', () => dialog.close());
dialog.addEventListener('close', () => citationTrigger?.focus());
dialog.addEventListener('click', event => {
  if (event.target !== dialog) return;
  const rect=dialog.getBoundingClientRect();
  if(event.clientX<rect.left||event.clientX>rect.right||event.clientY<rect.top||event.clientY>rect.bottom) dialog.close();
});
document.getElementById('copy-citation').addEventListener('click', async () => {
  try {await copyText(document.getElementById('citation-text').textContent);document.getElementById('citation-status').textContent = language === 'zh' ? 'BibTeX 已复制' : 'BibTeX copied to clipboard';}
  catch {document.getElementById('citation-status').textContent = language === 'zh' ? '请选中文字并手动复制' : 'Please select and copy the citation manually';}
});
document.getElementById('copy-email')?.addEventListener('click', async () => {
  const toast = document.getElementById('toast');
  try {await copyText('zhi-yuan.hu@connect.polyu.hk');toast.textContent=language==='zh'?'邮箱地址已复制':'Email address copied';}
  catch {toast.textContent='zhi-yuan.hu@connect.polyu.hk';}
  clearTimeout(toastTimer);toast.classList.add('visible');toastTimer=setTimeout(()=>toast.classList.remove('visible'),2500);
});
try {if(localStorage.getItem('zhiyuan-language') === 'zh') setLanguage('zh');} catch {}
updateCount();
