const header = document.getElementById('mainNav');
const navMenu = document.getElementById('navMenu');
const navLinks = document.querySelector('.nav-links');
const navAnchors = document.querySelectorAll('[data-nav]');

window.addEventListener(
  'scroll',
  () => {
    if (header) header.classList.toggle('scrolled', window.scrollY > 24);
  },
  { passive: true }
);

if (navMenu && navLinks) {
  navMenu.addEventListener('click', () => {
    const open = navLinks.classList.toggle('open');
    navMenu.setAttribute('aria-expanded', open ? 'true' : 'false');
  });

  navLinks.querySelectorAll('a').forEach((link) => {
    link.addEventListener('click', () => {
      navLinks.classList.remove('open');
      navMenu.setAttribute('aria-expanded', 'false');
    });
  });
}

const revealObserver = new IntersectionObserver(
  (entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
        revealObserver.unobserve(entry.target);
      }
    });
  },
  { threshold: 0.1, rootMargin: '0px 0px -32px 0px' }
);

document.querySelectorAll('.reveal').forEach((el) => revealObserver.observe(el));

const sections = ['help', 'about', 'services', 'platform', 'contact']
  .map((id) => document.getElementById(id))
  .filter(Boolean);

if (sections.length && navAnchors.length) {
  const sectionObserver = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (!entry.isIntersecting) return;
        const id = entry.target.id;
        navAnchors.forEach((a) => {
          a.classList.toggle('active', a.getAttribute('href') === `#${id}`);
        });
      });
    },
    { rootMargin: '-35% 0px -55% 0px', threshold: 0 }
  );

  sections.forEach((section) => sectionObserver.observe(section));
}
