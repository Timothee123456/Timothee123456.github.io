// ============================================================
// Echo Location - Keyboard Version with Level Selection
// Move with arrow keys (or WASD). ENTER for sonar ping.
// Collect gems, avoid walls, reach the exit.
// Amplifier power-up: 15% chance on gem to double next sonar radius.
// ============================================================

// -------------------- SOUND VARIABLES --------------------
let pingSound, loseLifeSound, gemSound, winSound, victorySound, gameOverSound;
let restartSound, stepSound, noPingsSound, bgm;

// -------------------- GAME CONFIGURATION --------------------
let maze = [];        // 0=path, 1=wall, 2=exit, 3=gem
let visible = [];     // revealed cells
let cols, rows;       // set by level
let cellW, cellH;

// Player position
let playerX, playerY;

// Level settings
let currentLevel = null;  // 'easy', 'normal', 'hard'
let levelParams = {
  easy:   { cols: 15, rows: 15, basePings: 25, pingsPerGem: 4, gemCount: 6, lives: 3 },
  normal: { cols: 25, rows: 25, basePings: 30, pingsPerGem: 5, gemCount: 8, lives: 3 },
  hard:   { cols: 31, rows: 31, basePings: 40, pingsPerGem: 6, gemCount: 11, lives: 3 }
};

// Game state (reset on level start)
let pings, lives, gameOver, win;
let revealTimeout = null;
const REVEAL_DURATION = 400;
const PING_RADIUS = 100;

// Amplifier power-up
let hasAmplifier = false;      // true = next ping is amplified
const AMPLIFIER_CHANCE = 0.15; // 15% chance on gem collection

let startX = 1, startY = 1;
let exitX, exitY;

// UI states
let gameState = "MENU";  // MENU, PLAYING, GAMEOVER, WIN

// Step sound cooldown
let lastStepTime = 0;
const STEP_COOLDOWN = 120;

// -------------------- PRELOAD SOUNDS --------------------
function preload() {
  pingSound = loadSound('ping.mp3');
  loseLifeSound = loadSound('lose_life.mp3');
  gemSound = loadSound('gem.mp3');
  winSound = loadSound('win.mp3');
  victorySound = loadSound('victory.mp3');
  gameOverSound = loadSound('loose.mp3');
  restartSound = loadSound('reset.mp3');
  stepSound = loadSound('footstep.wav');
  noPingsSound = loadSound('no_pings.mp3');
  bgm = loadSound('bgm.mp3');
}

// -------------------- MAZE GENERATION (Recursive Backtracking) --------------------
function generateMaze() {
  let grid = Array(rows).fill().map(() => Array(cols).fill(1));
  let startCol = 1;
  let startRow = 1;
  grid[startRow][startCol] = 0;
  let stack = [{x: startCol, y: startRow}];
  
  while (stack.length > 0) {
    let current = stack[stack.length - 1];
    let {x, y} = current;
    let neighbours = [];
    let dirs = [
      {dx: 0, dy: -2, wallX: x, wallY: y-1},
      {dx: 0, dy: 2,  wallX: x, wallY: y+1},
      {dx: -2, dy: 0, wallX: x-1, wallY: y},
      {dx: 2, dy: 0,  wallX: x+1, wallY: y}
    ];
    for (let d of dirs) {
      let nx = x + d.dx;
      let ny = y + d.dy;
      if (nx > 0 && nx < cols-1 && ny > 0 && ny < rows-1 && grid[ny][nx] === 1) {
        neighbours.push({nx, ny, wallX: d.wallX, wallY: d.wallY});
      }
    }
    if (neighbours.length > 0) {
      let chosen = random(neighbours);
      grid[chosen.ny][chosen.nx] = 0;
      grid[chosen.wallY][chosen.wallX] = 0;
      stack.push({x: chosen.nx, y: chosen.ny});
    } else {
      stack.pop();
    }
  }
  
  startX = 1;
  startY = 1;
  exitX = cols-2;
  exitY = rows-2;
  grid[exitY][exitX] = 2;
  
  // Place gems
  let gemCount = levelParams[currentLevel].gemCount;
  let placed = 0;
  while (placed < gemCount) {
    let rx = floor(random(1, cols-1));
    let ry = floor(random(1, rows-1));
    if (grid[ry][rx] === 0 && !(rx === startX && ry === startY) && !(rx === exitX && ry === exitY)) {
      grid[ry][rx] = 3;
      placed++;
    }
  }
  return grid;
}

