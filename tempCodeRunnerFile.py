<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>David</title>

  <!-- Bootstrap -->
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">

  <!-- Textillate animation CSS -->
  <link rel="stylesheet" href="assets/vendore/texllate/animate.css">

  <!-- Google Font: Orbitron for Neon look -->
  <link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&display=swap" rel="stylesheet">

  <!-- Custom CSS -->
  <link rel="stylesheet" href="style.css">

  <!-- Font Awesome -->
  <script src="https://kit.fontawesome.com/a076d05399.js" crossorigin="anonymous"></script>

  <style>
    body {
      font-family: 'Orbitron', sans-serif;
      background: linear-gradient(135deg, #000428, #004e92);
      color: #fff;
    }

    .navbar {
      background-color: #0f0f3f;
      padding: 1rem;
      display: flex;
      justify-content: space-between;
      align-items: center;
      box-shadow: 0 0 10px cyan;
    }

    .logo {
      font-size: 2rem;
      font-weight: bold;
      color: cyan;
    }

    .nav-links {
      list-style: none;
      display: flex;
      gap: 20px;
    }

    .nav-links li a {
      color: white;
      text-decoration: none;
      transition: color 0.3s;
    }

    .nav-links li a:hover {
      color: cyan;
    }

    .sidebar {
      position: fixed;
      left: 0;
      top: 70px;
      width: 180px;
      background: #111;
      padding: 10px;
      box-shadow: 3px 0 15px rgba(0, 255, 255, 0.5);
      height: calc(100% - 70px);
    }

    .sidebar-item {
      color: #aaa;
      padding: 10px;
      margin-bottom: 10px;
      cursor: pointer;
      transition: 0.3s;
    }

    .sidebar-item.active, .sidebar-item:hover {
      background-color: cyan;
      color: black;
      border-radius: 8px;
    }

    .chat-window textarea {
      width: 100%;
      height: 150px;
      border-radius: 12px;
      padding: 1rem;
      border: 1px solid cyan;
      background: #0f0f0f;
    }

    .button-container button {
      border: 1px solid cyan;
      color: cyan;
      background: transparent;
      transition: 0.3s;
    }

    .button-container button:hover {
      background-color: cyan;
      color: black;
    }

    .neon-text {
      font-size: 2rem;
      color: #0ff;
      text-shadow: 0 0 10px #0ff, 0 0 20px #0ff;
    }

    .main-content {
      margin-left: 200px;
      padding: 20px;
    }

    .image-container {
      position: relative;
      text-align: center;
    }

    .ai-image {
      width: 220px;
      border-radius: 50%;
      border: 4px solid cyan;
      box-shadow: 0 0 30px cyan;
      animation: pulse 3s infinite;
    }

    .speech-bubble {
      position: absolute;
      top: -20px;
      left: 50%;
      transform: translateX(-50%);
      background: #0ff;
      color: #000;
      padding: 10px 20px;
      border-radius: 20px;
      font-weight: bold;
      box-shadow: 0 0 10px #0ff;
    }

    @keyframes pulse {
      0% {
        transform: scale(1);
      }
      50% {
        transform: scale(1.05);
      }
      100% {
        transform: scale(1);
      }
    }

    .about-section {
      background: rgba(0, 255, 255, 0.1);
      border-left: 5px solid cyan;
      padding: 20px;
      margin: 20px;
      border-radius: 15px;
      box-shadow: 0 0 20px cyan;
    }

    .about-section h2 {
      color: cyan;
      text-shadow: 0 0 10px cyan;
    }

    .about-section p {
      color: #e0ffff;
      font-size: 1.1rem;
      line-height: 1.6;
    }
  </style>
</head>

<body>
  <!-- Navbar -->
  <nav class="navbar">
    <div class="logo">DAVID</div>
    <ul class="nav-links">
      <li><a href="#">Home</a></li>
      <li><a href="#">Features</a></li>
      <li><a href="#">Settings</a></li>
      <li><a href="#">Help</a></li>
    </ul>
  </nav>

  <!-- About Section -->
  <section class="about-section">
    <h2>About David</h2>
    <p>
      DAVID is your intelligent 3D AI assistant designed to make your digital experience interactive and futuristic.
      Whether you need help with daily tasks, guidance through voice commands, reminders, entertainment, or smart
      conversations, DAVID is always ready to serve with a touch of personality and a splash of neon.
    </p>
  </section>

  <!-- Sidebar -->
  <aside class="sidebar">
    <div class="sidebar-item active">🔹 AI Mode</div>
    <div class="sidebar-item">📢 Text-to-Speech</div>
    <div class="sidebar-item">🎤 Voice Input</div>
    <div class="sidebar-item">⚙ Settings</div>
  </aside>

  <!-- Main Section -->
  <main class="main-content">
    <div class="text-center">
      <div class="image-container my-4">
        <img src="ai.png" alt="AI Assistant" class="ai-image" id="david-btn">
        <div class="speech-bubble">David Start</div>
      </div>

      <!-- Chat Window -->
      <div class="chat-window mb-3">
        <textarea class="form-control text-light bg-dark" placeholder="Ask me anything..."></textarea>
      </div>

      <!-- Buttons -->
      <div class="button-container mb-5">
        <button id="chat-toggle-btn" class="btn btn-outline-light m-1">Chat Window</button>
        <button id="voice-activation-btn" class="btn btn-outline-light m-1">Mic</button>
        <button id="character-list-btn" class="btn btn-outline-light m-1">Characters</button>
        <button id="volume-control-btn" class="btn btn-outline-light m-1">Volume</button>
        <button id="stop-reset-btn" class="btn btn-outline-light m-1">Stop/Reset</button>
        <button id="dark-light-toggle-btn" class="btn btn-outline-light m-1">Dark/Light Mode</button>
        <button id="text-to-speech-btn" class="btn btn-outline-light m-1">Text-to-Speech</button>
        <button id="language-selection-btn" class="btn btn-outline-light m-1">Language</button>
      </div>

      <!-- Neon Welcome Text -->
      <div class="neon-text">WELCOME TO D.A.V.I.D WORLD !!!</div>
    </div>
  </main>

  <!-- Scripts -->
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.4/jquery.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>
  <script src="assets/vendore/texllate/jquery.fittext.js"></script>
  <script src="assets/vendore/texllate/jquery.lettering.js"></script>
  <script src="https://cdn.jsdelivr.net/gh/jschr/textillate/jquery.textillate.js"></script>
  <script src="script.js"></script>
</body>

</html>
