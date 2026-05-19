< !DOCTYPE
html >
< html
lang = "es" >
< head >
< meta
charset = "UTF-8" >
< meta
name = "viewport"
content = "width=device-width, initial-scale=1.0, user-scalable=no" >
< title > Core_Dump - Mario
Bros
3
D
Style < / title >
< style >
body
{
    margin: 0;
overflow: hidden;
font - family: 'Courier New', monospace;
}
# ui {
position: absolute;
top: 20
px;
left: 20
px;
right: 20
px;
background: rgba(0, 0, 0, 0.75);
backdrop - filter: blur(8
px);
border - radius: 16
px;
padding: 12
px
20
px;
display: flex;
justify - content: space - between;
flex - wrap: wrap;
color:  # 0f0;
border: 1
px
solid  # 0f0;
font - weight: bold;
text - shadow: 0
0
3
px  # 0f0;
z - index: 10;
pointer - events: none;
font - size: 1
rem;
}
.stat
{
background:  # 000000aa;
padding: 5
px
12
px;
border - radius: 20
px;
margin: 4
px;
}
.stat
span
{
color:  # ffaa44;
}
# message {
position: absolute;
bottom: 30
px;
left: 20
px;
background:  # 000000aa;
border - left: 4
px
solid  # 0f0;
padding: 8
px
15
px;
font - family: monospace;
font - size: 0.9
rem;
color:  # 0f0;
max - width: 350
px;
pointer - events: none;
z - index: 10;
border - radius: 0
8
px
8
px
0;
}
# controls-info {
position: absolute;
bottom: 20
px;
right: 20
px;
background:  # 000000aa;
padding: 5
px
10
px;
font - size: 0.7
rem;
color:  # aaa;
border - radius: 8
px;
font - family: monospace;
pointer - events: none;
}

@keyframes


