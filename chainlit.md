<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <style>
    body {
      font-family: Arial, sans-serif;
      text-align: center;
      margin: 0;
      transition: background-color 0.3s, color 0.3s;
    }
    .container {
      max-width: 800px;
      margin: 50px auto;
      padding: 20px;
      border-radius: 10px;
      box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
      transition: background-color 0.3s, box-shadow 0.3s;
    }
    .logo {
      width: 100px;
      height: 100px;
      margin-bottom: 20px;
    }
    .feature-box {
      margin: 20px 0;
      padding: 20px;
      border-radius: 10px;
      transition: background-color 0.3s;
    }
    /* Light Mode */
    body[data-theme='light'] {
      background-color: #f4f4f4;
      color: #333;
    }
    .container[data-theme='light'] {
      background-color: #fff;
      box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }
    .feature-box[data-theme='light'] {
      background-color: #fff;
      border: 1px solid #ddd;
    }
    /* Dark Mode */
    body[data-theme='dark'] {
      background-color: #333;
      color: #fff;
    }
    .container[data-theme='dark'] {
      background-color: #1a1a1a;
      box-shadow: 0 4px 8px rgba(255, 255, 255, 0.1);
    }
    .feature-box[data-theme='dark'] {
      background-color: #1a1a1a;
      border: 1px solid #444;
    }
  </style>
  <title>SlabGPT - Intelligent Document Inference</title>
</head>
<body data-theme="dark">
  <div class="container" data-theme="dark">
    <img class="logo" src="https://th.bing.com/th/id/OIP.YLesNgU54YXqBSTPNgcVrQHaHa?w=151&h=180&c=7&r=0&o=5&dpr=2&pid=1.7" alt="SlabGPT Logo">
    <h1>SlabGPT - Intelligent Document Inference</h1>
    <div class="feature-box" data-theme="dark">
      <h2>Key Features</h2>
      <p>Explore the power of SlabGPT for document inference and analysis.</p>
      <ul>
        <li>Retrieval Augmentation Generation/li>
        <li>Mistral 7b - Q4 Model</li>
        <li>Memory Footprint of 5gb, Local LLM</li>
        <li>Intelligent Document Inference</li>
        <!-- Add more features as needed -->
      </ul>
    </div>
    <div class="feature-box" data-theme="dark">
      <h2>How SlabGPT Works</h2>
      <p>SlabGPT utilizes cutting-edge machine learning algorithms to understand and infer information from slab documents.</p>
    </div>
    <!-- Add more feature boxes as needed -->
  </div>
</body>
</html>
