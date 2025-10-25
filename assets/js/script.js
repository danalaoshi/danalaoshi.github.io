// 页面加载完成后执行
document.addEventListener('DOMContentLoaded', function() {
  // 激活当前导航项
  const currentPath = window.location.pathname;
  const navLinks = document.querySelectorAll('.md-nav__link');

  navLinks.forEach(link => {
    if (link.getAttribute('href') === currentPath) {
      link.classList.add('md-nav__link--active');
    }
  });

  // 平滑滚动
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
      e.preventDefault();
      const target = document.querySelector(this.getAttribute('href'));
      if (target) {
        target.scrollIntoView({
          behavior: 'smooth'
        });
      }
    });
  });
});