pulse
{
    0 % {text - shadow: 0 0 2px  # 0f0; }
        100 % {text - shadow: 0 0 8px  # 0f0; }
}
.boss - alert
{
animation: pulse
0.5
s
infinite;
color:  # ff5555;
}
< / style >
    < / head >
        < body >
        < div
id = "ui" >
     < divH

.
class ="stat" > 💾 INTEGRIDAD: <


    span
id = "health" > 100 < / span > % < / div >
< div


class ="stat" > ⚡ ENERGÍA: <


    span
id = "energy" > 100 < / span > < / div >
< div


class ="stat" > 💰 BITS: <


    span
id = "bits" > 50 < / span > < / div >
< div


class ="stat" > 🛡️ KERNEL: <


    span
id = "kernel" > 0 < / span > / 3 | 🔥 FIREWALL: < span
id = "firewall" > 0 < / span > / 3 < / div >
< / div >
< div
id = "message" >
🎮 ¡Bienvenido! Recolecta
BITS(⭐), repara
KERNEL
y
FIREWALL
tocando
los
pedestales. < br >
🚫 Evita
los
enemigos(pierdes
integridad).< br >
⚔️
Cuando
ambos
estén
nivel
3, derrota
al
GIGA_VIRUS.
< / div >
< div
id = "controls-info" >
🎮 WASD
mover | ESPACIO
saltar |🐭 Ratón
para
mirar
< / div >

< !-- Import
Three.js
core and add - ons -->
< script
type = "importmap" >
{
    "imports": {
        "three": "https://unpkg.com/three@0.128.0/build/three.module.js",
        "three/addons/": "https://unpkg.com/three@0.128.0/examples/jsm/"
    }
}
< / script >

< script
type = "module" >
import * as THREE
from

'three';
import

{OrbitControls}
from

'three/addons/controls/OrbitControls.js';
import

{CSS2DRenderer, CSS2DObject}
from

'three/addons/renderers/CSS2DRenderer.js';

// -------------------- LÓGICA
DEL
JUEGO(MANTIENE
ESENCIA
ORIGINAL) --------------------


class GameState {
constructor() {
this.integridad = 100;
this.energia = 100;
this.bits = 50;
this.kernel = 0;
this.firewall = 0;
this.bossDefeated = false;
this.maxIntegridad = 100;
this.maxEnergia = 100;
}

addMessage(msg, isError = false) {
const msgDiv = document.getElementById('message');
const p = document.createElement('div');
p.textContent = ` > ${msg}`;
p.style.color = isError ? '#ff8888': '#88ff88';
msgDiv.appendChild(p);
if


(msgDiv.children.length > 5)
msgDiv.removeChild(msgDiv.children[0]);
// auto
scroll
msgDiv.scrollTop = msgDiv.scrollHeight;
}

// Reparación
desde
interfaz(usada
por
colisión
con
terminales)
repairKernel()
{
if (this.kernel >= 3)
{
    this.addMessage("❌ Kernel ya está al máximo.", true);
return false;
}
if (this.energia < 30 | | this.bits < 40) {
this.addMessage(`❌ Recursos
insuficientes: necesitas
30⚡ y
40💰`, true);
return false;
}
this.energia -= 30;
this.bits -= 40;
this.kernel + +;
this.addMessage(`🔧 ¡Kernel
reparado! Nivel ${this.kernel} / 3.
`, false);
this.updateUI();
return true;
}

repairFirewall()
{
if (this.firewall >= 3) {
this.addMessage("❌ Firewall ya está al máximo.", true);
return false;
}
if (this.energia < 25 | | this.bits < 35) {
this.addMessage(`❌ Recursos
insuficientes: necesitas
25⚡ y
35💰`, true);
return false;
}
this.energia -= 25;
this.bits -= 35;
this.firewall + +;
this.addMessage(`🛡️ ¡Firewall
reforzado! Nivel ${this.firewall} / 3.
`, false);
this.updateUI();
return true;
}

buyPatch()
{
if (this.bits < 50) {
this.addMessage(`❌ Parche cuesta 50💰.Tienes ${this.bits}💰`, true);
return false;
}
this.bits -= 50;
let
heal = Math.floor(Math.random() * 30) + 20;
this.integridad = Math.min(this.maxIntegridad, this.integridad + heal);
this.addMessage(`💊 Parche
aplicado: +${heal}
integridad.
`, false);
this.updateUI();
return true;
}

takeDamage(amount)
{
if (amount <= 0) return;
this.integridad = Math.max(0, this.integridad - amount);
this.addMessage(`💥 ¡Daño! -${amount}
INTEGRIDAD.
`, true);
this.updateUI();
if (this.integridad <= 0) {
this.addMessage("💀 GAME OVER - El sistema colapsó. Recarga la página.", true);
document.getElementById('game-over-flag')?.remove();
const gameOverDiv = document.createElement('div');
gameOverDiv.id = 'game-over-flag';
gameOverDiv.style.position = 'absolute';
gameOverDiv.style.top = '40%';
gameOverDiv.style.left = '50%';
gameOverDiv.style.transform = 'translate(-50%, -50%)';
gameOverDiv.style.backgroundColor = 'black';
gameOverDiv.style.border = '3px solid red';
gameOverDiv.style.padding = '20px';
gameOverDiv.style.color = 'red';
gameOverDiv.style.fontSize = '2rem';
gameOverDiv.style.zIndex = '100';
gameOverDiv.innerHTML = '💀 GAME OVER 💀<br>Recarga la página';
document.body.appendChild(gameOverDiv);
}
}

addBits(amount)
{
this.bits += amount;
this.addMessage(`💰 +${amount}
BITS
recolectados.
`, false);
this.updateUI();
}

updateUI()
{
document.getElementById('health').innerText = Math.floor(this.integridad);
document.getElementById('energy').innerText = Math.floor(this.energia);
document.getElementById('bits').innerText = Math.floor(this.bits);
document.getElementById('kernel').innerText = this.kernel;
document.getElementById('firewall').innerText = this.firewall;
}

canFightBoss()
{
return this.kernel >= 3 & & this.firewall >= 3 & & !this.bossDefeated;
}
}

// ---------- ESCENA
3
D, JUGADOR, ENEMIGOS
Y
MUNDO
MARIO
BROS - ---------
const
scene = new
THREE.Scene();
scene.background = new
THREE.Color(0x071a3b);
scene.fog = new
THREE.FogExp2(0x071a3b, 0.008);

const
camera = new
THREE.PerspectiveCamera(60, window.innerWidth / window.innerHeight, 0.1, 1000);
camera.position.set(0, 2, 6);

const
renderer = new
THREE.WebGLRenderer({antialias: true});
renderer.setSize(window.innerWidth, window.innerHeight);
renderer.shadowMap.enabled = true;
document.body.appendChild(renderer.domElement);

// CSS2D
para
textos
flotantes
const
labelRenderer = new
CSS2DRenderer();
labelRenderer.setSize(window.innerWidth, window.innerHeight);
labelRenderer.domElement.style.position = 'absolute';
labelRenderer.domElement.style.top = '0px';
labelRenderer.domElement.style.left = '0px';
labelRenderer.domElement.style.pointerEvents = 'none';
document.body.appendChild(labelRenderer.domElement);

// Controles
para
cámara(tercera
persona)
const
controls = new
OrbitControls(camera, renderer.domElement);
controls.enableZoom = true;
controls.enablePan = false;
controls.target.set(0, 1, 0);

// Luces
const
ambientLight = new
THREE.AmbientLight(0x404060);
scene.add(ambientLight);
const
sunLight = new
THREE.DirectionalLight(0xffeedd, 1);
sunLight.position.set(5, 10, 3);
sunLight.castShadow = true;
sunLight.receiveShadow = true;
scene.add(sunLight);
const
fillLight = new
THREE.PointLight(0x2266ff, 0.3);
fillLight.position.set(2, 3, 2);
scene.add(fillLight);

// Suelo
principal
const
groundMat = new
THREE.MeshStandardMaterial({color: 0x3a6b3a, roughness: 0.8, metalness: 0.1});
const
ground = new
THREE.Mesh(new
THREE.PlaneGeometry(30, 30), groundMat);
ground.rotation.x = -Math.PI / 2;
ground.position.y = -0.5;
ground.receiveShadow = true;
scene.add(ground);

// Plataformas
adicionales(estilo
Mario)
const
platformMat = new
THREE.MeshStandardMaterial({color: 0xaa8866, roughness: 0.4});
const
platforms = [
    {pos: [-3, 0.2, 2], size: [2, 0.3, 2]},
    {pos: [2, 0.8, -1], size: [2.5, 0.3, 2.5]},
    {pos: [4, 1.2, 2.5], size: [1.8, 0.3, 1.8]},
    {pos: [-2, 1.5, -2], size: [2, 0.3, 2]},
    {pos: [0, 2, 0], size: [1.5, 0.3, 1.5]} // pedestal central alto
];
platforms.forEach(p= > {
const
box = new
THREE.Mesh(new
THREE.BoxGeometry(p.size[0], p.size[1], p.size[2]), platformMat);
box.position.set(p.pos[0], p.pos[1], p.pos[2]);
box.castShadow = true;
box.receiveShadow = true;
scene.add(box);
});

// Jugador(un
adorable
cubo
robot
con
antena)
const
playerGeometry = new
THREE.BoxGeometry(0.5, 0.5, 0.5);
const
playerMaterial = new
THREE.MeshStandardMaterial({color: 0x33ccff, emissive: 0x004466});
const
player = new
THREE.Mesh(playerGeometry, playerMaterial);
player.castShadow = true;
player.position.set(0, 0, 0);
scene.add(player);

// Antena
const
antennaGeo = new
THREE.CylinderGeometry(0.05, 0.05, 0.3);
const
antennaMat = new
THREE.MeshStandardMaterial({color: 0xffaa44});
const
antenna = new
THREE.Mesh(antennaGeo, antennaMat);
antenna.position.y = 0.35;
player.add(antenna);

// Variables
de
movimiento
const
keyState = {w: false, s: false, a: false, d: false, space: false};
let
velocityY = 0;
let
isGrounded = false;
const
GRAVITY = -25;
const
JUMP_FORCE = 8;
const
MOVE_SPEED = 5;

window.addEventListener('keydown', (e) = > {
switch(e.code)
{
    case
'KeyW': keyState.w = true;
break;
case
'KeyS': keyState.s = true;
break;
case
'KeyA': keyState.a = true;
break;
case
'KeyD': keyState.d = true;
break;
case
'Space':
if (isGrounded) {
velocityY = JUMP_FORCE;
isGrounded = false;
keyState.space = true;
}
break;
}
});
window.addEventListener('keyup', (e) = > {
    switch(e.code)
{
case
'KeyW': keyState.w = false;
break;
case
'KeyS': keyState.s = false;
break;
case
'KeyA': keyState.a = false;
break;
case
'KeyD': keyState.d = false;
break;
case
'Space': keyState.space = false;
break;
}
});

// Detección
de
colisión
simple
con
suelo
y
plataformas
function
updatePlayerMovement(deltaTime)
{
// Movimiento
horizontal
let
move = new
THREE.Vector3(0, 0, 0);
if (keyState.w)
move.z -= 1;
if (keyState.s)
move.z += 1;
if (keyState.a)
move.x -= 1;
if (keyState.d)
move.x += 1;
move.normalize();
player.position.x += move.x * MOVE_SPEED * deltaTime;
player.position.z += move.z * MOVE_SPEED * deltaTime;

// Limitar
bordes
del mundo
player.position.x = Math.min(Math.max(player.position.x, -12), 12);
player.position.z = Math.min(Math.max(player.position.z, -12), 12);

// Gravedad
velocityY += GRAVITY * deltaTime;
player.position.y += velocityY * deltaTime;

// Colisión
con
suelo
Y = -0.5 + mitad
altura(0.25) = > -0.25
const
playerHalfHeight = 0.25;
if (player.position.y - playerHalfHeight <= -0.5)
{
    player.position.y = -0.5 + playerHalfHeight;
velocityY = 0;
isGrounded = true;
} else {
       // Colisión
con
plataformas
let
onPlat = false;
platforms.forEach(p= > {
    const
platY = p.pos[1] + 0.15; // mitad
altura
const
halfSizeX = p.size[0] / 2;
const
halfSizeZ = p.size[2] / 2;
if (player.position.x > p.pos[0] - halfSizeX & & player.position.x < p.pos[0] + halfSizeX & &
    player.position.z > p.pos[2] - halfSizeZ & & player.position.z < p.pos[2] + halfSizeZ)
{
if (player.position.y - playerHalfHeight <= platY & & velocityY <= 0 & & player.position.y + playerHalfHeight > platY)
{
    player.position.y = platY + playerHalfHeight;
velocityY = 0;
isGrounded = true;
onPlat = true;
}
}
});
if (!onPlat) isGrounded = false;
}
}

// ---------- OBJETOS DEL JUEGO ----------
const game = new GameState();
game.updateUI();

// Bits (estrellas doradas)
const bitsList =[];
const bitGeometry = new THREE.SphereGeometry(0.2, 16, 16);
const bitMaterial = new THREE.MeshStandardMaterial({color: 0xffaa44, emissive: 0x442200});
const
bitPositions = [[-2, 0.2, 1], [3, 0.2, -1], [1, 1.2, 2], [-1, 2.2, 0], [4, 0.5, 3], [-3, 1.8, -1.5], [0, 0.8, -3]];
bitPositions.forEach(pos= > {
    const
bit = new
THREE.Mesh(bitGeometry, bitMaterial);
bit.position.set(pos[0], pos[1], pos[2]);
bit.castShadow = true;
scene.add(bit);
bitsList.push(bit);
});

// Enemigos(bichos
móviles)
const
enemies = [];
const
enemyMat = new
THREE.MeshStandardMaterial({color: 0xff3366, emissive: 0x330000});
const
enemyPositions = [[-2, 0, 2], [3, 0.8, 1], [0, 1.5, -1.5], [2.5, 0, 3.5]];
enemyPositions.forEach(pos= > {
    const
enemy = new
THREE.Mesh(new
THREE.SphereGeometry(0.35, 16, 16), enemyMat);
enemy.position.set(pos[0], pos[1], pos[2]);
enemy.userData = {dir: 1, speed: 1.5, range: 2, startX: pos[0]};
enemy.castShadow = true;
scene.add(enemy);
enemies.push(enemy);
});

