'use strict';
// 每帧由共享引擎的确定性时间轴驱动；徽章只标注当前叙述的证据。
function heading(en, zh) {
  txt(en, 100, 205, {size: 42, fam:F.disp, w:700});
  txt(zh, 100, 257, {size: 31, fam:F.zh, c:C.dim});
}
function star(x,y,labels,active=-1,a=1) {
  const pts=[[x,y],[x+250,y-105],[x+250,y+105]];
  line(x,y,x+250,y-105,C.cyan,a,4);
  line(x,y,x+250,y+105,C.cyan,a,4);
  pts.forEach((p,i)=>chip(p[0],p[1],170,62,labels[i],i===active?C.now:C.cyan,a,30));
  return pts;
}
function squareTile(x,y,a=1) {
  panel(x-110,y-100,430,400,a,C.cyan);
  const p=[[x,y],[x+210,y],[x+210,y+200],[x,y+200]];
  p.forEach((q,i)=>chip(q[0],q[1],85,80,['0','1','0','2'][i],C.cyan,a,46));
  return p;
}
SCENES.square = S => {
  badgeQ(S,[[0,null,'computed']]);
  heading('ONE SQUARE, FOUR DIFFERENCES','一个方格，四条差');
  const p=squareTile(360,420);
  const v=4*Q(S,1,'This square',6);
  p.forEach((q,i)=>{
    const next=p[(i+1)%4],a=clamp(v-i);
    const dx=(next[0]-q[0])/Math.hypot(next[0]-q[0],next[1]-q[1]);
    const dy=(next[1]-q[1])/Math.hypot(next[0]-q[0],next[1]-q[1]);
    arrow(q[0]+48*dx,q[1]+48*dy,next[0]-48*dx,next[1]-48*dy,C.now,a,5);
  });
  panel(900,335,850,455,1,C.cyan,'SIGNED INTEGER DIFFERENCES');
  txt('1,  −1,  2,  −2',1325,450,{size:55,fam:F.math,align:'center',c:C.cyan});
  txt('sum = 0',1325,555,{size:44,fam:F.math,align:'center'});
  txt('0 is omitted',1325,650,{size:39,fam:F.disp,align:'center',a:at(S,1,1)});
  txt('81 possible squares  →  8 allowed',1325,735,{size:30,fam:F.disp,align:'center',a:at(S,2,1)});
};
SCENES.cards = S => {
  badgeQ(S,[[0,null,'argued']]);
  heading('A COLUMN IS A CARD','一列变成一张卡片');
  const pts=star(330,470,['02','10','21']);
  star(1120,470,['20','01','12']);
  const walk=[0,1,0,2,0],u=4*Q(S,1,'choose either leaf',14);
  const i=Math.min(3,Math.floor(u)),p=clamp(u-i),from=pts[walk[i]],to=pts[walk[i+1]];
  dot(from[0]+(to[0]-from[0])*p,from[1]+(to[1]-from[1])*p,27,'g');
  txt('choose → return → choose',960,700,{size:40,fam:F.disp,align:'center',a:at(S,1,0.7)});
  txt('b(r):  2, 3, 4, 6, 8, 12, …',960,790,{size:42,fam:F.math,align:'center',c:C.cyan,a:at(S,2,0.7)});
};
SCENES.rows = S => {
  badgeQ(S,[[0,null,'argued']]);
  heading('WHOLE ROWS HAVE THE SAME TWO STARS','整行仍然只有两处能分叉');
  star(320,450,['02020','10101','21212']);
  star(1130,450,['20202','01010','12121']);
  txt('A 1 fixes a pair; the rest is forced.',960,650,{size:37,fam:F.disp,align:'center',a:at(S,1,1)});
  const a=at(S,2,1);
  for(let j=0;j<8;j++) {
    const x=190+200*j;
    line(x,750,x+95,750,C.cyan,a,4);
    dot(x,750,15,'c',a); dot(x+95,750,15,'c',a);
  }
  txt('k = 4:  2b(4) − 4 = 8 separate edges',960,810,{size:34,fam:F.math,align:'center',c:C.argued,a});
};
SCENES.count = S => {
  badgeQ(S,[[0,null,'argued']]);
  heading('COUNT WALKS, THEN DIVIDE BY FOUR','先数走法，再按原题除以四');
  panel(120,325,780,340,1,C.argued,'TWO STARS');
  txt('4b(n)',510,515,{size:84,fam:F.math,align:'center',c:C.argued});
  panel(1020,325,780,340,1,C.argued,'SEPARATE EDGES');
  txt('2 × (2b(k) − 4)',1410,515,{size:57,fam:F.math,align:'center',c:C.argued,a:at(S,1,0.8)});
  const a=at(S,2,0.8);
  txt('T(n,k) = b(n) + b(k) − 2',960,735,{size:61,fam:F.math,align:'center',a});
  txt('n ≥ 1, k ≥ 1   |   labelled grids; T = N / 4',960,805,{size:29,fam:F.math,align:'center',c:C.dim,a});
};
SCENES.five = S => {
  badgeQ(S,[[0,null,'computed'],[1,'five-column Lean theorem','lean'],[2,'every width','argued']]);
  heading('FIVE COLUMNS: THE PARITY FORMULAS','五列：奇偶公式');
  panel(160,325,1600,375,1,C.cyan,'a(n) = T(n,4) = b(n) + 4');
  txt('a(2m+1) = 2^(m+1) + 4',960,435,{size:52,fam:F.math,align:'center'});
  txt('a(2m+2) = 3·2^m + 4',960,525,{size:52,fam:F.math,align:'center'});
  txt('m ≥ 0     |     6, 7, 8, 10, 12, 16, …',960,630,{size:34,fam:F.math,align:'center',c:C.cyan});
  txt('R. H. Hardin  •  Colin Barker',960,750,{size:31,fam:F.disp,align:'center',c:C.dim});
  txt('Haobo Ma  •  Wenlin Zhang   |   version 2',960,805,{size:31,fam:F.disp,align:'center',c:C.dim});
};
FILM.poster = () => {
  ctx.fillStyle = C.bg; ctx.fillRect(0,0,W,H);
  txt('TWO STARS COUNT THE GRIDS',960,225,{size:61,fam:F.disp,w:700,align:'center'});
  txt('方格计数的两颗星',960,300,{size:46,fam:F.zh,align:'center',c:C.cyan});
  star(340,510,['02','10','21']);
  star(1120,510,['20','01','12']);
  txt('T(n,k) = b(n) + b(k) − 2',960,765,{size:58,fam:F.math,align:'center'});
  txt('Haobo Ma  ·  Wenlin Zhang   |   DOI: 10.5281/zenodo.23903301',960,875,{size:27,fam:F.disp,align:'center',c:C.dim});
};