// -------------------- START A LEVEL --------------------
function startLevel(level) {
  currentLevel = level;
  let p = levelParams[level];
  cols = p.cols;
  rows = p.rows;
  cellW = width / cols;
  cellH = height / rows;
  
  maze = generateMaze();
  visible = Array(rows).fill().map(() => Array(cols).fill(false));
  pings = p.basePings;
  lives = p.lives;
  gameOver = false;
  win = false;
  playerX = startX;
  playerY = startY;
  hasAmplifier = false;  // reset amplifier on new game
  if (revealTimeout) clearTimeout(revealTimeout);
  gameState = "PLAYING";
}

// -------------------- RESET SAME LEVEL --------------------
function resetSameLevel() {
  if (currentLevel) {
    startLevel(currentLevel);
  } else {
    gameState = "MENU";
  }
}

// -------------------- PLAY WIN SEQUENCE --------------------
function playWinSequence() {
  if (winSound && !winSound.isPlaying()) {
    winSound.play();
    winSound.onended(() => {
      if (victorySound && !victorySound.isPlaying()) victorySound.play();
    });
  } else if (victorySound && !victorySound.isPlaying()) {
    victorySound.play();
  }
}

// -------------------- SONAR PING (with amplifier support) --------------------
function sonarPing() {
  if (gameState !== "PLAYING") return;
  if (pings <= 0) {
    if (noPingsSound && !noPingsSound.isPlaying()) noPingsSound.play();
    return;
  }
  
  pings--;
  if (pingSound) {
    pingSound.setVolume(2.0);
    pingSound.play();
  }
  
  // Determine ping radius (double if amplifier active)
  let currentRadius = hasAmplifier ? PING_RADIUS * 2 : PING_RADIUS;
  // Consume amplifier after this ping (whether used or not)
  if (hasAmplifier) {
    hasAmplifier = false;
  }
  
  let playerCenterX = playerX * cellW + cellW/2;
  let playerCenterY = playerY * cellH + cellH/2;
  
  for (let i = 0; i < cols; i++) {
    for (let j = 0; j < rows; j++) {
      let cellCenterX = i * cellW + cellW/2;
      let cellCenterY = j * cellH + cellH/2;
      let d = dist(playerCenterX, playerCenterY, cellCenterX, cellCenterY);
      if (d < currentRadius) {
        visible[i][j] = true;
      }
    }
  }
  
  if (revealTimeout) clearTimeout(revealTimeout);
  revealTimeout = setTimeout(() => {
    for (let i = 0; i < cols; i++) {
      for (let j = 0; j < rows; j++) {
        visible[i][j] = false;
      }
    }
    revealTimeout = null;
  }, REVEAL_DURATION);
}

// -------------------- PLAYER MOVEMENT & COLLISION --------------------
function tryMove(dx, dy) {
  if (gameState !== "PLAYING") return;
  
  let newX = playerX + dx;
  let newY = playerY + dy;
  if (newX < 0 || newX >= cols || newY < 0 || newY >= rows) return;
  
  let cellType = maze[newY][newX];
  
  // Footstep sound
  let now = millis();
  if (stepSound && now - lastStepTime > STEP_COOLDOWN) {
    stepSound.setVolume(0.5);
    stepSound.play();
    lastStepTime = now;
  }
  
  // Wall collision
  if (cellType === 1) {
    lives--;
    if (loseLifeSound && !loseLifeSound.isPlaying()) loseLifeSound.play();
    if (lives <= 0) {
      gameOver = true;
      win = false;
      gameState = "GAMEOVER";
      if (gameOverSound && !gameOverSound.isPlaying()) gameOverSound.play();
    } else {
      playerX = startX;
      playerY = startY;
      // hide all visible cells
      for (let i = 0; i < cols; i++)
        for (let j = 0; j < rows; j++)
          visible[i][j] = false;
    }
    return;
  }
  
  // Exit win
  if (cellType === 2) {
    win = true;
    gameOver = true;
    gameState = "WIN";
    playWinSequence();
    return;
  }
  
  // Gem collection
  if (cellType === 3) {
    let gain = levelParams[currentLevel].pingsPerGem;
    pings += gain;
    maze[newY][newX] = 0;
    if (gemSound && !gemSound.isPlaying()) gemSound.play();
    
    // Amplifier chance (only if not already active)
    if (!hasAmplifier && random(1) < AMPLIFIER_CHANCE) {
      hasAmplifier = true;
    }
  }
  
  playerX = newX;
  playerY = newY;
}