// Terminales
de
reparación
function
createTerminal(x, z, type, yOffset=0.2)
{
    const
group = new
THREE.Group();
const
base = new
THREE.Mesh(new
THREE.BoxGeometry(0.6, 0.2, 0.6), new
THREE.MeshStandardMaterial({color: 0x888888}));
base.position.y = 0;
group.add(base);
const
pillar = new
THREE.Mesh(new
THREE.CylinderGeometry(0.1, 0.15, 0.6, 6), new
THREE.MeshStandardMaterial({color: 0xccccaa}));
pillar.position.y = 0.4;
group.add(pillar);
const
sign = new
THREE.Mesh(new
THREE.BoxGeometry(0.5, 0.1, 0.5), new
THREE.MeshStandardMaterial({color: type == = 'kernel' ? 0x33ff99: 0xff9933}));
sign.position.y = 0.75;
group.add(sign);
group.position.set(x, yOffset, z);
scene.add(group);

// Texto
CSS2D
const
div = document.createElement('div');
div.textContent = type == = 'kernel' ? '🔧 REPARAR KERNEL (30⚡ 40💰)': '🛡️ REPARAR FIREWALL (25⚡ 35💰)';
div.style.backgroundColor = '#000000aa';
div.style.color = '#0f0';
div.style.padding = '4px 8px';
div.style.borderRadius = '12px';
div.style.fontSize = '12px';
div.style.border = '1px solid #0f0';
const
label = new
CSS2DObject(div);
label.position.set(x, yOffset + 1.1, z);
scene.add(label);

return {group, label, type};
}

