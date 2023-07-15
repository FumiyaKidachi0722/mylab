module.exports = `
  <header>
    <h1>My Website</h1>
    <nav>
      <div class="menu-toggle">
        <div class="bar"></div>
        <div class="bar"></div>
        <div class="bar"></div>
      </div>
      <ul class="menu">
        <li><a href="/">Home</a></li>
        <li><a href="/about">About</a></li>
        <li><a href="/contact">Contact</a></li>
      </ul>
    </nav>
    <style>
      body {
        font-family: Arial, sans-serif;
      }
      header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        background-color: #f2f2f2;
        padding: 10px;
      }
      h1 {
        margin: 0;
      }
      nav {
        display: flex;
        align-items: center;
        position: relative;
      }
      .menu-toggle {
        cursor: pointer;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        height: 24px;
        padding: 4px;
      }
      .bar {
        width: 24px;
        height: 3px;
        background-color: #333;
        transition: transform 0.3s ease;
      }
      .menu-toggle.open .bar:first-child {
        transform: rotate(45deg) translate(-2px, 5px);
      }
      .menu-toggle.open .bar:nth-child(2) {
        opacity: 0;
      }
      .menu-toggle.open .bar:last-child {
        transform: rotate(-45deg) translate(-2px, -5px);
      }
      .menu {
        list-style-type: none;
        padding: 0;
        margin: 0;
        display: none;
        position: absolute;
        top: 100%;
        left: 0;
        background-color: #f2f2f2;
        padding: 10px;
        z-index: 100;
      }
      .menu.open {
        display: block;
      }
      .menu li {
        margin-bottom: 10px;
      }
      @media (min-width: 769px) {
        .menu {
          display: flex;
          position: static;
          background-color: transparent;
          padding: 0;
          margin-left: auto;
        }
        .menu li {
          margin-bottom: 0;
          margin-right: 10px;
        }
        .menu-toggle {
          display: none;
        }
      }
    </style>
    <script>
      const menuToggle = document.querySelector('.menu-toggle');
      const menu = document.querySelector('.menu');

      menuToggle.addEventListener('click', function () {
        menu.classList.toggle('open');
      });

      // ブラウザのウィンドウサイズが変更されたときにメニューを閉じる
      window.addEventListener('resize', function () {
        if (window.innerWidth >= 769) {
          menu.classList.remove('open');
        }
      });
    </script>
  </header>
`;
