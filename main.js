const cursor = document.getElementById('cursor');
const ring = document.getElementById('cursorRing');
let mx = 0, my = 0, rx = 0, ry = 0;

document.addEventListener('mousemove', (e) => {
  mx = e.clientX;
  my = e.clientY;
  if (cursor) {
    cursor.style.left = mx + 'px';
    cursor.style.top = my + 'px';
  }
});

function animRing() {
  rx += (mx - rx) * 0.12;
  ry += (my - ry) * 0.12;
  if (ring) {
    ring.style.left = rx + 'px';
    ring.style.top = ry + 'px';
  }
  requestAnimationFrame(animRing);
}
animRing();

document.querySelectorAll('a, button').forEach((el) => {
  el.addEventListener('mouseenter', () => {
    if (!cursor) return;
    cursor.style.width = '16px';
    cursor.style.height = '16px';
    cursor.style.background = 'var(--gold2)';
  });
  el.addEventListener('mouseleave', () => {
    if (!cursor) return;
    cursor.style.width = '10px';
    cursor.style.height = '10px';
    cursor.style.background = 'var(--teal3)';
  });
});

const nav = document.getElementById('mainNav');
window.addEventListener('scroll', () => {
  if (nav) nav.classList.toggle('scrolled', window.scrollY > 60);
});

const observer = new IntersectionObserver(
  (entries) => {
    entries.forEach((e) => {
      if (e.isIntersecting) e.target.classList.add('visible');
    });
  },
  { threshold: 0.12 }
);
document.querySelectorAll('.reveal').forEach((el) => observer.observe(el));

function switchTab(tab, btn) {
  document.querySelectorAll('.pricing-tab').forEach((t) => t.classList.remove('active'));
  document.querySelectorAll('.pricing-panel').forEach((p) => p.classList.remove('active'));
  btn.classList.add('active');
  const panel = document.getElementById(tab + '-panel');
  if (panel) panel.classList.add('active');
}

const navMenu = document.getElementById('navMenu');
if (navMenu) {
  navMenu.addEventListener('click', () => {
    const links = document.querySelector('.nav-links');
    if (!links) return;
    if (links.style.display === 'flex') {
      links.style.display = 'none';
    } else {
      links.style.cssText =
        'display:flex;flex-direction:column;position:fixed;top:60px;left:0;right:0;background:rgba(10,20,50,.97);padding:2rem;gap:1.5rem;z-index:999;backdrop-filter:blur(20px);';
    }
  });
}