const
terminalKernel = createTerminal(-4, -2, 'kernel', 0);
const
terminalFirewall = createTerminal(4, 3, 'firewall', 0);

// Tienda(parche)
const
shopGroup = new
THREE.Group();
const
shopBase = new
THREE.Mesh(new
THREE.BoxGeometry(0.8, 0.2, 0.8), new
THREE.MeshStandardMaterial({color: 0x44aaff}));
shopGroup.add(shopBase);
const
shopPillar = new
THREE.Mesh(new
THREE.CylinderGeometry(0.15, 0.2, 0.5, 6), new
THREE.MeshStandardMaterial({color: 0xffaa44}));
shopPillar.position.y = 0.35;
shopGroup.add(shopPillar);
const
shopIcon = new
THREE.Mesh(new
THREE.SphereGeometry(0.2, 8, 8), new
THREE.MeshStandardMaterial({color: 0xff44ff}));
shopIcon.position.y = 0.7;
shopGroup.add(shopIcon);
shopGroup.position.set(-1, -0.3, 4);
scene.add(shopGroup);

const
shopLabelDiv = document.createElement('div');
shopLabelDiv.textContent = '💊 COMPRAR PARCHE (50💰)';
shopLabelDiv.style.cssText = 'background:#000;color:#ff0;padding:4px;border-radius:12px;font-size:12px;border:1px solid #ff0';
const
shopLabel = new
CSS2DObject(shopLabelDiv);
shopLabel.position.set(-1, 0.6, 4);
scene.add(shopLabel);

