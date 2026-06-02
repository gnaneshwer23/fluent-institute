const nav = document.getElementById('mainNav');
const navMenu = document.getElementById('navMenu');
const navLinks = document.querySelector('.nav-links');
const navAnchors = document.querySelectorAll('[data-nav]');

// Nav scroll state
window.addEventListener(
  'scroll',
  () => {
    if (nav) nav.classList.toggle('scrolled', window.scrollY > 48);
  },
  { passive: true }
);

// Mobile menu
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

// Scroll reveal
const revealObserver = new IntersectionObserver(
  (entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
        revealObserver.unobserve(entry.target);
      }
    });
  },
  { threshold: 0.12, rootMargin: '0px 0px -40px 0px' }
);

document.querySelectorAll('.reveal').forEach((el) => revealObserver.observe(el));

// Active nav on scroll
const sections = ['about', 'services', 'platform', 'contact']
  .map((id) => document.getElementById(id))
  .filter(Boolean);

if (sections.length && navAnchors.length) {
  const sectionObserver = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (!entry.isIntersecting) return;
        const id = entry.target.id;
        navAnchors.forEach((a) => {
          const href = a.getAttribute('href');
          a.classList.toggle('active', href === `#${id}`);
        });
      });
    },
    { rootMargin: '-40% 0px -55% 0px', threshold: 0 }
  );

  sections.forEach((section) => sectionObserver.observe(section));
}
