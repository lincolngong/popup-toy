const tips = ['我想你了','今天过得开心吗','想和你见面','顺顺利利','早点休息','天冷了，多穿衣服','今天有想我吗'];
const colors = ['pink','skyblue','lightgreen','lavender','lightyellow','plum','coral','bisque','oldlace'];

let timer = null;

function rand(min, max){ return Math.floor(Math.random()*(max-min+1))+min; }

function spawnToast(){
  const d = document.createElement('div');
  d.className = 'toast';
  d.textContent = tips[rand(0, tips.length-1)];
  d.style.background = colors[rand(0, colors.length-1)];

  document.body.appendChild(d);

  const { innerWidth: W, innerHeight: H } = window;
  const rect = d.getBoundingClientRect();
  const x = rand(0, Math.max(0, W - rect.width));
  const y = rand(0, Math.max(0, H - rect.height));
  d.style.left = x + 'px';
  d.style.top  = y + 'px';

  setTimeout(()=> d.remove(), 2500);
}

document.getElementById('start').onclick = () => {
  if (timer) return;
  spawnToast();
  timer = setInterval(spawnToast, rand(5000, 15000)); // 5~15s
};
document.getElementById('stop').onclick = () => {
  if (timer) { clearInterval(timer); timer = null; }
};