// Boss(GIGA_VIRUS), inicialmente
invisible
let
boss = null;
let
bossActive = false;
function
spawnBoss()
{
if (boss) return;
const
bossGeo = new
THREE.BoxGeometry(1.2, 1.2, 1.2);
const
bossMat = new
THREE.MeshStandardMaterial({color: 0xcc3333, emissive: 0x441111});
boss = new
THREE.Mesh(bossGeo, bossMat);
boss.position.set(0, 1, -6);
boss.castShadow = true;
scene.add(boss);
// ojos
const
eyeMat = new
THREE.MeshStandardMaterial({color: 0xff0000});
const
leftEye = new
THREE.Mesh(new
THREE.SphereGeometry(0.15, 8, 8), eyeMat);
leftEye.position.set(-0.4, 0.2, 0.6);
const
rightEye = new
THREE.Mesh(new
THREE.SphereGeometry(0.15, 8, 8), eyeMat);
rightEye.position.set(0.4, 0.2, 0.6);
boss.add(leftEye);
boss.add(rightEye);

const
bossLabelDiv = document.createElement('div');
bossLabelDiv.textContent = '💀 GIGA_VIRUS 💀';
bossLabelDiv.style.color = '#ff5555';
bossLabelDiv.style.fontSize = '20px';
bossLabelDiv.style.fontWeight = 'bold';
const
bossLabel = new
CSS2DObject(bossLabelDiv);
bossLabel.position.set(0, 1.5, -6);
scene.add(bossLabel);
boss.userData = {label: bossLabel, health: 120, maxHealth: 120};
}

// Detección
de
colisiones
y
lógica
del juego
let
lastTime = performance.now();
let
bossFightCooldown = false;