// -------------------- DRAW MAZE --------------------
function drawMaze() {
  for (let i = 0; i < cols; i++) {
    for (let j = 0; j < rows; j++) {
      let type = maze[j][i];
      let shouldDraw = (win) || (gameState === "GAMEOVER") || (type === 2) || (visible[i][j]);
      if (shouldDraw) {
        let x = i * cellW;
        let y = j * cellH;
        switch(type) {
          case 1: fill(85); rect(x, y, cellW, cellH); break;
          case 2: fill(0, 255, 0); rect(x, y, cellW, cellH); break;
          case 3: fill(255, 255, 0); ellipse(x + cellW/2, y + cellH/2, cellW * 0.6); break;
          default: fill(30); rect(x, y, cellW, cellH);
        }
      }
    }
  }
}

// -------------------- DRAW PLAYER (with amplifier ring) --------------------
function drawPlayer() {
  if (gameState !== "PLAYING") return;
  let px = playerX * cellW + cellW/2;
  let py = playerY * cellH + cellH/2;
  
  // Main player circle (cyan)
  fill(0, 255, 255);
  noStroke();
  ellipse(px, py, cellW * 0.7, cellH * 0.7);
  fill(0, 255, 255, 100);
  ellipse(px, py, cellW * 0.9, cellH * 0.9);
  
  // Amplifier indicator: yellow glowing ring
  if (hasAmplifier) {
    noFill();
    stroke(255, 255, 0, 200);
    strokeWeight(3);
    ellipse(px, py, cellW * 1.2, cellH * 1.2);
    strokeWeight(1);
    noStroke(); // reset for other drawings
  }
}

// -------------------- DRAW UI --------------------
function drawUI() {
  if (gameState === "MENU") {
    drawMenu();
    return;
  }
  
  // In-game UI
  fill(255);
  textSize(16);
  textAlign(LEFT, TOP);
  text("PINGS: " + pings, 10, 10);
  let hearts = "";
  for (let i = 0; i < lives; i++) hearts += "❤️ ";
  text("LIVES: " + hearts, 10, 35);
  
  // Show amplifier status
  if (hasAmplifier) {
    fill(255, 255, 0);
    text("AMPLIFIER READY! (next ping = double radius)", 10, 60);
  }
  
  if (gameState === "GAMEOVER") {
    textSize(32);
    textAlign(CENTER, CENTER);
    fill(255, 0, 0);
    text("GAME OVER", width/2, height/2);
    textSize(16);
    fill(200);
    text("Press R to restart same level | Press M for Menu", width/2, height/2 + 40);
  } else if (gameState === "WIN") {
    textSize(32);
    textAlign(CENTER, CENTER);
    fill(0, 255, 0);
    text("YOU ESCAPED!", width/2, height/2);
    textSize(16);
    fill(200);
    text("Press R to play same level again | Press M for Menu", width/2, height/2 + 40);
  } else {
    // playing: show controls hint
    textSize(12);
    textAlign(RIGHT, BOTTOM);
    fill(150);
    text("Arrow keys to move | ENTER for sonar ping", width-10, height-10);
  }
}