function
updateGameplay(deltaTime)
{
// 1.
Colisión
con
Bits
for (let i = 0; i < bitsList.length; i++) {
    const bit = bitsList[i];
const dist = player.position.distanceTo(bit.position);
if (dist < 0.5) {
scene.remove(bit);
bitsList.splice(i, 1);
game.addBits(15);
i--;
}
}

// 2.
Colisión
con
enemigos(daño)
for (let i = 0; i < enemies.length; i++) {
    const enemy = enemies[i];
const dist = player.position.distanceTo(enemy.position);
if (dist < 0.6) {
game.takeDamage(10);
// retroceder al jugador
const dir = player.position.clone().sub(enemy.position).normalize();
player.position.x += dir.x * 0.6;
player.position.z += dir.z * 0.6;
}
// movimiento simple de enemigos
if (enemy.userData) {
enemy.position.x += enemy.userData.speed * deltaTime * enemy.userData.dir;
if (Math.abs(enemy.position.x - enemy.userData.startX) > enemy.userData.range) {
enemy.userData.dir *= -1;
}
}
}

// 3.
Reparar
terminales(colisión)
const
distKernel = player.position.distanceTo(terminalKernel.group.position);
if (distKernel < 0.8) {
if (game.repairKernel()) {
// feedback visual
terminalKernel.group.children[2].material.color.setHex(0x88ff88);
}
}
const
distFirewall = player.position.distanceTo(terminalFirewall.group.position);
if (distFirewall < 0.8) {
if (game.repairFirewall()) {
terminalFirewall.group.children[2].material.color.setHex(0xffaa88);
}
}

// 4.
Tienda(parche)
const
distShop = player.position.distanceTo(shopGroup.position);
if (distShop < 1.0) {
game.buyPatch();
}

// 5.
Spawnear
boss
si
condiciones
cumplidas
y
no
ha
aparecido
if (game.canFightBoss() & & !boss & & !bossActive) {
spawnBoss();
bossActive = true;
game.addMessage("⚠️ ¡GIGA_VIRUS ha aparecido! Enfréntate a él.", true);
}

// 6.
Combate
contra
boss
if (boss & & bossActive) {
const distToBoss = player.position.distanceTo(boss.position);
if (distToBoss < 1.5 & & !bossFightCooldown) {
// ataque del jugador (saltar o chocar)
let damage = 25 + (game.kernel * 5) + (game.firewall * 5);
boss.userData.health -= damage;
game.addMessage(`⚔️ Atacas al virus: $
    {damage}
de
daño.Vida
restante: ${boss.userData.health}
`, false);
bossFightCooldown = true;
setTimeout(() = > {bossFightCooldown = false;}, 800);

// contraataque
del boss
if (boss.userData.health > 0)
{
    let
bossDmg = 15 + Math.floor(Math.random() * 20);
game.takeDamage(bossDmg);
} else {
       // derrota
game.bossDefeated = true;
game.addMessage("🏆 ¡GIGA_VIRUS DERROTADO! ¡Has salvado el sistema! 🏆", false);
scene.remove(boss);
if (boss.userData.label)
scene.remove(boss.userData.label);
boss = null;
bossActive = false;
game.bits += 200;
game.updateUI();
}
}
// animación
boss
if (boss)
{
    boss.position.y = 0.7 + Math.sin(Date.now() * 0.005) * 0.1;
}
}
}

// Animación
de
cámara
que
sigue
al
jugador
suavemente
function
updateCamera()
{
const
targetPos = player.position.clone();
const
idealOffset = new
THREE.Vector3(-3, 2.5, 4);
const
targetCamPos = targetPos.clone().add(idealOffset);
camera.position.lerp(targetCamPos, 0.05);
controls.target.lerp(targetPos, 0.1);
controls.update();
}

// Bucle
principal
let
previousTime = performance.now();
function
animate()
{
const
now = performance.now();
let
delta = Math.min(0.033, (now - previousTime) / 1000);
previousTime = now;

updatePlayerMovement(delta);
updateGameplay(delta);
updateCamera();

renderer.render(scene, camera);
labelRenderer.render(scene, camera);
requestAnimationFrame(animate);
}

animate();

// Inicialización
adicional
game.addMessage("🎉 ¡Modo Mario Bros 3D activado! Recolecta bits, repara el sistema y derrota al virus.", false);

// Pequeña
ayuda
visual: un
piso
auxiliar
transparente
para
saber
dónde
están
las
plataformas
const
wireframeHelper = new
THREE.GridHelper(25, 20, 0x88aaff, 0x335588);
wireframeHelper.position.y = -0.4;
scene.add(wireframeHelper);
< / script >
    < / body >
        < / html >