// -------------------- MENU SCREEN --------------------
function drawMenu() {
  background(0);
  fill(0, 255, 255);
  textSize(44);
  textAlign(CENTER, CENTER);
  text("ECHO LOCATION", width/2, height/3 - 60);
  
  let btnW = 160;
  let btnH = 60;
  let startY = height/2 - 40;
  let spacing = 125;  // as requested
  
  // Easy button
  fill(30);
  rect(width/2 - btnW - spacing, startY, btnW, btnH, 10);
  fill(0, 255, 0);
  textSize(26);
  text("EASY", width/2 - btnW - spacing + btnW/2, startY + btnH/2);
  
  // Normal button
  fill(30);
  rect(width/2 - btnW/2, startY, btnW, btnH, 10);
  fill(255, 255, 0);
  text("NORMAL", width/2 + btnW/2 - btnW/2, startY + btnH/2);
  
  // Hard button
  fill(30);
  rect(width/2 + spacing, startY, btnW, btnH, 10);
  fill(255, 0, 0);
  text("HARD", width/2 + spacing + btnW/2, startY + btnH/2);
  
  // Instructions panel
  fill(200);
  textSize(15);
  textAlign(CENTER, TOP);
  let instrY = startY + btnH + 30;
  text("⚫ HOW TO PLAY ⚫", width/2, instrY);
  textSize(13);
  text("You are trapped in a DARK MAZE. The green EXIT is your goal.", width/2, instrY + 25);
  text("Press ENTER to send a SONAR PING – it briefly reveals walls, paths and gems around you.", width/2, instrY + 45);
  text("Use ARROW KEYS or WASD to move the blue circle.", width/2, instrY + 65);
  text("Collect YELLOW GEMS to gain extra pings.", width/2, instrY + 85);
  text("Gems also have a 15% chance to give an AMPLIFIER (yellow ring).", width/2, instrY + 105);
  text("Amplifier makes your next sonar ping reveal TWICE the area.", width/2, instrY + 125);
  text("Avoid touching GREY WALLS – each hit costs 1 life and sends you back to the start.", width/2, instrY + 145);
  text("Lose all 3 lives and it's GAME OVER. Reach the exit to WIN!", width/2, instrY + 165);
  text("Press R to restart the same level | M to return to this menu.", width/2, instrY + 190);
  text("Choose a difficulty: EASY (small maze, 25 pings), NORMAL (balanced), HARD (large maze, 40 pings).", width/2, instrY + 215);
  
  // Detect mouse clicks on buttons
  if (mouseIsPressed) {
    let mx = mouseX;
    let my = mouseY;
    if (mx > width/2 - btnW - spacing && mx < width/2 - spacing && my > startY && my < startY + btnH) {
      startLevel('easy');
    }
    else if (mx > width/2 - btnW/2 && mx < width/2 + btnW/2 && my > startY && my < startY + btnH) {
      startLevel('normal');
    }
    else if (mx > width/2 + spacing && mx < width/2 + spacing + btnW && my > startY && my < startY + btnH) {
      startLevel('hard');
    }
  }
}

// -------------------- p5.js SETUP --------------------
function setup() {
  createCanvas(700, 700);
  cellW = width / 25;
  cellH = height / 25;
  gameState = "MENU";
  if (bgm) { bgm.loop(); bgm.setVolume(0.3); }
}

// -------------------- DRAW LOOP --------------------
function draw() {
  background(0);
  if (gameState === "PLAYING") {
    drawMaze();
    drawPlayer();
  } else if (gameState === "GAMEOVER" || gameState === "WIN") {
    drawMaze();  // show full map
  }
  drawUI();
}

// -------------------- KEYBOARD CONTROLS --------------------
function keyPressed() {
  if (gameState === "MENU") {
    if (key === '1') startLevel('easy');
    else if (key === '2') startLevel('normal');
    else if (key === '3') startLevel('hard');
    return;
  }
  
  if (key === 'r' || key === 'R') {
    resetSameLevel();
    return;
  }
  if (key === 'm' || key === 'M') {
    gameState = "MENU";
    return;
  }
  
  if (gameState !== "PLAYING") return;
  
  if (keyCode === ENTER) {
    sonarPing();
    return;
  }
  
  let dx = 0, dy = 0;
  if (keyCode === UP_ARROW || key === 'w' || key === 'W') dy = -1;
  else if (keyCode === DOWN_ARROW || key === 's' || key === 'S') dy = 1;
  else if (keyCode === LEFT_ARROW || key === 'a' || key === 'A') dx = -1;
  else if (keyCode === RIGHT_ARROW || key === 'd' || key === 'D') dx = 1;
  else return;
  
  tryMove(dx, dy);
}